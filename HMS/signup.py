from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form12(object):

    def signup(self):
        import pandas as pd
        from firebase import firebase

        df2 = pd.read_csv(r'C:/Users/Arshit/signup.txt', delimiter=' ')

        details = {}
        sign_up = {}

        a = df2.shape
        b = a[0]

        fn = self.lineEdit_2.text()
        ln = self.lineEdit_3.text()
        phno = self.lineEdit_4.text()
        eid=self.lineEdit_5.text()
        psswd=self.lineEdit_6.text()

        sign_up['First Name'] = fn
        sign_up['Last Name'] = ln
        sign_up['Phone NO'] = phno
        sign_up['Email ID'] = eid
        sign_up['Password'] = psswd

        details['Sign_Up'] = sign_up

        firebaseRef = firebase.FirebaseApplication("https://dbms-1bbf5.firebaseio.com/.json", None)
        firebaseRef.post('https://dbms-1bbf5.firebaseio.com/Details_Of_Sign_Up', details)

        df2.loc[b] = [fn, ln, phno, eid, psswd]
        df2.to_csv(r'C:/Users/Arshit/signup.txt', header='First Name', index=None, sep=' ', mode='w')


        print("Valid")
        self.pass_msg_valid()

        import pyrebase
        config = {
            'apiKey': "AIzaSyA5XX7cMnCADNmF-FePUHwKM1Uq6bxFg4E",
            'authDomain': "dbms-1bbf5.firebaseapp.com",
            'databaseURL': "https://dbms-1bbf5.firebaseio.com",
            'projectId': "dbms-1bbf5",
            'storageBucket': "dbms-1bbf5.appspot.com",
            'messagingSenderId': "281016098399",
            'appId': "1:281016098399:web:d49bc5ac61b876eb3045ea",
            'measurementId': "G-ENSPDHYDMQ"
        };

        firebase = pyrebase.initialize_app(config)
        auth = firebase.auth()
        user = auth.create_user_with_email_and_password(eid, psswd)

    def pass_msg_valid(self):
        self.window = QtWidgets.QWidget()
        from pass_msg2 import Ui_Form2
        self.ui = Ui_Form2()
        self.ui.setup(self.window)
        self.window.show()

    def back(self):
        self.window = QtWidgets.QMainWindow()
        from welcomepage import Ui_MainWindow
        self.ui = Ui_MainWindow()
        self.ui.setup(self.window)
        self.window.show()

    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(735, 676)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(20, 20, 691, 611))
        self.frame.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"background-color: rgb(54, 54, 54);\n"
"border-radius:15px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(450, 520, 171, 41))
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 520, 171, 41))
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
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 20, 201, 61))
        self.label.setStyleSheet("color: rgb(255, 254, 239);\n"
"font: 20pt \"Bernard MT Condensed\";")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(80, 140, 391, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(60, 110, 571, 31))
        self.lineEdit_2.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(60, 190, 571, 31))
        self.lineEdit_3.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(60, 270, 571, 31))
        self.lineEdit_4.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(60, 350, 571, 31))
        self.lineEdit_5.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(60, 430, 571, 31))
        self.lineEdit_6.setStyleSheet("font: 16pt \"Century\";\n"
"color: rgb(167, 167, 167);\n"
"border-bottom:1px solid;\n"
"border-bottom-color: rgb(167, 167, 167);")
        self.lineEdit_6.setText("")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setObjectName("lineEdit_6")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton.clicked.connect(self.signup)
        self.pushButton_2.clicked.connect(self.back)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Continue"))
        self.pushButton_2.setText(_translate("Form", "Back"))
        self.label.setText(_translate("Form", "       Sign Up"))
        self.lineEdit_2.setPlaceholderText(_translate("Form", "First Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Form", "Last Name"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "Phone Number"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "Email ID"))
        self.lineEdit_6.setPlaceholderText(_translate("Form", "Password"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form12()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
