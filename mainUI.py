# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(954, 550)
        MainWindow.setMinimumSize(QtCore.QSize(954, 550))
        MainWindow.setMaximumSize(QtCore.QSize(954, 550))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/res/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/res/background.png);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.keywordEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.keywordEdit.setGeometry(QtCore.QRect(680, 70, 215, 230))
        self.keywordEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.keywordEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.keywordEdit.setStyleSheet("background: rgb(255,102,102,100);\n"
"border:2px solid rgba(255,102,102,255); \n"
"border-radius:15px;\n"
"font: 11pt \"微软雅黑\";")
        self.keywordEdit.setObjectName("keywordEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(690, 40, 171, 30))
        self.label.setStyleSheet("background: rgb(255,102,102,0);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 40, 171, 30))
        self.label_2.setStyleSheet("background: rgb(255,102,102,0);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(360, 40, 221, 30))
        self.label_3.setStyleSheet("background: rgb(255,102,102,0);")
        self.label_3.setObjectName("label_3")
        self.checkButton_Label = QtWidgets.QLabel(self.centralwidget)
        self.checkButton_Label.setGeometry(QtCore.QRect(520, 330, 200, 200))
        self.checkButton_Label.setMinimumSize(QtCore.QSize(0, 0))
        self.checkButton_Label.setMaximumSize(QtCore.QSize(1999999, 199999))
        self.checkButton_Label.setAutoFillBackground(False)
        self.checkButton_Label.setStyleSheet("background: rgb(255, 255, 255, 0);\n"
"")
        self.checkButton_Label.setText("")
        self.checkButton_Label.setObjectName("checkButton_Label")
        self.loading_Label = QtWidgets.QLabel(self.centralwidget)
        self.loading_Label.setGeometry(QtCore.QRect(480, 420, 200, 80))
        self.loading_Label.setMinimumSize(QtCore.QSize(200, 80))
        self.loading_Label.setMaximumSize(QtCore.QSize(200, 80))
        self.loading_Label.setAutoFillBackground(False)
        self.loading_Label.setStyleSheet("background: rgb(255, 255, 255, 0);")
        self.loading_Label.setText("")
        self.loading_Label.setObjectName("loading_Label")
        self.resultEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.resultEdit.setGeometry(QtCore.QRect(345, 70, 271, 320))
        self.resultEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.resultEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.resultEdit.setStyleSheet("background: rgb(153,204,153,100);\n"
"border:2px solid rgba(153,204,153,255);\n"
"font: 11pt \"微软雅黑\";\n"
"border-radius:15px;")
        self.resultEdit.setObjectName("resultEdit")
        self.siteEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.siteEdit.setGeometry(QtCore.QRect(21, 70, 280, 320))
        self.siteEdit.setMinimumSize(QtCore.QSize(0, 0))
        self.siteEdit.setMaximumSize(QtCore.QSize(16777215, 19999))
        self.siteEdit.setStyleSheet("background: rgb(153,204,153,0);\n"
"border:2px solid rgba(153,204,153,255); \n"
"font: 11pt \"微软雅黑\";\n"
"border-radius:15px;")
        self.siteEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.siteEdit.setObjectName("siteEdit")
        self.msgLabel = QtWidgets.QLabel(self.centralwidget)
        self.msgLabel.setGeometry(QtCore.QRect(50, 410, 421, 98))
        self.msgLabel.setStyleSheet("background-image: url(:/newPrefix/res/msgbox.png);")
        self.msgLabel.setObjectName("msgLabel")
        self.titleBar = QtWidgets.QLabel(self.centralwidget)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 954, 29))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.titleBar.setFont(font)
        self.titleBar.setMouseTracking(True)
        self.titleBar.setStyleSheet("background: rgb(255,220,209,0);")
        self.titleBar.setObjectName("titleBar")
        self.hidenButton = QtWidgets.QPushButton(self.centralwidget)
        self.hidenButton.setGeometry(QtCore.QRect(890, 0, 30, 28))
        self.hidenButton.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/res/hind.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.hidenButton.setIcon(icon1)
        self.hidenButton.setObjectName("hidenButton")
        self.closeButton = QtWidgets.QPushButton(self.centralwidget)
        self.closeButton.setGeometry(QtCore.QRect(920, 0, 30, 28))
        self.closeButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/res/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setObjectName("closeButton")
        self.resultEdit.raise_()
        self.siteEdit.raise_()
        self.keywordEdit.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.loading_Label.raise_()
        self.checkButton_Label.raise_()
        self.msgLabel.raise_()
        self.titleBar.raise_()
        self.hidenButton.raise_()
        self.closeButton.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 954, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "小猫咪的工具箱"))
        self.label.setText(_translate("MainWindow", "邮箱关键字"))
        self.label_2.setText(_translate("MainWindow", "网站(去掉www)"))
        self.label_3.setText(_translate("MainWindow", "探测到的邮箱"))
        self.msgLabel.setText(_translate("MainWindow", "  点我，喵~~"))
        self.titleBar.setText(_translate("MainWindow", "  小猫咪的工具箱"))

import res_rc
