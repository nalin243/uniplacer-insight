# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'companyPlacementStatistics.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1060)
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(1920, 1060))
        MainWindow.setWindowIcon(QIcon(":/icons/iconlogo.png"))

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(60, -1, 60, 90)
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 2, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.lineGraphView = QChartView(self.centralwidget)
        self.lineGraphView.setObjectName(u"lineGraphView")
        self.lineGraphView.setStyleSheet(u"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.lineGraphView)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.totalcompaniesWidget = QWidget(self.centralwidget)
        self.totalcompaniesWidget.setObjectName(u"totalcompaniesWidget")
        self.totalcompaniesWidget.setMinimumSize(QSize(379, 101))
        self.totalcompaniesWidget.setMaximumSize(QSize(381, 101))
        self.totalcompaniesWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.totalCompaniesText = QLabel(self.totalcompaniesWidget)
        self.totalCompaniesText.setObjectName(u"totalCompaniesText")
        self.totalCompaniesText.setGeometry(QRect(120, 50, 241, 31))
        font = QFont()
        font.setFamilies([u"Lucida Sans"])
        font.setPointSize(18)
        font.setBold(True)
        self.totalCompaniesText.setFont(font)
        self.totalCompaniesLabel = QLabel(self.totalcompaniesWidget)
        self.totalCompaniesLabel.setObjectName(u"totalCompaniesLabel")
        self.totalCompaniesLabel.setGeometry(QRect(120, 20, 51, 31))
        self.totalCompaniesLabel.setFont(font)
        self.totalCompaniesImage = QLabel(self.totalcompaniesWidget)
        self.totalCompaniesImage.setObjectName(u"totalCompaniesImage")
        self.totalCompaniesImage.setGeometry(QRect(40, 20, 60, 60))
        self.totalCompaniesImage.setStyleSheet(u"")
        self.totalCompaniesImage.setPixmap(QPixmap(u":/icons/totalCompanyImg.png"))

        self.verticalLayout.addWidget(self.totalcompaniesWidget)

        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.companVisitedWidgets = QWidget(self.centralwidget)
        self.companVisitedWidgets.setObjectName(u"companVisitedWidgets")
        self.companVisitedWidgets.setMinimumSize(QSize(379, 101))
        self.companVisitedWidgets.setMaximumSize(QSize(381, 101))
        self.companVisitedWidgets.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.companiesVisitedText = QLabel(self.companVisitedWidgets)
        self.companiesVisitedText.setObjectName(u"companiesVisitedText")
        self.companiesVisitedText.setGeometry(QRect(120, 50, 241, 31))
        self.companiesVisitedText.setFont(font)
        self.companiesVisitedLabel = QLabel(self.companVisitedWidgets)
        self.companiesVisitedLabel.setObjectName(u"companiesVisitedLabel")
        self.companiesVisitedLabel.setGeometry(QRect(120, 20, 51, 31))
        self.companiesVisitedLabel.setFont(font)
        self.companiesVisitedImage = QLabel(self.companVisitedWidgets)
        self.companiesVisitedImage.setObjectName(u"companiesVisitedImage")
        self.companiesVisitedImage.setGeometry(QRect(40, 20, 60, 60))
        self.companiesVisitedImage.setStyleSheet(u"")
        self.companiesVisitedImage.setPixmap(QPixmap(u":/icons/companiesVisitedImg.png"))

        self.verticalLayout.addWidget(self.companVisitedWidgets)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.companiesHiredWidgets = QWidget(self.centralwidget)
        self.companiesHiredWidgets.setObjectName(u"companiesHiredWidgets")
        self.companiesHiredWidgets.setMinimumSize(QSize(371, 101))
        self.companiesHiredWidgets.setMaximumSize(QSize(381, 101))
        self.companiesHiredWidgets.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        self.companiesHiredText = QLabel(self.companiesHiredWidgets)
        self.companiesHiredText.setObjectName(u"companiesHiredText")
        self.companiesHiredText.setGeometry(QRect(120, 50, 241, 31))
        self.companiesHiredText.setFont(font)
        self.companiesHiredLabel = QLabel(self.companiesHiredWidgets)
        self.companiesHiredLabel.setObjectName(u"companiesHiredLabel")
        self.companiesHiredLabel.setGeometry(QRect(120, 20, 51, 31))
        self.companiesHiredLabel.setFont(font)
        self.companiesHiredImage = QLabel(self.companiesHiredWidgets)
        self.companiesHiredImage.setObjectName(u"companiesHiredImage")
        self.companiesHiredImage.setGeometry(QRect(40, 20, 60, 60))
        self.companiesHiredImage.setStyleSheet(u"")
        self.companiesHiredImage.setPixmap(QPixmap(u":/icons/companiesHiredImg.png"))

        self.hiredTableButton = QLabel(self.companiesHiredWidgets)
        self.hiredTableButton.setObjectName(u"hiredTableButton")
        self.hiredTableButton.setGeometry(QRect(350, 10, 15, 15))
        self.hiredTableButton.setPixmap(QPixmap(u":/icons/arrow 1.png"))

        self.verticalLayout.addWidget(self.companiesHiredWidgets)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalSpacer_2 = QSpacerItem(60, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.pieChartView = QChartView(self.centralwidget)
        self.pieChartView.setObjectName(u"pieChartView")
        self.pieChartView.setMaximumSize(QSize(501, 16777215))
        self.pieChartView.setStyleSheet(u"border-radius:10px;")

        self.horizontalLayout_2.addWidget(self.pieChartView)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.logoAndComboboxLayout = QHBoxLayout()
        self.logoAndComboboxLayout.setObjectName(u"logoAndComboboxLayout")
        self.LOGO = QLabel(self.centralwidget)
        self.LOGO.setObjectName(u"LOGO")
        self.LOGO.setMinimumSize(QSize(258, 165))
        self.LOGO.setMaximumSize(QSize(258, 165))
        self.LOGO.setStyleSheet(u"")
        self.LOGO.setPixmap(QPixmap(u":/icons/uni-placer 2(1).png"))

        self.logoAndComboboxLayout.addWidget(self.LOGO)

        self.horizontalSpacer_4 = QSpacerItem(115, 10, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.logoAndComboboxLayout.addItem(self.horizontalSpacer_4)

        self.layoutOfComboBoxes = QHBoxLayout()
        self.layoutOfComboBoxes.setSpacing(80)
        self.layoutOfComboBoxes.setObjectName(u"layoutOfComboBoxes")
        self.batchComboBox = QComboBox(self.centralwidget)
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.setObjectName(u"batchComboBox")
        self.batchComboBox.setMinimumSize(QSize(0, 31))
        self.batchComboBox.setEditable(False)

        self.layoutOfComboBoxes.addWidget(self.batchComboBox)

        self.typeOfJobCombobox = QComboBox(self.centralwidget)
        self.typeOfJobCombobox.addItem("")
        self.typeOfJobCombobox.addItem("")
        self.typeOfJobCombobox.addItem("")
        self.typeOfJobCombobox.setObjectName(u"typeOfJobCombobox")
        self.typeOfJobCombobox.setMinimumSize(QSize(0, 31))

        self.layoutOfComboBoxes.addWidget(self.typeOfJobCombobox)

        self.ctcCombobox = QComboBox(self.centralwidget)
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.addItem("")
        self.ctcCombobox.setObjectName(u"ctcCombobox")
        self.ctcCombobox.setMinimumSize(QSize(0, 31))

        self.layoutOfComboBoxes.addWidget(self.ctcCombobox)

        self.levelOfJobCombobox = QComboBox(self.centralwidget)
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.addItem("")
        self.levelOfJobCombobox.setObjectName(u"levelOfJobCombobox")
        self.levelOfJobCombobox.setMinimumSize(QSize(0, 31))

        self.layoutOfComboBoxes.addWidget(self.levelOfJobCombobox)

        self.sectorCombobox = QComboBox(self.centralwidget)
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.addItem("")
        self.sectorCombobox.setObjectName(u"sectorCombobox")
        self.sectorCombobox.setMinimumSize(QSize(0, 31))

        self.layoutOfComboBoxes.addWidget(self.sectorCombobox)


        self.logoAndComboboxLayout.addLayout(self.layoutOfComboBoxes)


        self.gridLayout.addLayout(self.logoAndComboboxLayout, 0, 0, 1, 1)

        self.barGraphAndNegDataLayout = QHBoxLayout()
        self.barGraphAndNegDataLayout.setSpacing(10)
        self.barGraphAndNegDataLayout.setObjectName(u"barGraphAndNegDataLayout")
        self.barGraphView = QChartView(self.centralwidget)
        self.barGraphView.setObjectName(u"barGraphView")
        self.barGraphView.setMinimumSize(QSize(0, 290))
        self.barGraphView.setMaximumSize(QSize(1231, 331))
        self.barGraphView.setStyleSheet(u"border-radius:10px;")

        self.barGraphAndNegDataLayout.addWidget(self.barGraphView)

        self.horizontalSpacer_3 = QSpacerItem(50, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.barGraphAndNegDataLayout.addItem(self.horizontalSpacer_3)

        self.negetiveDataWidgets = QWidget(self.centralwidget)
        self.negetiveDataWidgets.setObjectName(u"negetiveDataWidgets")
        self.negetiveDataWidgets.setMinimumSize(QSize(502, 290))
        self.negetiveDataWidgets.setMaximumSize(QSize(502, 331))
        self.negetiveDataWidgets.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"")
        # self.label = QLabel(self.negetiveDataWidgets)
        # self.label.setObjectName(u"label")
        # self.label.setGeometry(QRect(580, 10, 31, 31))
        # self.label.setPixmap(QPixmap(u"uniplacer-insight/src/uniplacerinsight/assets/arrow.png"))

        self.tableButton = QLabel(self.negetiveDataWidgets)
        self.tableButton.setObjectName(u"tableButton")
        self.tableButton.setGeometry(QRect(460, 10, 31, 31))
        self.tableButton.setPixmap(QPixmap(u":/icons/arrow.png"))

        self.layoutWidget = QWidget(self.negetiveDataWidgets)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(71, 56, 369, 78))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.companiesDidNotVisitImage = QLabel(self.layoutWidget)
        self.companiesDidNotVisitImage.setObjectName(u"companiesDidNotVisitImage")
        self.companiesDidNotVisitImage.setStyleSheet(u"")
        self.companiesDidNotVisitImage.setPixmap(QPixmap(u":/icons/companiesDidNotVistImg.png"))

        self.horizontalLayout.addWidget(self.companiesDidNotVisitImage)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.companiesNotVisitedLabel = QLabel(self.layoutWidget)
        self.companiesNotVisitedLabel.setObjectName(u"companiesNotVisitedLabel")
        self.companiesNotVisitedLabel.setFont(font)

        self.verticalLayout_2.addWidget(self.companiesNotVisitedLabel)

        self.companiesNotVisitedText = QLabel(self.layoutWidget)
        self.companiesNotVisitedText.setObjectName(u"companiesNotVisitedText")
        self.companiesNotVisitedText.setFont(font)

        self.verticalLayout_2.addWidget(self.companiesNotVisitedText)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.layoutWidget1 = QWidget(self.negetiveDataWidgets)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(71, 196, 366, 78))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.companiesDidNotHireImage = QLabel(self.layoutWidget1)
        self.companiesDidNotHireImage.setObjectName(u"companiesDidNotHireImage")
        self.companiesDidNotHireImage.setStyleSheet(u"")
        self.companiesDidNotHireImage.setPixmap(QPixmap(u":/icons/companiesDidNotHireImg.png"))

        self.horizontalLayout_3.addWidget(self.companiesDidNotHireImage)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.companiesNotHiredLabel = QLabel(self.layoutWidget1)
        self.companiesNotHiredLabel.setObjectName(u"companiesNotHiredLabel")
        self.companiesNotHiredLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.companiesNotHiredLabel)

        self.companiesNotHiredtext = QLabel(self.layoutWidget1)
        self.companiesNotHiredtext.setObjectName(u"companiesNotHiredtext")
        self.companiesNotHiredtext.setFont(font)

        self.verticalLayout_3.addWidget(self.companiesNotHiredtext)


        self.horizontalLayout_3.addLayout(self.verticalLayout_3)


        self.barGraphAndNegDataLayout.addWidget(self.negetiveDataWidgets)


        self.gridLayout.addLayout(self.barGraphAndNegDataLayout, 3, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.totalCompaniesText.setText(QCoreApplication.translate("MainWindow", u"Total Companies", None))
        self.totalCompaniesLabel.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.totalCompaniesImage.setText("")
        self.companiesVisitedText.setText(QCoreApplication.translate("MainWindow", u"Companies Visited", None))
        self.companiesVisitedLabel.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.companiesVisitedImage.setText("")
        self.companiesHiredText.setText(QCoreApplication.translate("MainWindow", u"Companies Hired", None))
        self.companiesHiredLabel.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.companiesHiredImage.setText("")
        self.hiredTableButton.setText("")
        self.LOGO.setText("")
        self.batchComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2024", None))
        self.batchComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2023", None))
        self.batchComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2022", None))
        self.batchComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"2021", None))

        self.typeOfJobCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Job Type(All)", None))
        self.typeOfJobCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"FULL TIME", None))
        self.typeOfJobCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"INTERNSHIP", None))

        self.ctcCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"CTC Range(All)", None))
        self.ctcCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"2LPA-5LPA", None))
        self.ctcCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"5LPA-10LPA", None))
        self.ctcCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"10LPA-15LPA", None))
        self.ctcCombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"15LPA-20LPA", None))
        self.ctcCombobox.setItemText(5, QCoreApplication.translate("MainWindow", u"20LPA-25LPA", None))
        self.ctcCombobox.setItemText(6, QCoreApplication.translate("MainWindow", u"25LPA-30LPA", None))
        self.ctcCombobox.setItemText(7, QCoreApplication.translate("MainWindow", u"30LPA-35LPA", None))
        self.ctcCombobox.setItemText(8, QCoreApplication.translate("MainWindow", u"35LPA-40LPA", None))

        self.levelOfJobCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Job Level(All)", None))
        self.levelOfJobCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Level 1 - Dream", None))
        self.levelOfJobCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Level 1 - General", None))
        self.levelOfJobCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Level 1 - BPO", None))
        self.levelOfJobCombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"Level 2 - Dream", None))
        self.levelOfJobCombobox.setItemText(5, QCoreApplication.translate("MainWindow", u"Level 2 - General", None))
        self.levelOfJobCombobox.setItemText(6, QCoreApplication.translate("MainWindow", u"Level 2 - BPO", None))
        self.levelOfJobCombobox.setItemText(7, QCoreApplication.translate("MainWindow", u"Level 3 - Dream", None))
        self.levelOfJobCombobox.setItemText(8, QCoreApplication.translate("MainWindow", u"Level 3 - General", None))
        self.levelOfJobCombobox.setItemText(9, QCoreApplication.translate("MainWindow", u"Level 3 - BPO", None))

        self.sectorCombobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Job Sector(All)", None))
        self.sectorCombobox.setItemText(1, QCoreApplication.translate("MainWindow", u"ACTUARY", None))
        self.sectorCombobox.setItemText(2, QCoreApplication.translate("MainWindow", u"ADVERTISING MEDIA PR", None))
        self.sectorCombobox.setItemText(3, QCoreApplication.translate("MainWindow", u"BANKING AND FINANCIAL SERVICES", None))
        self.sectorCombobox.setItemText(4, QCoreApplication.translate("MainWindow", u"BUSINESS DEVELOPMENT", None))
        self.sectorCombobox.setItemText(5, QCoreApplication.translate("MainWindow", u"CONSULTING", None))
        self.sectorCombobox.setItemText(6, QCoreApplication.translate("MainWindow", u"CUSTOMER TECHNICAL SUPPORT", None))
        self.sectorCombobox.setItemText(7, QCoreApplication.translate("MainWindow", u"DATA ANALYTICS", None))
        self.sectorCombobox.setItemText(8, QCoreApplication.translate("MainWindow", u"DESIGN ART", None))
        self.sectorCombobox.setItemText(9, QCoreApplication.translate("MainWindow", u"ENGINEERING", None))
        self.sectorCombobox.setItemText(10, QCoreApplication.translate("MainWindow", u"ENGINEERING CORE", None))
        self.sectorCombobox.setItemText(11, QCoreApplication.translate("MainWindow", u"ENGINEERING WEB SOFTWARE", None))
        self.sectorCombobox.setItemText(12, QCoreApplication.translate("MainWindow", u"EDUCATION TEACHING TRAINING", None))
        self.sectorCombobox.setItemText(13, QCoreApplication.translate("MainWindow", u"FINANCE", None))
        self.sectorCombobox.setItemText(14, QCoreApplication.translate("MainWindow", u"INFORMATION TECHNOLOGY", None))
        self.sectorCombobox.setItemText(15, QCoreApplication.translate("MainWindow", u"GENERAL MANAGEMENT", None))
        self.sectorCombobox.setItemText(16, QCoreApplication.translate("MainWindow", u"HUMAN RESOURCES", None))
        self.sectorCombobox.setItemText(17, QCoreApplication.translate("MainWindow", u"OPERATIONS PRODUCTION", None))
        self.sectorCombobox.setItemText(18, QCoreApplication.translate("MainWindow", u"PROJECT MANAGEMENT", None))
        self.sectorCombobox.setItemText(19, QCoreApplication.translate("MainWindow", u"QUALITY ASSURANCE", None))
        self.sectorCombobox.setItemText(20, QCoreApplication.translate("MainWindow", u"SALES", None))
        self.sectorCombobox.setItemText(21, QCoreApplication.translate("MainWindow", u"WRITING EDITING", None))

        # self.label.setText("")
        self.tableButton.setText("")
        self.companiesDidNotVisitImage.setText("")
        self.companiesNotVisitedLabel.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.companiesNotVisitedText.setText(QCoreApplication.translate("MainWindow", u"Companies Did Not Visit", None))
        self.companiesDidNotHireImage.setText("")
        self.companiesNotHiredLabel.setText(QCoreApplication.translate("MainWindow", u"100", None))
        self.companiesNotHiredtext.setText(QCoreApplication.translate("MainWindow", u"Companies Did Not Hire", None))
    # retranslateUi

