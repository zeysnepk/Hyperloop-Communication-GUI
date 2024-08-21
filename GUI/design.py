from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1660, 1064)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setSpacing(12)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setSpacing(12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(12, 0, 12, 12)
        self.horizontalLayout_2.setSpacing(12)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_date = QtWidgets.QLabel(self.centralwidget)
        self.label_date.setMaximumSize(QtCore.QSize(189, 19))
        self.label_date.setStyleSheet("font:14pt \"Chakra Petch\";\n"
"color: rgb(192, 192, 192);")
        self.label_date.setAlignment(QtCore.Qt.AlignCenter)
        self.label_date.setObjectName("label_date")
        self.verticalLayout.addWidget(self.label_date)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame_power = QtWidgets.QFrame(self.centralwidget)
        self.frame_power.setMinimumSize(QtCore.QSize(180, 180))
        self.frame_power.setMaximumSize(QtCore.QSize(180, 180))
        self.frame_power.setStyleSheet("#frame_power{\n"
"background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:0.0 rgba(255, 255, 255, 0), stop:0.001 rgba(69, 150, 255, 255));\n"
"border-radius:90px\n"
"}")
        self.frame_power.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_power.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_power.setObjectName("frame_power")
        self.frame_full_2 = QtWidgets.QFrame(self.frame_power)
        self.frame_full_2.setGeometry(QtCore.QRect(10, 10, 160, 160))
        self.frame_full_2.setMinimumSize(QtCore.QSize(160, 160))
        self.frame_full_2.setMaximumSize(QtCore.QSize(160, 160))
        self.frame_full_2.setStyleSheet("#frame_full_2{\n"
"    \n"
"    \n"
"    background-color: rgb(50, 50, 50);\n"
"    border-radius:80px\n"
"}")
        self.frame_full_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_full_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_full_2.setObjectName("frame_full_2")
        self.label_4 = QtWidgets.QLabel(self.frame_full_2)
        self.label_4.setGeometry(QtCore.QRect(20, 50, 121, 41))
        self.label_4.setMinimumSize(QtCore.QSize(121, 41))
        self.label_4.setMaximumSize(QtCore.QSize(121, 41))
        self.label_4.setStyleSheet("#label_4{\n"
"font: 15pt \"Microsoft Sans Serif\";\n"
"font-weight:bold;\n"
"color: rgb(108, 195, 255);\n"
"}\n"
"")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_watt = QtWidgets.QLabel(self.frame_full_2)
        self.label_watt.setGeometry(QtCore.QRect(0, 90, 161, 20))
        self.label_watt.setMinimumSize(QtCore.QSize(161, 20))
        self.label_watt.setMaximumSize(QtCore.QSize(161, 20))
        self.label_watt.setStyleSheet("#label_watt{\n"
"font: 16pt \"Microsoft Sans Serif\";\n"
"}")
        self.label_watt.setAlignment(QtCore.Qt.AlignCenter)
        self.label_watt.setObjectName("label_watt")
        self.line_2 = QtWidgets.QFrame(self.frame_full_2)
        self.line_2.setGeometry(QtCore.QRect(10, 80, 141, 20))
        self.line_2.setMinimumSize(QtCore.QSize(141, 20))
        self.line_2.setMaximumSize(QtCore.QSize(141, 20))
        self.line_2.setStyleSheet("")
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.verticalLayout.addWidget(self.frame_power)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout.addItem(spacerItem1)
        self.line_5 = QtWidgets.QFrame(self.centralwidget)
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.verticalLayout.addWidget(self.line_5)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.frame_temp = QtWidgets.QFrame(self.centralwidget)
        self.frame_temp.setMinimumSize(QtCore.QSize(170, 230))
        self.frame_temp.setMaximumSize(QtCore.QSize(170, 230))
        self.frame_temp.setStyleSheet("#frame_temp{\n"
"image: url(:/temp/Untitled design-6.png);\n"
"}")
        self.frame_temp.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_temp.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_temp.setObjectName("frame_temp")
        self.frame_full = QtWidgets.QFrame(self.frame_temp)
        self.frame_full.setGeometry(QtCore.QRect(63, 160, 44, 44))
        self.frame_full.setMinimumSize(QtCore.QSize(44, 44))
        self.frame_full.setMaximumSize(QtCore.QSize(44, 44))
        self.frame_full.setStyleSheet("#frame_full{\n"
"    background-color: rgb(69, 150, 255);\n"
"    border-radius:22px\n"
"}")
        self.frame_full.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_full.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_full.setObjectName("frame_full")
        self.frame_t1 = QtWidgets.QFrame(self.frame_temp)
        self.frame_t1.setGeometry(QtCore.QRect(75, 30, 8, 140))
        self.frame_t1.setMinimumSize(QtCore.QSize(8, 140))
        self.frame_t1.setMaximumSize(QtCore.QSize(8, 140))
        self.frame_t1.setStyleSheet("#frame_t1{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0 rgba(69, 150, 255, 255), stop:0.001 rgba(255, 255, 255, 0));\n"
"}")
        self.frame_t1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_t1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t1.setObjectName("frame_t1")
        self.frame_t2 = QtWidgets.QFrame(self.frame_temp)
        self.frame_t2.setGeometry(QtCore.QRect(86, 30, 8, 140))
        self.frame_t2.setMinimumSize(QtCore.QSize(8, 140))
        self.frame_t2.setMaximumSize(QtCore.QSize(8, 140))
        self.frame_t2.setStyleSheet("#frame_t2{\n"
"    background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:1, y2:0, stop:0.0 rgba(69, 150, 255, 255), stop:0.001 rgba(255, 255, 255, 0));\n"
"}")
        self.frame_t2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_t2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t2.setObjectName("frame_t2")
        self.label = QtWidgets.QLabel(self.frame_temp)
        self.label.setGeometry(QtCore.QRect(45, 20, 21, 21))
        self.label.setMinimumSize(QtCore.QSize(21, 21))
        self.label.setMaximumSize(QtCore.QSize(21, 21))
        self.label.setStyleSheet("#label{\n"
"font:700 22pt \"Chakra Petch\";\n"
"    color: rgb(118, 214, 255);\n"
"}")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_temp)
        self.label_2.setGeometry(QtCore.QRect(100, 20, 31, 21))
        self.label_2.setMinimumSize(QtCore.QSize(31, 21))
        self.label_2.setMaximumSize(QtCore.QSize(31, 21))
        self.label_2.setStyleSheet("#label_2{\n"
"font:700 22pt \"Chakra Petch\";\n"
"    color: rgb(118, 214, 255);\n"
"}")
        self.label_2.setObjectName("label_2")
        self.frame_t1.raise_()
        self.frame_t2.raise_()
        self.frame_full.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.verticalLayout.addWidget(self.frame_temp)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.graph_position = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_position.sizePolicy().hasHeightForWidth())
        self.graph_position.setSizePolicy(sizePolicy)
        self.graph_position.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_position.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_position.setObjectName("graph_position")
        self.verticalLayout_3.addWidget(self.graph_position)
        self.graph_speed = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_speed.sizePolicy().hasHeightForWidth())
        self.graph_speed.setSizePolicy(sizePolicy)
        self.graph_speed.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_speed.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_speed.setObjectName("graph_speed")
        self.verticalLayout_3.addWidget(self.graph_speed)
        self.graph_acc = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_acc.sizePolicy().hasHeightForWidth())
        self.graph_acc.setSizePolicy(sizePolicy)
        self.graph_acc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_acc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_acc.setObjectName("graph_acc")
        self.verticalLayout_3.addWidget(self.graph_acc)
        self.graph_ori = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graph_ori.sizePolicy().hasHeightForWidth())
        self.graph_ori.setSizePolicy(sizePolicy)
        self.graph_ori.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.graph_ori.setFrameShadow(QtWidgets.QFrame.Raised)
        self.graph_ori.setObjectName("graph_ori")
        self.verticalLayout_3.addWidget(self.graph_ori)
        self.label_info = QtWidgets.QLabel(self.centralwidget)
        self.label_info.setStyleSheet("#label_info{\n"
"font: 700 16pt \"Chakra Petch\";\n"
"}")
        self.label_info.setAlignment(QtCore.Qt.AlignCenter)
        self.label_info.setObjectName("label_info")
        self.verticalLayout_3.addWidget(self.label_info)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2.setStretch(2, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout.setSpacing(12)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(192, 192, 192);")
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_4.addWidget(self.label_11)
        self.label_time = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Chakra Petch")
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        self.label_time.setFont(font)
        self.label_time.setStyleSheet("\n"
"font: 700 30pt \"Chakra Petch\";\n"
"color: rgb(192, 192, 192);")
        self.label_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_time.setObjectName("label_time")
        self.verticalLayout_4.addWidget(self.label_time)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_16 = QtWidgets.QLabel(self.frame_2)
        self.label_16.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(122, 129, 255);")
        self.label_16.setAlignment(QtCore.Qt.AlignCenter)
        self.label_16.setObjectName("label_16")
        self.verticalLayout_5.addWidget(self.label_16)
        self.label_serit = QtWidgets.QLabel(self.frame_2)
        self.label_serit.setStyleSheet("font:700 30pt \"Chakra Petch\";\n"
"color: rgb(122, 129, 255);")
        self.label_serit.setAlignment(QtCore.Qt.AlignCenter)
        self.label_serit.setObjectName("label_serit")
        self.verticalLayout_5.addWidget(self.label_serit)
        self.horizontalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_18 = QtWidgets.QLabel(self.frame_3)
        self.label_18.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(255, 38, 0);")
        self.label_18.setAlignment(QtCore.Qt.AlignCenter)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_6.addWidget(self.label_18)
        self.label_batarya = QtWidgets.QLabel(self.frame_3)
        self.label_batarya.setStyleSheet("font:700 30pt \"Chakra Petch\";\n"
"color: rgb(255, 38, 0);")
        self.label_batarya.setAlignment(QtCore.Qt.AlignCenter)
        self.label_batarya.setObjectName("label_batarya")
        self.verticalLayout_6.addWidget(self.label_batarya)
        self.horizontalLayout.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_20 = QtWidgets.QLabel(self.frame_4)
        self.label_20.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(118, 214, 255);")
        self.label_20.setAlignment(QtCore.Qt.AlignCenter)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_7.addWidget(self.label_20)
        self.label_data_speed = QtWidgets.QLabel(self.frame_4)
        self.label_data_speed.setStyleSheet("font:700 24pt \"Chakra Petch\";\n"
"color: rgb(118, 214, 255);")
        self.label_data_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_data_speed.setObjectName("label_data_speed")
        self.verticalLayout_7.addWidget(self.label_data_speed)
        self.horizontalLayout.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_22 = QtWidgets.QLabel(self.frame_5)
        self.label_22.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(255, 251, 0);")
        self.label_22.setAlignment(QtCore.Qt.AlignCenter)
        self.label_22.setObjectName("label_22")
        self.verticalLayout_8.addWidget(self.label_22)
        self.label_stat = QtWidgets.QLabel(self.frame_5)
        self.label_stat.setStyleSheet("font:700 30pt \"Chakra Petch\";\n"
"color: rgb(148, 17, 0);")
        self.label_stat.setAlignment(QtCore.Qt.AlignCenter)
        self.label_stat.setObjectName("label_stat")
        self.verticalLayout_8.addWidget(self.label_stat)
        self.horizontalLayout.addWidget(self.frame_5)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(12, 12, 12, 12)
        self.horizontalLayout_3.setSpacing(12)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.pushButton_start = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_start.sizePolicy().hasHeightForWidth())
        self.pushButton_start.setSizePolicy(sizePolicy)
        self.pushButton_start.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_start.setStyleSheet("QPushButton {\n"
"background-color: rgb(146, 199, 113);\n"
"background-image: linear-gradient(to bottom, #E57373, #E53935);\n"
"color: rgb(255, 217, 200);\n"
"font: 22pt;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"border: 6px solid #50A140;\n"
"padding: 10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #50A140;\n"
"background-image: linear-gradient(to bottom, #EF5350, #C62828);\n"
"border: 2px solid #3B7920;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #50A140;\n"
"background-image: linear-gradient(to bottom, #EF5350, #B71C1C);\n"
"border: 2px solid  #3B7920;\n"
"padding-left: 6p;\n"
"padding-top: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #E0E0E0;\n"
"color: #AAAAAA;\n"
"border: 2px solid #CCCCCC;\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/basla/basla.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_start.setIcon(icon)
        self.pushButton_start.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_start.setObjectName("pushButton_start")
        self.horizontalLayout_3.addWidget(self.pushButton_start)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButton_stop = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_stop.sizePolicy().hasHeightForWidth())
        self.pushButton_stop.setSizePolicy(sizePolicy)
        self.pushButton_stop.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_stop.setStyleSheet("QPushButton {\n"
"background-color: #E74C3C;\n"
"background-image: linear-gradient(to bottom, #E57373, #E53935);\n"
"color: rgb(255, 217, 200);\n"
"font: 22pt;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"border: 6px solid #B22222;\n"
"padding: 10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #D32F2F;\n"
"background-image: linear-gradient(to bottom, #EF5350, #C62828);\n"
"border: 2px solid #8B0000;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #C62828;\n"
"background-image: linear-gradient(to bottom, #EF5350, #B71C1C);\n"
"border: 2px solid #880000;\n"
"padding-left: 6p;\n"
"padding-top: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #E0E0E0;\n"
"color: #AAAAAA;\n"
"border: 2px solid #CCCCCC;\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/dur/dur.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_stop.setIcon(icon1)
        self.pushButton_stop.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.horizontalLayout_3.addWidget(self.pushButton_stop)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButton_go = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_go.sizePolicy().hasHeightForWidth())
        self.pushButton_go.setSizePolicy(sizePolicy)
        self.pushButton_go.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_go.setStyleSheet("QPushButton {\n"
"background-color: #5296D5;\n"
"background-image: linear-gradient(to bottom, #E57373, #E53935);\n"
"color: rgb(255, 217, 200);\n"
"font: 22pt;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"border: 6px solid #437EB4;\n"
"padding: 10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #437EB4;\n"
"background-image: linear-gradient(to bottom, #EF5350, #C62828);\n"
"border: 2px solid #3972AE;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #437EB4;\n"
"background-image: linear-gradient(to bottom, #EF5350, #B71C1C);\n"
"border: 2px solid   #3972AE;\n"
"padding-left: 6p;\n"
"padding-top: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #E0E0E0;\n"
"color: #AAAAAA;\n"
"border: 2px solid #CCCCCC;\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/ileri/ileri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_go.setIcon(icon2)
        self.pushButton_go.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_go.setObjectName("pushButton_go")
        self.horizontalLayout_3.addWidget(self.pushButton_go)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.pushButton_back = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_back.sizePolicy().hasHeightForWidth())
        self.pushButton_back.setSizePolicy(sizePolicy)
        self.pushButton_back.setMinimumSize(QtCore.QSize(200, 60))
        self.pushButton_back.setStyleSheet("QPushButton {\n"
"background-color: #5296D5;\n"
"background-image: linear-gradient(to bottom, #E57373, #E53935);\n"
"color: rgb(255, 217, 200);\n"
"font: 22pt;\n"
"font-weight: bold;\n"
"border-radius: 10px;\n"
"border: 6px solid #437EB4;\n"
"padding: 10px;\n"
"text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #437EB4;\n"
"background-image: linear-gradient(to bottom, #EF5350, #C62828);\n"
"border: 2px solid #3972AE;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: #437EB4;\n"
"background-image: linear-gradient(to bottom, #EF5350, #B71C1C);\n"
"border: 2px solid   #3972AE;\n"
"padding-left: 6p;\n"
"padding-top: 6px;\n"
"}\n"
"\n"
"QPushButton:disabled{\n"
"background-color: #E0E0E0;\n"
"color: #AAAAAA;\n"
"border: 2px solid #CCCCCC;\n"
"}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/geri/geri.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_back.setIcon(icon3)
        self.pushButton_back.setIconSize(QtCore.QSize(32, 32))
        self.pushButton_back.setObjectName("pushButton_back")
        self.horizontalLayout_3.addWidget(self.pushButton_back)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        self.verticalLayout_16 = QtWidgets.QVBoxLayout()
        self.verticalLayout_16.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_16.setSpacing(12)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_10.setSpacing(12)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_13 = QtWidgets.QLabel(self.frame_6)
        self.label_13.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(214, 214, 214);")
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_9.addWidget(self.label_13)
        self.label_position = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Chakra Petch")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_position.setFont(font)
        self.label_position.setStyleSheet("\n"
"font: 700 18pt \"Chakra Petch\";")
        self.label_position.setAlignment(QtCore.Qt.AlignCenter)
        self.label_position.setObjectName("label_position")
        self.verticalLayout_9.addWidget(self.label_position)
        self.verticalLayout_10.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_7)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.label_14 = QtWidgets.QLabel(self.frame_7)
        self.label_14.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(214, 214, 214);")
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_11.addWidget(self.label_14)
        self.label_speed = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setFamily("Chakra Petch")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_speed.setFont(font)
        self.label_speed.setStyleSheet("\n"
"font: 700 18pt \"Chakra Petch\";")
        self.label_speed.setAlignment(QtCore.Qt.AlignCenter)
        self.label_speed.setObjectName("label_speed")
        self.verticalLayout_11.addWidget(self.label_speed)
        self.verticalLayout_10.addWidget(self.frame_7)
        self.frame_8 = QtWidgets.QFrame(self.centralwidget)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.label_26 = QtWidgets.QLabel(self.frame_8)
        self.label_26.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(214, 214, 214);")
        self.label_26.setAlignment(QtCore.Qt.AlignCenter)
        self.label_26.setObjectName("label_26")
        self.verticalLayout_12.addWidget(self.label_26)
        self.label_acc = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setFamily("Chakra Petch")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_acc.setFont(font)
        self.label_acc.setStyleSheet("\n"
"font: 700 18pt \"Chakra Petch\";")
        self.label_acc.setAlignment(QtCore.Qt.AlignCenter)
        self.label_acc.setObjectName("label_acc")
        self.verticalLayout_12.addWidget(self.label_acc)
        self.verticalLayout_10.addWidget(self.frame_8)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_10.addItem(spacerItem9)
        self.frame_9 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_9)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label_28 = QtWidgets.QLabel(self.frame_9)
        self.label_28.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(214, 214, 214);")
        self.label_28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_28.setObjectName("label_28")
        self.verticalLayout_13.addWidget(self.label_28)
        self.label_ori = QtWidgets.QLabel(self.frame_9)
        font = QtGui.QFont()
        font.setFamily("Chakra Petch")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label_ori.setFont(font)
        self.label_ori.setStyleSheet("\n"
"font: 700 16pt \"Chakra Petch\";")
        self.label_ori.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ori.setObjectName("label_ori")
        self.verticalLayout_13.addWidget(self.label_ori)
        self.verticalLayout_10.addWidget(self.frame_9)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_10.addItem(spacerItem10)
        self.frame_t = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_t.sizePolicy().hasHeightForWidth())
        self.frame_t.setSizePolicy(sizePolicy)
        self.frame_t.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_t.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_t.setObjectName("frame_t")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_t)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.label_30 = QtWidgets.QLabel(self.frame_t)
        self.label_30.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(214, 214, 214);")
        self.label_30.setAlignment(QtCore.Qt.AlignCenter)
        self.label_30.setObjectName("label_30")
        self.verticalLayout_14.addWidget(self.label_30)
        self.label_temp = QtWidgets.QLabel(self.frame_t)
        font = QtGui.QFont()
        font.setFamily("Chakra Petch")
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        self.label_temp.setFont(font)
        self.label_temp.setStyleSheet("\n"
"font: 700 18pt \"Chakra Petch\";")
        self.label_temp.setAlignment(QtCore.Qt.AlignCenter)
        self.label_temp.setObjectName("label_temp")
        self.verticalLayout_14.addWidget(self.label_temp)
        self.verticalLayout_10.addWidget(self.frame_t)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_10.addItem(spacerItem11)
        self.frame_11 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.label_32 = QtWidgets.QLabel(self.frame_11)
        self.label_32.setStyleSheet("font:18pt \"Chakra Petch\";\n"
"color: rgb(214, 214, 214);")
        self.label_32.setAlignment(QtCore.Qt.AlignCenter)
        self.label_32.setObjectName("label_32")
        self.verticalLayout_15.addWidget(self.label_32)
        self.label_watt_2 = QtWidgets.QLabel(self.frame_11)
        font = QtGui.QFont()
        font.setFamily("Chakra Petch")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        self.label_watt_2.setFont(font)
        self.label_watt_2.setStyleSheet("\n"
"font: 700 16pt \"Chakra Petch\";")
        self.label_watt_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_watt_2.setObjectName("label_watt_2")
        self.verticalLayout_15.addWidget(self.label_watt_2)
        self.verticalLayout_10.addWidget(self.frame_11)
        self.frame_logo = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_logo.sizePolicy().hasHeightForWidth())
        self.frame_logo.setSizePolicy(sizePolicy)
        self.frame_logo.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_logo.setStyleSheet("#frame_logo{\n"
"    image: url(:/logo/Untitled design.png);\n"
"}")
        self.frame_logo.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_logo.setObjectName("frame_logo")
        self.verticalLayout_10.addWidget(self.frame_logo)
        self.verticalLayout_16.addLayout(self.verticalLayout_10)
        self.horizontalLayout_4.addLayout(self.verticalLayout_16)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1660, 24))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.graph_position.setLayout(QtWidgets.QVBoxLayout())
        self.graph_speed.setLayout(QtWidgets.QVBoxLayout())
        self.graph_acc.setLayout(QtWidgets.QVBoxLayout())
        self.graph_ori.setLayout(QtWidgets.QVBoxLayout())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_date.setText(_translate("MainWindow", "2 Ağustos 2024 28:34:05"))
        self.label_4.setText(_translate("MainWindow", "GÜÇ\n"
"TÜKETİMİ"))
        self.label_watt.setText(_translate("MainWindow", "0 W"))
        self.label.setText(_translate("MainWindow", "T1"))
        self.label_2.setText(_translate("MainWindow", "T2"))
        self.label_info.setText(_translate("MainWindow", "TextLabel"))
        self.label_11.setText(_translate("MainWindow", "Zaman\n"
"(saniye)"))
        self.label_time.setText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "Şerit Sayısı"))
        self.label_serit.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Batarya Durumu"))
        self.label_batarya.setText(_translate("MainWindow", "0"))
        self.label_20.setText(_translate("MainWindow", "Veri Alım Hızı"))
        self.label_data_speed.setText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "Araç Durumu"))
        self.label_stat.setText(_translate("MainWindow", "OFF"))
        self.pushButton_start.setText(_translate("MainWindow", "BAŞLA"))
        self.pushButton_stop.setText(_translate("MainWindow", "STOP"))
        self.pushButton_go.setText(_translate("MainWindow", "İLERİ"))
        self.pushButton_back.setText(_translate("MainWindow", "GERİ"))
        self.label_13.setText(_translate("MainWindow", "POZİSYON(m)"))
        self.label_position.setText(_translate("MainWindow", "X : \n"
"Y :\n"
"Z :"))
        self.label_14.setText(_translate("MainWindow", "HIZ(m/s)"))
        self.label_speed.setText(_translate("MainWindow", "X :\n"
"Y :\n"
"Z :"))
        self.label_26.setText(_translate("MainWindow", "İVME(m/s²)"))
        self.label_acc.setText(_translate("MainWindow", "X :\n"
"Y :\n"
"Z :"))
        self.label_28.setText(_translate("MainWindow", "YÖNELİM(°)"))
        self.label_ori.setText(_translate("MainWindow", "Roll :\n"
"Pitch :\n"
"Yaw :"))
        self.label_30.setText(_translate("MainWindow", "SICAKLIK(°C)"))
        self.label_temp.setText(_translate("MainWindow", "T1 :\n"
"T2 :"))
        self.label_32.setText(_translate("MainWindow", "GÜÇ TÜKETİMİ(Watt)"))
        self.label_watt_2.setText(_translate("MainWindow", "0"))
import pic_rc
