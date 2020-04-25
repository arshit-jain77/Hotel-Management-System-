# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'payment.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from online import *
from card import *
from cash import *

class Ui_Form4(object):

    def nextwindow(self,upi,card,cash):

        if upi:
            self.open_upi()
        elif card:
            self.open_card()
        elif cash:
            self.open_cash()

    def open_upi(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form7()
        self.ui.setup(self.window)
        self.window.show()

    def open_card(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form8()
        self.ui.setup(self.window)
        self.window.show()

    def open_cash(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form9()
        self.ui.setup(self.window)
        self.window.show()

    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(612, 551)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 571, 511))
        self.frame_2.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"background-color: rgb(54, 54, 54);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(110, 40, 381, 71))
        self.label.setStyleSheet("font: 25 20pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label.setObjectName("label")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(150, 180, 261, 31))
        self.radioButton.setStyleSheet("color: rgb(207, 207, 207);\n"
"font: 16pt \"Baskerville Old Face\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 270, 261, 31))
        self.radioButton_2.setStyleSheet("color: rgb(207, 207, 207);\n"
"font: 16pt \"Baskerville Old Face\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(150, 360, 311, 31))
        self.radioButton_3.setStyleSheet("color: rgb(207, 207, 207);\n"
"font: 16pt \"Baskerville Old Face\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(360, 440, 171, 41))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(253, 255, 229);\n"
"font: 16pt \"Bernard MT Condensed\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(0, 85, 255);\n"
"color: rgb(253, 255, 229);\n"
"font: 16pt \"Bernard MT Condensed\";\n"
"}\n"
"")
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(lambda:(self.nextwindow(self.radioButton.isChecked(),self.radioButton_2.isChecked(),self.radioButton_3.isChecked())))

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Mode Of Payment"))
        self.radioButton.setText(_translate("Form", "UPI"))
        self.radioButton_2.setText(_translate("Form", "Debit / Credit Card"))
        self.radioButton_3.setText(_translate("Form", "Cash"))
        self.pushButton.setText(_translate("Form", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form4()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
