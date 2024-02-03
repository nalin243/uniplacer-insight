from numpy.lib.function_base import place
import pandas
from sqlalchemy import create_engine
from mysql.connector import connect,Error
from sqlalchemy.sql.dml import coercions

from PySide6.QtCore import QThreadPool
from data.normalizeworker import NormalizeWorker

from resources.loadinganimationdialog import LoadingAnimationDialog

import os

class DataManager():

	def __init__(self,app=None,appstorage=None,loadinganimationdialog=None):

		self.app = app
		self.appstorage = appstorage

		username,password,host,dbname = self.appstorage.getDbCredentials()

		self._dbUsername = username
		self._dbPassword = password
		self._dbName = dbname
		self._dbHost = host

		self._coeFilePath = ""
		self._placementFilePath = ""
		self._companyFilePath = ""

		self.folderPath = ""
		self.loadinganimationdialog = loadinganimationdialog

		self.threadpool = QThreadPool()


	def setDbConfig(self,username,password,name,host):
		self._dbUsername = username
		self._dbPassword = password
		self._dbName = name
		self._dbHost = host

	def setFolderPath(self,path):
		self.folderPath = path
		self.setExcelFilePaths()

	def setExcelFilePaths(self):
		#used to set the file paths for the excel files that we fetch data from
		coeFilePath = ""
		placementFilePath = ""
		companyFilePath = ""

		try:
			folderList = os.listdir(self.folderPath)

			for file in folderList:
				if "Overall_COE_" in str(file):
					coeFilePath = self.folderPath+"/"+file
				if "DB_Batch_" in str(file):
					placementFilePath = self.folderPath+"/"+file
				if "PLACEMENT_JOB_PROFILE" in str(file):
					companyFilePath = self.folderPath+"/"+file

		except Exception as e:
			print(e)

		self._coeFilePath = coeFilePath
		self._placementFilePath = placementFilePath
		self._companyFilePath = companyFilePath

		self.normalizeworker = NormalizeWorker(self.normalizeAndPushToSql,self.checkDb,self.setExcelFilePaths)

		self.normalizeworker.startSignal.connect(self.loadinganimationdialog.show)
		self.normalizeworker.endSignal.connect(self.loadinganimationdialog.close)

		self.threadpool.start(self.normalizeworker)

	def normalizeAndPushToSql(self):
		try:			
			engine = create_engine("mysql+mysqlconnector://{}:{}@{}/{}".format(self._dbUsername,self._dbPassword,self._dbHost,self._dbName))

			placementData = pandas.read_excel("{}".format(self._placementFilePath),"Single",usecols=["Roll No","Placed","CTC","Stipend","Type","Category","Bi Weekly","IT/ Non IT","Enrolled in SS"])
			overallData = pandas.read_excel("{}".format(self._coeFilePath),"Overall")
			companyData = pandas.read_excel("{}".format(self._companyFilePath),"Sheet0",usecols=["Title","Company Name","Position Type","Source","Date of Visit","Job sector","Placement category","Status","Location","CTC Currency","CTC Minnimum","CTC Maximum","Number of Students Eligible","Number of Students Applied","Number of Select Students","Average Package Offered"])

			year = (self._placementFilePath.split("_"))[-2]

			#cleaning up data
			overallData.drop(columns=["Date of Birth","Address","Semester","PIN Code","Contact No.","History of Arrear","E-Mail","GPA1","GPA2","GPA3","GPA4","GPA5","GPA6","GPA7","GPA8","GPA9","GPA10"],axis=1,inplace=True)
			overallData.rename(columns={"Office Name":"Office_Name","Course Name":"Course_Name","Student Name":"Student_Name","Register No.":"Register_No.","Bi Weekly":"Bi_Weekly","IT/ Non IT":"IT/_Non_IT","Enrolled in SS":"Enrolled_in_SS","Standing Arrear":"Standing_Arrear"},inplace=True)
			placementData.rename(columns={"Roll No":"Register_No.","Bi Weekly":"Bi_Weekly","IT/ Non IT":"IT/_Non_IT","Enrolled in SS":"Enrolled_in_SS"},inplace=True)
			companyData.rename(columns={"Company Name":"Company_Name","Position Type":"Position_Type","Date of Visit":"Date_of_Visit","Job sector":"Job_sector","Placement category":"Placement_category","CTC Currency":"CTC_Currency","CTC Minnimum":"CTC_Minimum","CTC Maximum":"CTC_Maximum","Number of Students Eligible":"Number_of_Students_Eligible","Number of Students Applied":"Number_of_Students_Applied","Number of Select Students":"Number_of_Select_Students","Average Package Offered":"Average_Package_Offered"},inplace=True)

			#merging the dataframes to get a single df with all the data from the two tables
			combinedData = pandas.merge(overallData,placementData,left_on='Register_No.',right_on='Register_No.',how='outer',suffixes=('_left','_right'))

			#converting dataframe to sql table and putting in database
			combinedData.to_sql("students_{}".format(year),con=engine,if_exists='replace',index=False)
			companyData.to_sql("profiles_{}".format(year),con=engine,if_exists='replace',index=False)
		except Exception as e:
			print(e)


	def getStudentPlacementStatBarChartData(self,campusFilter,batchFilter):

		categories = ["Applied Data Science","Atmospheric Science","Biochemistry","Biotechnology","Chemistry","Computer Science","Information Tehcnology","Mathematics","Visual Communication","Accounting and Finance","Commerce","Computer Applications","Journalism and Mass Communication","Business Administration","Digital Marketing","Data Science","Fashion Designing","Psychology"]
		
		categoriesEnrolled = []
		categoriesNotEnrolled = []

		campusQuery = "select count(*) from students_{}".format(batchFilter)

		try:
			connection = connect(host=self._dbHost,user=self._dbUsername,password=self._dbPassword,database=self._dbName)
			cursor = connection.cursor()

			for category in categories:
				cursor.execute("select count(*) from students_{} where Enrolled_in_SS='Enrolled' and Branch like '{}' and Office_Name like '{}' ".format(batchFilter,category,"%" if campusFilter==None else campusFilter))
				value1 = cursor.fetchall()[0][0]
				# print(value1,category)
				categoriesEnrolled.append(value1)
				cursor.reset()

				cursor.execute("select count(*) from students_{} where (Enrolled_in_SS like 'Not Enrolled' or Enrolled_in_SS is null) and Branch like '{}' and Office_Name like '{}' ".format(batchFilter,category,"%" if campusFilter==None else campusFilter))
				categoriesNotEnrolled.append(cursor.fetchall()[0][0])

				cursor.reset()

			barChartYaxisRange = max(max(categoriesNotEnrolled),max(categoriesEnrolled))+20

			return (categoriesEnrolled,categoriesNotEnrolled,categories,barChartYaxisRange)

		except Exception as e:
			pass


	def getStudentPlacementStatAggregates(self,campusFilter=None,batchFilter=None,departmentFilter=None,courseFilter=None,genderFilter=None):
		totalStudents = 0
		totalEnrolled = 0
		totalNotEnrolled = 0
		totalPlaced = 0
		totalNotPlaced = 0
		totalDisqualified = 0
		try:
			connection = connect(host=self._dbHost,user=self._dbUsername,password=self._dbPassword,database=self._dbName)
			cursor = connection.cursor()

			totalQuery = "select count(*) from students_{} where Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format(batchFilter,"%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalEnrolledQuery = "select count(*) from students_{} where Enrolled_in_SS='Enrolled' and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format(batchFilter,"%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalNotEnrolledQuery = "select count(*) from students_{} where (Enrolled_in_SS like 'Not Enrolled' or Enrolled_in_SS is null) and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format(batchFilter,"%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalPlacedQuery = "select count(*) from students_{} where Placed is not null and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format(batchFilter,"%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalNotPlacedQuery = "select count(*) from students_{} where Placed is null and Enrolled_in_SS='Enrolled' and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format(batchFilter,"%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalDisqualifiedQuery = "select count(*) from students_{} where Enrolled_in_SS like 'Not Blocked' or Enrolled_in_SS like 'Removed' and  Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format(batchFilter,"%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)

			cursor.execute(totalQuery)
			totalStudents = cursor.fetchall()[0][0] 
			cursor.reset()

			cursor.execute(totalEnrolledQuery)
			totalEnrolled = cursor.fetchall()[0][0] 
			cursor.reset()

			cursor.execute(totalNotEnrolledQuery)
			totalNotEnrolled = cursor.fetchall()[0][0]
			cursor.reset() 

			cursor.execute(totalPlacedQuery)
			totalPlaced = cursor.fetchall()[0][0]
			cursor.reset()

			cursor.execute(totalNotPlacedQuery)
			totalNotPlaced = cursor.fetchall()[0][0]
			cursor.reset()

			cursor.execute(totalDisqualifiedQuery)
			totalDisqualified = cursor.fetchall()[0][0]
			cursor.reset()
					
			return (totalStudents,totalEnrolled,totalNotEnrolled,totalPlaced,totalNotPlaced,totalDisqualified)

		except Error as e:
			if "uniplacer_insight.students_2024" in str(e.msg):
				# print("table does not exist")
				pass
			print(e)


	def getCompanyAggregates(self,jobTypeFilter,jobSectorFilter,ctcFilter,companyLevelFilter, batchFilter):
		#getting company aggregates for second module according to the filters
		totalCompanies = 0
		totalVisited = 0
		totalNotVisited = 0
		companiesHired = 0
		companiesNotHired = 0

		minimum_ctc,_,maximum_ctc = ctcFilter.split(" ")

		try:

			connection = connect(host=self._dbHost,user=self._dbUsername,password=self._dbPassword,database=self._dbName)
			cursor = connection.cursor()

			totalCompaniesQuery = "select count(*) from profiles_{} where Position_Type like '{}' and Job_sector like '{}' and Placement_category like '{}' and CTC_Minimum >= {} and CTC_Maximum <= {};".format(batchFilter,"%" if jobTypeFilter==None else jobTypeFilter, "%" if jobSectorFilter==None else jobSectorFilter, "%" if companyLevelFilter==None else companyLevelFilter, "%" if minimum_ctc==None else minimum_ctc, "%" if maximum_ctc==None else maximum_ctc)
			totalVisitedQuery = "select count(*) from profiles_{} where Date_of_Visit is not null and Position_Type like '{}' and Job_sector like '{}' and Placement_category like '{}' and CTC_Minimum >= {} and CTC_Maximum <= {};".format(batchFilter,"%" if jobTypeFilter==None else jobTypeFilter, "%" if jobSectorFilter==None else jobSectorFilter, "%" if companyLevelFilter==None else companyLevelFilter, "%" if minimum_ctc==None else minimum_ctc, "%" if maximum_ctc==None else maximum_ctc)
			totalNotVisitedQuery = "select count(*) from profiles_{} where Date_of_Visit is null and Position_Type like '{}' and Job_sector like '{}' and Placement_category like '{}' and CTC_Minimum >= {} and CTC_Maximum <= {};".format(batchFilter,"%" if jobTypeFilter==None else jobTypeFilter, "%" if jobSectorFilter==None else jobSectorFilter, "%" if companyLevelFilter==None else companyLevelFilter, "%" if minimum_ctc==None else minimum_ctc, "%" if maximum_ctc==None else maximum_ctc)
			companiesHiredQuery = "select count(*) from profiles_{} where Number_of_Select_Students > 0 and Position_Type like '{}' and Job_sector like '{}' and Placement_category like '{}' and CTC_Minimum >= {} and CTC_Maximum <= {};".format(batchFilter,"%" if jobTypeFilter==None else jobTypeFilter, "%" if jobSectorFilter==None else jobSectorFilter, "%" if companyLevelFilter==None else companyLevelFilter, "%" if minimum_ctc==None else minimum_ctc, "%" if maximum_ctc==None else maximum_ctc)
			companiesNotHiredQuery = "select count(*) from profiles_{} where Number_of_Select_Students = 0 is not null and Position_Type like '{}' and Job_sector like '{}' and Placement_category like '{}' and CTC_Minimum >= {} and CTC_Maximum <= {};".format(batchFilter,"%" if jobTypeFilter==None else jobTypeFilter, "%" if jobSectorFilter==None else jobSectorFilter, "%" if companyLevelFilter==None else companyLevelFilter, "%" if minimum_ctc==None else minimum_ctc, "%" if maximum_ctc==None else maximum_ctc)

			cursor.execute(totalCompaniesQuery)
			totalCompanies = cursor.fetchall()[0][0] 
			cursor.reset()

			cursor.execute(totalVisitedQuery)
			totalVisited = cursor.fetchall()[0][0] 
			cursor.reset()

			cursor.execute(totalNotVisitedQuery)
			totalNotVisited = cursor.fetchall()[0][0]
			cursor.reset() 

			cursor.execute(companiesHiredQuery)
			companiesHired = cursor.fetchall()[0][0]
			cursor.reset()

			cursor.execute(companiesNotHiredQuery)
			companiesNotHired = cursor.fetchall()[0][0]
			cursor.reset()
						
			return (totalCompanies, totalVisited, totalNotVisited, companiesHired, companiesNotHired)

		except Error as e:
			print(e)


	def checkDb(self):

		if(self._dbHost == None or self._dbName == None or self._dbPassword == None or self._dbUsername == None):
			return 3

		try:
			connection = connect(host=self._dbHost,user=self._dbUsername,password=self._dbPassword,database=self._dbName)
			cursor = connection.cursor()
			cursor.execute("select * from students_2024")

			return 0
		except Error as e:
			if "not allowed to connect" in str(e):
				return 4
			elif "Can't connect to MySQL server on" in str(e):
				return 3
			elif "refused" in str(e):
				return 2
			elif "uniplacer_insight.students" in str(e.msg):
				return 1


		return -1
