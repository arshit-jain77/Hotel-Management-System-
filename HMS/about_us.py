# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about_us.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1078, 773)
        Form.setStyleSheet("background-color: rgb(247, 247, 247);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(380, 10, 681, 751))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(0, 210, 691, 471))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("hotel6.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 161, 161))
        self.label_2.setStyleSheet("Image: url(:/newPrefix/logo_hotel.png)")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("blue_heaven.jpeg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 331, 41))
        self.label_3.setStyleSheet("font: 24pt \"Baskerville Old Face\";")
        self.label_3.setObjectName("label_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 700, 141, 41))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"font: 16pt \"Baskerville Old Face\";\n"
"    background-color: rgb(0, 170, 255);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"font: 16pt \"Baskerville Old Face\";\n"
"background-color: rgb(0, 123, 184);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(370, 700, 121, 41))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"font: 16pt \"Baskerville Old Face\";\n"
"    background-color: rgb(0, 170, 255);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"font: 16pt \"Baskerville Old Face\";\n"
"background-color: rgb(0, 123, 184);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 361, 61))
        self.label_4.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(10, 270, 361, 31))
        self.label_5.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 300, 301, 41))
        self.label_6.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 340, 281, 31))
        self.label_7.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(10, 370, 241, 41))
        self.label_8.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_8.setObjectName("label_8")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(10, 660, 271, 41))
        self.label_13.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_13.setObjectName("label_13")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(10, 410, 301, 41))
        self.label_10.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"\n"
"color: rgb(0, 0, 255);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(10, 500, 301, 31))
        self.label_11.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_11.setObjectName("label_11")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(10, 540, 341, 31))
        self.label_15.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_15.setObjectName("label_15")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(10, 620, 341, 31))
        self.label_17.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_17.setObjectName("label_17")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(10, 460, 311, 21))
        self.label_16.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"\n"
"color: rgb(0, 0, 255);")
        self.label_16.setObjectName("label_16")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(10, 580, 321, 41))
        self.label_12.setStyleSheet("font: 12pt \"Baskerville Old Face\";")
        self.label_12.setObjectName("label_12")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.show_hotel2)

    def show_hotel2(self):
        self.label.setPixmap(QtGui.QPixmap("hotel2.jpg"))
        if self.pushButton.clicked.connect(self.show_hotel3):
            return
        if self.pushButton_2.clicked.connect(self.show_hotel):
            return

    def show_hotel3(self):
        self.label.setPixmap(QtGui.QPixmap("hotel3.jpg"))
        if self.pushButton.clicked.connect(self.show_hotel4):
            return
        if self.pushButton_2.clicked.connect(self.show_hotel2):
            return

    def show_hotel4(self):
        self.label.setPixmap(QtGui.QPixmap("hotel4.jpg"))
        if self.pushButton.clicked.connect(self.show_hotel5):
            return
        if self.pushButton_2.clicked.connect(self.show_hotel3):
            return

    def show_hotel5(self):
        self.label.setPixmap(QtGui.QPixmap("hotel5.jpg"))
        if self.pushButton.clicked.connect(self.show_hotel6):
            return
        if self.pushButton_2.clicked.connect(self.show_hotel4):
            return

    def show_hotel6(self):
        self.label.setPixmap(QtGui.QPixmap("hotel6.jpg"))
        if self.pushButton_2.clicked.connect(self.show_hotel):
            return
        if self.pushButton.clicked.connect(self.show_hotel5):
            return

    def show_hotel(self):
        self.label.setPixmap(QtGui.QPixmap("hote2.jpg"))
        if self.pushButton.clicked.connect(self.show_hotel2):
            return
        if self.pushButton_2.clicked.connect(self.show_hotel6):
            return


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_3.setText(_translate("Form", "Blue Heaven Hotel"))
        self.pushButton_2.setText(_translate("Form", "Previous"))
        self.pushButton.setText(_translate("Form", "Next"))
        self.label_4.setText(_translate("Form", "Blue Heaven Hotel is a wholly-owned"))
        self.label_5.setText(_translate("Form", "hotel, one of India\'s most established "))
        self.label_6.setText(_translate("Form", "hotel and property companies with an"))
        self.label_7.setText(_translate("Form", "outstanding portfolio of investment "))
        self.label_8.setText(_translate("Form", "and development properties."))
        self.label_13.setText(_translate("Form", "stresses of today’s complex world."))
        self.label_10.setText(_translate("Form", "Voted “Best Regional Hotel Chain” "))
        self.label_11.setText(_translate("Form", "Sincerity is the hallmark of the hotel. "))
        self.label_15.setText(_translate("Form", "The Group is known to its guests, partners,"))
        self.label_17.setText(_translate("Form", "the sense of confidence which alleviates the "))
        self.label_16.setText(_translate("Form", " by readers in India from 2017 to 2019."))
        self.label_12.setText(_translate("Form", "and owners for its sincerity in people and "))
import logo


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
