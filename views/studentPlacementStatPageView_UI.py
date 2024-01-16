# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QMainWindow,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

import images

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1082)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setMaximumSize(QSize(1920, 1080))
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color:#D9D9D9; \n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1080))
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.horizontalLayout_2 = QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.dashContainer = QWidget(self.centralwidget)
        self.dashContainer.setObjectName(u"dashContainer")
        self.dashContainer.setMinimumSize(QSize(0, 0))
        self.dashContainer.setMaximumSize(QSize(16777215, 16777215))
        self.dashContainer.setLayoutDirection(Qt.LeftToRight)
        self.dashContainer.setStyleSheet(u"#dashContainer{\n"
"background-image:url(:/icons/studentStatbg.png);\n"
"}")
        self.gridLayout = QGridLayout(self.dashContainer)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.appLogo = QLabel(self.dashContainer)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setMaximumSize(QSize(258, 60))
        self.appLogo.setPixmap(QPixmap(u":/icons/applogo.png"))
        self.appLogo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.appLogo)

        self.horizontalSpacer_9 = QSpacerItem(85, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.campusComboBox = QComboBox(self.dashContainer)
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.addItem("")
        self.campusComboBox.setObjectName(u"campusComboBox")
        self.campusComboBox.setMinimumSize(QSize(277, 47))

        self.horizontalLayout.addWidget(self.campusComboBox)

        self.horizontalSpacer_8 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_8)

        self.batchComboBox = QComboBox(self.dashContainer)
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.addItem("")
        self.batchComboBox.setObjectName(u"batchComboBox")
        self.batchComboBox.setMinimumSize(QSize(277, 47))
        self.batchComboBox.setMaximumSize(QSize(277, 47))

        self.horizontalLayout.addWidget(self.batchComboBox)

        self.horizontalSpacer_3 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)

        self.departmentComboBox = QComboBox(self.dashContainer)
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.addItem("")
        self.departmentComboBox.setObjectName(u"departmentComboBox")
        self.departmentComboBox.setMinimumSize(QSize(277, 47))
        self.departmentComboBox.setMaximumSize(QSize(277, 47))

        self.horizontalLayout.addWidget(self.departmentComboBox)

        self.horizontalSpacer_4 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.courseComboBox = QComboBox(self.dashContainer)
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.addItem("")
        self.courseComboBox.setObjectName(u"courseComboBox")
        self.courseComboBox.setMinimumSize(QSize(277, 47))
        self.courseComboBox.setMaximumSize(QSize(277, 47))

        self.horizontalLayout.addWidget(self.courseComboBox)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.genderComboBox = QComboBox(self.dashContainer)
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.addItem("")
        self.genderComboBox.setObjectName(u"genderComboBox")
        self.genderComboBox.setMinimumSize(QSize(277, 47))
        self.genderComboBox.setMaximumSize(QSize(277, 47))

        self.horizontalLayout.addWidget(self.genderComboBox)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.barGraph = QChartView(self.dashContainer)
        self.barGraph.setObjectName(u"barGraph")
        self.barGraph.setMinimumSize(QSize(0, 300))

        self.horizontalLayout_5.addWidget(self.barGraph)


        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_4, 5, 1, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(20)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayoutLeftSide = QVBoxLayout()
        self.verticalLayoutLeftSide.setSpacing(72)
        self.verticalLayoutLeftSide.setObjectName(u"verticalLayoutLeftSide")
        self.verticalLayoutLeftSide.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayoutLeftSide.setContentsMargins(0, 0, -1, -1)
        self.totalStudents = QFrame(self.dashContainer)
        self.totalStudents.setObjectName(u"totalStudents")
        self.totalStudents.setMinimumSize(QSize(400, 122))
        self.totalStudents.setMaximumSize(QSize(400, 122))
        self.totalStudents.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.totalStudents.setFrameShape(QFrame.StyledPanel)
        self.totalStudents.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.totalStudents)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(-1, 9, -1, -1)
        self.totalStudentsImage = QLabel(self.totalStudents)
        self.totalStudentsImage.setObjectName(u"totalStudentsImage")
        self.totalStudentsImage.setMinimumSize(QSize(95, 95))
        self.totalStudentsImage.setMaximumSize(QSize(95, 95))
        self.totalStudentsImage.setPixmap(QPixmap(u":/icons/graduating-student.png"))
        self.totalStudentsImage.setScaledContents(True)

        self.gridLayout_5.addWidget(self.totalStudentsImage, 0, 0, 1, 1)

        self.totalStudentsVerticalLayout = QVBoxLayout()
        self.totalStudentsVerticalLayout.setSpacing(2)
        self.totalStudentsVerticalLayout.setObjectName(u"totalStudentsVerticalLayout")
        self.totalStudentsVerticalLayout.setContentsMargins(10, 10, -1, 10)
        self.totalStudentsNumber = QLabel(self.totalStudents)
        self.totalStudentsNumber.setObjectName(u"totalStudentsNumber")
        self.totalStudentsNumber.setMinimumSize(QSize(0, 19))
        self.totalStudentsNumber.setMaximumSize(QSize(16777215, 25))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.totalStudentsNumber.setFont(font)

        self.totalStudentsVerticalLayout.addWidget(self.totalStudentsNumber)

        self.totalStudentsText = QLabel(self.totalStudents)
        self.totalStudentsText.setObjectName(u"totalStudentsText")
        self.totalStudentsText.setFont(font)

        self.totalStudentsVerticalLayout.addWidget(self.totalStudentsText)


        self.gridLayout_5.addLayout(self.totalStudentsVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutLeftSide.addWidget(self.totalStudents)

        self.studentsEligible = QFrame(self.dashContainer)
        self.studentsEligible.setObjectName(u"studentsEligible")
        self.studentsEligible.setMinimumSize(QSize(400, 122))
        self.studentsEligible.setMaximumSize(QSize(400, 122))
        self.studentsEligible.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.studentsEligible.setFrameShape(QFrame.StyledPanel)
        self.studentsEligible.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.studentsEligible)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.studentsEligibleImage = QLabel(self.studentsEligible)
        self.studentsEligibleImage.setObjectName(u"studentsEligibleImage")
        self.studentsEligibleImage.setMinimumSize(QSize(95, 95))
        self.studentsEligibleImage.setMaximumSize(QSize(95, 95))
        self.studentsEligibleImage.setPixmap(QPixmap(u":/icons/checked.png"))
        self.studentsEligibleImage.setScaledContents(True)

        self.gridLayout_6.addWidget(self.studentsEligibleImage, 0, 0, 1, 1)

        self.studentsEligibleVerticalLayout = QVBoxLayout()
        self.studentsEligibleVerticalLayout.setSpacing(2)
        self.studentsEligibleVerticalLayout.setObjectName(u"studentsEligibleVerticalLayout")
        self.studentsEligibleVerticalLayout.setContentsMargins(10, 10, -1, 10)
        self.studentsEligibleNumber = QLabel(self.studentsEligible)
        self.studentsEligibleNumber.setObjectName(u"studentsEligibleNumber")
        self.studentsEligibleNumber.setMinimumSize(QSize(0, 19))
        self.studentsEligibleNumber.setMaximumSize(QSize(16777215, 25))
        self.studentsEligibleNumber.setFont(font)

        self.studentsEligibleVerticalLayout.addWidget(self.studentsEligibleNumber)

        self.studentsEligibleText = QLabel(self.studentsEligible)
        self.studentsEligibleText.setObjectName(u"studentsEligibleText")
        self.studentsEligibleText.setFont(font)

        self.studentsEligibleVerticalLayout.addWidget(self.studentsEligibleText)


        self.gridLayout_6.addLayout(self.studentsEligibleVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutLeftSide.addWidget(self.studentsEligible)

        self.studentsApplied = QFrame(self.dashContainer)
        self.studentsApplied.setObjectName(u"studentsApplied")
        self.studentsApplied.setMinimumSize(QSize(400, 122))
        self.studentsApplied.setMaximumSize(QSize(400, 122))
        self.studentsApplied.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.studentsApplied.setFrameShape(QFrame.StyledPanel)
        self.studentsApplied.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.studentsApplied)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.studentsAppliedImage = QLabel(self.studentsApplied)
        self.studentsAppliedImage.setObjectName(u"studentsAppliedImage")
        self.studentsAppliedImage.setMinimumSize(QSize(95, 95))
        self.studentsAppliedImage.setMaximumSize(QSize(95, 95))
        self.studentsAppliedImage.setPixmap(QPixmap(u":/icons/list.png"))
        self.studentsAppliedImage.setScaledContents(True)

        self.gridLayout_7.addWidget(self.studentsAppliedImage, 0, 0, 1, 1)

        self.studentsAppliedVerticalLayout = QVBoxLayout()
        self.studentsAppliedVerticalLayout.setSpacing(2)
        self.studentsAppliedVerticalLayout.setObjectName(u"studentsAppliedVerticalLayout")
        self.studentsAppliedVerticalLayout.setContentsMargins(10, 10, -1, 10)
        self.studentsAppliedNumber = QLabel(self.studentsApplied)
        self.studentsAppliedNumber.setObjectName(u"studentsAppliedNumber")
        self.studentsAppliedNumber.setMinimumSize(QSize(0, 19))
        self.studentsAppliedNumber.setMaximumSize(QSize(16777215, 25))
        self.studentsAppliedNumber.setFont(font)

        self.studentsAppliedVerticalLayout.addWidget(self.studentsAppliedNumber)

        self.studentsAppliedText = QLabel(self.studentsApplied)
        self.studentsAppliedText.setObjectName(u"studentsAppliedText")
        self.studentsAppliedText.setFont(font)

        self.studentsAppliedVerticalLayout.addWidget(self.studentsAppliedText)


        self.gridLayout_7.addLayout(self.studentsAppliedVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutLeftSide.addWidget(self.studentsApplied)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutLeftSide.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayoutLeftSide)

        self.pieChart = QChartView(self.dashContainer)
        self.pieChart.setObjectName(u"pieChart")

        self.horizontalLayout_3.addWidget(self.pieChart)

        self.verticalLayoutRightSide = QVBoxLayout()
        self.verticalLayoutRightSide.setSpacing(72)
        self.verticalLayoutRightSide.setObjectName(u"verticalLayoutRightSide")
        self.totalCompanies = QFrame(self.dashContainer)
        self.totalCompanies.setObjectName(u"totalCompanies")
        self.totalCompanies.setMinimumSize(QSize(400, 122))
        self.totalCompanies.setMaximumSize(QSize(400, 122))
        self.totalCompanies.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.totalCompanies.setFrameShape(QFrame.StyledPanel)
        self.totalCompanies.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.totalCompanies)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.totalCompaniesImage = QLabel(self.totalCompanies)
        self.totalCompaniesImage.setObjectName(u"totalCompaniesImage")
        self.totalCompaniesImage.setMinimumSize(QSize(95, 95))
        self.totalCompaniesImage.setMaximumSize(QSize(95, 95))
        self.totalCompaniesImage.setPixmap(QPixmap(u":/icons/job.png"))
        self.totalCompaniesImage.setScaledContents(True)

        self.gridLayout_3.addWidget(self.totalCompaniesImage, 0, 0, 1, 1)

        self.totalCompanies_2 = QVBoxLayout()
        self.totalCompanies_2.setSpacing(2)
        self.totalCompanies_2.setObjectName(u"totalCompanies_2")
        self.totalCompanies_2.setContentsMargins(10, 10, -1, 10)
        self.totalCompaniesNumber = QLabel(self.totalCompanies)
        self.totalCompaniesNumber.setObjectName(u"totalCompaniesNumber")
        self.totalCompaniesNumber.setMinimumSize(QSize(0, 19))
        self.totalCompaniesNumber.setMaximumSize(QSize(16777215, 25))
        self.totalCompaniesNumber.setFont(font)

        self.totalCompanies_2.addWidget(self.totalCompaniesNumber)

        self.totalCompaniesText = QLabel(self.totalCompanies)
        self.totalCompaniesText.setObjectName(u"totalCompaniesText")
        self.totalCompaniesText.setFont(font)

        self.totalCompanies_2.addWidget(self.totalCompaniesText)


        self.gridLayout_3.addLayout(self.totalCompanies_2, 0, 1, 1, 1)


        self.verticalLayoutRightSide.addWidget(self.totalCompanies)

        self.studentsNotApplied = QFrame(self.dashContainer)
        self.studentsNotApplied.setObjectName(u"studentsNotApplied")
        self.studentsNotApplied.setMinimumSize(QSize(400, 122))
        self.studentsNotApplied.setMaximumSize(QSize(400, 122))
        self.studentsNotApplied.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.studentsNotApplied.setFrameShape(QFrame.StyledPanel)
        self.studentsNotApplied.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.studentsNotApplied)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, -1)
        self.studentsNotAppliedImage = QLabel(self.studentsNotApplied)
        self.studentsNotAppliedImage.setObjectName(u"studentsNotAppliedImage")
        self.studentsNotAppliedImage.setMinimumSize(QSize(95, 95))
        self.studentsNotAppliedImage.setMaximumSize(QSize(95, 95))
        self.studentsNotAppliedImage.setPixmap(QPixmap(u":/icons/delete.png"))
        self.studentsNotAppliedImage.setScaledContents(True)

        self.gridLayout_2.addWidget(self.studentsNotAppliedImage, 0, 0, 1, 1)

        self.studentsNotAppliedVerticalLayout = QVBoxLayout()
        self.studentsNotAppliedVerticalLayout.setSpacing(2)
        self.studentsNotAppliedVerticalLayout.setObjectName(u"studentsNotAppliedVerticalLayout")
        self.studentsNotAppliedVerticalLayout.setContentsMargins(10, 10, -1, 10)
        self.studentsNotAppliedNumber = QLabel(self.studentsNotApplied)
        self.studentsNotAppliedNumber.setObjectName(u"studentsNotAppliedNumber")
        self.studentsNotAppliedNumber.setMinimumSize(QSize(0, 19))
        self.studentsNotAppliedNumber.setMaximumSize(QSize(16777215, 25))
        self.studentsNotAppliedNumber.setFont(font)

        self.studentsNotAppliedVerticalLayout.addWidget(self.studentsNotAppliedNumber)

        self.studentsNotAppliedText = QLabel(self.studentsNotApplied)
        self.studentsNotAppliedText.setObjectName(u"studentsNotAppliedText")
        self.studentsNotAppliedText.setFont(font)

        self.studentsNotAppliedVerticalLayout.addWidget(self.studentsNotAppliedText)


        self.gridLayout_2.addLayout(self.studentsNotAppliedVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutRightSide.addWidget(self.studentsNotApplied)

        self.totalStudentsPlaced = QFrame(self.dashContainer)
        self.totalStudentsPlaced.setObjectName(u"totalStudentsPlaced")
        self.totalStudentsPlaced.setMinimumSize(QSize(400, 122))
        self.totalStudentsPlaced.setMaximumSize(QSize(400, 122))
        self.totalStudentsPlaced.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.totalStudentsPlaced.setFrameShape(QFrame.StyledPanel)
        self.totalStudentsPlaced.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.totalStudentsPlaced)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(-1, 9, -1, -1)
        self.studentsPlacedImage = QLabel(self.totalStudentsPlaced)
        self.studentsPlacedImage.setObjectName(u"studentsPlacedImage")
        self.studentsPlacedImage.setMinimumSize(QSize(95, 95))
        self.studentsPlacedImage.setMaximumSize(QSize(95, 95))
        self.studentsPlacedImage.setPixmap(QPixmap(u":/icons/email.png"))
        self.studentsPlacedImage.setScaledContents(True)

        self.gridLayout_4.addWidget(self.studentsPlacedImage, 0, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(10, 10, -1, 10)
        self.studentsPlacedNumber = QLabel(self.totalStudentsPlaced)
        self.studentsPlacedNumber.setObjectName(u"studentsPlacedNumber")
        self.studentsPlacedNumber.setMinimumSize(QSize(0, 19))
        self.studentsPlacedNumber.setMaximumSize(QSize(16777215, 25))
        self.studentsPlacedNumber.setFont(font)

        self.verticalLayout_3.addWidget(self.studentsPlacedNumber)

        self.studentsPlacedText = QLabel(self.totalStudentsPlaced)
        self.studentsPlacedText.setObjectName(u"studentsPlacedText")
        self.studentsPlacedText.setFont(font)

        self.verticalLayout_3.addWidget(self.studentsPlacedText)


        self.gridLayout_4.addLayout(self.verticalLayout_3, 0, 1, 1, 1)


        self.verticalLayoutRightSide.addWidget(self.totalStudentsPlaced)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutRightSide.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayoutRightSide)


        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_6, 4, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 30, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_7, 4, 2, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 25, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.gridLayout.addItem(self.verticalSpacer_5, 2, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.dashContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Student Placement Statistics", None))
        self.appLogo.setText("")
        self.campusComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.campusComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Kattankulathur", None))
        self.campusComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Ramapuram", None))
        self.campusComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Tiruchirappalli", None))
        self.campusComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Vadapalani", None))
        self.campusComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Modinagar", None))

        self.campusComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Campus", None))
        self.batchComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2024", None))
        self.batchComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2023", None))
        self.batchComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2022", None))
        self.batchComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"2021", None))
        self.batchComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"2020", None))

        self.batchComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Batch", None))
        self.departmentComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.departmentComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Applied Data Science", None))
        self.departmentComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Atmospheric Science", None))
        self.departmentComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Biochemistry", None))
        self.departmentComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Biotechnology", None))
        self.departmentComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Chemistry", None))
        self.departmentComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Computer Science", None))
        self.departmentComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Information Technology", None))
        self.departmentComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Mathematics", None))
        self.departmentComboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Visual Communication", None))
        self.departmentComboBox.setItemText(10, QCoreApplication.translate("MainWindow", u"Accounting and Finance", None))
        self.departmentComboBox.setItemText(11, QCoreApplication.translate("MainWindow", u"Commerce", None))
        self.departmentComboBox.setItemText(12, QCoreApplication.translate("MainWindow", u"Computer Applications", None))
        self.departmentComboBox.setItemText(13, QCoreApplication.translate("MainWindow", u"Journalism and Mass Communication", None))
        self.departmentComboBox.setItemText(14, QCoreApplication.translate("MainWindow", u"Business Administration", None))
        self.departmentComboBox.setItemText(15, QCoreApplication.translate("MainWindow", u"Digital Marketing", None))
        self.departmentComboBox.setItemText(16, QCoreApplication.translate("MainWindow", u"Data Science", None))
        self.departmentComboBox.setItemText(17, QCoreApplication.translate("MainWindow", u"Fashion Designing", None))
        self.departmentComboBox.setItemText(18, QCoreApplication.translate("MainWindow", u"Psychology", None))

        self.departmentComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Department ", None))
        self.courseComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.courseComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"B.A", None))
        self.courseComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"B.B.A", None))
        self.courseComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"B.C.A", None))
        self.courseComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"B.Com", None))
        self.courseComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"M.Sc", None))
        self.courseComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"B.Sc", None))
        self.courseComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"M.Com", None))

        self.courseComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.genderComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"All", None))
        self.genderComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.genderComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))
        self.genderComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Other", None))

        self.genderComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.totalStudentsImage.setText("")
        # self.totalStudentsNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.totalStudentsText.setText(QCoreApplication.translate("MainWindow", u"TOTAL STUDENTS", None))
        self.studentsEligibleImage.setText("")
        # self.studentsEligibleNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsEligibleText.setText(QCoreApplication.translate("MainWindow", u"STUDENTS ELIGIBLE", None))
        self.studentsAppliedImage.setText("")
        # self.studentsAppliedNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsAppliedText.setText(QCoreApplication.translate("MainWindow", u"STUDENTS APPLIED", None))
        self.totalCompaniesImage.setText("")
        # self.totalCompaniesNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.totalCompaniesText.setText(QCoreApplication.translate("MainWindow", u"TOTAL COMPANIES", None))
        self.studentsNotAppliedImage.setText("")
        # self.studentsNotAppliedNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsNotAppliedText.setText(QCoreApplication.translate("MainWindow", u"NOT APPLIED", None))
        self.studentsPlacedImage.setText("")
        # self.studentsPlacedNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsPlacedText.setText(QCoreApplication.translate("MainWindow", u"STUDENTS PLACED", None))
    # retranslateUi

