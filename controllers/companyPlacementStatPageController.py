
#controller will change the viewmodel according to the filters
class CompanyPlacementStatPageController():

	def __init__(self,app,viewmodel):
		self.app = app 
		self.viewmodel = viewmodel
		

	def changeFilter(self,jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter):
		self.viewmodel.setCompanyAggregates(jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter)

	def returnToLanding(self):
		self.app.displayView(-1)