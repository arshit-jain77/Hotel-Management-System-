# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pass_msg2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from details import *


class Ui_Form2(object):

    def details(self):
        from details import Ui_Form
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setup(self.window)
        self.window.show()

    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(553, 229)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(10, 20, 531, 191))
        self.frame.setStyleSheet("background-color: rgb(115, 115, 115);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(130, 40, 381, 61))
        self.label_2.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(30, 40, 81, 71))
        self.label.setStyleSheet("image: url(:/newPrefix/verified.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 120, 171, 41))
        self.pushButton_3.setStyleSheet("QPushButton\n"
"{\n"
"border-radius:15px;\n"
"background-color: rgb(0, 170, 255);\n"
"color: rgb(253, 255, 229);\n"
"font: 16pt \"Bernard MT Condensed\";\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"background-color: rgb(0, 85, 255);\n"
"color: rgb(253, 255, 229);\n"
"font: 16pt \"Bernard MT Condensed\";\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_3.clicked.connect(self.details)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", " You have entered the Valid Password."))
        self.pushButton_3.setText(_translate("Form", "Continue"))

import verify
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form2()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
