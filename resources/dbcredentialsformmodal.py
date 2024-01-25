# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dbcredentialsform.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QWidget,QDialog)

class DbCredentialsFormModal(QDialog):

    def __init__(self,parent=None):

        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 400)
        self.submitButton = QPushButton(Form)
        self.submitButton.setObjectName(u"submitButton")
        self.submitButton.setGeometry(QRect(120, 290, 151, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.submitButton.setFont(font)
        self.dbPassInputBox = QLineEdit(Form)
        self.dbPassInputBox.setObjectName(u"dbPassInputBox")
        self.dbPassInputBox.setGeometry(QRect(30, 90, 331, 41))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Sans Serif"])
        font1.setPointSize(10)
        self.dbPassInputBox.setFont(font1)
        self.dbPassInputBox.setEchoMode(QLineEdit.Password)
        self.dbUserInputBox = QLineEdit(Form)
        self.dbUserInputBox.setObjectName(u"dbUserInputBox")
        self.dbUserInputBox.setGeometry(QRect(30, 30, 331, 41))
        self.dbUserInputBox.setFont(font1)
        self.dbUserInputBox.setEchoMode(QLineEdit.Normal)
        self.dbHostInputBox = QLineEdit(Form)
        self.dbHostInputBox.setObjectName(u"dbHostInputBox")
        self.dbHostInputBox.setGeometry(QRect(30, 150, 331, 41))
        self.dbHostInputBox.setFont(font1)
        self.dbHostInputBox.setEchoMode(QLineEdit.Normal)
        self.dbNameInputBox = QLineEdit(Form)
        self.dbNameInputBox.setObjectName(u"dbNameInputBox")
        self.dbNameInputBox.setGeometry(QRect(30, 210, 331, 41))
        self.dbNameInputBox.setFont(font1)
        self.dbNameInputBox.setEchoMode(QLineEdit.Normal)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"DB-CREDENTIALS", None))
        self.submitButton.setText(QCoreApplication.translate("Form", u"SUBMIT", None))
        self.dbPassInputBox.setPlaceholderText(QCoreApplication.translate("Form", u"PASSWORD", None))
        self.dbUserInputBox.setPlaceholderText(QCoreApplication.translate("Form", u"USER", None))
        self.dbHostInputBox.setPlaceholderText(QCoreApplication.translate("Form", u"HOSTNAME", None))
        self.dbNameInputBox.setPlaceholderText(QCoreApplication.translate("Form", u"NAME", None))
    # retranslateUi

