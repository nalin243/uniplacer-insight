
class CompanyPlacementStatPageViewModel():

	def __init__(self,datamanager):

		self.datamanager = datamanager

		self.totalCompanies = 0
		self.totalVisited = 0
		self.totalNotVisited = 0
		self.companiesHired = 0
		self.companiesNotHired = 0



	def getCompanyAggregates(self):
		return (self.totalCompanies,self.totalVisited,self.totalNotVisited,self.companiesHired,self.companiesNotHired)


	def setCompanyAggregates(self,jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter):
		try:
			(totalCompanies,totalVisited,totalNotVisited,companiesHired,companiesNotHired) = self.datamanager.getCompanyAggregates(jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter)
			
			self.totalCompanies = totalCompanies
			self.totalVisited = totalVisited
			self.totalNotVisited = totalNotVisited
			self.companiesHired = companiesHired
			self.companiesNotHired = companiesNotHired

		except Exception as e:
			if "cannot unpack non-iterable NoneType" in str(e):
				self.totalCompanies = 0
				self.totalVisited = 0
				self.totalNotVisited = 0
				self.companiesHired = 0
				self.companiesNotHired = 0