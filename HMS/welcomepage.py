from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from signup import *
from signin import *

class Ui_MainWindow(object):
    def signup(self):
        self.window=QtWidgets.QMainWindow()
        from signup import Ui_Form12
        self.ui=Ui_Form12()
        self.ui.setup(self.window)
        self.window.show()
        # MainWindow.hide()

    def signin(self):
        self.window=QtWidgets.QMainWindow()
        from signin import Ui_Form
        self.ui=Ui_Form()
        self.ui.setup(self.window)
        self.window.show()
        # MainWindow.hide()

    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(863, 755)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(-10, 0, 881, 671))
        self.frame_2.setStyleSheet("")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(-30, -20, 1511, 771))
        self.label.setStyleSheet("background-image: url(:/newPrefix/hotel.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(30, 10, 381, 81))
        self.label_2.setStyleSheet("font: 75 26pt \"Script MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 80, 451, 91))
        self.label_3.setStyleSheet("font: 75 26pt \"Script MT Bold\";\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.frame = QtWidgets.QFrame(self.frame_2)
        self.frame.setGeometry(QtCore.QRect(50, 270, 291, 321))
        self.frame.setStyleSheet("background-color: rgb(63, 63, 63);\n"
"background-color: rgb(68, 68, 68);\n"
"alternate-background-color: rgb(55, 55, 55);\n"
"border-radius:15px")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(20, 90, 251, 81))
        self.pushButton.setStyleSheet("QPushButton\n"
"{\n"
"font: 20pt \"Baskerville Old Face\";\n"
"background-color: rgb(0, 170, 255);\n"
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
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 251, 81))
        self.pushButton_2.setStyleSheet("QPushButton\n"
"{\n"
"font: 20pt \"Baskerville Old Face\";\n"
"background-color: rgb(0, 170, 255);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"font: 20pt \"Baskerville Old Face\";\n"
"background-color: rgb(0, 123, 184);\n"
"border-radius:15px;\n"
"color: rgb(255, 255, 255);\n"
"}")

        self.pushButton_2.setObjectName("pushButton_2")
        self.toolButton = QtWidgets.QToolButton(self.frame_2)
        self.toolButton.setGeometry(QtCore.QRect(120, 190, 141, 141))
        self.toolButton.setStyleSheet("border-radius:70px;\n"
"background-color: rgb(85, 170, 255);")
        self.toolButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/newPrefix/login.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton.setIcon(icon)
        self.toolButton.setIconSize(QtCore.QSize(160, 150))
        self.toolButton.setObjectName("toolButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 863, 31))
        self.menubar.setObjectName("menubar")
        self.menuHome = QtWidgets.QMenu(self.menubar)
        self.menuHome.setObjectName("menuHome")
        self.menuRooms = QtWidgets.QMenu(self.menubar)
        self.menuRooms.setObjectName("menuRooms")
        self.menuAbout_Us = QtWidgets.QMenu(self.menubar)
        self.menuAbout_Us.setObjectName("menuAbout_Us")
        self.menuContact_Us = QtWidgets.QMenu(self.menubar)
        self.menuContact_Us.setObjectName("menuContact_Us")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuHome.menuAction())
        self.menubar.addAction(self.menuRooms.menuAction())
        self.menubar.addAction(self.menuAbout_Us.menuAction())
        self.menubar.addAction(self.menuContact_Us.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.signup)
        self.pushButton_2.clicked.connect(self.signin)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Spend Quality"))
        self.label_3.setText(_translate("MainWindow", "Holidays With Us"))
        self.pushButton.setText(_translate("MainWindow", "Sign Up"))
        self.pushButton_2.setText(_translate("MainWindow", "Sign In"))
        self.menuHome.setTitle(_translate("MainWindow", "Home"))
        self.menuRooms.setTitle(_translate("MainWindow", "Rooms"))
        self.menuAbout_Us.setTitle(_translate("MainWindow", "About Us"))
        self.menuContact_Us.setTitle(_translate("MainWindow", "Contact Us"))

import hotelimg
import login

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
