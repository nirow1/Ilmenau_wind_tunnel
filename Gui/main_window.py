import statistics
import logging
import csv
import os

from PySide6.QtWidgets import QMainWindow, QFileDialog, QLabel
from PySide6.QtCore import QSize, QTimer
from PySide6.QtGui import QIcon, QPixmap
from datetime import datetime
from typing import List, Any

from Utils.custom_validator import NumberValidator, FloatValidator
from Generated_qt.ui_Ilmenau_wind_tunnel import Ui_MainWindow
from Gui.Charts.wind_velocity_graph import WindVelocityDonut
from Device_communication.tlaskan import TlaskanControl
from Device_communication.logo import LogoControl
from Gui.Charts.line_chart import LineChart


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self._init_graphical_changes()
        self._disable_enable_buttons(False)
        self.chart_count = 0
        self.average_speed = [0]
        self.pump_on = 0

        # validator
        self.ui.save_timer_le.setValidator(NumberValidator(5))
        self.ui.set_velocity_le.setValidator(FloatValidator(2,1, 50))
        self.ui.set_temp_le.setValidator(FloatValidator(2, 1, 60))

        # charts setup block
        self.wind_velocity_view = WindVelocityDonut()
        self.ui.speed_graph.addWidget(self.wind_velocity_view)
        self.temp_chart = LineChart("Temperatures", 3600, (15 , 65),
                                    ["Temp 3", "Temp 4", "Temp 5", "Temp 6"], line_count=4)
        self.ui.scale_chart.addWidget(self.temp_chart)

        # device communication block
        self.velocity_tlaskan = TlaskanControl()
        self.logo = LogoControl()

        # data saving
        self.data_to_save: List[Any] = [0.0 for _ in range(12)]
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

        # heater
        self.ui.enable_heater_tg.clicked.connect(self._heater_on_off)
        self.ui.temp_reg_tg.clicked.connect(lambda: self.logo.write_logo_state(2, b'\x01'))
        self.ui.set_temp_btn.clicked.connect(lambda: self.logo.write_logo_value(18 ,
                                                                                int(float(self.ui.set_temp_le.text()) * 10)))

        # speed control
        self.ui.set_velocity_btn.clicked.connect(lambda: self.logo.write_logo_value(
                                                     4,
                                                     int(float(self.ui.set_velocity_le.text()) * 20)))

        self.ui.stop_btn.clicked.connect(self._stop_wind_tunnel)

    def _handle_emits(self):
        self.velocity_tlaskan.TLASKAN_DATA.connect(self._handle_main_panel_data)
        self.logo.LOGO_DATA.connect(self._handle_logo_data)

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

        self.ui.atm_temp_lbl.setText(f"Atm. temp.= {tlaskan_data[2]} °C")
        self.ui.velocity_pressure_lbl.setText(str(tlaskan_data[3]) + " Pa")
        self.ui.atmosphere_lbl.setText(f"Atm. P. = {str(tlaskan_data[1])} Pa")
        self.ui.humidity_lbl.setText(f"Humidity = {str(tlaskan_data[0])} %")
        if self.saving:
            self.data_to_save[1:7] = tlaskan_data

    def _handle_logo_data(self, logo_data):
        for i in range(3,7):
            temp_lbl: QLabel = self.ui.widget_34.findChild(QLabel, "temp_lbl_"+str(i))
            temp_lbl.setText(f"T{str(i)} = {str(logo_data[7+i])} °C")

        self.ui.temp_lbl_1.setText(f"Boiler temp. = {str(logo_data[8])} °C")
        self.ui.hz_lbl.setText(f"Hz = {str(logo_data[7] / 20)}")
        self.ui.heater_power_lbl.setText(f"Boiler Power = {logo_data[14]} %")

        self.change_led(self.ui.led_1, "red", logo_data[0])
        self.change_led(self.ui.led_2, "blue", logo_data[1])
        self.change_led(self.ui.led_3, "green", logo_data[2])
        self.change_led(self.ui.led_4, "green", logo_data[3])
        self.change_led(self.ui.led_5, "red", logo_data[4])
        self.change_led(self.ui.led_6, "red", logo_data[5])
        self.change_led(self.ui.led_7, "green", logo_data[6])
        self.pump_on = logo_data[2]

        if self.chart_count == 10:
            self.temp_chart.update_chart(logo_data[10:14])
            self.chart_count = 0
        self.chart_count+=1

        if self.ui.temp_reg_tg.isChecked() and not logo_data[3]:
            self.ui.temp_reg_tg.setChecked(False)

        if logo_data[0] == 0 and logo_data[1] == 0 and logo_data[2] == 0 and logo_data[3] == 0 and logo_data[5] == 0:
            self.ui.set_temp_btn.setEnabled(False)
        else:
            self.ui.set_temp_btn.setEnabled(True)

        if self.saving:
            self.data_to_save[7] = logo_data[8]
            self.data_to_save[8:12] = logo_data[10:14]

    def _init_graphical_changes(self):
        self.ui.change_dir_btn.setIcon(QIcon("./App_data/dir_icon.png"))
        self.ui.change_dir_btn.setIconSize(QSize(54, 30))

        self.ui.j4_logo_lbl.setPixmap(QPixmap('./App_data/4j_logo_150x50.png'))

        for i in range(1,8):
            led: QLabel = self.ui.widget_20.findChild(QLabel, "led_" + str(i))
            led.setPixmap(QPixmap('./App_data/grey_led_15.png'))

        self.setWindowIcon(QIcon("./App_data/ico.ico"))
        self.setWindowTitle("Wind Tunnel")
        self.setMinimumSize(QSize(1400, 790))

        self.ui.disconnect_tunnel_btn.hide()
        self.ui.stop_saving_btn.hide()
        self.ui.speed_avg_cb.setChecked(True)
        self.ui.temp_reg_tg.setEnabled(False)

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

        self._disable_enable_buttons(True)

    def _disconnect_tunnel(self):
        try:
            self.ui.disconnect_tunnel_btn.hide()
            self.ui.connect_tunel_btn.show()

            self.velocity_tlaskan.disconnect()
            self.logo.disconnect()

            self._stop_saving()

            self._disable_enable_buttons(False)
        except Exception as e:
            logging.getLogger().warning(f"{e}")

    def _disable_enable_buttons(self, state: bool):
        self.ui.zero_values_btn.setEnabled(state)
        self.ui.set_velocity_btn.setEnabled(state)
        self.ui.set_temp_btn.setEnabled(state)
        self.ui.enable_heater_tg.setEnabled(state)
        self.ui.stop_btn.setEnabled(state)

    def _open_dir_dialog(self):
        options = QFileDialog(self).options()
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder", "", options=options)
        self.ui.dir_path_line.setText(folder_path)

    def _zero_values_of_all_measurements(self):
        self.velocity_tlaskan.set_zero_value()

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
                writer.writerow(["Time", "%", "Pa", "oC", "Pa", "m.s-1", "kg.m-3",
                                 "boiler", "T3", "T4", "T5", "T6"])
            writer.writerow(self.data_to_save)
        self.save_count += 1

    def _set_save_name(self):
        self.save_file_name = self.ui.file_name_le.text()

    def _heater_on_off(self):
        self.ui.temp_reg_tg.setEnabled(self.ui.enable_heater_tg.isChecked())
        if not self.ui.enable_heater_tg.isChecked():
            self.ui.temp_reg_tg.setChecked(False)
        self.logo.write_logo_state(0, b'\x01')

    def _stop_wind_tunnel(self):
        self.logo.write_logo_value(18,0)
        self.logo.write_logo_value(4,0)
        if self.pump_on:
            self.logo.write_logo_state(0, b'\x01')
            if self.ui.enable_heater_tg.isChecked():
                self.ui.enable_heater_tg.setChecked(False)
            if self.ui.temp_reg_tg.isChecked():
                self.ui.temp_reg_tg.setChecked(False)
                self.logo.write_logo_state(2, b'\x01')

    @staticmethod
    def change_led(label: QLabel, color: str, state: bool):
        if state:
            label.setPixmap(QPixmap(f"./App_data/{color}_led_15.png"))
        else:
            label.setPixmap(QPixmap('./App_data/grey_led_15.png'))
