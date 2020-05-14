# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'available.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form16(object):

    def click(self):
        import pandas as pd
        df3 = pd.read_csv(r'C:/Users/Arshit/available.txt', delimiter=' ')
        a = df3.shape
        b = a[0]
        print(a, b)
        single = df3.iloc[b - 1][0]
        double = df3.iloc[b - 1][1]
        triple = df3.iloc[b - 1][2]
        quadraple = df3.iloc[b - 1][3]
        queen = df3.iloc[b - 1][4]
        king = df3.iloc[b - 1][5]

        print(single, double, triple, quadraple, queen, king)

        self.lineEdit.setText(str(single))
        self.lineEdit_2.setText(str(double))
        self.lineEdit_3.setText(str(triple))
        self.lineEdit_4.setText(str(quadraple))
        self.lineEdit_5.setText(str(queen))
        self.lineEdit_6.setText(str(king))


    def details(self):
        from details import Ui_Form
        self.window = QtWidgets.QWidget()
        self.ui = Ui_Form()
        self.ui.setup(self.window)
        self.window.show()
        # Form.hide()


    def setup(self, Form):
        Form.setObjectName("Form")
        Form.resize(736, 705)
        Form.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame_2 = QtWidgets.QFrame(Form)
        self.frame_2.setGeometry(QtCore.QRect(10, 10, 711, 681))
        self.frame_2.setStyleSheet("background-color: rgb(74, 74, 74);\n"
"background-color: rgb(54, 54, 54);\n"
"border-radius:15px;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(40, 30, 611, 631))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(110, 250, 81, 51))
        self.label_7.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_7.setObjectName("label_7")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 260, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_4.setGeometry(QtCore.QRect(300, 320, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setGeometry(QtCore.QRect(110, 310, 121, 51))
        self.label_4.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(110, 130, 81, 51))
        self.label_3.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_3.setObjectName("label_3")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_5.setGeometry(QtCore.QRect(300, 380, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 200, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_6.setGeometry(QtCore.QRect(300, 440, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(110, 190, 91, 51))
        self.label_2.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(300, 140, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setGeometry(QtCore.QRect(110, 370, 101, 51))
        self.label_5.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setGeometry(QtCore.QRect(110, 430, 91, 51))
        self.label_6.setStyleSheet("font: 12pt \"Baskerville Old Face\";\n"
"color: rgb(184, 184, 184);")
        self.label_6.setObjectName("label_6")
        self.label_15 = QtWidgets.QLabel(self.frame)
        self.label_15.setGeometry(QtCore.QRect(240, 20, 381, 81))
        self.label_15.setStyleSheet("color: rgb(190, 190, 190);\n"
"font: 16pt \"Baskerville Old Face\";")
        self.label_15.setObjectName("label_15")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 40, 171, 41))
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
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setGeometry(QtCore.QRect(400, 550, 171, 41))
        self.pushButton_4.setStyleSheet("QPushButton\n"
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
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.pushButton_3.clicked.connect(self.click)
        self.pushButton_4.clicked.connect(self.details)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_7.setText(_translate("Form", "Triple        "))
        self.label_4.setText(_translate("Form", "Quadraple  "))
        self.label_3.setText(_translate("Form", "Single         "))
        self.label_2.setText(_translate("Form", "Double       "))
        self.label_5.setText(_translate("Form", "Queen       "))
        self.label_6.setText(_translate("Form", "King          "))
        self.label_15.setText(_translate("Form", "to see availability of rooms"))
        self.pushButton_3.setText(_translate("Form", "Click"))
        self.pushButton_4.setText(_translate("Form", "Continue"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form16()
    ui.setup(Form)
    Form.show()
    sys.exit(app.exec_())
