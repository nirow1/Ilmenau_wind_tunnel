# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ilmenau_wind_tunnelBqtnwA.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)

from Gui.Custom_widgets.toggle import AnimatedToggle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1294, 864)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.centralwidget.setStyleSheet(u"QSlider{ margin: 0px;}\n"
"QSlider::groove:horizontal{\n"
"border-radius: 5px;\n"
"height: 10px;\n"
"margin: 0px;\n"
"}\n"
"QSlider::groove:horizontal:hover{ background-color: rgb(200, 200, 200)}\n"
"QSlider::handle:horizontal{\n"
"border: none;\n"
"height: 10px;\n"
"width: 10px;\n"
"margin:0px;\n"
"border-radius: 5px;\n"
"background-color:#1FA808;\n"
"}\n"
"QSlider::sub-page:horizontal {\n"
"background-color: rgb(160,160,160);\n"
"border-radius: 3px;\n"
" }\n"
"QSlider::add-page:horizontal {\n"
"background-color: rgb(190,190,190);\n"
"border-radius: 2px;\n"
" }\n"
"\n"
"QWidget{\n"
"background-color: rgb(250, 250, 250);\n"
"border-radius: 3px;\n"
"font: 11pt \\\"Yu Gothic UI\\\";\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border: 1px solid rgb(180, 180, 180);\n"
"	border-radius: 5px;\n"
"	\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
""
                        "}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #729D1F;\n"
"}\n"
"\n"
"#widget, #widget_2, #widget_13, #widget_16,  #widget_11, #widget_40, #widget_18, #widget_20, #widget_34{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.widget_19 = QWidget(self.centralwidget)
        self.widget_19.setObjectName(u"widget_19")
        self.widget_19.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_16 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_16.setSpacing(4)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.widget_19)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(550, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, -1, 3, 3)
        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMinimumSize(QSize(0, 100))
        self.widget_5.setMaximumSize(QSize(16777215, 120))
        self.widget_5.setStyleSheet(u"QWidget{\n"
"	background-color: #ccc;\n"
"}\n"
"QPushButton {\n"
"    border-radius: 5px;\n"
"    border: 1px solid #4CAF50;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(230, 230, 230);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #729D1F;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_7 = QWidget(self.widget_5)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.dir_path_line = QLineEdit(self.widget_7)
        self.dir_path_line.setObjectName(u"dir_path_line")
        self.dir_path_line.setMinimumSize(QSize(0, 30))
        self.dir_path_line.setReadOnly(True)

        self.horizontalLayout_8.addWidget(self.dir_path_line)

        self.change_dir_btn = QPushButton(self.widget_7)
        self.change_dir_btn.setObjectName(u"change_dir_btn")
        self.change_dir_btn.setMaximumSize(QSize(30, 30))
        self.change_dir_btn.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.change_dir_btn)

        self.start_saving_btn = QPushButton(self.widget_7)
        self.start_saving_btn.setObjectName(u"start_saving_btn")
        self.start_saving_btn.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_8.addWidget(self.start_saving_btn)

        self.stop_saving_btn = QPushButton(self.widget_7)
        self.stop_saving_btn.setObjectName(u"stop_saving_btn")
        self.stop_saving_btn.setMinimumSize(QSize(90, 30))

        self.horizontalLayout_8.addWidget(self.stop_saving_btn)


        self.verticalLayout_2.addWidget(self.widget_7)

        self.widget_9 = QWidget(self.widget_5)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.file_name_le = QLineEdit(self.widget_9)
        self.file_name_le.setObjectName(u"file_name_le")
        self.file_name_le.setEnabled(True)
        self.file_name_le.setMinimumSize(QSize(0, 30))
        self.file_name_le.setMaximumSize(QSize(200, 16777215))
        self.file_name_le.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.file_name_le)

        self.set_name_btn = QPushButton(self.widget_9)
        self.set_name_btn.setObjectName(u"set_name_btn")
        self.set_name_btn.setMinimumSize(QSize(75, 30))

        self.horizontalLayout_3.addWidget(self.set_name_btn)

        self.save_timer_le = QLineEdit(self.widget_9)
        self.save_timer_le.setObjectName(u"save_timer_le")
        self.save_timer_le.setMinimumSize(QSize(0, 30))
        self.save_timer_le.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_3.addWidget(self.save_timer_le)

        self.save_timer_chb = AnimatedToggle(self.widget_9)
        self.save_timer_chb.setObjectName(u"save_timer_chb")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_timer_chb.sizePolicy().hasHeightForWidth())
        self.save_timer_chb.setSizePolicy(sizePolicy)
        self.save_timer_chb.setMinimumSize(QSize(60, 0))
        self.save_timer_chb.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_3.addWidget(self.save_timer_chb)

        self.label = QLabel(self.widget_9)
        self.label.setObjectName(u"label")

        self.horizontalLayout_3.addWidget(self.label)


        self.verticalLayout_2.addWidget(self.widget_9)


        self.verticalLayout.addWidget(self.widget_5)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMaximumSize(QSize(16777215, 80))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.zero_values_btn = QPushButton(self.widget_4)
        self.zero_values_btn.setObjectName(u"zero_values_btn")
        self.zero_values_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.zero_values_btn)

        self.connect_tunel_btn = QPushButton(self.widget_4)
        self.connect_tunel_btn.setObjectName(u"connect_tunel_btn")
        self.connect_tunel_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.connect_tunel_btn)

        self.disconnect_tunnel_btn = QPushButton(self.widget_4)
        self.disconnect_tunnel_btn.setObjectName(u"disconnect_tunnel_btn")
        self.disconnect_tunnel_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.disconnect_tunnel_btn)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_40 = QWidget(self.widget)
        self.widget_40.setObjectName(u"widget_40")
        self.verticalLayout_8 = QVBoxLayout(self.widget_40)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.widget_25 = QWidget(self.widget_40)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.atm_temp_lbl = QLabel(self.widget_25)
        self.atm_temp_lbl.setObjectName(u"atm_temp_lbl")
        self.atm_temp_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.atm_temp_lbl)

        self.heater_power_lbl = QLabel(self.widget_25)
        self.heater_power_lbl.setObjectName(u"heater_power_lbl")
        self.heater_power_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.heater_power_lbl)

        self.temp_lbl_1 = QLabel(self.widget_25)
        self.temp_lbl_1.setObjectName(u"temp_lbl_1")
        self.temp_lbl_1.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_10.addWidget(self.temp_lbl_1)


        self.verticalLayout_8.addWidget(self.widget_25)

        self.widget_26 = QWidget(self.widget_40)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.atmosphere_lbl = QLabel(self.widget_26)
        self.atmosphere_lbl.setObjectName(u"atmosphere_lbl")
        self.atmosphere_lbl.setMaximumSize(QSize(16777215, 16777215))
        self.atmosphere_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.atmosphere_lbl)

        self.humidity_lbl = QLabel(self.widget_26)
        self.humidity_lbl.setObjectName(u"humidity_lbl")
        self.humidity_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_14.addWidget(self.humidity_lbl)


        self.verticalLayout_8.addWidget(self.widget_26)


        self.verticalLayout.addWidget(self.widget_40)

        self.widget_42 = QWidget(self.widget)
        self.widget_42.setObjectName(u"widget_42")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_42.sizePolicy().hasHeightForWidth())
        self.widget_42.setSizePolicy(sizePolicy1)
        self.speed_graph = QGridLayout(self.widget_42)
        self.speed_graph.setObjectName(u"speed_graph")
        self.speed_graph.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget_42)
        self.frame.setObjectName(u"frame")
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)

        self.speed_graph.addWidget(self.frame, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget_42)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.widget_3)
        self.widget_6.setObjectName(u"widget_6")
        self.gridLayout = QGridLayout(self.widget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 1, 0, 1)
        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 5, 0, 5)
        self.widget_8 = QWidget(self.widget_10)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 50))
        self.widget_8.setStyleSheet(u"QLabel{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.horizontalLayout_12 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, 1, -1, 1)
        self.widget_41 = QWidget(self.widget_8)
        self.widget_41.setObjectName(u"widget_41")
        self.widget_41.setStyleSheet(u"")
        self.horizontalLayout_25 = QHBoxLayout(self.widget_41)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.velocity_pressure_lbl = QLabel(self.widget_41)
        self.velocity_pressure_lbl.setObjectName(u"velocity_pressure_lbl")
        self.velocity_pressure_lbl.setMinimumSize(QSize(100, 40))
        self.velocity_pressure_lbl.setMaximumSize(QSize(40, 40))
        self.velocity_pressure_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_25.addWidget(self.velocity_pressure_lbl)


        self.horizontalLayout_12.addWidget(self.widget_41)

        self.wind_velocity_lbl = QLabel(self.widget_8)
        self.wind_velocity_lbl.setObjectName(u"wind_velocity_lbl")
        self.wind_velocity_lbl.setMinimumSize(QSize(140, 0))
        self.wind_velocity_lbl.setMaximumSize(QSize(16777215, 60))
        self.wind_velocity_lbl.setStyleSheet(u"")
        self.wind_velocity_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_12.addWidget(self.wind_velocity_lbl)

        self.widget_12 = QWidget(self.widget_8)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_6 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, 0)
        self.hz_lbl = QLabel(self.widget_12)
        self.hz_lbl.setObjectName(u"hz_lbl")
        self.hz_lbl.setMinimumSize(QSize(100, 40))
        self.hz_lbl.setMaximumSize(QSize(40, 40))
        self.hz_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_6.addWidget(self.hz_lbl)


        self.horizontalLayout_12.addWidget(self.widget_12)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 41))
        self.widget_11.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 3, 1, 3)
        self.widget_33 = QWidget(self.widget_11)
        self.widget_33.setObjectName(u"widget_33")
        self.widget_33.setMinimumSize(QSize(225, 0))
        self.horizontalLayout_7 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_5.addWidget(self.widget_33)

        self.widget_39 = QWidget(self.widget_11)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMaximumSize(QSize(230, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.set_velocity_btn = QPushButton(self.widget_39)
        self.set_velocity_btn.setObjectName(u"set_velocity_btn")
        self.set_velocity_btn.setMinimumSize(QSize(0, 33))
        self.set_velocity_btn.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_35.addWidget(self.set_velocity_btn)

        self.set_velocity_le = QLineEdit(self.widget_39)
        self.set_velocity_le.setObjectName(u"set_velocity_le")
        self.set_velocity_le.setMinimumSize(QSize(0, 33))
        self.set_velocity_le.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_35.addWidget(self.set_velocity_le)

        self.label_7 = QLabel(self.widget_39)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_35.addWidget(self.label_7)


        self.horizontalLayout_5.addWidget(self.widget_39)

        self.widget_50 = QWidget(self.widget_11)
        self.widget_50.setObjectName(u"widget_50")
        self.widget_50.setMaximumSize(QSize(120, 16777215))
        self.horizontalLayout_36 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.speed_avg_cb = QCheckBox(self.widget_50)
        self.speed_avg_cb.setObjectName(u"speed_avg_cb")
        self.speed_avg_cb.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout_36.addWidget(self.speed_avg_cb)


        self.horizontalLayout_5.addWidget(self.widget_50)


        self.verticalLayout_3.addWidget(self.widget_11)

        self.widget_16 = QWidget(self.widget_10)
        self.widget_16.setObjectName(u"widget_16")
        self.horizontalLayout_13 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(1, 3, 1, 3)
        self.widget_31 = QWidget(self.widget_16)
        self.widget_31.setObjectName(u"widget_31")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_31.sizePolicy().hasHeightForWidth())
        self.widget_31.setSizePolicy(sizePolicy2)
        self.widget_31.setMinimumSize(QSize(0, 0))
        self.widget_31.setMaximumSize(QSize(225, 16777215))
        self.horizontalLayout_9 = QHBoxLayout(self.widget_31)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.enable_heater_btn = QPushButton(self.widget_31)
        self.enable_heater_btn.setObjectName(u"enable_heater_btn")
        self.enable_heater_btn.setMinimumSize(QSize(0, 33))
        self.enable_heater_btn.setMaximumSize(QSize(83, 16777215))

        self.horizontalLayout_9.addWidget(self.enable_heater_btn)

        self.temp_reg_chb = AnimatedToggle(self.widget_31)
        self.temp_reg_chb.setObjectName(u"temp_reg_chb")
        self.temp_reg_chb.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_9.addWidget(self.temp_reg_chb)

        self.label_11 = QLabel(self.widget_31)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_9.addWidget(self.label_11)


        self.horizontalLayout_13.addWidget(self.widget_31)

        self.widget_15 = QWidget(self.widget_16)
        self.widget_15.setObjectName(u"widget_15")
        sizePolicy2.setHeightForWidth(self.widget_15.sizePolicy().hasHeightForWidth())
        self.widget_15.setSizePolicy(sizePolicy2)
        self.widget_15.setMaximumSize(QSize(230, 16777215))
        self.horizontalLayout_11 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.set_temp_btn = QPushButton(self.widget_15)
        self.set_temp_btn.setObjectName(u"set_temp_btn")
        self.set_temp_btn.setMinimumSize(QSize(0, 33))
        self.set_temp_btn.setMaximumSize(QSize(85, 16777215))

        self.horizontalLayout_11.addWidget(self.set_temp_btn)

        self.set_temp_le = QLineEdit(self.widget_15)
        self.set_temp_le.setObjectName(u"set_temp_le")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.set_temp_le.sizePolicy().hasHeightForWidth())
        self.set_temp_le.setSizePolicy(sizePolicy3)
        self.set_temp_le.setMinimumSize(QSize(0, 33))
        self.set_temp_le.setMaximumSize(QSize(60, 16777215))

        self.horizontalLayout_11.addWidget(self.set_temp_le)

        self.label_2 = QLabel(self.widget_15)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_11.addWidget(self.label_2)


        self.horizontalLayout_13.addWidget(self.widget_15)

        self.widget_30 = QWidget(self.widget_16)
        self.widget_30.setObjectName(u"widget_30")
        self.widget_30.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_13.addWidget(self.widget_30)


        self.verticalLayout_3.addWidget(self.widget_16)


        self.gridLayout.addWidget(self.widget_10, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_32 = QWidget(self.widget)
        self.widget_32.setObjectName(u"widget_32")
        self.widget_32.setMinimumSize(QSize(0, 72))
        self.widget_32.setMaximumSize(QSize(16777215, 100))

        self.verticalLayout.addWidget(self.widget_32)


        self.horizontalLayout_16.addWidget(self.widget)

        self.widget_2 = QWidget(self.widget_19)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, -1, 3, 3)
        self.widget_13 = QWidget(self.widget_2)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy4)
        self.verticalLayout_6 = QVBoxLayout(self.widget_13)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(1, -1, 1, 1)
        self.stackedWidget = QStackedWidget(self.widget_13)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.verticalLayout_14 = QVBoxLayout(self.page_4)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(2, -1, 2, -1)
        self.stackedWidget.addWidget(self.page_4)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setEnabled(True)
        self.verticalLayout_10 = QVBoxLayout(self.page)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(2, -1, 2, -1)
        self.stackedWidget.addWidget(self.page)
        self.scale_view_pg = QWidget()
        self.scale_view_pg.setObjectName(u"scale_view_pg")
        self.verticalLayout_12 = QVBoxLayout(self.scale_view_pg)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(2, -1, 2, -1)
        self.widget_24 = QWidget(self.scale_view_pg)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_11 = QVBoxLayout(self.widget_24)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.widget_34 = QWidget(self.widget_24)
        self.widget_34.setObjectName(u"widget_34")
        self.widget_34.setMinimumSize(QSize(0, 41))
        self.widget_34.setMaximumSize(QSize(16777215, 50))
        self.horizontalLayout_17 = QHBoxLayout(self.widget_34)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.temp_lbl_3 = QLabel(self.widget_34)
        self.temp_lbl_3.setObjectName(u"temp_lbl_3")
        self.temp_lbl_3.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.temp_lbl_3)

        self.temp_lbl_4 = QLabel(self.widget_34)
        self.temp_lbl_4.setObjectName(u"temp_lbl_4")
        self.temp_lbl_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.temp_lbl_4)

        self.temp_lbl_5 = QLabel(self.widget_34)
        self.temp_lbl_5.setObjectName(u"temp_lbl_5")
        self.temp_lbl_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.temp_lbl_5)

        self.temp_lbl_6 = QLabel(self.widget_34)
        self.temp_lbl_6.setObjectName(u"temp_lbl_6")
        self.temp_lbl_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_17.addWidget(self.temp_lbl_6)


        self.verticalLayout_11.addWidget(self.widget_34)


        self.verticalLayout_12.addWidget(self.widget_24)

        self.widget_18 = QWidget(self.scale_view_pg)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy4.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy4)
        self.horizontalLayout_23 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(1, 1, 1, 1)
        self.widget_38 = QWidget(self.widget_18)
        self.widget_38.setObjectName(u"widget_38")
        self.scale_chart = QGridLayout(self.widget_38)
        self.scale_chart.setObjectName(u"scale_chart")
        self.scale_chart.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_23.addWidget(self.widget_38)


        self.verticalLayout_12.addWidget(self.widget_18)

        self.stackedWidget.addWidget(self.scale_view_pg)
        self.pressure_view_pg = QWidget()
        self.pressure_view_pg.setObjectName(u"pressure_view_pg")
        self.verticalLayout_7 = QVBoxLayout(self.pressure_view_pg)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, -1, 2, -1)
        self.stackedWidget.addWidget(self.pressure_view_pg)

        self.verticalLayout_6.addWidget(self.stackedWidget)

        self.widget_49 = QWidget(self.widget_13)
        self.widget_49.setObjectName(u"widget_49")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_49)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.gerlitz_logo_lbl = QLabel(self.widget_49)
        self.gerlitz_logo_lbl.setObjectName(u"gerlitz_logo_lbl")
        self.gerlitz_logo_lbl.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_33.addWidget(self.gerlitz_logo_lbl)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer)

        self.j4_logo_lbl = QLabel(self.widget_49)
        self.j4_logo_lbl.setObjectName(u"j4_logo_lbl")
        self.j4_logo_lbl.setMinimumSize(QSize(150, 50))

        self.horizontalLayout_33.addWidget(self.j4_logo_lbl)


        self.verticalLayout_6.addWidget(self.widget_49)


        self.verticalLayout_5.addWidget(self.widget_13)


        self.horizontalLayout_16.addWidget(self.widget_2)


        self.verticalLayout_4.addWidget(self.widget_19)

        self.widget_20 = QWidget(self.centralwidget)
        self.widget_20.setObjectName(u"widget_20")
        self.widget_20.setMinimumSize(QSize(0, 30))
        self.horizontalLayout = QHBoxLayout(self.widget_20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.widget_29 = QWidget(self.widget_20)
        self.widget_29.setObjectName(u"widget_29")

        self.horizontalLayout.addWidget(self.widget_29)

        self.label_3 = QLabel(self.widget_20)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.label_3)

        self.led_1 = QLabel(self.widget_20)
        self.led_1.setObjectName(u"led_1")
        self.led_1.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.led_1)

        self.widget_28 = QWidget(self.widget_20)
        self.widget_28.setObjectName(u"widget_28")

        self.horizontalLayout.addWidget(self.widget_28)

        self.label_5 = QLabel(self.widget_20)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.label_5)

        self.led_2 = QLabel(self.widget_20)
        self.led_2.setObjectName(u"led_2")
        self.led_2.setMaximumSize(QSize(25, 25))

        self.horizontalLayout.addWidget(self.led_2)

        self.widget_23 = QWidget(self.widget_20)
        self.widget_23.setObjectName(u"widget_23")

        self.horizontalLayout.addWidget(self.widget_23)

        self.label_8 = QLabel(self.widget_20)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout.addWidget(self.label_8)

        self.led_3 = QLabel(self.widget_20)
        self.led_3.setObjectName(u"led_3")
        self.led_3.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.led_3)

        self.widget_22 = QWidget(self.widget_20)
        self.widget_22.setObjectName(u"widget_22")

        self.horizontalLayout.addWidget(self.widget_22)

        self.label_4 = QLabel(self.widget_20)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.label_4)

        self.led_4 = QLabel(self.widget_20)
        self.led_4.setObjectName(u"led_4")
        self.led_4.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.led_4)

        self.widget_21 = QWidget(self.widget_20)
        self.widget_21.setObjectName(u"widget_21")

        self.horizontalLayout.addWidget(self.widget_21)

        self.label_10 = QLabel(self.widget_20)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(80, 16777215))

        self.horizontalLayout.addWidget(self.label_10)

        self.led_5 = QLabel(self.widget_20)
        self.led_5.setObjectName(u"led_5")
        self.led_5.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.led_5)

        self.widget_17 = QWidget(self.widget_20)
        self.widget_17.setObjectName(u"widget_17")

        self.horizontalLayout.addWidget(self.widget_17)

        self.label_12 = QLabel(self.widget_20)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(130, 16777215))

        self.horizontalLayout.addWidget(self.label_12)

        self.led_6 = QLabel(self.widget_20)
        self.led_6.setObjectName(u"led_6")
        self.led_6.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.led_6)

        self.widget_14 = QWidget(self.widget_20)
        self.widget_14.setObjectName(u"widget_14")

        self.horizontalLayout.addWidget(self.widget_14)

        self.label_9 = QLabel(self.widget_20)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout.addWidget(self.label_9)

        self.led_7 = QLabel(self.widget_20)
        self.led_7.setObjectName(u"led_7")
        self.led_7.setMaximumSize(QSize(30, 16777215))

        self.horizontalLayout.addWidget(self.led_7)

        self.widget_35 = QWidget(self.widget_20)
        self.widget_35.setObjectName(u"widget_35")

        self.horizontalLayout.addWidget(self.widget_35)


        self.verticalLayout_4.addWidget(self.widget_20)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.change_dir_btn.setText("")
        self.start_saving_btn.setText(QCoreApplication.translate("MainWindow", u"Start saving", None))
        self.stop_saving_btn.setText(QCoreApplication.translate("MainWindow", u"Stop saving", None))
        self.set_name_btn.setText(QCoreApplication.translate("MainWindow", u"Set name", None))
        self.save_timer_chb.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Timer", None))
        self.zero_values_btn.setText(QCoreApplication.translate("MainWindow", u"Zero Values", None))
        self.connect_tunel_btn.setText(QCoreApplication.translate("MainWindow", u"Connect to tunnel", None))
        self.disconnect_tunnel_btn.setText(QCoreApplication.translate("MainWindow", u"Disconnect from tunnel", None))
        self.atm_temp_lbl.setText(QCoreApplication.translate("MainWindow", u"Atm. temp.= XX", None))
        self.heater_power_lbl.setText(QCoreApplication.translate("MainWindow", u"Heater Power = XX", None))
        self.temp_lbl_1.setText(QCoreApplication.translate("MainWindow", u"Boiler temp. = XX", None))
        self.atmosphere_lbl.setText(QCoreApplication.translate("MainWindow", u"Atm. P. = XX", None))
        self.humidity_lbl.setText(QCoreApplication.translate("MainWindow", u"Humidity = XX", None))
        self.velocity_pressure_lbl.setText(QCoreApplication.translate("MainWindow", u"Pa", None))
        self.wind_velocity_lbl.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.hz_lbl.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.set_velocity_btn.setText(QCoreApplication.translate("MainWindow", u"Set velocity", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.speed_avg_cb.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.enable_heater_btn.setText(QCoreApplication.translate("MainWindow", u"En. Heater", None))
        self.temp_reg_chb.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Temp. reg.", None))
        self.set_temp_btn.setText(QCoreApplication.translate("MainWindow", u"set temp", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00b0C", None))
        self.temp_lbl_3.setText(QCoreApplication.translate("MainWindow", u"T3 = XX", None))
        self.temp_lbl_4.setText(QCoreApplication.translate("MainWindow", u"T4 = XX", None))
        self.temp_lbl_5.setText(QCoreApplication.translate("MainWindow", u"T5 = XX", None))
        self.temp_lbl_6.setText(QCoreApplication.translate("MainWindow", u"T6 = XX", None))
        self.gerlitz_logo_lbl.setText("")
        self.j4_logo_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SSR alarm", None))
        self.led_1.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Emergency", None))
        self.led_2.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Running pump", None))
        self.led_3.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Heater", None))
        self.led_4.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"FC error", None))
        self.led_5.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Low water presure", None))
        self.led_6.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cold water valve", None))
        self.led_7.setText("")
    # retranslateUi

