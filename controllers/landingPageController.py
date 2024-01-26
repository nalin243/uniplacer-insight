import os
from pathlib import Path

class LandingPageController():

	_currentCardIndex = 0

	def __init__(self,app,datamanager):
		self.app = app
		self.datamanager = datamanager

	def showModuleWindow(self,event):
		#contains code to show the module that has been clicked
		#this function can't change show or hide views by itself and has to call an application function to do so
		# self.setExcelFilePaths(self.dirPath)
		self.app.displayView(self._currentCardIndex)

	def setCurrentCardIndex(self, index):
		if index < 0 or index > 2:
			pass
		else:
			self._currentCardIndex = index

	def setDirPath(self,path):
		self.datamanager.setFolderPath(path)


	def getCurrentCardIndex(self):
		return self._currentCardIndex


	def updateDbAuth(self,username,password,name,host):
		self.app.setDbConfig(username,password,name,host)

	def checkDb(self):
		return self.app.datamanager.checkDb()


	def showErrorModal(self,code):
		self.app.showErrorModal(code)

