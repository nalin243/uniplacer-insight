from models.tablemodel import TableModel

class StudentPlacementStatPageViewModel():

	def __init__(self,datamanager):
		self.datamanager = datamanager

		self.totalStudents = 0
		self.totalEnrolledStudents = 0
		self.totalNotEnrolledStudents = 0
		self.totalDisqualified = 0
		self.totalPlacedStudents = 0
		self.totalNotPlacedStudents = 0

		self.placedList = []
		self.notPlacedList = []

		self.categories = []

		self.barChartYaxisRange = 0

		self.placedTableData = None


	def getPlacedData(self):

		return self.placedTableData

	def setPlacedData(self,campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter):
		try:

			placedTableData = self.datamanager.getPlacedData(campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter)
			self.placedTableData = TableModel(placedTableData)

		except Exception as e:
			print(e)
			if "cannot unpack non-iterable NoneType" in str(e):
				self.placedTableData = None


	def getStudentAggregates(self):
		#getting aggregate code
		return (self.totalStudents,self.totalEnrolledStudents,self.totalNotEnrolledStudents,self.totalPlacedStudents,self.totalNotPlacedStudents,self.totalDisqualified)


	def setStudentAggregates(self,campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter):
		#setting aggregate code
		try:
			(totalStudents,totalEnrolled,totalNotEnrolled,totalPlaced,totalNotPlaced,totalDisqualified) = self.datamanager.getStudentPlacementStatAggregates(campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter)
			self.totalStudents = totalStudents
			self.totalEnrolledStudents = totalEnrolled
			self.totalNotEnrolledStudents = totalNotEnrolled
			self.totalPlacedStudents = totalPlaced
			self.totalNotPlacedStudents = totalNotPlaced
			self.totalDisqualified = totalDisqualified
		except Exception as e:
			if "cannot unpack non-iterable NoneType" in str(e):
				self.totalStudents = 0
				self.totalEnrolledStudents = 0
				self.totalNotEnrolledStudents = 0
				self.totalDisqualified = 0
				self.totalPlacedStudents = 0
				self.totalNotPlacedStudents = 0

				self.placedList = []
				self.notPlacedList = []

				self.categories = []

				self.barChartYaxisRange = 0
			print(e,"StudentPlacementStatPageViewModel")


	def getBarChartValues(self):
		return (self.placedList,self.notPlacedList,self.categories,self.barChartYaxisRange)


	def setBarChartValues(self,campusFilter,batchFilter):
		placedList = []
		notPlacedList = []
		categories = []
		barChartYaxisRange = 0
		try:
			placedList,notPlacedList,categories,barChartYaxisRange = self.datamanager.getStudentPlacementStatBarChartData(campusFilter,batchFilter)
		except Exception as e:
			# print(e.__class__.__name__)
			pass

		self.placedList = placedList
		self.notPlacedList = notPlacedList
		self.categories = categories
		self.barChartYaxisRange = barChartYaxisRange

