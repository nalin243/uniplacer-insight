from models.tablemodel import TableModel

class CompanyPlacementStatPageViewModel():

	def __init__(self,datamanager):

		self.datamanager = datamanager

		self.totalCompanies = 0
		self.totalVisited = 0
		self.totalNotVisited = 0
		self.companiesHired = 0
		self.companiesNotHired = 0

		self.barChartYaxisRange = 0
		self.sectorsHired = []

		self.sectors = []

		self.months = []
		self.companiesArriving = []

		self.tableData = None

	def getTableData(self):
		
		return self.tableData

	def setTableData(self,jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter,batchFilter):
		try:
			
			tableData = self.datamanager.getTableData(jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter,batchFilter)
			self.tableData = TableModel(tableData)

		except Exception as e:
			print(e)
			if "cannot unpack non-iterable NoneType" in str(e):
				self.tableData = None


	def getCompanyAggregates(self):
		return (self.totalCompanies,self.totalVisited,self.totalNotVisited,self.companiesHired,self.companiesNotHired)


	def setCompanyAggregates(self,jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter, batchFilter):
		try:
			(totalCompanies,totalVisited,totalNotVisited,companiesHired,companiesNotHired) = self.datamanager.getCompanyAggregates(jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter, batchFilter)
			
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

	def getBarChartData(self):
		return (self.sectorsHired,self.barChartYaxisRange,self.sectors)

	def setBarChartData(self,batchFilter):
		try:
			(sectors,sectorsHired,barChartYaxisRange) = self.datamanager.getCompanyStatBarChartData(batchFilter)

			self.sectorsHired = sectorsHired
			self.barChartYaxisRange = barChartYaxisRange
			self.sectors = sectors

		except Exception as e:
			if "cannot unpack non-iterable NoneType" in str(e):
				self.barChartYaxisRange = 0
				self.sectorsHired = []
				sectors = []

	def getLineChartData(self):
		return (self.months,self.companiesArriving)

	def setLineChartData(self,batchFilter):
		try:
			(months,companiesArriving) = self.datamanager.getCompanyLineChartData(batchFilter)
			
			self.months = months
			self.companiesArriving = companiesArriving

		except Exception as e:
			if "cannot unpack non-iterable NoneType" in str(e):
				self.months = []
				self.companiesArriving = []
