#This is the main controller file that will create instantiate all the controllers and views. 

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from views.landingPageView import LandingPageView
from views.studentPlacementStatPageView import StudentPlacementStatPageView
from views.databaseincompletemodal import DatabaseIncompleteModal

from controllers.landingPageController import LandingPageController
from controllers.studentPlacementStatPageController import StudentPlacementStatPageController

from models.studentPlacementStatPageViewModel import StudentPlacementStatPageViewModel

from data.datamanager import DataManager

class Application(QApplication):

	_currentPage = -1      # -1 indidcates that current page is landing page
	flag = False

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
		self.dialog = DatabaseIncompleteModal(self.landingpageview.widget)

		self.displayView(-1)#first page is always landing page

		self.exec()#start the event loop

	def setFlag(self,flag):
		Application.flag = flag

	def getCurrentPage(self):
		return Application._currentPage

	def setCurrentPage(self,pageIndex):
		Application._currentPage = pageIndex

	def displayView(self,viewIndex):
		#use this function to show appropriate view

		Application.flag = self.datamanager.tableExists()

		self._currentPage = viewIndex
		Application._currentPage = viewIndex
		match Application._currentPage:
			case -1:
				self.landingpageview.show()
				self.studentplacementstatpageview.close()
				# for other views to be added and closed later...

			case 0:
				if(Application.flag):
					self.studentplacementstatpageview.show()
					self.landingpageview.close()
				else:
					if self.dialog.exec():
						pass
			case 1:
				if(Application.flag):
					pass
			case 2:
				if(Application.flag):
					pass


app = Application()


#The usage of flag: 
#Flag is used to check whether the data is present in the sql database or not
#If the desired tables are not present then the corresponding module simply won't open