# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'online.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from exit import *

class Ui_Form7(object):

    def gen_otp(self):
        import random
        otp = random.randint(1000, 9999)
        print("The " + str(otp) + " has been generated")
        self.lineEdit_3.setText(str(otp))

    def gen_uid(self):
        import random
        uid = random.randint(100000, 999999)
        print("The Unique ID is " + str(uid) + " and is not to be shared with anyone")
        self.lineEdit_8.setText(str(uid))
        import pandas as pd
        df3 = pd.read_csv(r'C:/Users/Arshit/bill.txt', delimiter=' ')
        a = df3.shape
        b = a[0]

        b=b-1
        name=df3.iloc[b][0]
        phno=str(df3.iloc[b][1])
        nights=str(df3.iloc[b][2])
        room_type=df3.iloc[b][3]
        no_of_rooms=str(df3.iloc[b][4])
        ac=df3.iloc[b][5]
        eb=str(df3.iloc[b][6])
        bill=str(df3.iloc[b][7])

        from firebase import firebase
        import json
        import urllib

        billing = {}
        customer = {}
        customer["Name"] = name
        customer["Phone No"] = phno
        customer["Room Type"] = room_type
        customer["No Of Rooms"] = no_of_rooms
        customer["Nights"] = nights
        customer["AC"]=ac
        customer["ExtraBed"]=eb
        customer["Price"] = bill
        customer["UniqueID"]=uid
        billing["Customer"]=customer

        df5 = pd.read_csv(r'C:/Users/Arshit/status.txt', delimiter=' ')
        a = df5.shape
        b = a[0]
        status = 'Paid via UPI'
        df5.loc[b] = [uid, status]
        df5.to_csv(r'C:/Users/Arshit/status.txt', header='Unique ID', index=None, sep=' ', mode='w')
        payment={}
        payment['Unique_ID'] = uid
        payment['Status'] = status
        firebaseRef = firebase.FirebaseApplication("https://dbms-1bbf5.firebaseio.com/.json", None)
        firebaseRef.post('https://dbms-1bbf5.firebaseio.com/Details_Of_Status_of_Payment', payment)
        firebaseRef.post('https://dbms-1bbf5.firebaseio.com/Details_Of_Bill', billing)

    def exit(self):
        self.window = QtWidgets.QWidget()
        from exit import Ui_Form
        self.ui = Ui_Form()
        self.ui.setup(self.window)
        self.window.show()

    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(674, 769)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 651, 731))
        self.frame_2.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"background-color: rgb(54, 54, 54);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 140, 391, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(270, 30, 91, 71))
        self.label.setStyleSheet("font: 25 20pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(410, 660, 171, 41))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(320, 150, 201, 41))
        self.pushButton_2.setStyleSheet("QPushButton\n"
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
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(80, 140, 241, 71))
        self.label_2.setStyleSheet("font: 12pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(150, 240, 161, 41))
        self.label_3.setStyleSheet("font: 10pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(150, 310, 151, 41))
        self.label_4.setStyleSheet("font: 12pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(330, 310, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 400, 601, 31))
        self.label_9.setStyleSheet("font: 10pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(30, 430, 601, 41))
        self.label_10.setStyleSheet("font: 10pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(120, 550, 181, 41))
        self.label_11.setStyleSheet("font: 12pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_11.setObjectName("label_11")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(330, 550, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setGeometry(QtCore.QRect(40, 610, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"\n"
"color: rgb(207, 207, 207);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(330, 240, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(20, 500, 281, 41))
        self.label_13.setStyleSheet("font: 12pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 490, 231, 41))
        self.pushButton_3.setStyleSheet("QPushButton\n"
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
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(self.gen_otp)
        self.pushButton_3.clicked.connect(self.gen_uid)
        self.pushButton.clicked.connect(self.exit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "UPI"))
        self.pushButton.setText(_translate("Form", "Continue"))
        self.pushButton_2.setText(_translate("Form", "Generate OTP"))
        self.label_2.setText(_translate("Form", "Click to generate OTP"))
        self.label_3.setText(_translate("Form", "Generated OTP is"))
        self.label_4.setText(_translate("Form", "Enter the OTP"))
        self.label_9.setText(_translate("Form", "A 6 digit unique ID will be generated and this is supposed to "))
        self.label_10.setText(_translate("Form", "be shown at the reception before taking your room keys."))
        self.label_11.setText(_translate("Form", "Your unique ID is"))
        self.label_12.setText(_translate("Form", "Please DO NOT SHARE your UNIQUE ID with anyone."))
        self.label_13.setText(_translate("Form", "Click to generate Unique ID"))
        self.pushButton_3.setText(_translate("Form", "Generate Unique ID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form7()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
