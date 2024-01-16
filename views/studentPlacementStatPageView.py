from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from views.studentPlacementStatPageView_UI import Ui_MainWindow


class StudentPlacementStatPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller,viewmodel):
		super().__init__()

		self.setupUi(self)

		self.controller = controller
		self.viewmodel = viewmodel

		self.totalStudentsNumber.setText(str(self.viewmodel._totalStudents))
		self.studentsEligibleNumber.setText(str(self.viewmodel._totalEligibleStudents))
		self.studentsAppliedNumber.setText(str(self.viewmodel._totalStudentsApplied))
		self.studentsNotAppliedNumber.setText(str(self.viewmodel._totalStudentsNotApplied))
		self.totalCompaniesNumber.setText(str(self.viewmodel._totalCompanies))
		self.studentsPlacedNumber.setText(str(self.viewmodel._totalStudentsPlaced))

		self.campusFilter = self.campusComboBox.currentText()
		self.batchFitler = self.batchComboBox.currentText()
		self.departmentFilter = self.departmentComboBox.currentText()
		self.courseFilter = self.courseComboBox.currentText()
		self.genderFilter = self.genderComboBox.currentText()

		self.campusComboBox.currentTextChanged.connect(self.filterChanged)
		self.batchComboBox.currentTextChanged.connect(self.filterChanged)
		self.departmentComboBox.currentTextChanged.connect(self.filterChanged)
		self.courseComboBox.currentTextChanged.connect(self.filterChanged)
		self.genderComboBox.currentTextChanged.connect(self.filterChanged)

		self.show()


	def filterChanged(self):
		self.campusFilter = self.campusComboBox.currentText()
		self.batchFitler = self.batchComboBox.currentText()
		self.departmentFilter = self.departmentComboBox.currentText()
		self.courseFilter = self.courseComboBox.currentText()
		self.genderFilter = self.genderComboBox.currentText()

		self.controller.changeFilter(self.campusFilter,self.batchFitler,self.departmentFilter,self.courseFilter,self.genderFilter)
