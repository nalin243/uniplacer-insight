# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'landingView.ui'
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
from PySide6.QtWidgets import (QApplication, QWidget, QHBoxLayout, QLabel,
    QMainWindow, QRadioButton, QSizePolicy, QStackedWidget,
    QVBoxLayout)

import images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1440, 810)
        MainWindow.setMinimumSize(QSize(1440, 810))
        MainWindow.setMaximumSize(QSize(1440, 810))
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
        self.stackedWidgetForCards = QStackedWidget(self.widget)
        self.stackedWidgetForCards.setObjectName(u"stackedWidgetForCards")
        self.stackedWidgetForCards.setGeometry(QRect(480, 52, 330, 400))
        self.stackedWidgetForCards.setMinimumSize(QSize(330, 400))
        self.stackedWidgetForCards.setMaximumSize(QSize(330, 400))
        self.stackedWidgetForCards.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.studentPlacementStatCard = QWidget(self.page)
        self.studentPlacementStatCard.setObjectName(u"studentPlacementStatCard")
        self.studentPlacementStatCard.setGeometry(QRect(0, 0, 330, 400))
        self.studentPlacementStatCard.setMinimumSize(QSize(330, 400))
        self.studentPlacementStatCard.setMaximumSize(QSize(330, 400))
        self.studentPlacementStatCard.setCursor(QCursor(Qt.ArrowCursor))
        self.studentPlacementStatCard.setStyleSheet(u"#studentPlacementStatCard {\n"
"\n"
"border-top-right-radius: 34px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}")
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

        self.studentPlacementStatCardButtons = QWidget(self.studentPlacementStatCard)
        self.studentPlacementStatCardButtons.setObjectName(u"studentPlacementStatCardButtons")
        self.studentPlacementStatCardButtons.setMinimumSize(QSize(310, 40))
        self.studentPlacementStatCardButtons.setMaximumSize(QSize(310, 40))
        self.horizontalLayout = QHBoxLayout(self.studentPlacementStatCardButtons)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.emptyButtonStudentCard_2 = QLabel(self.studentPlacementStatCardButtons)
        self.emptyButtonStudentCard_2.setObjectName(u"emptyButtonStudentCard_2")
        self.emptyButtonStudentCard_2.setMaximumSize(QSize(30, 16777215))
        self.emptyButtonStudentCard_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.emptyButtonStudentCard_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.emptyButtonStudentCard_2, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.studentPlacementStatCardRButtons = QWidget(self.studentPlacementStatCardButtons)
        self.studentPlacementStatCardRButtons.setObjectName(u"studentPlacementStatCardRButtons")
        self.studentPlacementStatCardRButtons.setMinimumSize(QSize(80, 30))
        self.studentPlacementStatCardRButtons.setMaximumSize(QSize(80, 30))
        self.studentPlacementStatCardRButtons.setSizeIncrement(QSize(0, 0))
        self.horizontalLayout_10 = QHBoxLayout(self.studentPlacementStatCardRButtons)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(9, 0, 9, 0)
        self.radioButton_13 = QRadioButton(self.studentPlacementStatCardRButtons)
        self.radioButton_13.setObjectName(u"radioButton_13")
        self.radioButton_13.setMaximumSize(QSize(16777215, 16777215))
        self.radioButton_13.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_13.setChecked(True)

        self.horizontalLayout_10.addWidget(self.radioButton_13, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.radioButton_14 = QRadioButton(self.studentPlacementStatCardRButtons)
        self.radioButton_14.setObjectName(u"radioButton_14")
        self.radioButton_14.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_14.setCheckable(False)
        self.radioButton_14.setChecked(False)

        self.horizontalLayout_10.addWidget(self.radioButton_14, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.radioButton_15 = QRadioButton(self.studentPlacementStatCardRButtons)
        self.radioButton_15.setObjectName(u"radioButton_15")
        self.radioButton_15.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_15.setCheckable(False)

        self.horizontalLayout_10.addWidget(self.radioButton_15, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout.addWidget(self.studentPlacementStatCardRButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.studentPlacementStatCardNextButton = QLabel(self.studentPlacementStatCardButtons)
        self.studentPlacementStatCardNextButton.setObjectName(u"studentPlacementStatCardNextButton")
        self.studentPlacementStatCardNextButton.setMinimumSize(QSize(25, 25))
        self.studentPlacementStatCardNextButton.setMaximumSize(QSize(30, 30))
        self.studentPlacementStatCardNextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.studentPlacementStatCardNextButton.setPixmap(QPixmap(u":/icons/arrow.png"))
        self.studentPlacementStatCardNextButton.setScaledContents(True)
        self.studentPlacementStatCardNextButton.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.studentPlacementStatCardNextButton, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.studentPlacementStatCardButtons)

        self.stackedWidgetForCards.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.companyPlacementStatCard = QWidget(self.page_2)
        self.companyPlacementStatCard.setObjectName(u"companyPlacementStatCard")
        self.companyPlacementStatCard.setGeometry(QRect(0, 0, 330, 400))
        self.companyPlacementStatCard.setMinimumSize(QSize(330, 400))
        self.companyPlacementStatCard.setMaximumSize(QSize(330, 400))
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

        self.companyStatCardButtons = QWidget(self.companyPlacementStatCard)
        self.companyStatCardButtons.setObjectName(u"companyStatCardButtons")
        self.companyStatCardButtons.setMinimumSize(QSize(310, 40))
        self.companyStatCardButtons.setMaximumSize(QSize(310, 40))
        self.horizontalLayout_3 = QHBoxLayout(self.companyStatCardButtons)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.companyPlacementStatCardPrevButton = QLabel(self.companyStatCardButtons)
        self.companyPlacementStatCardPrevButton.setObjectName(u"companyPlacementStatCardPrevButton")
        self.companyPlacementStatCardPrevButton.setMaximumSize(QSize(30, 16777215))
        self.companyPlacementStatCardPrevButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.companyPlacementStatCardPrevButton.setPixmap(QPixmap(u":/icons/arrow2.png"))
        self.companyPlacementStatCardPrevButton.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.companyPlacementStatCardPrevButton, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.companyPlacementStatCardRButtons = QWidget(self.companyStatCardButtons)
        self.companyPlacementStatCardRButtons.setObjectName(u"companyPlacementStatCardRButtons")
        self.companyPlacementStatCardRButtons.setMinimumSize(QSize(80, 30))
        self.companyPlacementStatCardRButtons.setMaximumSize(QSize(80, 30))
        self.horizontalLayout_4 = QHBoxLayout(self.companyPlacementStatCardRButtons)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(15, 0, 9, 0)
        self.radioButton_4 = QRadioButton(self.companyPlacementStatCardRButtons)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_4.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.radioButton_4, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.radioButton_5 = QRadioButton(self.companyPlacementStatCardRButtons)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_5.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_5, 0, Qt.AlignRight|Qt.AlignVCenter)

        self.radioButton_6 = QRadioButton(self.companyPlacementStatCardRButtons)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_6.setCheckable(False)

        self.horizontalLayout_4.addWidget(self.radioButton_6, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.companyPlacementStatCardRButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.companyPlacementStatCardNextButton = QLabel(self.companyStatCardButtons)
        self.companyPlacementStatCardNextButton.setObjectName(u"companyPlacementStatCardNextButton")
        self.companyPlacementStatCardNextButton.setMaximumSize(QSize(30, 16777215))
        self.companyPlacementStatCardNextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.companyPlacementStatCardNextButton.setPixmap(QPixmap(u":/icons/arrow.png"))
        self.companyPlacementStatCardNextButton.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.companyPlacementStatCardNextButton, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_4.addWidget(self.companyStatCardButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.performanceCard = QWidget(self.page_3)
        self.performanceCard.setObjectName(u"performanceCard")
        self.performanceCard.setGeometry(QRect(0, 0, 330, 400))
        self.performanceCard.setMinimumSize(QSize(330, 400))
        self.performanceCard.setMaximumSize(QSize(330, 400))
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
        self.performanceCardImage.setMaximumSize(QSize(16777215, 16777215))
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

        self.performanceCardButtons = QWidget(self.performanceCard)
        self.performanceCardButtons.setObjectName(u"performanceCardButtons")
        self.performanceCardButtons.setMinimumSize(QSize(310, 40))
        self.performanceCardButtons.setMaximumSize(QSize(310, 40))
        self.horizontalLayout_5 = QHBoxLayout(self.performanceCardButtons)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.performanceCardPrevButton = QLabel(self.performanceCardButtons)
        self.performanceCardPrevButton.setObjectName(u"performanceCardPrevButton")
        self.performanceCardPrevButton.setMaximumSize(QSize(30, 16777215))
        self.performanceCardPrevButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.performanceCardPrevButton.setPixmap(QPixmap(u":/icons/arrow2.png"))
        self.performanceCardPrevButton.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.performanceCardPrevButton)

        self.performanceCardRButtons = QWidget(self.performanceCardButtons)
        self.performanceCardRButtons.setObjectName(u"performanceCardRButtons")
        self.performanceCardRButtons.setMinimumSize(QSize(80, 30))
        self.performanceCardRButtons.setMaximumSize(QSize(80, 30))
        self.horizontalLayout_6 = QHBoxLayout(self.performanceCardRButtons)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(15, 0, -1, 0)
        self.radioButton_7 = QRadioButton(self.performanceCardRButtons)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_7.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.performanceCardRButtons)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_8.setCheckable(False)

        self.horizontalLayout_6.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.performanceCardRButtons)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_9.setChecked(True)

        self.horizontalLayout_6.addWidget(self.radioButton_9, 0, Qt.AlignHCenter)


        self.horizontalLayout_5.addWidget(self.performanceCardRButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.performanceCardEmptyLabel = QLabel(self.performanceCardButtons)
        self.performanceCardEmptyLabel.setObjectName(u"performanceCardEmptyLabel")
        self.performanceCardEmptyLabel.setMaximumSize(QSize(30, 16777215))
        self.performanceCardEmptyLabel.setCursor(QCursor(Qt.PointingHandCursor))
        self.performanceCardEmptyLabel.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.performanceCardEmptyLabel)


        self.verticalLayout_5.addWidget(self.performanceCardButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page_3)
        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 170, 381, 171))
        self.title.setMaximumSize(QSize(16777215, 16777215))
        self.title.setPixmap(QPixmap(u":/icons/title.png"))
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)
        self.uploadButton = QLabel(self.widget)
        self.uploadButton.setObjectName(u"uploadButton")
        self.uploadButton.setGeometry(QRect(30, 30, 30, 30))
        self.uploadButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.uploadButton.setPixmap(QPixmap(u":/icons/files1.png"))
        self.uploadButton.setScaledContents(True)

        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidgetForCards.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.studentPlacementStatCardImage_2.setText("")
        self.studentPlacementStatCardTitle_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">STUDENT PLACEMENT STATISTICS</span></p></body></html>", None))
        self.emptyButtonStudentCard_2.setText("")
        self.radioButton_13.setText("")
        self.radioButton_14.setText("")
        self.radioButton_15.setText("")
        self.studentPlacementStatCardNextButton.setText("")
        self.companyPlacementStatCardImage.setText("")
        self.companyPlacementStatCardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">COMPANY PLACEMENT STATISTICS</span></p></body></html>", None))
        self.companyPlacementStatCardPrevButton.setText("")
        self.radioButton_4.setText("")
        self.radioButton_5.setText("")
        self.radioButton_6.setText("")
        self.companyPlacementStatCardNextButton.setText("")
        self.performanceCardImage.setText("")
        self.performanceCardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:700;\">STUDENT PERFORMANCE REPORT</span></p></body></html>", None))
        self.performanceCardPrevButton.setText("")
        self.radioButton_7.setText("")
        self.radioButton_8.setText("")
        self.radioButton_9.setText("")
        self.performanceCardEmptyLabel.setText("")
        self.title.setText("")
        self.uploadButton.setText("")
    # retranslateUi

