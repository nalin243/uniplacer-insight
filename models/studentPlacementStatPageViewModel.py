

class StudentPlacementStatPageViewModel():

	def __init__(self,datamanager):
		self.datamanager = datamanager

		self.totalStudents = 0
		self.totalEnrolledStudents = 0
		self.totalNotEnrolledStudents = 0
		self.totalDisqualified = 0
		self.totalPlacedStudents = 0
		self.totalNotPlacedStudents = 0

	def getStudentAggregates(self):
		#getting aggregate code
		return (self.totalStudents,self.totalEnrolledStudents,self.totalNotEnrolledStudents,self.totalPlacedStudents,self.totalNotPlacedStudents,self.totalDisqualified)


	def setStudentAggregates(self,campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter):
		#setting aggregate code
		try:
			(totalStudents,totalEnrolled,totalNotEnrolled,totalPlaced,totalNotPlaced,totalDisqualified) = self.datamanager.getStudentAggregates(campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter)
			self.totalStudents = totalStudents
			self.totalEnrolledStudents = totalEnrolled
			self.totalNotEnrolledStudents = totalNotEnrolled
			self.totalPlacedStudents = totalPlaced
			self.totalNotPlacedStudents = totalNotPlaced
			self.totalDisqualified = totalDisqualified
		except Exception as e:
			print(e.__class__.__name__)