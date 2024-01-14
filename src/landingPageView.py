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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QRadioButton,
    QSizePolicy, QStackedWidget, QVBoxLayout, QWidget, QGraphicsBlurEffect,QGraphicsOpacityEffect)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setMinimumSize(1920, 1080)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#centralwidget {\n"
"	background-image: url(\"../uniplacer-insight/assets/bg.png\");\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.blueCard = QFrame(self.widget)
        self.blueCard.setObjectName(u"blueCard")
        self.blueCard.setEnabled(True)


        self.blueCard.setMinimumSize(QSize(1279, 725))
        self.blueCard.setMaximumSize(QSize(1279, 725))
        self.blueCard.setFrameShape(QFrame.StyledPanel)
        self.blueCard.setFrameShadow(QFrame.Raised)

        self.title = QLabel(self.blueCard)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(30, 230, 591, 271))
        self.title.setMaximumSize(QSize(16777215, 16777215))
        self.title.setPixmap(QPixmap(u"../uniplacer-insight/assets/title.png"))
        self.title.setScaledContents(True)
        self.title.setAlignment(Qt.AlignCenter)

        self.stackedWidgetForCards = QStackedWidget(self.blueCard)
        self.stackedWidgetForCards.setObjectName(u"stackedWidgetForCards")
        self.stackedWidgetForCards.setGeometry(QRect(685, 32, 554, 664))
        self.stackedWidgetForCards.setStyleSheet(u"")
        self.stackedWidgetForCards.setFrameShape(QFrame.NoFrame)
        self.stackedWidgetForCards.setFrameShadow(QFrame.Plain)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.studentPlacementStatCard = QFrame(self.page)
        self.studentPlacementStatCard.setObjectName(u"studentPlacementStatCard")
        self.studentPlacementStatCard.setGeometry(QRect(0, 0, 554, 664))
        self.studentPlacementStatCard.setCursor(QCursor(Qt.ArrowCursor))
        self.studentPlacementStatCard.setStyleSheet(u"#studentPlacementStatCard {\n"
"\n"
"border-radius: 20px 20px;\n"
"background-color: rgb(255, 255, 255);\n"
"\n"
"}")
        self.studentPlacementStatCard.setFrameShape(QFrame.StyledPanel)
        self.studentPlacementStatCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.studentPlacementStatCard)
        self.verticalLayout_2.setSpacing(40)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(19, 22, 19, 10)
        self.studentPlacementStatCardImage = QLabel(self.studentPlacementStatCard)
        self.studentPlacementStatCardImage.setObjectName(u"studentPlacementStatCardImage")
        self.studentPlacementStatCardImage.setMinimumSize(QSize(0, 400))
        self.studentPlacementStatCardImage.setMaximumSize(QSize(16777215, 16777215))
        self.studentPlacementStatCardImage.setPixmap(QPixmap(u"../uniplacer-insight/assets/land-graph.png"))
        self.studentPlacementStatCardImage.setScaledContents(True)
        self.studentPlacementStatCardImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.studentPlacementStatCardImage)

        self.studentPlacementStatCardTitle = QLabel(self.studentPlacementStatCard)
        self.studentPlacementStatCardTitle.setObjectName(u"studentPlacementStatCardTitle")
        self.studentPlacementStatCardTitle.setMaximumSize(QSize(16777215, 16777215))
        self.studentPlacementStatCardTitle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.studentPlacementStatCardTitle.setScaledContents(False)
        self.studentPlacementStatCardTitle.setAlignment(Qt.AlignCenter)
        self.studentPlacementStatCardTitle.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.studentPlacementStatCardTitle, 0, Qt.AlignTop)

        self.studentPlacementStatCardButtons_2 = QFrame(self.studentPlacementStatCard)
        self.studentPlacementStatCardButtons_2.setObjectName(u"studentPlacementStatCardButtons_2")
        self.studentPlacementStatCardButtons_2.setMinimumSize(QSize(520, 50))
        self.studentPlacementStatCardButtons_2.setMaximumSize(QSize(16777215, 16777215))
        self.studentPlacementStatCardButtons_2.setFrameShape(QFrame.StyledPanel)
        self.studentPlacementStatCardButtons_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.studentPlacementStatCardButtons_2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 8)
        self.emptyButtonStudentCard = QLabel(self.studentPlacementStatCardButtons_2)
        self.emptyButtonStudentCard.setObjectName(u"emptyButtonStudentCard")
        self.emptyButtonStudentCard.setMaximumSize(QSize(30, 16777215))
        self.emptyButtonStudentCard.setCursor(QCursor(Qt.PointingHandCursor))
        self.emptyButtonStudentCard.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.emptyButtonStudentCard, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.studentPlacementStatCardRButtons_2 = QFrame(self.studentPlacementStatCardButtons_2)
        self.studentPlacementStatCardRButtons_2.setObjectName(u"studentPlacementStatCardRButtons_2")
        self.studentPlacementStatCardRButtons_2.setMaximumSize(QSize(80, 16777215))
        self.studentPlacementStatCardRButtons_2.setFrameShape(QFrame.StyledPanel)
        self.studentPlacementStatCardRButtons_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.studentPlacementStatCardRButtons_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.radioButton_10 = QRadioButton(self.studentPlacementStatCardRButtons_2)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_10.setChecked(True)

        self.horizontalLayout_8.addWidget(self.radioButton_10, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.radioButton_11 = QRadioButton(self.studentPlacementStatCardRButtons_2)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_11.setChecked(False)

        self.horizontalLayout_8.addWidget(self.radioButton_11, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.radioButton_12 = QRadioButton(self.studentPlacementStatCardRButtons_2)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_8.addWidget(self.radioButton_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_7.addWidget(self.studentPlacementStatCardRButtons_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.studentPlacementStatCardNextButton_2 = QLabel(self.studentPlacementStatCardButtons_2)
        self.studentPlacementStatCardNextButton_2.setObjectName(u"studentPlacementStatCardNextButton_2")
        self.studentPlacementStatCardNextButton_2.setMaximumSize(QSize(30, 16777215))
        self.studentPlacementStatCardNextButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.studentPlacementStatCardNextButton_2.setPixmap(QPixmap(u"../uniplacer-insight/assets/arrow.png"))
        self.studentPlacementStatCardNextButton_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.studentPlacementStatCardNextButton_2, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_2.addWidget(self.studentPlacementStatCardButtons_2, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.companyPlacementStatCard = QFrame(self.page_2)
        self.companyPlacementStatCard.setObjectName(u"companyPlacementStatCard")
        self.companyPlacementStatCard.setGeometry(QRect(0, 0, 554, 664))
        self.companyPlacementStatCard.setCursor(QCursor(Qt.ArrowCursor))
        self.companyPlacementStatCard.setStyleSheet(u"\n"
"\n"
"	border-radius: 20px 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"")
        self.companyPlacementStatCard.setFrameShape(QFrame.StyledPanel)
        self.companyPlacementStatCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.companyPlacementStatCard)
        self.verticalLayout_3.setSpacing(40)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(19, 22, 19, 10)
        self.companyPlacementStatCardImage = QLabel(self.companyPlacementStatCard)
        self.companyPlacementStatCardImage.setObjectName(u"companyPlacementStatCardImage")
        self.companyPlacementStatCardImage.setMinimumSize(QSize(0, 400))
        self.companyPlacementStatCardImage.setMaximumSize(QSize(16777215, 16777215))
        self.companyPlacementStatCardImage.setPixmap(QPixmap(u"../uniplacer-insight/assets/card2.png"))
        self.companyPlacementStatCardImage.setScaledContents(True)
        self.companyPlacementStatCardImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.companyPlacementStatCardImage)

        self.companyPlacementStatCardTitle = QLabel(self.companyPlacementStatCard)
        self.companyPlacementStatCardTitle.setObjectName(u"companyPlacementStatCardTitle")
        self.companyPlacementStatCardTitle.setMaximumSize(QSize(16777215, 16777215))
        self.companyPlacementStatCardTitle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.companyPlacementStatCardTitle.setScaledContents(False)
        self.companyPlacementStatCardTitle.setAlignment(Qt.AlignCenter)
        self.companyPlacementStatCardTitle.setWordWrap(True)

        self.verticalLayout_3.addWidget(self.companyPlacementStatCardTitle, 0, Qt.AlignTop)

        self.companyStatCardButtons = QFrame(self.companyPlacementStatCard)
        self.companyStatCardButtons.setObjectName(u"companyStatCardButtons")
        self.companyStatCardButtons.setMinimumSize(QSize(520, 50))
        self.companyStatCardButtons.setMaximumSize(QSize(16777215, 16777215))
        self.companyStatCardButtons.setFrameShape(QFrame.StyledPanel)
        self.companyStatCardButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.companyStatCardButtons)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.companyPlacementStatCardPrevButton = QLabel(self.companyStatCardButtons)
        self.companyPlacementStatCardPrevButton.setObjectName(u"companyPlacementStatCardPrevButton")
        self.companyPlacementStatCardPrevButton.setMaximumSize(QSize(30, 16777215))
        self.companyPlacementStatCardPrevButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.companyPlacementStatCardPrevButton.setPixmap(QPixmap(u"../uniplacer-insight/assets/arrow2.png"))
        self.companyPlacementStatCardPrevButton.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.companyPlacementStatCardPrevButton, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.companyPlacementStatCardRButtons = QFrame(self.companyStatCardButtons)
        self.companyPlacementStatCardRButtons.setObjectName(u"companyPlacementStatCardRButtons")
        self.companyPlacementStatCardRButtons.setMaximumSize(QSize(70, 16777215))
        self.companyPlacementStatCardRButtons.setFrameShape(QFrame.StyledPanel)
        self.companyPlacementStatCardRButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.companyPlacementStatCardRButtons)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.radioButton_4 = QRadioButton(self.companyPlacementStatCardRButtons)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.radioButton_4, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.radioButton_5 = QRadioButton(self.companyPlacementStatCardRButtons)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.radioButton_5.setChecked(True)

        self.horizontalLayout_4.addWidget(self.radioButton_5, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.radioButton_6 = QRadioButton(self.companyPlacementStatCardRButtons)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.radioButton_6, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_3.addWidget(self.companyPlacementStatCardRButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.companyPlacementStatCardNextButton = QLabel(self.companyStatCardButtons)
        self.companyPlacementStatCardNextButton.setObjectName(u"companyPlacementStatCardNextButton")
        self.companyPlacementStatCardNextButton.setMaximumSize(QSize(30, 16777215))
        self.companyPlacementStatCardNextButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.companyPlacementStatCardNextButton.setPixmap(QPixmap(u"../uniplacer-insight/assets/arrow.png"))
        self.companyPlacementStatCardNextButton.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.companyPlacementStatCardNextButton, 0, Qt.AlignRight|Qt.AlignVCenter)


        self.verticalLayout_3.addWidget(self.companyStatCardButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.performanceCard = QFrame(self.page_3)
        self.performanceCard.setObjectName(u"performanceCard")
        self.performanceCard.setGeometry(QRect(0, 0, 554, 664))
        self.performanceCard.setCursor(QCursor(Qt.ArrowCursor))
        self.performanceCard.setStyleSheet(u"\n"
"\n"
"	border-radius: 20px 20px;\n"
"	background-color: rgb(255, 255, 255);\n"
"")
        self.performanceCard.setFrameShape(QFrame.StyledPanel)
        self.performanceCard.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.performanceCard)
        self.verticalLayout_4.setSpacing(40)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(19, 22, 19, 10)
        self.performanceCardImage = QLabel(self.performanceCard)
        self.performanceCardImage.setObjectName(u"performanceCardImage")
        self.performanceCardImage.setMinimumSize(QSize(0, 400))
        self.performanceCardImage.setMaximumSize(QSize(16777215, 16777215))
        self.performanceCardImage.setPixmap(QPixmap(u"../uniplacer-insight/assets/card3.png"))
        self.performanceCardImage.setScaledContents(True)
        self.performanceCardImage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.performanceCardImage)

        self.performanceCardTitle = QLabel(self.performanceCard)
        self.performanceCardTitle.setObjectName(u"performanceCardTitle")
        self.performanceCardTitle.setMaximumSize(QSize(16777215, 16777215))
        self.performanceCardTitle.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.performanceCardTitle.setScaledContents(True)
        self.performanceCardTitle.setAlignment(Qt.AlignCenter)
        self.performanceCardTitle.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.performanceCardTitle, 0, Qt.AlignTop)

        self.performanceCardButtons = QFrame(self.performanceCard)
        self.performanceCardButtons.setObjectName(u"performanceCardButtons")
        self.performanceCardButtons.setMinimumSize(QSize(520, 50))
        self.performanceCardButtons.setMaximumSize(QSize(16777215, 16777215))
        self.performanceCardButtons.setFrameShape(QFrame.StyledPanel)
        self.performanceCardButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.performanceCardButtons)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 10, -1, 9)
        self.performanceCardPrevButton = QLabel(self.performanceCardButtons)
        self.performanceCardPrevButton.setObjectName(u"performanceCardPrevButton")
        self.performanceCardPrevButton.setMaximumSize(QSize(30, 16777215))
        self.performanceCardPrevButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.performanceCardPrevButton.setPixmap(QPixmap(u"../uniplacer-insight/assets/arrow2.png"))
        self.performanceCardPrevButton.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.performanceCardPrevButton)

        self.performanceCardRButtons = QFrame(self.performanceCardButtons)
        self.performanceCardRButtons.setObjectName(u"performanceCardRButtons")
        self.performanceCardRButtons.setMaximumSize(QSize(70, 16777215))
        self.performanceCardRButtons.setFrameShape(QFrame.StyledPanel)
        self.performanceCardRButtons.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.performanceCardRButtons)
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.radioButton_7 = QRadioButton(self.performanceCardRButtons)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout_6.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.performanceCardRButtons)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setCursor(QCursor(Qt.PointingHandCursor))

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


        self.verticalLayout_4.addWidget(self.performanceCardButtons, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.stackedWidgetForCards.addWidget(self.page_3)
        self.fileButton = QPushButton(self.blueCard)
        self.fileButton.setObjectName(u"fileButton")
        self.fileButton.setGeometry(QRect(22, 22, 50, 50))
        self.fileButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.fileButton.setStyleSheet(u"")
        icon = QIcon()
        icon.addFile(u"../uniplacer-insight/assets/databaseUpload.png", QSize(), QIcon.Normal, QIcon.Off)
        self.fileButton.setIcon(icon)
        self.fileButton.setIconSize(QSize(50, 50))
        self.fileButton.setAutoDefault(False)
        self.fileButton.setFlat(True)
        self.label = QLabel(self.blueCard)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(32, 32, 30, 30))
        self.label.setPixmap(QPixmap(u"../uniplacer-insight/assets/files1.png"))
        self.label.setScaledContents(True)

        self.gridLayout.addWidget(self.blueCard, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignVCenter)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidgetForCards.setCurrentIndex(0)
        self.fileButton.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.title.setText("")
        self.studentPlacementStatCardImage.setText("")
        self.studentPlacementStatCardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">STUDENT PLACEMENT STATISTICS</span></p></body></html>", None))
        self.emptyButtonStudentCard.setText("")
        self.radioButton_10.setText("")
        self.radioButton_11.setText("")
        self.radioButton_12.setText("")
        self.studentPlacementStatCardNextButton_2.setText("")
        self.companyPlacementStatCardImage.setText("")
        self.companyPlacementStatCardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">COMPANY PLACEMENT STATISTICS</span></p></body></html>", None))
        self.companyPlacementStatCardPrevButton.setText("")
        self.radioButton_4.setText("")
        self.radioButton_5.setText("")
        self.radioButton_6.setText("")
        self.companyPlacementStatCardNextButton.setText("")
        self.performanceCardImage.setText("")
        self.performanceCardTitle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:700;\">STUDENT PERFORMANCE REPORT</span></p></body></html>", None))
        self.performanceCardPrevButton.setText("")
        self.radioButton_7.setText("")
        self.radioButton_8.setText("")
        self.radioButton_9.setText("")
        self.performanceCardEmptyLabel.setText("")
        self.fileButton.setText("")
        self.label.setText("")
    # retranslateUi

