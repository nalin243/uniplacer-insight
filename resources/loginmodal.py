# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginModal_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################


from PySide6 import QtCore
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget, QDialog)

from resources.customstackedwidget import QStackedWidget

import images

class LoginModal(QDialog):

    def __init__(self, loginauth ,parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.loginauth = loginauth

        self.stackedWidget.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidget.setTransitionSpeed(100)
        self.stackedWidget.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
        self.stackedWidget.setSlideTransition(True)

        self.forgotPasswordLink.mousePressEvent = self.otpCard
        self.confirmOtpButton.clicked.connect(self.passConfCard)
        self.confirmPasswordInput.textChanged.connect(self.matchPassword)

    def otpCard(self, event):
        self.loginauth.setUsername(self.userNameInput.text())
        self.stackedWidget.slideToNextWidget()
        self.loginauth.sendOtp()

    def passConfCard(self, event):
        if (self.loginauth.checkOtp(self.otpInput.text())):
             self.stackedWidget.slideToNextWidget()
        else:
             self.wrongOtpLabel.setText("Wrong otp")

    def matchPassword(self, event):

        if (self.newPasswordInput.text() != self.confirmPasswordInput.text()):
            self.passMismatchLabel.setText("Passwords do not match!")
        else:
            self.passMismatchLabel.setText(" ")
        

    def setupUi(self, Form):
        if not Form.objectName():
             Form.setObjectName(u"Form")
        Form.resize(400, 350)
        # self.setWindowFlag(Qt.FramelessWindowHint)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 400, 350))
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.wrongCredLabel = QLabel(self.login)
        self.wrongCredLabel.setObjectName(u"wrongCredLabel")
        self.wrongCredLabel.setGeometry(QRect(0, 300, 400, 30))
        self.wrongCredLabel.setFont(QFont("serif",10,QFont.DemiBold))
        self.wrongCredLabel.setAlignment(Qt.AlignHCenter)
        self.passwordImage = QLabel(self.login)
        self.passwordImage.setObjectName(u"passwordImage")
        self.passwordImage.setGeometry(QRect(50, 150, 30, 30))
        self.passwordImage.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.passwordImage.setPixmap(QPixmap(u":/icons/key 1.png"))
        self.loginHeading = QLabel(self.login)
        self.loginHeading.setObjectName(u"loginHeading")
        self.loginHeading.setGeometry(QRect(110, 30, 160, 30))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.loginHeading.setFont(font)
        self.loginHeading.setStyleSheet(u"padding:30px")
        self.userNameInput = QLineEdit(self.login)
        self.userNameInput.setObjectName(u"userNameInput")
        self.userNameInput.setGeometry(QRect(40, 90, 321, 51))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.userNameInput.setFont(font1)
        self.userNameInput.setStyleSheet(u"border-top-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"\n"
"\n"
"border: 2px solid gray;\n"
"background-color: rgb(235, 235, 235);\n"
"\n"
"padding-left:45px;")
        self.userNameInput.setFrame(True)
        self.userNameInput.setDragEnabled(False)
        self.userNameImage = QLabel(self.login)
        self.userNameImage.setObjectName(u"userNameImage")
        self.userNameImage.setGeometry(QRect(50, 100, 30, 30))
        self.userNameImage.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.userNameImage.setPixmap(QPixmap(u":/icons/user(2) 1.png"))
        self.forgotPasswordLink = QLabel(self.login)
        self.forgotPasswordLink.setObjectName(u"forgotPasswordLink")
        self.forgotPasswordLink.setGeometry(QRect(50, 200, 305, 20))
        self.forgotPasswordLink.setAlignment(Qt.AlignRight)
        self.forgotPasswordLink.setCursor(QCursor(Qt.PointingHandCursor))


        self.passwordInput = QLineEdit(self.login)
        self.passwordInput.setObjectName(u"passwordInput")
        self.passwordInput.setGeometry(QRect(40, 140, 321, 51))
        self.passwordInput.setFont(font1)
        self.passwordInput.setStyleSheet(u"border-bottom-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"background-color: rgb(235, 235, 235);\n"
"padding: 45px;\n"
"border:2px solid grey\n"
"")
        self.passwordInput.setFrame(True)
        self.passwordInput.setEchoMode(QLineEdit.Password)
        self.signInButton = QPushButton(self.login)
        self.signInButton.setObjectName(u"signInButton")
        self.signInButton.setGeometry(QRect(90, 240, 211, 51))
        font2 = QFont()
        font2.setFamilies([u"Nirmala UI"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setStrikeOut(False)
        font2.setKerning(True)
        self.signInButton.setFont(font2)
        self.signInButton.setStyleSheet(u"background-color: rgb(48, 149, 143);\n"
"\n"
"border-radius: 5px;")
        self.signInButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stackedWidget.addWidget(self.login)
        self.wrongCredLabel.raise_()
        self.loginHeading.raise_()
        self.userNameInput.raise_()
        self.userNameImage.raise_()
        self.forgotPasswordLink.raise_()
        self.passwordInput.raise_()
        self.signInButton.raise_()
        self.passwordImage.raise_()
        self.otpPage = QWidget()
        self.otpPage.setObjectName(u"otpPage")
        self.otpPage.setStyleSheet(u"#page_2 {\n"
"	background-image: url(:/icons/otpbg.png);\n"
"}\n"
"")
        self.otpHeading = QLabel(self.otpPage)
        self.otpHeading.setObjectName(u"otpHeading")
        self.otpHeading.setGeometry(QRect(150, 120, 100, 20))
        self.otpHeading.setStyleSheet(u"")
        self.otpInput = QLineEdit(self.otpPage)
        self.otpInput.setObjectName(u"otpInput")
        self.otpInput.setGeometry(QRect(100, 150, 201, 41))
        font3 = QFont()
        font3.setBold(True)
        self.otpInput.setFont(font3)
        self.otpInput.setStyleSheet(u"padding:10px")
        self.wrongOtpLabel = QLabel(self.otpPage)
        self.wrongOtpLabel.setGeometry(QRect(170, 240, 100, 25))
        self.wrongOtpLabel.setFont(QFont("serif",10,QFont.DemiBold))
        self.confirmOtpButton = QPushButton(self.otpPage)
        self.confirmOtpButton.setObjectName(u"confirmOtpButton")
        self.confirmOtpButton.setGeometry(QRect(150, 200, 100, 25))
        self.confirmOtpButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.stackedWidget.addWidget(self.otpPage)
        self.newCredPage = QWidget()
        self.newCredPage.setObjectName(u"newCredPage")
        self.newPasswordInput = QLineEdit(self.newCredPage)
        self.newPasswordInput.setObjectName(u"newPasswordInput")
        self.newPasswordInput.setGeometry(QRect(50, 130, 311, 51))
        self.newPasswordInput.setFont(font1)
        self.newPasswordInput.setStyleSheet(u"\n"
"background-color: rgb(235, 235, 235);\n"
"padding: 45px;\n"
"border:2px solid grey\n"
"")
        self.newPasswordInput.setFrame(True)
        self.newPasswordInput.setEchoMode(QLineEdit.Password)
        self.emailInput = QLineEdit(self.newCredPage)
        self.emailInput.setObjectName(u"emailInput")
        self.emailInput.setGeometry(QRect(50, 80, 311, 51))
        self.emailInput.setFont(font1)
        self.emailInput.setStyleSheet(u"border-top-right-radius: 8px;\n"
"border-top-left-radius: 8px;\n"
"\n"
"\n"
"border: 2px solid gray;\n"
"background-color: rgb(235, 235, 235);\n"
"\n"
"padding-left:45px;")
        self.emailInput.setFrame(True)
        self.emailInput.setDragEnabled(False)
        self.newPassImage = QLabel(self.newCredPage)
        self.newPassImage.setObjectName(u"newPassImage")
        self.newPassImage.setGeometry(QRect(60, 140, 30, 30))
        self.newPassImage.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.newPassImage.setPixmap(QPixmap(u":/icons/key 1.png"))
        self.emailImage = QLabel(self.newCredPage)
        self.emailImage.setObjectName(u"emailImage")
        self.emailImage.setGeometry(QRect(60, 90, 30, 30))
        self.emailImage.setStyleSheet(u"background-color: rgb(235, 235, 235);")
        self.emailImage.setPixmap(QPixmap(u":/icons/user(2) 1.png"))
        self.confirmPasswordInput = QLineEdit(self.newCredPage)
        self.confirmPasswordInput.setObjectName(u"confirmPasswordInput")
        self.confirmPasswordInput.setGeometry(QRect(50, 180, 311, 51))
        self.confirmPasswordInput.setFont(font1)
        self.confirmPasswordInput.setStyleSheet(u"border-bottom-right-radius: 8px;\n"
"border-bottom-left-radius: 8px;\n"
"background-color: rgb(235, 235, 235);\n"
"padding: 45px;\n"
"border:2px solid grey\n"
"")
        self.confirmPasswordInput.setFrame(True)
        self.confirmPasswordInput.setEchoMode(QLineEdit.Password)
        self.confirmPassImage = QLabel(self.newCredPage)
        self.confirmPassImage.setObjectName(u"confirmPassImage")
        self.confirmPassImage.setGeometry(QRect(60, 190, 30, 30))
        self.confirmPassImage.setPixmap(QPixmap(u":/icons/confirmation 1.png"))
        self.confirmCredButton = QPushButton(self.newCredPage)
        self.confirmCredButton.setObjectName(u"confirmCredButton")
        self.confirmCredButton.setGeometry(QRect(150, 250, 121, 31))
        self.confirmCredButton.setFont(font3)
        self.confirmCredButton.setStyleSheet(u"background-color: rgb(48, 149, 143);\n"
"border-radius: 5px\n"
"")
        self.confirmCredButton.setCursor(QCursor(Qt.PointingHandCursor))

        self.passMismatchLabel = QLabel(self.newCredPage)
        self.passMismatchLabel.setGeometry(QRect(0, 300, 400, 40))
        self.passMismatchLabel.setAlignment(Qt.AlignHCenter)
        self.passMismatchLabel.setFont(QFont("serif",10,QFont.DemiBold))

        self.newCredHeading = QLabel(self.newCredPage)
        self.newCredHeading.setObjectName(u"newCredHeading")
        self.newCredHeading.setGeometry(QRect(130, 40, 160, 30))
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(True)
        self.newCredHeading.setFont(font4)
        self.stackedWidget.addWidget(self.newCredPage)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.wrongCredLabel.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" color:#df0000;\"></span></p></body></html>", None))
        self.passwordImage.setText("")
        self.loginHeading.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.userNameInput.setPlaceholderText(QCoreApplication.translate("Form", u"USERNAME", None))
        self.userNameImage.setText("")
        self.forgotPasswordLink.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600; color:#e20000;\">Forgot password?</span></p></body></html>", None))
        self.passwordInput.setPlaceholderText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.signInButton.setText(QCoreApplication.translate("Form", u"Sign In", None))
        self.otpHeading.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">ENTER OTP</span></p></body></html>", None))
        self.otpInput.setPlaceholderText(QCoreApplication.translate("Form", u"OTP", None))
        self.confirmOtpButton.setText(QCoreApplication.translate("Form", u"confirm", None))
        self.newPasswordInput.setPlaceholderText(QCoreApplication.translate("Form", u"NEW PASSWORD", None))
        self.emailInput.setPlaceholderText(QCoreApplication.translate("Form", u"E-MAIL", None))
        self.newPassImage.setText("")
        self.emailImage.setText("")
        self.confirmPasswordInput.setPlaceholderText(QCoreApplication.translate("Form", u"CONFIRM PASSWORD", None))
        self.confirmPassImage.setText("")
        self.confirmCredButton.setText(QCoreApplication.translate("Form", u"CONFIRM", None))
        self.newCredHeading.setText(QCoreApplication.translate("Form", u"SET CREDENTIALS", None))
    # retranslateUi

