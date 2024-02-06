
#controller will change the viewmodel according to the filters
class CompanyPlacementStatPageController():

	def __init__(self,app,viewmodel):
		self.app = app 
		self.viewmodel = viewmodel		

	def updateBarAndLineChartValues(self,batchFilter):
		self.viewmodel.setBarChartData(batchFilter)
		self.viewmodel.setLineChartData(batchFilter)

	def changeFilter(self,jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter, batchFilter):
		self.viewmodel.setCompanyAggregates(jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter,batchFilter)

	def returnToLanding(self):
		self.app.displayView(-1)