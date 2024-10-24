import statistics
import logging
import csv
import os

from PySide6.QtWidgets import QMainWindow, QFileDialog
from PySide6.QtCore import QSize, QTimer
from PySide6.QtGui import QIcon, QPixmap
from datetime import datetime
from typing import List, Any

from Gui.Charts.wind_velocity_graph import WindVelocityDonut
from Generated_qt.ui_Ilmenau_wind_tunnel import Ui_MainWindow
from Device_communication.tlaskan import TlaskanControl
from Device_communication.scales import ScaleControl
from Utils.custom_validator import NumberValidator
from Device_communication.logo import LogoControl
from Gui.Charts.line_chart import LineChart


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_graphical_changes()
        self._disable_enable_buttons(False)
        self.rho = 0
        self.average_speed = [0]

        # validator
        self.ui.save_timer_le.setValidator(NumberValidator())

        # charts setup block
        self.wind_velocity_view = WindVelocityDonut()
        self.ui.speed_graph.addWidget(self.wind_velocity_view)
        self.scale_chart = LineChart("draft", 120, (-1000 , 1000), ["shit"])
        self.ui.scale_chart.addWidget(self.scale_chart)

        # device communication block
        self.velocity_tlaskan = TlaskanControl()
        self.logo = LogoControl()
        self.scales = ScaleControl()

        # data saving
        self.data_to_save: List[Any] = [0.0 for _ in range(31)]
        self.save_timer = QTimer()
        self.save_timer.timeout.connect(self._save_data)
        self.reset_save_file = False
        self.save_file_name = ""
        self.save_file_path = ""
        self.save_count = 0
        self.saving = False

        self._handle_emits()
        self._binding_buttons_to_functions()

    def _binding_buttons_to_functions(self):

        # connection handling
        self.ui.connect_tunel_btn.clicked.connect(self._connect_tunnel)
        self.ui.disconnect_tunnel_btn.clicked.connect(self._disconnect_tunnel)

        # saving handling
        self.ui.start_saving_btn.clicked.connect(self._start_saving)
        self.ui.stop_saving_btn.clicked.connect(self._stop_saving)
        self.ui.change_dir_btn.clicked.connect(self._open_dir_dialog)
        self.ui.set_name_btn.clicked.connect(self._set_save_name)

        # zero values
        self.ui.zero_values_btn.clicked.connect(self._zero_values_of_all_measurements)

        self.ui.vfd_btn.clicked.connect(self._change_vfd)

        # slider value changed
        self.ui.hz_sld.valueChanged.connect(self._hz_handling)

    def _handle_emits(self):
        self.velocity_tlaskan.TLASKAN_DATA.connect(self._handle_main_panel_data)
        self.logo.LOGO_DATA.connect(self._handle_logo_data)
        self.scales.SCALE_MEASUREMENTS.connect(self._handle_scales)

    def _handle_main_panel_data(self, tlaskan_data):
        self.average_speed.append(tlaskan_data[4])
        if len(self.average_speed) > 5:
            self.average_speed.pop(0)
        if not self.ui.speed_avg_cb.isChecked():
            self.wind_velocity_view.set_wind_velocity(tlaskan_data[4])
            self.ui.wind_velocity_lbl.setText(f"V = {str(tlaskan_data[4])} m/s")
        else:
            self.wind_velocity_view.set_wind_velocity(round(statistics.mean(self.average_speed), 1))
            self.ui.wind_velocity_lbl.setText(f"V = {str(round(statistics.mean(self.average_speed), 1))} m/s")
        self.ui.velocity_pressure_lbl.setText(str(tlaskan_data[3]) + " Pa")
        self.ui.temp_1_lbl.setText("T1 = " + str(tlaskan_data[2]))
        self.ui.atmosphere_lbl.setText("Atm = " + str(tlaskan_data[1]))
        self.ui.humidity_lbl.setText("Feuchtigkeit = " + str(tlaskan_data[0]))
        self.rho = tlaskan_data[5]
        if self.saving:
            self.data_to_save[1:7] = tlaskan_data

    def _handle_logo_data(self, logo_data):
        self.ui.temp_2_lbl.setText("T2 = " + str(logo_data[0]))
        if self.saving:
            self.data_to_save[7] = logo_data[0]
            self.data_to_save[28] = logo_data[1]

    def _handle_scales(self, force):
        self.ui.pressure_x.setText(f"Fx = {force[1]}N")
        self.ui.pressure_y.setText(f"Fy = {force[2]}N")
        self.ui.mz_lbl.setText(f"Mz = {force[3]} N.m")
        self.scale_chart.update_chart(force[1:3])
        if self.saving:
            self.data_to_save[24:28] = force

    def _init_graphical_changes(self):
        self.ui.change_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.change_dir_btn.setIconSize(QSize(54, 30))

        self.ui.j4_logo_lbl.setPixmap(QPixmap('./App_data/4j_logo_150x50.png'))

        self.setWindowIcon(QIcon("./App_data/ico.png"))
        self.setWindowTitle("Wind Tunnel")
        self.setMinimumSize(QSize(1500, 750))

        self.ui.disconnect_tunnel_btn.hide()
        self.ui.stop_saving_btn.hide()

    def _start_saving(self):
        self.ui.start_saving_btn.hide()
        self.ui.stop_saving_btn.show()
        self.saving = True
        self._get_file_path()
        self.save_count = 0
        self.save_timer.start(1000)
        self.reset_save_file = True

    def _stop_saving(self):
        self.ui.stop_saving_btn.hide()
        self.ui.start_saving_btn.show()
        self.saving = False
        self.save_timer.stop()

    def _connect_tunnel(self):
        self.ui.connect_tunel_btn.hide()
        self.ui.disconnect_tunnel_btn.show()

        # logo connection
        self.logo.start()

        # velocity tlaskan connection
        self.velocity_tlaskan.start()

        # scales connection
        self.scales.start()

        self._disable_enable_buttons(True)

    def _disconnect_tunnel(self):
        try:
            self.ui.disconnect_tunnel_btn.hide()
            self.ui.connect_tunel_btn.show()

            self.velocity_tlaskan.disconnect()
            self.logo.disconnect()
            self.scales.disconnect()

            self._stop_saving()

            self._disable_enable_buttons(False)
        except Exception as e:
            logging.getLogger().warning(f"{e}")

    def _disable_enable_buttons(self, state: bool):
        self.ui.zero_values_btn.setEnabled(state)
        self.ui.vfd_btn.setEnabled(state)
        self.ui.hz_sld.setEnabled(state)

    def _open_dir_dialog(self):
        options = QFileDialog(self).options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        self.ui.dir_path_line.setText(folder_path)

    def _zero_values_of_all_measurements(self):
        self.scales.set_zero_values()
        self.velocity_tlaskan.set_zero_value()

    def _hz_handling(self, hz_value):
        self.ui.hz_lbl.setText(str(hz_value) + " %")
        self.logo.write_logo_data(hz_value)

    def _get_file_path(self):
        file_path = self.ui.dir_path_line.text()
        if file_path == "":
            file_path = os.getcwd()
        if self.save_file_name == "":
            name = "Wind_tunel_" + datetime.now().strftime("%Y-%m-%d_%H%M")
        else:
            name = self.save_file_name

        file_path += f"/{name}.csv"
        self.save_file_path = file_path

    def _save_data(self):
        save_duration = self.ui.save_timer_le.text()
        if self.ui.save_timer_chb.isChecked() and save_duration != "" and self.save_count >= int(save_duration)-1:
            self._stop_saving()

        exists = os.path.exists(self.save_file_path)

        time = datetime.now().time()
        self.data_to_save[0] = time

        if self.reset_save_file:
            open(self.save_file_path, "w")
            exists = False
            self.reset_save_file = False

        with open(self.save_file_path, 'a', newline="") as f:
            writer = csv.writer(f)
            if not exists:
                writer.writerow(["Time", "%", "Pa", "oC", "Pa", "m.s-1", "kg.m-3", "oC", "N", "N", "N.m",
                                 "mm", "mm", "m.s-1", "m.s-1"])
            writer.writerow(self.data_to_save)
        self.save_count += 1

    def _set_save_name(self):
        self.save_file_name = self.ui.file_name_le.text()

    def _change_vfd(self):
        self.logo.change_vfd()
        if self.ui.vfd_btn.text() == "Turn on VFD":
            self.ui.vfd_btn.setText("Turn off VFD")
        else:
            self.ui.vfd_btn.setText("Turn on VFD")
