# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCharts import QChartView,QChart
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
        MainWindow.setMinimumSize(QSize(960, 540))
        MainWindow.setMaximumSize(QSize(1920, 1060))
        MainWindow.setStyleSheet(u"#MainWindow{\n"
"	background-color:#D9D9D9; \n"
"}")
        MainWindow.setWindowIcon(QIcon(":/icons/iconlogo.png"))

        self.MainWindow = MainWindow

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1920, 1060))
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
        self.horizontalSpacer_2 = QSpacerItem(90, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.appLogo = QLabel(self.dashContainer)
        self.appLogo.setObjectName(u"appLogo")
        self.appLogo.setMaximumSize(QSize(268, 60))
        self.appLogo.setMinimumSize(QSize(268, 60))
        self.appLogo.setPixmap(QPixmap(u":/icons/applogo.png"))
        self.appLogo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.appLogo)

        self.horizontalSpacer_9 = QSpacerItem(115, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_9)

        self.horizontalSpacer = QSpacerItem(60, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

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
        self.campusComboBox.setMinimumSize(QSize(227, 47))
        self.campusComboBox.setMaximumSize(QSize(227, 47))

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
        self.batchComboBox.setMinimumSize(QSize(227, 47))
        self.batchComboBox.setMaximumSize(QSize(227, 47))

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
        self.departmentComboBox.setMinimumSize(QSize(227, 47))
        self.departmentComboBox.setMaximumSize(QSize(227, 47))

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
        self.courseComboBox.addItem("")
        self.courseComboBox.setObjectName(u"courseComboBox")
        self.courseComboBox.setMinimumSize(QSize(227, 47))
        self.courseComboBox.setMaximumSize(QSize(227, 47))

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
        self.genderComboBox.setMinimumSize(QSize(227, 47))
        self.genderComboBox.setMaximumSize(QSize(227, 47))

        self.horizontalLayout.addWidget(self.genderComboBox)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.barGraphDisplay = QChartView(self.centralwidget)
        self.barGraphDisplay.setObjectName(u"barGraph")
        self.barGraphDisplay.setMinimumSize(QSize(100, 345))

        self.horizontalLayout_5.addWidget(self.barGraphDisplay)

        self.gridLayout.addItem(self.horizontalLayout_5, 4, 1, 1, 1)

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
        self.totalStudents.setMinimumSize(QSize(200, 122))
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
        self.totalStudentsNumber.setMinimumSize(QSize(0, 10))
        self.totalStudentsNumber.setMaximumSize(QSize(16777215, 25))
        self.font = QFont()
        self.font.setPointSize(18)
        self.font.setBold(True)
        self.totalStudentsNumber.setFont(self.font)

        self.totalStudentsVerticalLayout.addWidget(self.totalStudentsNumber)

        self.totalStudentsText = QLabel(self.totalStudents)
        self.totalStudentsText.setObjectName(u"totalStudentsText")
        self.totalStudentsText.setFont(self.font)

        self.totalStudentsVerticalLayout.addWidget(self.totalStudentsText)


        self.gridLayout_5.addLayout(self.totalStudentsVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutLeftSide.addWidget(self.totalStudents)

        self.studentsNotEnrolled = QFrame(self.dashContainer)
        self.studentsNotEnrolled.setObjectName(u"studentsNotEnrolled")
        self.studentsNotEnrolled.setMinimumSize(QSize(200, 122))
        self.studentsNotEnrolled.setMaximumSize(QSize(400, 122))
        self.studentsNotEnrolled.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.studentsNotEnrolled.setFrameShape(QFrame.StyledPanel)
        self.studentsNotEnrolled.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.studentsNotEnrolled)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.studentsNotEnrolledImage = QLabel(self.studentsNotEnrolled)
        self.studentsNotEnrolledImage.setObjectName(u"studentsNotEnrolledImage")
        self.studentsNotEnrolledImage.setMinimumSize(QSize(95, 95))
        self.studentsNotEnrolledImage.setMaximumSize(QSize(95, 95))
        self.studentsNotEnrolledImage.setPixmap(QPixmap(u":/icons/no.png"))
        self.studentsNotEnrolledImage.setScaledContents(True)

        self.gridLayout_6.addWidget(self.studentsNotEnrolledImage, 0, 0, 1, 1)

        self.studentsNotEnrolledVerticalLayout = QVBoxLayout()
        self.studentsNotEnrolledVerticalLayout.setSpacing(2)
        self.studentsNotEnrolledVerticalLayout.setObjectName(u"studentsNotEnrolledVerticalLayout")
        self.studentsNotEnrolledVerticalLayout.setContentsMargins(10, 10, -1, 10)
        self.studentsNotEnrolledNumber = QLabel(self.studentsNotEnrolled)
        self.studentsNotEnrolledNumber.setObjectName(u"studentsNotEnrolledNumber")
        self.studentsNotEnrolledNumber.setMinimumSize(QSize(0, 19))
        self.studentsNotEnrolledNumber.setMaximumSize(QSize(16777215, 25))
        self.studentsNotEnrolledNumber.setFont(self.font)

        self.studentsNotEnrolledVerticalLayout.addWidget(self.studentsNotEnrolledNumber)

        self.studentsNotEnrolledText = QLabel(self.studentsNotEnrolled)
        self.studentsNotEnrolledText.setObjectName(u"studentsNotEnrolledText")
        self.studentsNotEnrolledText.setFont(self.font)

        self.studentsNotEnrolledVerticalLayout.addWidget(self.studentsNotEnrolledText)


        self.gridLayout_6.addLayout(self.studentsNotEnrolledVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutLeftSide.addWidget(self.studentsNotEnrolled)

        self.studentsEnrolled = QFrame(self.dashContainer)
        self.studentsEnrolled.setObjectName(u"studentsEnrolled")
        self.studentsEnrolled.setMinimumSize(QSize(200, 122))
        self.studentsEnrolled.setMaximumSize(QSize(400, 122))
        self.studentsEnrolled.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.studentsEnrolled.setFrameShape(QFrame.StyledPanel)
        self.studentsEnrolled.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.studentsEnrolled)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.studentsEnrolledImage = QLabel(self.studentsEnrolled)
        self.studentsEnrolledImage.setObjectName(u"studentsEnrolledImage")
        self.studentsEnrolledImage.setMinimumSize(QSize(95, 95))
        self.studentsEnrolledImage.setMaximumSize(QSize(95, 95))
        self.studentsEnrolledImage.setPixmap(QPixmap(u":/icons/list.png"))
        self.studentsEnrolledImage.setScaledContents(True)

        self.gridLayout_7.addWidget(self.studentsEnrolledImage, 0, 0, 1, 1)

        self.studentsEnrolledVerticalLayout = QVBoxLayout()
        self.studentsEnrolledVerticalLayout.setSpacing(2)
        self.studentsEnrolledVerticalLayout.setObjectName(u"studentsEnrolledVerticalLayout")
        self.studentsEnrolledVerticalLayout.setContentsMargins(10, 10, -1, 10)
        self.studentsEnrolledNumber = QLabel(self.studentsEnrolled)
        self.studentsEnrolledNumber.setObjectName(u"studentsEnrolledNumber")
        self.studentsEnrolledNumber.setMinimumSize(QSize(0, 19))
        self.studentsEnrolledNumber.setMaximumSize(QSize(16777215, 25))
        self.studentsEnrolledNumber.setFont(self.font)

        self.studentsEnrolledVerticalLayout.addWidget(self.studentsEnrolledNumber)

        self.studentsEnrolledText = QLabel(self.studentsEnrolled)
        self.studentsEnrolledText.setObjectName(u"studentsEnrolledText")
        self.studentsEnrolledText.setFont(self.font)

        self.studentsEnrolledVerticalLayout.addWidget(self.studentsEnrolledText)


        self.gridLayout_7.addLayout(self.studentsEnrolledVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutLeftSide.addWidget(self.studentsEnrolled)

        self.verticalSpacer = QSpacerItem(20, 150, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayoutLeftSide.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.verticalLayoutLeftSide)


        self.pieChart = QChart()

        self.pieChartDisplay = QChartView(self.pieChart)
        self.pieChartDisplay.setObjectName(u"pieChartDisplay")

        self.horizontalLayout_3.addWidget(self.pieChartDisplay)

        self.verticalLayoutRightSide = QVBoxLayout()
        self.verticalLayoutRightSide.setSpacing(72)
        self.verticalLayoutRightSide.setObjectName(u"verticalLayoutRightSide")
        self.totalDisqualified = QFrame(self.dashContainer)
        self.totalDisqualified.setObjectName(u"totalDisqualified")
        self.totalDisqualified.setMinimumSize(QSize(200, 122))
        self.totalDisqualified.setMaximumSize(QSize(400, 122))
        self.totalDisqualified.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.totalDisqualified.setFrameShape(QFrame.StyledPanel)
        self.totalDisqualified.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.totalDisqualified)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(-1, 9, -1, -1)
        self.totalDisqualifiedImage = QLabel(self.totalDisqualified)
        self.totalDisqualifiedImage.setObjectName(u"totalDisqualifiedImage")
        self.totalDisqualifiedImage.setMinimumSize(QSize(95, 95))
        self.totalDisqualifiedImage.setMaximumSize(QSize(95, 95))
        self.totalDisqualifiedImage.setPixmap(QPixmap(u":/icons/ban-user.png"))
        self.totalDisqualifiedImage.setScaledContents(True)

        self.gridLayout_3.addWidget(self.totalDisqualifiedImage, 0, 0, 1, 1)

        self.totalDisqualified_2 = QVBoxLayout()
        self.totalDisqualified_2.setSpacing(2)
        self.totalDisqualified_2.setObjectName(u"totalDisqualified_2")
        self.totalDisqualified_2.setContentsMargins(10, 10, -1, 10)
        self.totalDisqualifiedNumber = QLabel(self.totalDisqualified)
        self.totalDisqualifiedNumber.setObjectName(u"totalDisqualifiedNumber")
        self.totalDisqualifiedNumber.setMinimumSize(QSize(0, 19))
        self.totalDisqualifiedNumber.setMaximumSize(QSize(16777215, 25))
        self.totalDisqualifiedNumber.setFont(self.font)

        self.totalDisqualified_2.addWidget(self.totalDisqualifiedNumber)

        self.totalDisqualifiedText = QLabel(self.totalDisqualified)
        self.totalDisqualifiedText.setObjectName(u"totalDisqualifiedText")
        self.totalDisqualifiedText.setFont(self.font)

        self.totalDisqualified_2.addWidget(self.totalDisqualifiedText)


        self.gridLayout_3.addLayout(self.totalDisqualified_2, 0, 1, 1, 1)


        self.verticalLayoutRightSide.addWidget(self.totalDisqualified)

        self.studentsNotPlaced = QFrame(self.dashContainer)
        self.studentsNotPlaced.setObjectName(u"studentsNotPlaced")
        self.studentsNotPlaced.setMinimumSize(QSize(200, 122))
        self.studentsNotPlaced.setMaximumSize(QSize(400, 122))
        self.studentsNotPlaced.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.studentsNotPlaced.setFrameShape(QFrame.StyledPanel)
        self.studentsNotPlaced.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.studentsNotPlaced)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, -1)
        self.studentsNotPlacedImage = QLabel(self.studentsNotPlaced)
        self.studentsNotPlacedImage.setObjectName(u"studentsNotPlacedImage")
        self.studentsNotPlacedImage.setMinimumSize(QSize(95, 95))
        self.studentsNotPlacedImage.setMaximumSize(QSize(95, 95))
        self.studentsNotPlacedImage.setPixmap(QPixmap(u":/icons/delete.png"))
        self.studentsNotPlacedImage.setScaledContents(True)

        self.gridLayout_2.addWidget(self.studentsNotPlacedImage, 0, 0, 1, 1)

        self.studentsNotPlacedVerticalLayout = QVBoxLayout()
        self.studentsNotPlacedVerticalLayout.setSpacing(2)
        self.studentsNotPlacedVerticalLayout.setObjectName(u"studentsNotPlacedVerticalLayout")
        self.studentsNotPlacedVerticalLayout.setContentsMargins(10, 10, -1, 10)
        self.studentsNotPlacedNumber = QLabel(self.studentsNotPlaced)
        self.studentsNotPlacedNumber.setObjectName(u"studentsNotPlacedNumber")
        self.studentsNotPlacedNumber.setMinimumSize(QSize(0, 19))
        self.studentsNotPlacedNumber.setMaximumSize(QSize(16777215, 25))
        self.studentsNotPlacedNumber.setFont(self.font)

        self.studentsNotPlacedVerticalLayout.addWidget(self.studentsNotPlacedNumber)

        self.studentsNotPlacedText = QLabel(self.studentsNotPlaced)
        self.studentsNotPlacedText.setObjectName(u"studentsNotPlacedText")
        self.studentsNotPlacedText.setFont(self.font)

        self.studentsNotPlacedVerticalLayout.addWidget(self.studentsNotPlacedText)


        self.gridLayout_2.addLayout(self.studentsNotPlacedVerticalLayout, 0, 1, 1, 1)


        self.verticalLayoutRightSide.addWidget(self.studentsNotPlaced)

        self.totalStudentsPlaced = QFrame(self.dashContainer)
        self.totalStudentsPlaced.setObjectName(u"totalStudentsPlaced")
        self.totalStudentsPlaced.setMinimumSize(QSize(200, 122))
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
        self.studentsPlacedNumber.setFont(self.font)

        self.verticalLayout_3.addWidget(self.studentsPlacedNumber)

        self.studentsPlacedText = QLabel(self.totalStudentsPlaced)
        self.studentsPlacedText.setObjectName(u"studentsPlacedText")
        self.studentsPlacedText.setFont(self.font)

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
        self.campusComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Campus(All)", None))
        self.campusComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Faculty of Science and Humanities, Kattankulathur", None))
        self.campusComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Faculty of Science and Humanities, Ramapuram", None))
        self.campusComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"College of Science and Humanities,Tiruchirappalli", None))
        self.campusComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Faculty of Science and Humanities, Vadapalani", None))
        self.campusComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Faculty of Science and Humanities, Modinagar", None))

        self.campusComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Campus", None))
        self.batchComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"2024", None))
        self.batchComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"2023", None))
        self.batchComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"2022", None))
        self.batchComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"2021", None))
        self.batchComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"2020", None))

        self.batchComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Batch", None))
        self.departmentComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Department(All)", None))
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
        self.courseComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Course(All)", None))
        self.courseComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"B.A", None))
        self.courseComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"B.B.A.", None))
        self.courseComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"B.C.A.", None))
        self.courseComboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"B.Com.", None))
        self.courseComboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"M.Sc.", None))
        self.courseComboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"B.Sc.", None))
        self.courseComboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"M.Com.", None))
        self.courseComboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"M.C.A.", None))

        self.courseComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Course", None))
        self.genderComboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Gender(All)", None))
        self.genderComboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.genderComboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))
        self.genderComboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Other", None))

        self.genderComboBox.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Gender", None))
        self.totalStudentsImage.setText("")
        # self.totalStudentsNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.totalStudentsText.setText(QCoreApplication.translate("MainWindow", u"TOTAL STUDENTS", None))
        self.studentsNotPlacedImage.setText("")
        # self.studentsNotPlacedNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsNotEnrolledText.setText(QCoreApplication.translate("MainWindow", u"NOT ENROLLED", None))
        self.studentsEnrolledImage.setText("")
        # self.studentsEnrolledNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsEnrolledText.setText(QCoreApplication.translate("MainWindow", u"ENROLLED STUDENTS", None))
        self.totalDisqualifiedImage.setText("")
        # self.totalDisqualifiedNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.totalDisqualifiedText.setText(QCoreApplication.translate("MainWindow", u"REMOVED/BLOCKED", None))
        self.studentsNotEnrolledImage.setText("")
        # self.studentsNotEnrolledNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsNotPlacedText.setText(QCoreApplication.translate("MainWindow", u"NOT PLACED", None))
        self.studentsPlacedImage.setText("")
        # self.studentsPlacedNumber.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.studentsPlacedText.setText(QCoreApplication.translate("MainWindow", u"PLACED STUDENTS", None))
    # retranslateUi
