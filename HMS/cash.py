# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cash.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from exit import *
class Ui_Form9(object):

    def gen_uid(self):
        import random
        uid = random.randint(100000, 999999)
        print("The Unique ID is " + str(uid) + " and is not to be shared with anyone")
        self.lineEdit_8.setText(str(uid))

        import pandas as pd
        df3 = pd.read_csv(r'C:/Users/Arshit/bill.txt', delimiter=' ')
        a = df3.shape
        b = a[0]

        b = b - 1
        name = df3.iloc[b][0]
        phno = str(df3.iloc[b][1])
        nights = str(df3.iloc[b][2])
        room_type = df3.iloc[b][3]
        no_of_rooms = str(df3.iloc[b][4])
        ac = df3.iloc[b][5]
        eb = str(df3.iloc[b][6])
        bill = str(df3.iloc[b][7])

        from firebase import firebase

        billing = {}
        customer = {}
        customer["Name"] = name
        customer["Phone No"] = phno
        customer["Room Type"] = room_type
        customer["No Of Rooms"] = no_of_rooms
        customer["Nights"] = nights
        customer["AC"] = ac
        customer["ExtraBed"] = eb
        customer["Price"] = bill
        customer["UniqueID"] = uid
        billing["Customer"] = customer

        df5 = pd.read_csv(r'C:/Users/Arshit/status.txt', delimiter=' ')
        a = df5.shape
        b = a[0]
        status = 'Not Paid'
        df5.loc[b] = [uid, status]
        df5.to_csv(r'C:/Users/Arshit/status.txt', header='Unique ID', index=None, sep=' ', mode='w')
        payment = {}
        payment['Unique_ID'] = uid
        payment['Status'] = status
        firebaseRef = firebase.FirebaseApplication("https://dbms-1bbf5.firebaseio.com/.json", None)
        firebaseRef.post('https://dbms-1bbf5.firebaseio.com/Details_Of_Status_of_Payment', payment)
        firebaseRef.post('https://dbms-1bbf5.firebaseio.com/Details_Of_Bill', billing)

    def exit(self):
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setup(self.window)
        self.window.show()

    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(693, 531)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 651, 491))
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
        self.label.setGeometry(QtCore.QRect(130, 10, 411, 71))
        self.label.setStyleSheet("font: 25 20pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(430, 400, 171, 41))
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
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setGeometry(QtCore.QRect(30, 90, 601, 31))
        self.label_9.setStyleSheet("font: 10pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setGeometry(QtCore.QRect(30, 120, 601, 41))
        self.label_10.setStyleSheet("font: 10pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setGeometry(QtCore.QRect(140, 270, 191, 31))
        self.label_11.setStyleSheet("font: 12pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_11.setObjectName("label_11")
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setGeometry(QtCore.QRect(30, 190, 281, 41))
        self.label_13.setStyleSheet("font: 12pt \"Bookman Old Style\";\n"
"color: rgb(207, 207, 207);")
        self.label_13.setObjectName("label_13")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(330, 190, 231, 41))
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
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_8.setGeometry(QtCore.QRect(340, 260, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_8.setFont(font)
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setGeometry(QtCore.QRect(30, 330, 471, 41))
        font = QtGui.QFont()
        font.setFamily("Baskerville Old Face")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"\n"
"color: rgb(207, 207, 207);")
        self.label_14.setObjectName("label_14")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_3.clicked.connect(self.gen_uid)
        self.pushButton.clicked.connect(self.exit)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "             Cash"))
        self.pushButton.setText(_translate("Form", "Continue"))
        self.label_9.setText(_translate("Form", "A 6 digit unique ID will be generated and this is supposed to "))
        self.label_10.setText(_translate("Form", "be shown at the reception before taking your room keys."))
        self.label_11.setText(_translate("Form", "Your unique ID is"))
        self.label_13.setText(_translate("Form", "Click to generate Unique ID"))
        self.pushButton_3.setText(_translate("Form", "Generate Unique ID"))
        self.label_14.setText(_translate("Form", "Please DO NOT SHARE your UNIQUE ID with anyone."))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form9()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
