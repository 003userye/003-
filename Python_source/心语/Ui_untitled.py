# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Python_source\心语\untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("background-image:url(D:/A_图片/hulu.jpg)")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 330, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{\n"
                                    "border:2px solid rgb(6,168,255); \n"
                                    "font-size:14px; \n"
                                    "border-radius:10px;\n"
                                    "}\n"
                                    "QLineEdit:hover{\n"
                                    "\n"
                                    "color:white;\n"
                                    "\n"
                                    "\n"
                                    "}")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.clicked.connect(self.showtext)
        self.pushButton.setGeometry(QtCore.QRect(250, 380, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(15)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{\n"
                                        "\n"
                                        "border:2px solid rgb(212,243,255);\n"
                                        "border-radius:15px;\n"
                                        "\n"
                                        "}\n"
                                        "\n"
                                        "QPushButton:hover{\n"
                                        "\n"
                                        "border:2px solid rgb(6,168,255);\n"
                                        "\n"
                                        "\n"
                                        "}\n"
                                        "")
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(180, 60, 256, 192))
        self.listWidget.setObjectName("listWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lineEdit.setText(_translate("MainWindow", "请输入文本"))
        self.pushButton.setText(_translate("MainWindow", "Try"))

    def showtext(self,MainWindow):
        text1 = self.lineEdit.text()
        self.pushButton.setText(text1)