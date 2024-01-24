#This is the main controller file that will create instantiate all the controllers and views. 

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from mysql.connector import errorcode
from PySide6.QtCore import Slot,QObject

from views.landingPageView import LandingPageView
from views.studentPlacementStatPageView import StudentPlacementStatPageView
from resources.errormodal import ErrorModal

from controllers.landingPageController import LandingPageController
from controllers.studentPlacementStatPageController import StudentPlacementStatPageController

from models.studentPlacementStatPageViewModel import StudentPlacementStatPageViewModel

from data.datamanager import DataManager

class Application(QApplication):

	_currentPage = -1      # -1 indidcates that current page is landing page

	def __init__(self):
		super(Application,self).__init__([])

		self.datamanager = DataManager(self)

		#instantiating the models
		self.studentplacementstatpageviewmodel = StudentPlacementStatPageViewModel(self.datamanager)

		#instantiating the controllers
		self.landingpagecontroller = LandingPageController(self,self.datamanager)
		self.studentplacementstatpagecontroller = StudentPlacementStatPageController(self,self.studentplacementstatpageviewmodel)

		#instantiating all the views and dialog boxes
		self.landingpageview = LandingPageView(self.landingpagecontroller)
		self.studentplacementstatpageview = StudentPlacementStatPageView(self.studentplacementstatpagecontroller,self.studentplacementstatpageviewmodel)
		self.dialog = ErrorModal(self.landingpageview.widget)

		self.displayView(-1)#first page is always landing page

		self.exec()#start the event loop

	def showErrorModal(self,code):
		if(code==2):
			self.dialog.setWindowTitleText("Database Connection Refused")
			self.dialog.setErrorText("Make sure database configuration is correct and database is reachable")
			self.dialog.exec()
		if(code==1):
			self.dialog.setWindowTitleText("Incomplete Database")
			self.dialog.setErrorText("Make sure all required tables are present in database")
			self.dialog.exec()

	def getCurrentPage(self):
		return Application._currentPage

	def setCurrentPage(self,pageIndex):
		Application._currentPage = pageIndex

	def displayView(self,viewIndex):
		#use this function to show appropriate view

		dbConnStatus = self.datamanager.checkDb()#checking to whether appropriate tables exist and that db connection has no issues
		Application._currentPage = viewIndex


		match Application._currentPage:
			case -1:
				self.landingpageview.show()
				self.studentplacementstatpageview.close()
				# for other views to be added and closed later...
			case 0:
				if(dbConnStatus==0):
					self.studentplacementstatpageview.show()
					self.landingpageview.close()
				elif(dbConnStatus==2):
					self.showErrorModal(2)
				elif(dbConnStatus==1):
					self.showErrorModal(1)
			case 1:
				pass
			case 2:
				pass


app = Application()