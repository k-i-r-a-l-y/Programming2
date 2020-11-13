# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'lab9JyWTjp.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

import worker as w
from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_MainWindow(object):

    workers = []

    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(452, 553)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 81, 41))
        font = QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 50, 81, 41))
        self.label_2.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 90, 81, 41))
        self.label_3.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 141, 41))
        self.label_4.setFont(font)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 170, 81, 41))
        self.label_5.setFont(font)
        self.in_name = QLineEdit(self.centralwidget)
        self.in_name.setObjectName(u"in_name")
        self.in_name.setGeometry(QRect(80, 20, 361, 21))
        self.in_idcode = QLineEdit(self.centralwidget)
        self.in_idcode.setObjectName(u"in_idcode")
        self.in_idcode.setGeometry(QRect(90, 60, 351, 21))
        self.in_address = QLineEdit(self.centralwidget)
        self.in_address.setObjectName(u"in_address")
        self.in_address.setGeometry(QRect(90, 100, 351, 21))
        self.in_phone_number = QLineEdit(self.centralwidget)
        self.in_phone_number.setObjectName(u"in_phone_number")
        self.in_phone_number.setGeometry(QRect(150, 140, 291, 21))
        self.in_email = QLineEdit(self.centralwidget)
        self.in_email.setObjectName(u"in_email")
        self.in_email.setGeometry(QRect(80, 180, 361, 21))
        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setGeometry(QRect(10, 220, 81, 41))
        self.btn_edit = QPushButton(self.centralwidget)
        self.btn_edit.setObjectName(u"btn_edit")
        self.btn_edit.setGeometry(QRect(120, 220, 81, 41))
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setGeometry(QRect(360, 220, 81, 41))
        self.btn_modify = QPushButton(self.centralwidget)
        self.btn_modify.setObjectName(u"btn_modify")
        self.btn_modify.setGeometry(QRect(240, 220, 81, 41))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 270, 131, 41))
        self.label_6.setFont(font)
        self.list_persons = QListWidget(self.centralwidget)
        self.list_persons.setObjectName(u"list_persons")
        self.list_persons.setGeometry(QRect(10, 310, 431, 231))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.btn_add.clicked.connect(self.add_or_modify_worker)
        self.btn_edit.clicked.connect(self.edit_worker)
        self.btn_modify.clicked.connect(self.add_or_modify_worker)
    # setupUi

    def edit_worker(self):
        worker = self.list_persons.currentItem().text()
        id = worker.split(",")[0]
        for worker in self.workers:
           if worker.get_id() == id:
                self.in_idcode.setText(worker.get_id())
                self.in_name.setText(worker.get_name())
                self.in_address.setText(worker.get_address())
                self.in_phone_number.setText(worker.get_phone_number())
                self.in_email.setText(worker.get_email())

    def print_workers(self):
        self.list_persons.clear()
        for worker in self.workers:
            self.list_persons.addItem(worker.__str__())

    def add_or_modify_worker(self):
        worker = w.Worker(self.in_idcode.text(),self.in_name.text(), self.in_address.text(), self.in_phone_number.text(), self.in_email.text())
        if worker not in self.workers:
            self.workers.append(worker)
            self.workers.sort()
            self.print_workers()
        else:
            for work_person in self.workers:
                if work_person == worker:
                    work_person.set_name(worker.get_name())
                    work_person.set_address(worker.get_address())
                    work_person.set_phone_number(worker.get_phone_number())
                    work_person.set_email(worker.get_email())
            self.print_workers()
        self.save_to_file()

    def save_to_file(self):
        f = open("database.txt","w")
        for worker in self.workers:
            print(worker.__str__(), file=f)
        f.close()

    def load_data_from_file(self):
        try:
            f = open("database.txt","r")
            for line in f:
                data = line.rstrip().split(",")
                worker = w.Worker(data[0], data[1], data[2], data[3], data[4])
                self.workers.append(worker)
            self.print_workers()
            f.close()
        except:
            pass

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Workers", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"ID code:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Phone number:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.in_phone_number.setPlaceholderText(QCoreApplication.translate("MainWindow", u"+36201234567", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.btn_edit.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.btn_modify.setText(QCoreApplication.translate("MainWindow", u"Modify", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"List of persons:", None))
    # retranslateUi

import sys
app = QApplication(sys.argv)
MainWindow = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.load_data_from_file()
MainWindow.show()
sys.exit(app.exec_())