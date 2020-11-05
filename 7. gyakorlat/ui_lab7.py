# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab7hbYrhE.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import lab6

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2 import QtWidgets
from PySide2.QtWidgets import *

class Ui_MainWindow(object):

    listTrain = {}

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(533, 484)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 47, 13))
        self.trainList = QListWidget(self.centralwidget)
        self.trainList.setObjectName(u"trainList")
        self.trainList.setGeometry(QRect(20, 60, 491, 101))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 180, 47, 13))
        self.stopsList = QListWidget(self.centralwidget)
        self.stopsList.setObjectName(u"stopsList")
        self.stopsList.setGeometry(QRect(20, 200, 491, 141))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 360, 47, 13))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(30, 400, 47, 13))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 360, 47, 13))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(320, 400, 47, 13))
        self.inId = QLineEdit(self.centralwidget)
        self.inId.setObjectName(u"inId")
        self.inId.setGeometry(QRect(80, 360, 161, 20))
        self.inArrival = QLineEdit(self.centralwidget)
        self.inArrival.setObjectName(u"inArrival")
        self.inArrival.setGeometry(QRect(80, 400, 161, 20))
        self.inName = QLineEdit(self.centralwidget)
        self.inName.setObjectName(u"inName")
        self.inName.setGeometry(QRect(350, 360, 161, 20))
        self.inDest = QLineEdit(self.centralwidget)
        self.inDest.setObjectName(u"inDest")
        self.inDest.setGeometry(QRect(350, 400, 161, 20))
        self.btnAddNew = QPushButton(self.centralwidget)
        self.btnAddNew.setObjectName(u"btnAddNew")
        self.btnAddNew.setGeometry(QRect(390, 440, 121, 31))
        self.btnOpen = QPushButton(self.centralwidget)
        self.btnOpen.setObjectName(u"btnOpen")
        self.btnOpen.setGeometry(QRect(20, 440, 121, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.btnAddNew.clicked.connect(self.create_new_train)
        self.btnOpen.clicked.connect(self.load_trains)
        self.trainList.itemClicked.connect(self.load_stops)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Inter City", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Trains:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Stops:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Id:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"From:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"To:", None))
        self.btnAddNew.setText(QCoreApplication.translate("MainWindow", u"Add new train", None))
        self.btnOpen.setText(QCoreApplication.translate("MainWindow", u"Load trains", None))
    # retranslateUi

    def create_new_train(self):
        t1 = lab6.IC(self.inId.text(),self.inName.text(),self.inArrival.text(), self.inDest.text())
        if t1.get_id() not in self.listTrain:
            self.trainList.addItem(t1.get_id() + " - " + t1.get_name())
            self.listTrain[t1.get_id()] = t1

    def load_trains(self):
        filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Select file...", "*.txt")
        f = open(filename,"r")
        for line in f:
            data = line.split(";")
            t1 = lab6.IC(data[0],data[1],data[2],data[3])
            if t1.get_id() not in self.listTrain:
                self.trainList.addItem(t1.get_id() + " - " + t1.get_name())
                self.listTrain[t1.get_id()] = t1


    def load_stops(self, item):
        self.stopsList.clear()
        tmp = item.text()
        tmp_list = tmp.split(" ")
        for stop in self.listTrain[tmp_list[0]].get_stops():
            self.stopsList.addItem(stop.__str__())

import sys
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec_())
