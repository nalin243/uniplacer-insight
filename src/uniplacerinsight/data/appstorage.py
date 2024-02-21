from PySide6.QtCore import QStandardPaths,QDir

import sqlite3 as sq

class AppStorage():

	def __init__(self,appDataPath):

		self.connection = sq.connect(appDataPath.filePath("appstorage.db"))
		self.cursor = self.connection.cursor()

		self.cursor.execute("create table if not exists db_credentials ( username varchar(20) primary key, password varchar(200),host varchar(100),dbname varchar(50) ) ")

	def storeDbCredentials(self,username,password,name,host):
		#check if credentials are already present, if they are replace them or else insert values

		updateCredQuery = "update db_credentials set username='{}',password='{}',host='{}',dbname='{}'".format(username,password,host,name)
		insertCredQuery = "insert into db_credentials values('{}','{}','{}','{}')".format(username,password,host,name)

		self.cursor.execute("select count(*) from db_credentials")
		if(self.cursor.fetchall()[0][0] == 1):
			self.cursor.execute(updateCredQuery)
			self.connection.commit()
		else:
			self.cursor.execute(insertCredQuery)
			self.connection.commit()


	def getDbCredentials(self):
		try:
			self.cursor.execute("select * from db_credentials")
			return self.cursor.fetchall()[0]
		except Exception as e:
			if str(e.__class__.__name__) == "IndexError":
				return (None,None,None,None)

