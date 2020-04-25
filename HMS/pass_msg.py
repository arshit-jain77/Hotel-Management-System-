# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pass_msg.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
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
        self.label_2.setGeometry(QtCore.QRect(140, 20, 381, 61))
        self.label_2.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(180, 90, 241, 61))
        self.label_3.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(20, 60, 111, 81))
        self.label.setStyleSheet("image: url(:/newPrefix/circle-cropped.png);")
        self.label.setText("")
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "You have entered the invalid password."))
        self.label_3.setText(_translate("Form", "Re-enter the password."))

import source
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
