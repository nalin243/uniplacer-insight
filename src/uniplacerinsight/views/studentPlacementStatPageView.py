from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCharts import QPieSeries,QChart,QPieSlice,QLegend,QBarSeries,QBarSet,QBarCategoryAxis,QValueAxis
from PySide6.QtCore import QSize, Qt,QEasingCurve, QRect
from PySide6.QtGui import QCloseEvent, QPainter,QColor,QFont

import functools

from pandas.core.base import NoNewAttributesMixin

from views.studentPlacementStatPageView_UI import Ui_MainWindow

from resources.studentsplacedmodal import PlacedTableData


class StudentPlacementStatPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller,viewmodel):
		super().__init__()

		self.setupUi(self)

		self.controller = controller
		self.viewmodel = viewmodel

		self.studentsplacedmodal = PlacedTableData(self.viewmodel, self.centralwidget)

		self.campusFilter = None if self.campusComboBox.currentText()=="Campus(All)" else self.campusComboBox.currentText()
		self.batchFilter = None if self.batchComboBox.currentText()=="All" else self.batchComboBox.currentText()
		self.departmentFilter = None if self.departmentComboBox.currentText()=="Department(All)" else self.departmentComboBox.currentText()
		self.courseFilter = None if self.courseComboBox.currentText()=="Course(All)" else self.courseComboBox.currentText()
		self.genderFilter = None if self.genderComboBox.currentText()=="Gender(All)" else self.genderComboBox.currentText()

		self.studentsPlacedButton.mousePressEvent = self.showPlacedTableViewModal

		self.studentsEligiblePercent = 0
		self.studentsAppliedPercent = 0
		self.studentsNotAppliedPercent = 0
		self.studentsPlacedPercent = 0

		self.campusComboBox.currentTextChanged.connect(self.filterChanged)
		self.campusComboBox.currentTextChanged.connect(self.barChartFiltersChanged)
		self.batchComboBox.currentTextChanged.connect(self.barChartFiltersChanged)
		self.batchComboBox.currentTextChanged.connect(self.filterChanged)
		self.departmentComboBox.currentTextChanged.connect(self.filterChanged)
		self.courseComboBox.currentTextChanged.connect(self.filterChanged)
		self.genderComboBox.currentTextChanged.connect(self.filterChanged)

		self.MainWindow.resizeEvent = self.resizing

	def resizing(self,event):
		bigFont = QFont()
		bigFont.setFamilies([u"Lucida Sans"])
		bigFont.setPointSize(18)
		bigFont.setBold(True)

		smallFont = QFont()
		smallFont.setFamilies([u"Lucida Sans"])
		smallFont.setPointSize(15)
		smallFont.setBold(True)

		if int(self.MainWindow.size().height()) <= 770:
			self.verticalLayoutLeftSide.setSpacing(2)
			self.verticalLayoutRightSide.setSpacing(2)

		if self.pieChartDisplay.size().width() <= 860:
			self.pieChartDisplay.setMinimumWidth(self.pieChartDisplay.size().width()-100)

		if int(self.MainWindow.size().height()) <= 900  or  int(self.MainWindow.size().width()) <= 1700:

			self.pieChart.legend().setFont(QFont("Serif", 15, QFont.Normal))

			self.genderComboBox.setMinimumSize(QSize(177,47))
			self.courseComboBox.setMinimumSize(QSize(177,47))
			self.departmentComboBox.setMinimumSize(QSize(177,47))
			self.batchComboBox.setMinimumSize(QSize(177,47))
			self.campusComboBox.setMinimumSize(QSize(177,47))
			self.genderComboBox.setMinimumSize(QSize(177,47))
			self.courseComboBox.setMinimumSize(QSize(177,47))
			self.departmentComboBox.setMinimumSize(QSize(177,47))
			self.batchComboBox.setMinimumSize(QSize(177,47))
			self.campusComboBox.setMinimumSize(QSize(177,47))

			self.studentsPlacedButton.setGeometry(QRect(229, 10, 18, 18))

			self.totalStudentsNumber.setFont(smallFont)
			self.totalStudentsText.setFont(smallFont)

			self.studentsNotEnrolledNumber.setFont(smallFont)
			self.studentsNotEnrolledText.setFont(smallFont)

			self.studentsEnrolledNumber.setFont(smallFont)
			self.studentsEnrolledText.setFont(smallFont)

			self.studentsPlacedNumber.setFont(smallFont)
			self.studentsPlacedText.setFont(smallFont)

			self.studentsNotPlacedNumber.setFont(smallFont)
			self.studentsNotPlacedText.setFont(smallFont)

			self.totalDisqualifiedNumber.setFont(smallFont)
			self.totalDisqualifiedText.setFont(smallFont)

			self.totalStudents.setMaximumHeight(120)
			self.totalStudents.setMinimumHeight(120)

			self.studentsEnrolled.setMaximumHeight(120)
			self.studentsEnrolled.setMinimumHeight(120)

			self.studentsNotEnrolled.setMaximumHeight(120)
			self.studentsNotEnrolled.setMinimumHeight(120)

			self.studentsNotPlaced.setMaximumHeight(120)
			self.studentsNotPlaced.setMinimumHeight(120)

			self.totalStudentsPlaced.setMaximumHeight(120)
			self.totalStudentsPlaced.setMinimumHeight(120)

			self.totalDisqualified.setMaximumHeight(120)
			self.totalDisqualified.setMinimumHeight(120)	

			self.totalStudentsImage.setMinimumSize(QSize(70, 70))
			self.totalStudentsImage.setMaximumSize(QSize(70, 70))

			self.studentsEnrolledImage.setMinimumSize(QSize(70, 70))
			self.studentsEnrolledImage.setMaximumSize(QSize(70, 70))

			self.studentsNotEnrolledImage.setMinimumSize(QSize(70, 70))

			self.totalDisqualifiedImage.setMinimumSize(QSize(70, 70))
			self.totalDisqualifiedImage.setMaximumSize(QSize(70, 70))

			self.studentsPlacedImage.setMinimumSize(QSize(70, 70))
			self.studentsPlacedImage.setMaximumSize(QSize(70, 70))

			self.studentsNotPlacedImage.setMinimumSize(QSize(70, 70))
			self.studentsNotPlacedImage.setMaximumSize(QSize(70, 70))

			self.barGraphDisplay.setMinimumSize(QSize(100, 200))

		elif int(self.MainWindow.size().width()) >= 1700 or int(self.MainWindow.size().height()) >= 860:

			# if int(self.MainWindow.size().width()) >= 1632:
			self.verticalLayoutLeftSide.setSpacing(72)
			self.verticalLayoutRightSide.setSpacing(72)

			self.pieChart.legend().setFont(QFont("Serif", 20, QFont.Normal))

			self.genderComboBox.setMinimumSize(QSize(227,47))
			self.courseComboBox.setMinimumSize(QSize(227,47))
			self.departmentComboBox.setMinimumSize(QSize(227,47))
			self.batchComboBox.setMinimumSize(QSize(227,47))
			self.campusComboBox.setMinimumSize(QSize(227,47))
			self.genderComboBox.setMinimumSize(QSize(227,47))
			self.courseComboBox.setMinimumSize(QSize(227,47))
			self.departmentComboBox.setMinimumSize(QSize(227,47))
			self.batchComboBox.setMinimumSize(QSize(227,47))
			self.campusComboBox.setMinimumSize(QSize(227,47))

			self.studentsPlacedButton.setGeometry(QRect(320, 10, 18, 18))

			self.totalStudentsNumber.setFont(bigFont)
			self.totalStudentsText.setFont(bigFont)

			self.studentsNotEnrolledNumber.setFont(bigFont)
			self.studentsNotEnrolledText.setFont(bigFont)

			self.studentsEnrolledNumber.setFont(bigFont)
			self.studentsEnrolledText.setFont(bigFont)

			self.studentsPlacedNumber.setFont(bigFont)
			self.studentsPlacedText.setFont(bigFont)

			self.studentsNotPlacedNumber.setFont(bigFont)
			self.studentsNotPlacedText.setFont(bigFont)

			self.totalDisqualifiedNumber.setFont(bigFont)
			self.totalDisqualifiedText.setFont(bigFont)

			self.totalStudents.setMaximumHeight(122)
			self.totalStudents.setMinimumHeight(122)

			self.studentsEnrolled.setMaximumHeight(122)
			self.studentsEnrolled.setMinimumHeight(122)

			self.studentsNotEnrolled.setMaximumHeight(122)
			self.studentsNotEnrolled.setMinimumHeight(122)

			self.studentsNotPlaced.setMaximumHeight(122)
			self.studentsNotPlaced.setMinimumHeight(122)

			self.totalStudentsPlaced.setMaximumHeight(122)
			self.totalStudentsPlaced.setMinimumHeight(122)

			self.totalDisqualified.setMaximumHeight(122)
			self.totalDisqualified.setMinimumHeight(122)	

			self.totalStudentsImage.setMinimumSize(QSize(95, 95))
			self.totalStudentsImage.setMaximumSize(QSize(95, 95))

			self.studentsEnrolledImage.setMinimumSize(QSize(95, 95))
			self.studentsEnrolledImage.setMaximumSize(QSize(95, 95))

			self.studentsNotEnrolledImage.setMinimumSize(QSize(95, 95))
			self.studentsNotEnrolledImage.setMaximumSize(QSize(95, 95))

			self.totalDisqualifiedImage.setMinimumSize(QSize(95, 95))
			self.totalDisqualifiedImage.setMaximumSize(QSize(95, 95))

			self.studentsPlacedImage.setMinimumSize(QSize(95, 95))
			self.studentsPlacedImage.setMaximumSize(QSize(95, 95))

			self.studentsNotPlacedImage.setMinimumSize(QSize(95, 95))
			self.studentsNotPlacedImage.setMaximumSize(QSize(95, 95))

			self.barGraphDisplay.setMinimumSize(QSize(100, 345))


	def showPlacedTableViewModal(self, event):
		self.studentsplacedmodal.exec()

	def closeEvent(self, event):
		self.controller.returnToLanding()
		return super().closeEvent(event)


	def initBarChart(self,enrolledSet=[],notEnrolledSet=[],categories=[],barChartYaxisRange=0):
		self.barChart = QChart()
		self.barGraphDisplay.setChart(self.barChart)
		self.enrolledSet = None 
		self.notEnrolledSet = None
		self.barChart.zoom(10.0)

		self.axis_x =  QBarCategoryAxis()
		self.axis_y = QValueAxis()
		self.axis_y.setLabelFormat("%d")

		self.enrolledSet = QBarSet("Enrolled")
		self.notEnrolledSet = QBarSet("Not Enrolled")

		self.enrolledSet.append(enrolledSet)
		self.notEnrolledSet.append(notEnrolledSet)

		self.series = QBarSeries()

		self.series.hovered.connect(self.barHovered)

		self.series.append(self.enrolledSet)
		self.series.append(self.notEnrolledSet)

		self.barChart.addSeries(self.series)
		self.barChart.setAnimationOptions(QChart.SeriesAnimations)

		self.categories = categories

		self.axis_x.append(self.categories)

		self.barChart.addAxis(self.axis_x,Qt.AlignBottom)
		self.series.attachAxis(self.axis_x)

		self.axis_y.setRange(0,barChartYaxisRange)

		self.barChart.addAxis(self.axis_y,Qt.AlignLeft)
		self.series.attachAxis(self.axis_y)

		self.barChart.legend().setVisible(True)
		self.barChart.legend().setAlignment(Qt.AlignTop)

	def barHovered(self, status, index, barset):
		if status:
			self.series.setLabelsVisible(True)
		else:
			self.series.setLabelsVisible(False)


	def initPieChart(self,enrolledData,placedData):
		self.pieChart.removeAllSeries()
		self.pieChart.setAnimationOptions(QChart.SeriesAnimations)
		self.pieChart.setAnimationEasingCurve(QEasingCurve.OutQuint)
		self.pieChart.setAnimationDuration(2000)

		self.outerSeries = QPieSeries()
		self.outerSeries.setHoleSize(0.35)
		# self.outerSeries.setPieSize(0.71)

		self.innerSeries = QPieSeries()
		self.innerSeries.setHoleSize(0.60)
		self.innerSeries.setPieSize(0.70)

		self.sliceshovered = []

		self.outerColors = ["#2ecc71","#e67e22","#e74c3c"]
		self.innerColors = ["#3498db","#808080"]

		for self.item in enrolledData:
			self.outerSeries.append(QPieSlice(self.item[0],self.item[1]))

		for self.item in placedData:
			self.innerSeries.append(QPieSlice(self.item[0],self.item[1]))

		for index,self.slice in enumerate(self.outerSeries.slices()):

			self.color = QColor(self.outerColors[index])

			if(self.slice.label() == "Enrolled"):
				self.innerSeries.setPieEndAngle(self.slice.percentage()*360)
				self.slice.setLabelPosition(QPieSlice.LabelInsideNormal)
				self.slice.setLabel("{:.0f}%".format(round(self.slice.percentage()*100),2))
				self.slice.setLabelBrush(QColor("#006400"))
				self.slice.setColor(self.color)
				self.slice.setLabelVisible(True)
				self.slice.setLabelFont(QFont("Serif", 13, QFont.Medium))
				continue

			self.slice.setLabel("{:.0f}%".format(round(self.slice.percentage()*100),2))
			self.slice.setLabelArmLengthFactor(0.05)
			self.slice.setLabelBrush(self.color)
			self.slice.setColor(self.color)
			self.slice.setBorderWidth(1)
			# self.color.setAlpha(100)
			self.slice.setBorderColor(QColor("black"))
			self.slice.setExplodeDistanceFactor(0.001)
			self.slice.setExploded(True)
			self.slice.setLabelVisible(True)
			self.slice.setLabelFont(QFont("Serif", 13, QFont.Medium))
			# self.slice.hovered.connect(functools.partial(self.pieSliceHovered,self.slice))

		for index,self.slice in enumerate(self.innerSeries.slices()):

			self.color = QColor(self.innerColors[index])
			self.slice.setLabel("{:.2f}%".format(round(self.slice.percentage()*100),2))
			self.slice.setLabelArmLengthFactor(0.05)
			self.slice.setLabelBrush(self.color)
			self.slice.setExploded(True)
			self.slice.setLabelVisible(True)
			self.slice.setExplodeDistanceFactor(0.001)
			self.slice.setLabelFont(QFont("Serif", 13, QFont.Medium))
			self.slice.setColor(self.color)
			self.slice.hovered.connect(functools.partial(self.pieSliceHovered,self.slice))

		self.pieChart.addSeries(self.outerSeries)
		self.pieChart.addSeries(self.innerSeries)
		

		self.pieChart.legend().setFont(QFont("Serif", 20, QFont.Normal))
		self.pieChart.legend().setMarkerShape(QLegend.MarkerShapeCircle)

		self.pieChart.legend().markers()[3].setLabel(self.placedData[0][0])
		self.pieChart.legend().markers()[4].setLabel(self.placedData[1][0])

		self.pieChart.legend().markers()[0].setLabel(self.enrolledData[0][0])
		self.pieChart.legend().markers()[1].setLabel(self.enrolledData[1][0])
		self.pieChart.legend().markers()[2].setLabel(self.enrolledData[2][0])


		self.pieChart.legend().setAlignment(Qt.AlignRight)
		self.pieChartDisplay.setRenderHint(QPainter.Antialiasing)

	def pieSliceHovered(self,pieSlice,state):
		self.pieChart.zoom(2.0)
		if(state):
			pieSlice.setExplodeDistanceFactor(0.1)
		else:
			pieSlice.setExplodeDistanceFactor(0.001)


	def show(self):

		self.controller.changeFilter(self.campusFilter,self.batchFilter,self.departmentFilter,self.courseFilter,self.genderFilter)

		self.totalStudentsNumber.setText(str(self.viewmodel.getStudentAggregates()[0]))
		self.studentsNotPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[4]))
		self.studentsEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[1]))
		self.studentsNotEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[2]))
		self.totalDisqualifiedNumber.setText(str(self.viewmodel.getStudentAggregates()[5]))
		self.studentsPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[3]))

		self.campusFilter = None if self.campusComboBox.currentText()=="Campus(All)" else self.campusComboBox.currentText()

		self.controller.updateBarChartValues(self.campusFilter,self.batchFilter)
		(placedSet,notPlacedSet,categories,barChartYaxisRange) = self.viewmodel.getBarChartValues()
		self.initBarChart(placedSet,notPlacedSet,categories,barChartYaxisRange)

		self.enrolledData = [['Enrolled', self.viewmodel.totalEnrolledStudents],['Not Enrolled', self.viewmodel.totalNotEnrolledStudents],['Removed/Blocked',self.viewmodel.totalDisqualified]]
		self.placedData = [['Placed',self.viewmodel.totalPlacedStudents],['Not Placed',self.viewmodel.totalNotPlacedStudents]]
		self.initPieChart(self.enrolledData,self.placedData)

		super().show()	

	def barChartFiltersChanged(self):
		self.campusFilter = None if self.campusComboBox.currentText()=="Campus(All)" else self.campusComboBox.currentText()
		self.batchFilter = None if self.batchComboBox.currentText()=="All" else self.batchComboBox.currentText()

		self.controller.updateBarChartValues(self.campusFilter,self.batchFilter)
		(placedSet,notPlacedSet,categories,barChartYaxisRange) = self.viewmodel.getBarChartValues()
		self.initBarChart(placedSet,notPlacedSet,categories,barChartYaxisRange)

	def filterChanged(self):
		self.campusFilter = None if self.campusComboBox.currentText()=="Campus(All)" else self.campusComboBox.currentText()
		self.batchFilter = None if self.batchComboBox.currentText()=="All" else self.batchComboBox.currentText()
		self.departmentFilter = None if self.departmentComboBox.currentText()=="Department(All)" else self.departmentComboBox.currentText()
		self.courseFilter = None if self.courseComboBox.currentText()=="Course(All)" else self.courseComboBox.currentText()
		self.genderFilter = None if self.genderComboBox.currentText()=="Gender(All)" else self.genderComboBox.currentText()

		self.controller.changeFilter(self.campusFilter,self.batchFilter,self.departmentFilter,self.courseFilter,self.genderFilter)

		self.totalStudentsNumber.setText(str(self.viewmodel.getStudentAggregates()[0]))
		self.studentsNotPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[4]))
		self.studentsEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[1]))
		self.studentsNotEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[2]))
		self.totalDisqualifiedNumber.setText(str(self.viewmodel.getStudentAggregates()[5]))
		self.studentsPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[3]))

		self.enrolledData = [['Enrolled', self.viewmodel.totalEnrolledStudents],['Not Enrolled', self.viewmodel.totalNotEnrolledStudents],['Removed/Blocked',self.viewmodel.totalDisqualified]]
		self.placedData = [['Placed',self.viewmodel.totalPlacedStudents],['Not Placed',self.viewmodel.totalNotPlacedStudents]]
		self.initPieChart(self.enrolledData,self.placedData)