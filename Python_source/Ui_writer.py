# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Python_source\writer.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 618)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 618))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 618))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet("QMainWindow{\n"
"    \n"
"\n"
"    \n"
"}")
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setDockNestingEnabled(False)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Left_widget = QtWidgets.QWidget(self.centralwidget)
        self.Left_widget.setGeometry(QtCore.QRect(0, 0, 129, 595))
        self.Left_widget.setMaximumSize(QtCore.QSize(1000, 618))
        self.Left_widget.setStyleSheet("QWidget{\n"
"        color:#232C51;\n"
"        background:gray;\n"
"        border-top:1px solid darkGray;\n"
"        border-bottom:1px solid darkGray;\n"
"       \n"
"    }\n"
"QWidget{\n"
"    background:gray;\n"
"    border-top:1px solid white;\n"
"    border-bottom:1px solid white;\n"
"    border-left:1px solid white;\n"
"    border-top-left-radius:10px;\n"
"    border-bottom-left-radius:10px;\n"
"}")
        self.Left_widget.setObjectName("Left_widget")
        self.pushButton_ID = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_ID.setGeometry(QtCore.QRect(2, 80, 120, 23))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_ID.setFont(font)
        self.pushButton_ID.setStyleSheet("\n"
"color:yellow;\n"
"border:none\n"
"\n"
"")
        self.pushButton_ID.setObjectName("pushButton_ID")
        self.pushButton_WebLabel = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_WebLabel.setGeometry(QtCore.QRect(2, 370, 126, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_WebLabel.setFont(font)
        self.pushButton_WebLabel.setStyleSheet("QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("e:\\Python_source\\标签.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_WebLabel.setIcon(icon)
        self.pushButton_WebLabel.setObjectName("pushButton_WebLabel")
        self.pushButton_YunGongXiang = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_YunGongXiang.setGeometry(QtCore.QRect(2, 313, 126, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_YunGongXiang.setFont(font)
        self.pushButton_YunGongXiang.setStyleSheet("QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("e:\\Python_source\\共享_常规.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_YunGongXiang.setIcon(icon1)
        self.pushButton_YunGongXiang.setObjectName("pushButton_YunGongXiang")
        self.pushButton_Setting = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_Setting.setGeometry(QtCore.QRect(2, 427, 126, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_Setting.setFont(font)
        self.pushButton_Setting.setStyleSheet("QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("e:\\Python_source\\设置.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Setting.setIcon(icon2)
        self.pushButton_Setting.setObjectName("pushButton_Setting")
        self.pushButton_CallUs = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_CallUs.setGeometry(QtCore.QRect(2, 484, 126, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_CallUs.setFont(font)
        self.pushButton_CallUs.setStyleSheet("QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("e:\\Python_source\\客服.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_CallUs.setIcon(icon3)
        self.pushButton_CallUs.setObjectName("pushButton_CallUs")
        self.pushButton_About = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_About.setGeometry(QtCore.QRect(2, 541, 126, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_About.setFont(font)
        self.pushButton_About.setStyleSheet("\n"
"QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("e:\\Python_source\\关于.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_About.setIcon(icon4)
        self.pushButton_About.setObjectName("pushButton_About")
        self.pushButton_KuoZhan = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_KuoZhan.setGeometry(QtCore.QRect(2, 142, 126, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_KuoZhan.setFont(font)
        self.pushButton_KuoZhan.setStyleSheet("QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("e:\\Python_source\\添加.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_KuoZhan.setIcon(icon5)
        self.pushButton_KuoZhan.setObjectName("pushButton_KuoZhan")
        self.pushButton_WoDeChuangZuo = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_WoDeChuangZuo.setGeometry(QtCore.QRect(2, 199, 126, 40))
        self.pushButton_WoDeChuangZuo.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_WoDeChuangZuo.setFont(font)
        self.pushButton_WoDeChuangZuo.setStyleSheet("\n"
"QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("e:\\Python_source\\我的 (1).png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_WoDeChuangZuo.setIcon(icon6)
        self.pushButton_WoDeChuangZuo.setObjectName("pushButton_WoDeChuangZuo")
        self.pushButton_XuunZhaoLingGan = QtWidgets.QPushButton(self.Left_widget)
        self.pushButton_XuunZhaoLingGan.setGeometry(QtCore.QRect(2, 256, 126, 40))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton_XuunZhaoLingGan.setFont(font)
        self.pushButton_XuunZhaoLingGan.setStyleSheet("QPushButton{\n"
"        border:none;\n"
"        color:white;\n"
"        font-size:12px;\n"
"        height:40px;\n"
"        padding-left:5px;\n"
"        padding-right:10px;\n"
"       \n"
"    }\n"
"    QPushButton:hover{\n"
"        color:black;\n"
"        border:1px solid #F3F3F5;\n"
"        border-radius:10px;\n"
"        background:LightGray;\n"
"    }")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("e:\\Python_source\\灵感.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_XuunZhaoLingGan.setIcon(icon7)
        self.pushButton_XuunZhaoLingGan.setObjectName("pushButton_XuunZhaoLingGan")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(129, 0, 871, 595))
        self.widget.setStyleSheet("QWidget{\n"
"        color:#232C51;\n"
"        background:gray;\n"
"        border-top:1px solid darkGray;\n"
"        border-bottom:1px solid darkGray;\n"
"        border-right:1px solid darkGray;\n"
"        border-top-right-radius:10px;\n"
"        border-bottom-right-radius:10px;\n"
"    }\n"
"QWidget{\n"
"    background:white;\n"
"    border-top:1px solid white;\n"
"    border-bottom:1px solid white;\n"
"    border-left:1px solid white;\n"
"}")
        self.widget.setObjectName("widget")
        self.lineEdit_Seek = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_Seek.setGeometry(QtCore.QRect(50, 10, 531, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.lineEdit_Seek.setFont(font)
        self.lineEdit_Seek.setStyleSheet("QLineEdit{\n"
"    border-color: rgb(25, 25, 25);\n"
"border-radius:10px;\n"
"}")
        self.lineEdit_Seek.setText("")
        self.lineEdit_Seek.setObjectName("lineEdit_Seek")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(10, 12, 30, 30))
        font = QtGui.QFont()
        font.setFamily("楷体")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("QLabel{\n"
"\n"
"border:none\n"
"\n"
"}")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("e:\\Python_source\\搜索.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.pushButton_Close = QtWidgets.QPushButton(self.widget)
        self.pushButton_Close.setGeometry(QtCore.QRect(820, 20, 25, 25))
        self.pushButton_Close.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_Close.setStyleSheet("QPushButton{\n"
"\n"
"background:#F76677;\n"
"\n"
"border-radius:10px;\n"
"\n"
"\n"
"}")
        self.pushButton_Close.setText("")
        self.pushButton_Close.setObjectName("pushButton_Close")
        self.pushButton_Min = QtWidgets.QPushButton(self.widget)
        self.pushButton_Min.setGeometry(QtCore.QRect(700, 20, 25, 25))
        self.pushButton_Min.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_Min.setStatusTip("")
        self.pushButton_Min.setStyleSheet("QPushButton{\n"
"\n"
"background:#6DDF6D;\n"
"\n"
"border-radius:10px;\n"
"\n"
"}")
        self.pushButton_Min.setText("")
        self.pushButton_Min.setObjectName("pushButton_Min")
        self.pushButton_Break = QtWidgets.QPushButton(self.widget)
        self.pushButton_Break.setGeometry(QtCore.QRect(760, 20, 25, 25))
        self.pushButton_Break.setMaximumSize(QtCore.QSize(25, 25))
        self.pushButton_Break.setStyleSheet("QPushButton{\n"
"\n"
"background:#F7D674;\n"
"\n"
"border-radius:10px;\n"
"\n"
"}")
        self.pushButton_Break.setText("")
        self.pushButton_Break.setObjectName("pushButton_Break")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(50, 90, 124, 200))
        self.label_2.setStyleSheet("QLabel{\n"
"\n"
"border-color:#ffff00;\n"
"\n"
"border-radius:0px;\n"
"       \n"
"}\n"
"   QLabel:hover{\n"
"        border:5px solid blue;\n"
"        border-radius:0px;\n"
"        background:LightGray;\n"
"    }")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Administrator/Desktop/书封/1597316318(1).png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_Close.clicked.connect(MainWindow.close)
        self.pushButton_Min.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_ID.setText(_translate("MainWindow", "003"))
        self.pushButton_WebLabel.setText(_translate("MainWindow", "网站标签"))
        self.pushButton_YunGongXiang.setText(_translate("MainWindow", "云共享"))
        self.pushButton_Setting.setText(_translate("MainWindow", "设置"))
        self.pushButton_CallUs.setText(_translate("MainWindow", "联系我们"))
        self.pushButton_About.setText(_translate("MainWindow", "关于"))
        self.pushButton_KuoZhan.setText(_translate("MainWindow", "扩展"))
        self.pushButton_WoDeChuangZuo.setText(_translate("MainWindow", "我的创作"))
        self.pushButton_XuunZhaoLingGan.setText(_translate("MainWindow", "找寻灵感"))
        self.lineEdit_Seek.setPlaceholderText(_translate("MainWindow", "搜索本地书集+我的创作"))
        self.pushButton_Close.setToolTip(_translate("MainWindow", "关闭"))
        self.pushButton_Min.setToolTip(_translate("MainWindow", "最小化"))
        self.pushButton_Break.setToolTip(_translate("MainWindow", "休眠"))