from PyQt5 import QtCore, QtGui, QtWidgets
from payment import *

class Ui_Form(object):

    def retrieveText(self,ac):

        import pandas as pd
        df3 = pd.read_csv(r'C:/Users/Arshit/bill.txt', delimiter=' ')
        df5 = pd.read_csv(r'C:/Users/Arshit/signin.txt', delimiter=' ')
        z = df5.shape[0]
        bill = 0
        a = df3.shape
        b = a[0]

        fn=df5.iloc[z-1][0]
        ln=df5.iloc[z-1][1]
        name=fn+ln
        phno=df5.iloc[z-1][2]

        room_type = str(self.comboBox.currentText())
        print("room", room_type)
        no_of_rooms = self.lineEdit.text()
        no_of_rooms = int(no_of_rooms)
        print("no of rooms", no_of_rooms)
        nights = self.lineEdit_2.text()
        nights = int(nights)
        print("nights", nights)
        print("continue")

        if room_type == 'Single':
            if ac:
                yes = 1
            else:
                yes = 0
            eb = int(self.lineEdit_3.text())
            bill = (no_of_rooms * 1000 * nights) + (yes * 500 * nights*no_of_rooms) + (eb * 400 * nights)
            print(bill)
            self.lineEdit_4.setText(str(bill))
            df3.loc[b] = [name, phno, nights, room_type,no_of_rooms, ac, eb, bill]

        elif room_type == 'Double':
            if ac:
                yes = 1
            else:
                yes = 0
            eb = int(self.lineEdit_3.text())
            bill = (no_of_rooms * 1500 * nights) + (yes * 500 * nights*no_of_rooms) + (eb * 400 * nights)
            self.lineEdit_4.setText(str(bill))
            df3.loc[b] = [name, phno, nights, room_type,no_of_rooms, ac, eb, bill]


        elif room_type == 'Triple':
            if ac:
                yes = 1
            else:
                yes = 0
            eb = int(self.lineEdit_3.text())
            bill = (no_of_rooms * 2000 * nights) + (yes * 500 * nights*no_of_rooms) + (eb * 400 * nights)
            print(bill)
            self.lineEdit_4.setText(str(bill))
            df3.loc[b] = [name, phno, nights, room_type,no_of_rooms, ac, eb, bill]


        elif room_type == 'Quadraple':
            if ac:
                yes = 1
            else:
                yes = 0
            eb = int(self.lineEdit_3.text())
            bill = (no_of_rooms * 2500 * nights) + (yes * 500 * nights*no_of_rooms) + (eb * 400 * nights)
            print(bill)
            self.lineEdit_4.setText(str(bill))
            df3.loc[b] = [name, phno, nights, room_type,no_of_rooms, ac, eb, bill]

        elif room_type == 'Queen':
            if ac:
                yes = 1
            else:
                yes = 0
            eb = int(self.lineEdit_3.text())
            bill = (no_of_rooms * 3500 * nights) + (yes * 500 * nights*no_of_rooms) + (eb * 400 * nights)
            print(bill)
            self.lineEdit_4.setText(str(bill))
            # customer["Price"] = bill
            df3.loc[b] = [name, phno, nights, room_type,no_of_rooms, ac, eb, bill]

        elif room_type == 'King':
            if ac:
                yes = 1
            else:
                yes = 0
            eb = int(self.lineEdit_3.text())
            bill = (no_of_rooms * 5000 * nights) + (yes * 500 * nights*no_of_rooms) + (eb * 400 * nights)
            print(bill)
            self.lineEdit_4.setText(str(bill))
            # customer["Price"] = bill
            df3.loc[b] = [name, phno, nights, room_type,no_of_rooms, ac, eb, bill]

        df3.to_csv(r'C:/Users/Arshit/bill.txt', header='Name', index=None, sep=' ', mode='w')

        print("Thank you so much for Booking ! Have a nice trip ahead...")

    def payment(self):
        self.window = QtWidgets.QWidget()
        from payment import Ui_Form4
        self.ui = Ui_Form4()
        self.ui.setup(self.window)
        self.window.show()

    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(902, 932)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(30, 30, 841, 881))
        self.frame.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"background-color: rgb(54, 54, 54);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(20, 20, 811, 321))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 20, 331, 51))
        self.label.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(40, 70, 311, 51))
        self.label_2.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(40, 120, 311, 51))
        self.label_3.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(460, 20, 301, 51))
        self.label_4.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(460, 70, 311, 51))
        self.label_5.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        self.label_6.setGeometry(QtCore.QRect(460, 120, 301, 51))
        self.label_6.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_2)
        self.label_7.setGeometry(QtCore.QRect(40, 180, 401, 51))
        self.label_7.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setGeometry(QtCore.QRect(40, 240, 411, 51))
        self.label_8.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_8.setObjectName("label_8")
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setGeometry(QtCore.QRect(30, 320, 771, 541))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_9 = QtWidgets.QLabel(self.frame_3)
        self.label_9.setGeometry(QtCore.QRect(40, 20, 231, 51))
        self.label_9.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame_3)
        self.label_10.setGeometry(QtCore.QRect(40, 90, 331, 51))
        self.label_10.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_10.setObjectName("label_10")
        self.comboBox = QtWidgets.QComboBox(self.frame_3)
        self.comboBox.setGeometry(QtCore.QRect(450, 30, 231, 41))
        self.comboBox.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"background-color: rgb(17, 204, 255);\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_11 = QtWidgets.QLabel(self.frame_3)
        self.label_11.setGeometry(QtCore.QRect(40, 170, 331, 51))
        self.label_11.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_11.setObjectName("label_11")
        self.radioButton = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton.setGeometry(QtCore.QRect(40, 330, 119, 23))
        self.radioButton.setStyleSheet("\n"
"font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(202, 202, 202);")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_3)
        self.radioButton_2.setGeometry(QtCore.QRect(190, 330, 119, 23))
        self.radioButton_2.setStyleSheet("color: rgb(224, 224, 224);\n"
"color: rgb(202, 202, 202);\n"
"font: 12pt \"Baskerville Old Face\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.label_12 = QtWidgets.QLabel(self.frame_3)
        self.label_12.setGeometry(QtCore.QRect(40, 250, 331, 51))
        self.label_12.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_12.setObjectName("label_12")
        self.label_14 = QtWidgets.QLabel(self.frame_3)
        self.label_14.setGeometry(QtCore.QRect(350, 390, 181, 51))
        self.label_14.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_14.setObjectName("label_14")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(470, 480, 171, 41))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_2.setGeometry(QtCore.QRect(180, 390, 151, 41))
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
        self.lineEdit = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit.setGeometry(QtCore.QRect(462, 90, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(460, 170, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_3.setGeometry(QtCore.QRect(460, 250, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_3)
        self.lineEdit_4.setGeometry(QtCore.QRect(480, 390, 151, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_2.clicked.connect(lambda : self.retrieveText(self.radioButton.isChecked()))
        self.pushButton.clicked.connect(self.payment)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Single         : Rs.1000 per night"))
        self.label_2.setText(_translate("Form", "Double       : Rs.1500 per night"))
        self.label_3.setText(_translate("Form", "Triple         : Rs.2000 per night"))
        self.label_4.setText(_translate("Form", "Quadraple  : Rs.2500 per night"))
        self.label_5.setText(_translate("Form", "Queen        : Rs.3500 per night"))
        self.label_6.setText(_translate("Form", "King           : Rs.5000 per night"))
        self.label_7.setText(_translate("Form", "Extra charges for AC : Rs.500 per night"))
        self.label_8.setText(_translate("Form", "Charges for Extra Bed : Rs.400 per bed"))
        self.label_9.setText(_translate("Form", "Select the type of room"))
        self.label_10.setText(_translate("Form", "Number of rooms to be booked"))
        self.comboBox.setItemText(0, _translate("Form", "Single"))
        self.comboBox.setItemText(1, _translate("Form", "Double"))
        self.comboBox.setItemText(2, _translate("Form", "Triple"))
        self.comboBox.setItemText(3, _translate("Form", "Quadraple"))
        self.comboBox.setItemText(4, _translate("Form", "Queen"))
        self.comboBox.setItemText(5, _translate("Form", "King"))
        self.label_11.setText(_translate("Form", "Number of nights you want to stay"))
        self.radioButton.setText(_translate("Form", "A/C"))
        self.radioButton_2.setText(_translate("Form", "Non-A/C"))
        self.label_12.setText(_translate("Form", "Number of extra beds required"))
        self.label_14.setText(_translate("Form", "to see your Bill:"))
        self.pushButton.setText(_translate("Form", "Continue"))
        self.pushButton_2.setText(_translate("Form", "Click Here"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
