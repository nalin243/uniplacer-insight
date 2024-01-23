from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtCharts import QPieSeries,QChart,QPieSlice,QLegend
from PySide6.QtCore import Qt
from PySide6.QtGui import QPainter,QColor,QFont

import functools

from views.studentPlacementStatPageView_UI import Ui_MainWindow


class StudentPlacementStatPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller,viewmodel):
		super().__init__()

		self.setupUi(self)

		self.controller = controller
		self.viewmodel = viewmodel

		self.campusFilter = None if self.campusComboBox.currentText()=="All" else self.campusComboBox.currentText()
		self.batchFitler = None if self.batchComboBox.currentText()=="All" else self.batchComboBox.currentText()
		self.departmentFilter = None if self.departmentComboBox.currentText()=="All" else self.departmentComboBox.currentText()
		self.courseFilter = None if self.courseComboBox.currentText()=="All" else self.courseComboBox.currentText()
		self.genderFilter = None if self.genderComboBox.currentText()=="All" else self.genderComboBox.currentText()

		self.studentsEligiblePercent = 0
		self.studentsAppliedPercent = 0
		self.studentsNotAppliedPercent = 0
		self.studentsPlacedPercent = 0

		self.campusComboBox.currentTextChanged.connect(self.filterChanged)
		self.batchComboBox.currentTextChanged.connect(self.filterChanged)
		self.departmentComboBox.currentTextChanged.connect(self.filterChanged)
		self.courseComboBox.currentTextChanged.connect(self.filterChanged)
		self.genderComboBox.currentTextChanged.connect(self.filterChanged)


	def initPieChart(self,data):
		self.pieChart.removeAllSeries()
		self.series = QPieSeries()
		self.series.setHoleSize(0.25)
		self.series.setPieSize(0.71)

		self.colors = ["#2ecc71","#e67e22","#e74c3c"]

		for self.item in data:
			self.series.append(QPieSlice(self.item[0],self.item[1]))

		for index,self.slice in enumerate(self.series.slices()):

			self.color = QColor(self.colors[index])

			self.slice.setLabel("{:.2f}%".format(round(self.slice.percentage()*100),2))
			self.slice.setLabelBrush(self.color)
			self.slice.setColor(self.color)
			self.slice.setBorderWidth(5)
			self.color.setAlpha(100)
			self.slice.setBorderColor(self.color)
			self.slice.setExplodeDistanceFactor(0.001)
			self.slice.setExploded(True)
			self.slice.setLabelVisible(True)
			self.slice.setLabelFont(QFont("Serif", 11, QFont.Medium))
			self.slice.hovered.connect(functools.partial(self.pieSliceHovered,self.slice))

		self.pieChart.addSeries(self.series)

		self.pieChart.legend().setFont(QFont("Serif", 20, QFont.Normal))
		self.pieChart.legend().setMarkerShape(QLegend.MarkerShapeCircle)

		for index,marker in enumerate(self.pieChart.legend().markers()):
			marker.setLabel(self.data[index][0])


		self.pieChart.legend().setAlignment(Qt.AlignRight)
		self.pieChartDisplay.setRenderHint(QPainter.Antialiasing)

	def pieSliceHovered(self,pieSlice,state):
		self.pieChart.zoom(2.0)
		if(state):
			pieSlice.setExplodeDistanceFactor(0.1)
		else:
			pieSlice.setExplodeDistanceFactor(0.001)


	def show(self):

		self.controller.changeFilter(self.campusFilter,self.batchFitler,self.departmentFilter,self.courseFilter,self.genderFilter)

		self.totalStudentsNumber.setText(str(self.viewmodel.getStudentAggregates()[0]))
		self.studentsNotPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[4]))
		self.studentsEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[1]))
		self.studentsNotEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[2]))
		self.totalDisqualifiedNumber.setText(str(self.viewmodel.getStudentAggregates()[5]))
		self.studentsPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[3]))

		self.data = [['Enrolled', self.viewmodel.totalEnrolledStudents],['Not Enrolled', self.viewmodel.totalNotEnrolledStudents],['Removed/Blocked',self.viewmodel.totalDisqualified]]
		self.initPieChart(self.data)

		super().show()	

	def filterChanged(self):
		self.campusFilter = None if self.campusComboBox.currentText()=="All" else self.campusComboBox.currentText()
		self.batchFitler = None if self.batchComboBox.currentText()=="All" else self.batchComboBox.currentText()
		self.departmentFilter = None if self.departmentComboBox.currentText()=="All" else self.departmentComboBox.currentText()
		self.courseFilter = None if self.courseComboBox.currentText()=="All" else self.courseComboBox.currentText()
		self.genderFilter = None if self.genderComboBox.currentText()=="All" else self.genderComboBox.currentText()

		self.controller.changeFilter(self.campusFilter,self.batchFitler,self.departmentFilter,self.courseFilter,self.genderFilter)

		self.totalStudentsNumber.setText(str(self.viewmodel.getStudentAggregates()[0]))
		self.studentsNotPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[4]))
		self.studentsEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[1]))
		self.studentsNotEnrolledNumber.setText(str(self.viewmodel.getStudentAggregates()[2]))
		self.totalDisqualifiedNumber.setText(str(self.viewmodel.getStudentAggregates()[5]))
		self.studentsPlacedNumber.setText(str(self.viewmodel.getStudentAggregates()[3]))

		self.data = [['Enrolled', self.viewmodel.totalEnrolledStudents],['Not Enrolled', self.viewmodel.totalNotEnrolledStudents],['Removed/Blocked',self.viewmodel.totalDisqualified]]
		self.initPieChart(self.data)