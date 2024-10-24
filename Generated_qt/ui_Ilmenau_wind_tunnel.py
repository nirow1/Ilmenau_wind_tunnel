# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ilmenau_wind_tunnelkkdbhT.ui'
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
    QPushButton, QSizePolicy, QSlider, QSpacerItem,
    QStackedWidget, QVBoxLayout, QWidget)

from Gui.Custom_widgets.toggle import AnimatedToggle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1302, 820)
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
"#widget, #widget_2, #widget_13, #widget_28, #widget_10, #widget_40, #widget_18, #widget_19, #widget_15{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(550, 16777215))
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, -1, 3, -1)
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

        self.vfd_btn = QPushButton(self.widget_4)
        self.vfd_btn.setObjectName(u"vfd_btn")
        self.vfd_btn.setMinimumSize(QSize(0, 40))

        self.horizontalLayout_2.addWidget(self.vfd_btn)


        self.verticalLayout.addWidget(self.widget_4)

        self.widget_40 = QWidget(self.widget)
        self.widget_40.setObjectName(u"widget_40")
        self.horizontalLayout_24 = QHBoxLayout(self.widget_40)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.temp_1_lbl = QLabel(self.widget_40)
        self.temp_1_lbl.setObjectName(u"temp_1_lbl")
        self.temp_1_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.temp_1_lbl)

        self.temp_2_lbl = QLabel(self.widget_40)
        self.temp_2_lbl.setObjectName(u"temp_2_lbl")
        self.temp_2_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_24.addWidget(self.temp_2_lbl)

        self.atmosphere_lbl = QLabel(self.widget_40)
        self.atmosphere_lbl.setObjectName(u"atmosphere_lbl")

        self.horizontalLayout_24.addWidget(self.atmosphere_lbl)

        self.humidity_lbl = QLabel(self.widget_40)
        self.humidity_lbl.setObjectName(u"humidity_lbl")

        self.horizontalLayout_24.addWidget(self.humidity_lbl)


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
        self.gridLayout.setContentsMargins(0, -1, 0, -1)
        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.widget_10.setStyleSheet(u"QLabel{\n"
"	border: 1px solid #ccc;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.widget_10)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.widget_8 = QWidget(self.widget_10)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 50))
        self.widget_8.setStyleSheet(u"")
        self.verticalLayout_4 = QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.wind_velocity_lbl = QLabel(self.widget_8)
        self.wind_velocity_lbl.setObjectName(u"wind_velocity_lbl")
        self.wind_velocity_lbl.setMinimumSize(QSize(140, 0))
        self.wind_velocity_lbl.setMaximumSize(QSize(16777215, 60))
        self.wind_velocity_lbl.setStyleSheet(u"")
        self.wind_velocity_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.wind_velocity_lbl, 0, Qt.AlignmentFlag.AlignHCenter)


        self.verticalLayout_3.addWidget(self.widget_8)

        self.widget_41 = QWidget(self.widget_10)
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


        self.verticalLayout_3.addWidget(self.widget_41)

        self.widget_12 = QWidget(self.widget_10)
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


        self.verticalLayout_3.addWidget(self.widget_12, 0, Qt.AlignmentFlag.AlignBottom)

        self.widget_11 = QWidget(self.widget_10)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setMinimumSize(QSize(0, 40))
        self.widget_11.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.widget_33 = QWidget(self.widget_11)
        self.widget_33.setObjectName(u"widget_33")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_33)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.widget_33)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 35))
        self.pushButton.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_7.addWidget(self.pushButton)


        self.horizontalLayout_5.addWidget(self.widget_33)

        self.widget_39 = QWidget(self.widget_11)
        self.widget_39.setObjectName(u"widget_39")
        self.widget_39.setMaximumSize(QSize(270, 16777215))
        self.horizontalLayout_35 = QHBoxLayout(self.widget_39)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.hz_sld = QSlider(self.widget_39)
        self.hz_sld.setObjectName(u"hz_sld")
        self.hz_sld.setMaximumSize(QSize(250, 16777215))
        self.hz_sld.setStyleSheet(u"")
        self.hz_sld.setMaximum(100)
        self.hz_sld.setOrientation(Qt.Orientation.Horizontal)
        self.hz_sld.setTickPosition(QSlider.TickPosition.TicksBelow)
        self.hz_sld.setTickInterval(1)

        self.horizontalLayout_35.addWidget(self.hz_sld)


        self.horizontalLayout_5.addWidget(self.widget_39)

        self.widget_50 = QWidget(self.widget_11)
        self.widget_50.setObjectName(u"widget_50")
        self.horizontalLayout_36 = QHBoxLayout(self.widget_50)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.speed_avg_cb = QCheckBox(self.widget_50)
        self.speed_avg_cb.setObjectName(u"speed_avg_cb")

        self.horizontalLayout_36.addWidget(self.speed_avg_cb)


        self.horizontalLayout_5.addWidget(self.widget_50)


        self.verticalLayout_3.addWidget(self.widget_11)


        self.gridLayout.addWidget(self.widget_10, 1, 0, 1, 1)


        self.horizontalLayout_4.addWidget(self.widget_6)


        self.verticalLayout.addWidget(self.widget_3)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_5 = QVBoxLayout(self.widget_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(3, -1, 3, 0)
        self.widget_13 = QWidget(self.widget_2)
        self.widget_13.setObjectName(u"widget_13")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget_13.sizePolicy().hasHeightForWidth())
        self.widget_13.setSizePolicy(sizePolicy2)
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
        self.label_6 = QLabel(self.widget_24)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_6)


        self.verticalLayout_12.addWidget(self.widget_24)

        self.widget_25 = QWidget(self.scale_view_pg)
        self.widget_25.setObjectName(u"widget_25")
        self.horizontalLayout_10 = QHBoxLayout(self.widget_25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(1, 1, 1, 1)
        self.widget_26 = QWidget(self.widget_25)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_14 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pressure_x = QLabel(self.widget_26)
        self.pressure_x.setObjectName(u"pressure_x")

        self.horizontalLayout_14.addWidget(self.pressure_x)

        self.pressure_y = QLabel(self.widget_26)
        self.pressure_y.setObjectName(u"pressure_y")

        self.horizontalLayout_14.addWidget(self.pressure_y)


        self.horizontalLayout_10.addWidget(self.widget_26)

        self.widget_27 = QWidget(self.widget_25)
        self.widget_27.setObjectName(u"widget_27")
        self.widget_27.setMaximumSize(QSize(500, 16777215))
        self.horizontalLayout_15 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.mz_lbl = QLabel(self.widget_27)
        self.mz_lbl.setObjectName(u"mz_lbl")
        self.mz_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout_15.addWidget(self.mz_lbl)


        self.horizontalLayout_10.addWidget(self.widget_27)


        self.verticalLayout_12.addWidget(self.widget_25)

        self.widget_18 = QWidget(self.scale_view_pg)
        self.widget_18.setObjectName(u"widget_18")
        sizePolicy2.setHeightForWidth(self.widget_18.sizePolicy().hasHeightForWidth())
        self.widget_18.setSizePolicy(sizePolicy2)
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


        self.horizontalLayout.addWidget(self.widget_2)

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
        self.vfd_btn.setText(QCoreApplication.translate("MainWindow", u"Turn on VFD", None))
        self.temp_1_lbl.setText(QCoreApplication.translate("MainWindow", u"T1 = XX", None))
        self.temp_2_lbl.setText(QCoreApplication.translate("MainWindow", u"T2 = XX", None))
        self.atmosphere_lbl.setText(QCoreApplication.translate("MainWindow", u"Atm P = XX", None))
        self.humidity_lbl.setText(QCoreApplication.translate("MainWindow", u"Humidity = XX", None))
        self.wind_velocity_lbl.setText(QCoreApplication.translate("MainWindow", u"ms", None))
        self.velocity_pressure_lbl.setText(QCoreApplication.translate("MainWindow", u"Pa", None))
        self.hz_lbl.setText(QCoreApplication.translate("MainWindow", u"Hz", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Cooling On ", None))
        self.speed_avg_cb.setText(QCoreApplication.translate("MainWindow", u"Average", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Aerodynamic balance: lift, drag, pitching torque", None))
        self.pressure_x.setText(QCoreApplication.translate("MainWindow", u"Fx = XX.X N", None))
        self.pressure_y.setText(QCoreApplication.translate("MainWindow", u"Fy = XX.X N", None))
        self.mz_lbl.setText(QCoreApplication.translate("MainWindow", u"Mz = X.XX N.m", None))
        self.gerlitz_logo_lbl.setText("")
        self.j4_logo_lbl.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

