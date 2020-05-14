# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'room_a.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(840, 713)
        Form.setStyleSheet("background-color: rgb(68, 68, 68);")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(560, 610, 251, 81))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"font: 20pt \"Baskerville Old Face\";\n"
"    background-color: rgb(0, 170, 255);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"font: 20pt \"Baskerville Old Face\";\n"
"background-color: rgb(0, 123, 184);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(-10, -10, 881, 601))
        self.label.setStyleSheet("")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("room1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 610, 251, 81))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"font: 20pt \"Baskerville Old Face\";\n"
"    background-color: rgb(0, 170, 255);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"font: 20pt \"Baskerville Old Face\";\n"
"background-color: rgb(0, 123, 184);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.show_room2)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Next"))
        self.pushButton_2.setText(_translate("Form", "Previous"))

    def show_room1(self):
        self.label.setPixmap(QtGui.QPixmap("room1.jpg"))
        if self.pushButton.clicked.connect(self.show_room2):
            return
        if self.pushButton_2.clicked.connect(self.show_room6):
            return


    def show_room2(self):
        self.label.setPixmap(QtGui.QPixmap("room2.jpg"))
        if self.pushButton.clicked.connect(self.show_room3):
            return
        if self.pushButton_2.clicked.connect(self.show_room1):
            return

    def show_room3(self):
        self.label.setPixmap(QtGui.QPixmap("room3.jpg"))
        if self.pushButton.clicked.connect(self.show_room4):
            return
        if self.pushButton_2.clicked.connect(self.show_room2):
            return

    def show_room4(self):
        self.label.setPixmap(QtGui.QPixmap("room4.jpg"))
        if self.pushButton.clicked.connect(self.show_room5):
            return
        if self.pushButton_2.clicked.connect(self.show_room3):
            return

    def show_room5(self):
        self.label.setPixmap(QtGui.QPixmap("room5.jpg"))
        if self.pushButton.clicked.connect(self.show_room6):
            return
        if self.pushButton_2.clicked.connect(self.show_room4):
            return

    def show_room6(self):
        self.label.setPixmap(QtGui.QPixmap("room6.jpg"))
        if self.pushButton_2.clicked.connect(self.show_room5):
            return
        if self.pushButton.clicked.connect(self.show_room1):
            return

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
