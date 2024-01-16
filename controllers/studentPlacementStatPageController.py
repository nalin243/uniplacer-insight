
#controller will change the viewmodel according to the filters
class StudentPlacementStatPageController():

	def __init__(self,app,viewmodel):
		self.app = app
		self.viewmodel = viewmodel


	def changeFilter(self,campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter):
		self.viewmodel.setAggregates(campusFilter,batchFilter,departmentFilter,courseFilter,genderFilter)