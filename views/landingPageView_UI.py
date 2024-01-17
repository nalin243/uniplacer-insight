# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'landingView.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QRadioButton, QSizePolicy, QVBoxLayout, QWidget)
import images

from resources.customstackedwidget import QStackedWidget

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 810)
        MainWindow.setMinimumSize(QSize(1440, 810))
        MainWindow.setMaximumSize(QSize(1440, 810))
        MainWindow.setFocusPolicy(Qt.StrongFocus)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1440, 810))
        self.centralwidget.setMaximumSize(QSize(1440, 810))
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	background-image: url(:/icons/bg.png);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(850, 505))
        self.widget.setMaximumSize(QSize(850, 505))
        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 170, 381, 171))
        self.title.setMaximumSize(QSize(16777215, 16777215))
        self.title.setCursor(QCursor(Qt.PointingHandCursor))
        self.title.setPixmap(QPixmap(u":/icons/title.png"))
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.CardOutline = QWidget(self.widget)
        self.CardOutline.setObjectName(u"CardOutline")
        self.CardOutline.setGeometry(QRect(468, 52, 334, 404))
        self.CardOutline.setMinimumSize(QSize(334, 404))
        self.CardOutline.setMaximumSize(QSize(334, 404))
        self.CardOutline.setStyleSheet(u"#CardOutline:hover{\n"
"	border: 20px solid;\n"
"	border-color: rgba(217, 217, 217,200);\n"
"	border-top-right-radius: 34px;\n"
"}")
        self.stackedWidgetForCards = QStackedWidget(self.CardOutline)
        self.stackedWidgetForCards.setObjectName(u"stackedWidgetForCards")
        self.stackedWidgetForCards.setGeometry(QRect(2, 2, 330, 360))
        self.stackedWidgetForCards.setMinimumSize(QSize(330, 360))
        self.stackedWidgetForCards.setMaximumSize(QSize(330, 360))
        self.stackedWidgetForCards.setStyleSheet(u"QStackedWidget#stackedWidgetforCards{\n"
"	border: 5px solid;\n"
"	border-color: rgb(0, 0, 0);\n"
"}")
        self.stackedWidgetForCards.setTransitionDirection(QtCore.Qt.Horizontal)
        self.stackedWidgetForCards.setTransitionSpeed(500)
        self.stackedWidgetForCards.setTransitionEasingCurve(QtCore.QEasingCurve.Linear)
        self.stackedWidgetForCards.setSlideTransition(True)


        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.studentPlacementStatCard = QWidget(self.page)
        self.studentPlacementStatCard.setObjectName(u"studentPlacementStatCard")
        self.studentPlacementStatCard.setGeometry(QRect(0, 0, 330, 360))
        self.studentPlacementStatCard.setMinimumSize(QSize(330, 360))
        self.studentPlacementStatCard.setMaximumSize(QSize(330, 360))
        self.studentPlacementStatCard.setCursor(QCursor(Qt.ArrowCursor))
        self.studentPlacementStatCard.setStyleSheet(u"#studentPlacementStatCard {\n"
"\n"
"border-top-right-radius: 34px;\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.studentPlacementStatCard)
        self.verticalLayout_3.setSpacing(20)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(13, 11, 19, 10)
        self.studentPlacementStatCardImage_2 = QLabel(self.studentPlacementStatCard)
        self.studentPlacementStatCardImage_2.setObjectName(u"studentPlacementStatCardImage_2")
        self.studentPlacementStatCardImage_2.setMinimumSize(QSize(305, 241))
        self.studentPlacementStatCardImage_2.setMaximumSize(QSize(305, 241))
        self.studentPlacementStatCardImage_2.setPixmap(QPixmap(u":/icons/land-graph.png"))
        self.studentPlacementStatCardImage_2.setScaledContents(True)
        self.studentPlacementStatCardImage_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.studentPlacementStatCardImage_2)

        self.studentPlacementStatCardTitle_2 = QLabel(self.studentPlacementStatCard)
        self.studentPlacementStatCardTitle_2.setObjectName(u"studentPlacementStatCardTitle_2")
        self.studentPlacementStatCardTitle_2.setMinimumSize(QSize(241, 75))
        self.studentPlacementStatCardTitle_2.setMaximumSize(QSize(241, 75))
        self.studentPlacementStatCardTitle_2.setStyleSheet(u"")
        self.studentPlacementStatCardTitle_2.setScaledContents(False)
        self.studentPlacementStatCardTitle_2.setAlignment(Qt.AlignCenter)
        self.studentPlacementStatCardTitle_2.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.studentPlacementStatCardTitle_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.companyPlacementStatCard = QWidget(self.page_2)
        self.companyPlacementStatCard.setObjectName(u"companyPlacementStatCard")
        self.companyPlacementStatCard.setGeometry(QRect(0, 0, 330, 360))
        self.companyPlacementStatCard.setMinimumSize(QSize(330, 360))
        self.companyPlacementStatCard.setMaximumSize(QSize(330, 360))
        self.companyPlacementStatCard.setCursor(QCursor(Qt.ArrowCursor))
        self.companyPlacementStatCard.setStyleSheet(u"\n"
"\n"
"	border-top-right-radius: 34px;\n"
"	background-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.companyPlacementStatCard)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(13, 11, 19, 10)
        self.companyPlacementStatCardImage = QLabel(self.companyPlacementStatCard)
        self.companyPlacementStatCardImage.setObjectName(u"companyPlacementStatCardImage")
        self.companyPlacementStatCardImage.setMinimumSize(QSize(305, 241))
        self.companyPlacementStatCardImage.setMaximumSize(QSize(305, 241))
        self.companyPlacementStatCardImage.setPixmap(QPixmap(u":/icons/card2.png"))
        self.companyPlacementStatCardImage.setScaledContents(True)
        self.companyPlacementStatCardImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.companyPlacementStatCardImage)

        self.companyPlacementStatCardTitle = QLabel(self.companyPlacementStatCard)
        self.companyPlacementStatCardTitle.setObjectName(u"companyPlacementStatCardTitle")
        self.companyPlacementStatCardTitle.setMinimumSize(QSize(241, 75))
        self.companyPlacementStatCardTitle.setMaximumSize(QSize(241, 75))
        self.companyPlacementStatCardTitle.setStyleSheet(u"")
        self.companyPlacementStatCardTitle.setScaledContents(False)
        self.companyPlacementStatCardTitle.setAlignment(Qt.AlignCenter)
        self.companyPlacementStatCardTitle.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.companyPlacementStatCardTitle, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.performanceCard = QWidget(self.page_3)
        self.performanceCard.setObjectName(u"performanceCard")
        self.performanceCard.setGeometry(QRect(0, 0, 330, 360))
        self.performanceCard.setMinimumSize(QSize(330, 360))
        self.performanceCard.setMaximumSize(QSize(330, 360))
        self.performanceCard.setCursor(QCursor(Qt.ArrowCursor))
        self.performanceCard.setStyleSheet(u"\n"
"	border-top-right-radius: 34px;\n"
"	background-color: rgb(255, 255, 255);\n"
"")
        self.verticalLayout_5 = QVBoxLayout(self.performanceCard)
        self.verticalLayout_5.setSpacing(20)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(13, 11, 19, 10)
        self.performanceCardImage = QLabel(self.performanceCard)
        self.performanceCardImage.setObjectName(u"performanceCardImage")
        self.performanceCardImage.setMinimumSize(QSize(305, 241))
        self.performanceCardImage.setMaximumSize(QSize(305, 241))
        self.performanceCardImage.setPixmap(QPixmap(u":/icons/card3.png"))
        self.performanceCardImage.setScaledContents(True)
        self.performanceCardImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.performanceCardImage)

        self.performanceCardTitle = QLabel(self.performanceCard)
        self.performanceCardTitle.setObjectName(u"performanceCardTitle")
        self.performanceCardTitle.setMinimumSize(QSize(241, 75))
        self.performanceCardTitle.setMaximumSize(QSize(241, 75))
        self.performanceCardTitle.setStyleSheet(u"")
        self.performanceCardTitle.setScaledContents(True)
        self.performanceCardTitle.setAlignment(Qt.AlignCenter)
        self.performanceCardTitle.setWordWrap(True)

        self.verticalLayout_5.addWidget(self.performanceCardTitle, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page_3)
        self.CardButtons = QWidget(self.CardOutline)
        self.CardButtons.setObjectName(u"CardButtons")
        self.CardButtons.setGeometry(QRect(2, 360, 330, 40))
        self.CardButtons.setMinimumSize(QSize(330, 40))
        self.CardButtons.setMaximumSize(QSize(330, 40))
        self.CardButtons.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.horizontalLayout_3 = QHBoxLayout(self.CardButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 0, 9, 0)
        self.CardPrevButton = QLabel(self.CardButtons)
        self.CardPrevButton.setObjectName(u"CardPrevButton")
        self.CardPrevButton.setMaximumSize(QSize(30, 16777215))
        self.CardPrevButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CardPrevButton.setPixmap(QPixmap(u":/icons/arrow2.png"))
        self.CardPrevButton.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.CardPrevButton, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.StatCardRadioButtons = QWidget(self.CardButtons)
        self.StatCardRadioButtons.setObjectName(u"StatCardRadioButtons")
        self.StatCardRadioButtons.setMinimumSize(QSize(80, 30))
        self.StatCardRadioButtons.setMaximumSize(QSize(80, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.StatCardRadioButtons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 9, 0)
        self.radio1 = QRadioButton(self.StatCardRadioButtons)
        self.radio1.setObjectName(u"radio1")
        self.radio1.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio1.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.radio1, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.radio2 = QRadioButton(self.StatCardRadioButtons)
        self.radio2.setObjectName(u"radio2")
        self.radio2.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio2.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radio2, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.radio3 = QRadioButton(self.StatCardRadioButtons)
        self.radio3.setObjectName(u"radio3")
        self.radio3.setCursor(QCursor(Qt.PointingHandCursor))
        self.radio3.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.radio3, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.StatCardRadioButtons)

        self.CardNextButton = QLabel(self.CardButtons)
        self.CardNextButton.setObjectName(u"CardNextButton")
        self.CardNextButton.setMaximumSize(QSize(30, 16777215))
        self.CardNextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.CardNextButton.setStyleSheet(u"")
        self.CardNextButton.setPixmap(QPixmap(u":/icons/arrow.png"))
        self.CardNextButton.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.CardNextButton, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.fileButton = QPushButton(self.widget)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setGeometry(QRect(25, 25, 45, 45))
        self.fileButton.setMinimumSize(QSize(45, 45))
        self.fileButton.setMaximumSize(QSize(45, 45))
        self.fileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.fileButton.setFocusPolicy(Qt.NoFocus)
        self.fileButton.setStyleSheet(u"QPushButton#pushButton:pressed{\n"
"	padding: 10px;\n"
"}")
        icon = QIcon()
        iconThemeName = u"accessories-calculator"
        if QIcon.hasThemeIcon(iconThemeName):
            icon = QIcon.fromTheme(iconThemeName)
        else:
            icon.addFile(u":/icons/files1.png", QSize(), QIcon.Normal, QIcon.Off)

        self.fileButton.setIcon(icon)
        self.fileButton.setIconSize(QSize(30, 30))
        self.fileButton.setFlat(True)

        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidgetForCards.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText("")
        self.studentPlacementStatCardImage_2.setText("")
        self.studentPlacementStatCardTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">STUDENT PLACEMENT STATISTICS</span></p></body></html>", None))
        self.companyPlacementStatCardImage.setText("")
        self.companyPlacementStatCardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">COMPANY PLACEMENT STATISTICS</span></p></body></html>", None))
        self.performanceCardImage.setText("")
        self.performanceCardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">STUDENT PERFORMANCE REPORT</span></p></body></html>", None))
        self.CardPrevButton.setText("")
        self.radio1.setText("")
        self.radio2.setText("")
        self.radio3.setText("")
        self.CardNextButton.setText("")
        self.fileButton.setText("")
    # retranslateUi

