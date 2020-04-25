from PyQt5 import QtCore, QtGui, QtWidgets
from pass_msg2_signin import *
from pass_msg import *
from welcomepage import *

class Ui_Form(object):

    def signin(self):
        import pandas as pd
        df2 = pd.read_csv(r'C:/Users/Arshit/signup.txt', delimiter=' ')
        df5=pd.read_csv(r'C:/Users/Arshit/signin.txt',delimiter=' ')
        f=0
        # _translate = QtCore.QCoreApplication.translate
        fn=self.lineEdit_2.text()
        ln=self.lineEdit_3.text()
        phno=self.lineEdit_4.text()
        eid = self.lineEdit_5.text()
        psswd = self.lineEdit_6.text()
        z = df2.shape[0]
        print(df2.shape[0])
        # z=z+1
        # print(z)
        # print(df2)
        df5.loc[z] = [fn,ln,phno]
        df5.to_csv(r'C:/Users/Arshit/signin.txt', header='FirstName', index=None, sep=' ', mode='w')

        for i in range(z):
            if eid == df2.iloc[i][3] and psswd == df2.iloc[i][4]:
                print("Continue")
                self.pass_msg_valid()
                f = 1
                break
            else:
                f = 0
        if f == 0:
            print("U have entered incorect password or id , Please RE-enter ")
            self.pass_msg()

    def pass_msg(self):
        self.window = QtWidgets.QWidget()
        from pass_msg import Ui_Form
        self.ui = Ui_Form()
        self.ui.setup(self.window)
        self.window.show()
        # Form.hide()

    def pass_msg_valid(self):
        self.window = QtWidgets.QWidget()
        from pass_msg2_signin import Ui_Form2
        self.ui = Ui_Form2()
        self.ui.setup(self.window)
        self.window.show()
        # Form.hide()

    def back(self):
        self.window = QtWidgets.QMainWindow()
        from welcomepage import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setup(self.window)
        self.window.show()
        # Form.hide()

    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(784, 703)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 20, 761, 641))
        self.frame_2.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"background-color: rgb(54, 54, 54);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        self.pushButton.setGeometry(QtCore.QRect(490, 550, 171, 41))
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
        self.pushButton_2.setGeometry(QtCore.QRect(100, 540, 171, 41))
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
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(250, 20, 201, 61))
        self.label.setStyleSheet("color: rgb(255, 254, 239);\n"
"font: 20pt \"Bernard MT Condensed\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit.setGeometry(QtCore.QRect(80, 140, 391, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 120, 571, 31))
        self.lineEdit_2.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(100, 200, 571, 31))
        self.lineEdit_3.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(100, 280, 571, 31))
        self.lineEdit_4.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(100, 360, 571, 31))
        self.lineEdit_5.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(100, 450, 571, 31))
        self.lineEdit_6.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.signin)
        self.pushButton_2.clicked.connect(self.back)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Continue"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "        Sign In"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "First Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Last Name"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Phone Number"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Email ID"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
