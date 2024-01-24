from numpy.lib.function_base import place
import pandas
from sqlalchemy import create_engine
from mysql.connector import connect,Error
from sqlalchemy.sql.dml import coercions

from PySide6.QtCore import QThreadPool
from data.normalizeworker import NormalizeWorker

import os


import simple_dotenv as sd 

class DataManager():

	def __init__(self,app):

		self.app = app

		self._dbUsername = str(sd.GetEnv("DB_USER"))
		self._dbPassword = str(sd.GetEnv("DB_PASSWORD"))
		self._dbName = str(sd.GetEnv("DB_NAME"))
		self._dbHost = str(sd.GetEnv("DB_HOST"))

		self._coeFilePath = ""
		self._placementFilePath = ""
		self._companyFilePath = ""

		self.folderPath = ""

		self._threadpool = QThreadPool()

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

		normalizeworker = NormalizeWorker(self.normalizeAndPushToSql,self.checkDb,self.setExcelFilePaths)
		self._threadpool.start(normalizeworker)

	def normalizeAndPushToSql(self):
		try:
			
			engine = create_engine("mysql+mysqlconnector://{}:{}@{}/{}".format(self._dbUsername,self._dbPassword,self._dbHost,self._dbName))

			placementData = pandas.read_excel("{}".format(self._placementFilePath),"Single",usecols=["Roll No","Placed","CTC","Stipend","Type","Category","Bi Weekly","IT/ Non IT","Enrolled in SS"])
			overallData = pandas.read_excel("{}".format(self._coeFilePath),"Overall")
			companyData = pandas.read_excel("{}".format(self._companyFilePath),"Sheet0",usecols=["Title","Company Name","Position Type","Source","Date of Visit","Job sector","Placement category","Status","Location","CTC Currency","CTC Minnimum","CTC Maximum","Number of Students Eligible","Number of Students Applied","Number of Select Students","Average Package Offered"])

			#cleaning up data
			overallData.drop(columns=["Date of Birth","Address","Semester","PIN Code","Contact No.","History of Arrear","E-Mail","GPA1","GPA2","GPA3","GPA4","GPA5","GPA6","GPA7","GPA8","GPA9","GPA10"],axis=1,inplace=True)
			overallData.rename(columns={"Office Name":"Office_Name","Course Name":"Course_Name","Student Name":"Student_Name","Register No.":"Register_No.","Bi Weekly":"Bi_Weekly","IT/ Non IT":"IT/_Non_IT","Enrolled in SS":"Enrolled_in_SS","Standing Arrear":"Standing_Arrear"},inplace=True)
			placementData.rename(columns={"Roll No":"Register_No.","Bi Weekly":"Bi_Weekly","IT/ Non IT":"IT/_Non_IT","Enrolled in SS":"Enrolled_in_SS"},inplace=True)
			companyData.rename(columns={"Company Name":"Company_Name","Position Type":"Position_Type","Date of Visit":"Date_of_Visit","Job sector":"Job_sector","Placement category":"Placement_category","CTC Currency":"CTC_Currency","CTC Minnimum":"CTC_Minimum","CTC Maximum":"CTC_Maximum","Number of Students Eligible":"Number_of_Students_Eligible","Number of Students Applied":"Number_of_Students_Applied","Number of Select Students":"Number_of_Select_Students","Average Package Offered":"Average_Package_Offered"},inplace=True)

			#merging the dataframes to get a single df with all the data from the two tables
			combinedData = pandas.merge(overallData,placementData,left_on='Register_No.',right_on='Register_No.',how='outer',suffixes=('_left','_right'))

			#converting dataframe to sql table and putting in database
			combinedData.to_sql("students",con=engine,if_exists='replace',index=False)
			companyData.to_sql("profiles",con=engine,if_exists='replace',index=False)

		except Exception as e:
			print(e)


	def getBarChartData(self,campusFilter):

		categories = ["Applied Data Science","Atmospheric Science","Biochemistry","Biotechnology","Chemistry","Computer Science","Information Tehcnology","Mathematics","Visual Communication","Accounting and Finance","Commerce","Computer Applications","Journalism and Mass Communication","Business Administration","Digital Marketing","Data Science","Fashion Designing","Psychology"]
		
		categoriesEnrolled = []
		categoriesNotEnrolled = []

		campusQuery = "select count(*) from students"

		try:
			connection = connect(host=self._dbHost,user=self._dbUsername,password=self._dbPassword,database=self._dbName)
			cursor = connection.cursor()

			for category in categories:
				cursor.execute("select count(*) from students where Enrolled_in_SS='Enrolled' and Branch like '{}' and Office_Name like '{}' ".format(category,"%" if campusFilter==None else campusFilter))
				value1 = cursor.fetchall()[0][0]
				# print(value1,category)
				categoriesEnrolled.append(value1)
				cursor.reset()

				cursor.execute("select count(*) from students where (Enrolled_in_SS like 'Not Enrolled' or Enrolled_in_SS is null) and Branch like '{}' and Office_Name like '{}' ".format(category,"%" if campusFilter==None else campusFilter))
				categoriesNotEnrolled.append(cursor.fetchall()[0][0])

				cursor.reset()

			barChartYaxisRange = max(max(categoriesNotEnrolled),max(categoriesEnrolled))+20

			return (categoriesEnrolled,categoriesNotEnrolled,categories,barChartYaxisRange)

		except Exception as e:
			pass


	def getStudentAggregates(self,campusFilter=None,batchFilter=None,departmentFilter=None,courseFilter=None,genderFilter=None):
		totalStudents = 0
		totalEnrolled = 0
		totalNotEnrolled = 0
		totalPlaced = 0
		totalNotPlaced = 0
		totalDisqualified = 0
		try:
			connection = connect(host=self._dbHost,user=self._dbUsername,password=self._dbPassword,database=self._dbName)
			cursor = connection.cursor()

			totalQuery = "select count(*) from students where Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format("%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalEnrolledQuery = "select count(*) from students where Enrolled_in_SS='Enrolled' and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format("%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalNotEnrolledQuery = "select count(*) from students where (Enrolled_in_SS like 'Not Enrolled' or Enrolled_in_SS is null) and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format("%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalPlacedQuery = "select count(*) from students where Placed is not null and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format("%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalNotPlacedQuery = "select count(*) from students where Placed is null and Enrolled_in_SS='Enrolled' and Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format("%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)
			totalDisqualifiedQuery = "select count(*) from students where Enrolled_in_SS like 'Not Blocked' or Enrolled_in_SS like 'Removed' and  Office_Name like '{}' and  Branch like '{}' and Course_Name like '{}' and Gender like '{}';".format("%" if campusFilter==None else campusFilter,"%" if departmentFilter==None else departmentFilter,"%" if courseFilter==None else courseFilter,"%" if genderFilter==None else genderFilter)

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
			if "uniplacer_insight.students" in str(e.msg):
				# print("table does not exist")
				pass


	def checkDb(self):
		try:
			connection = connect(host=self._dbHost,user=self._dbUsername,password=self._dbPassword,database=self._dbName)
			cursor = connection.cursor()
			cursor.execute("select * from students")

			return 0
		except Error as e:
			if "refused" in str(e):
				return 2
			if "uniplacer_insight.students" in str(e.msg):
				return 1


		return -1
