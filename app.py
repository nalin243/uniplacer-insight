#This is the main controller file that will create instantiate all the controllers and views. 

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from views.landingPageView import LandingPageView
from views.studentPlacementStatPageView import StudentPlacementStatPageView

from controllers.landingPageController import LandingPageController
from controllers.studentPlacementStatPageController import StudentPlacementStatPageController

class Application(QApplication):

	__currentPage = -1# -1 indidcates that current page is landing page

	def __init__(self):
		super(Application,self).__init__([])

		#instantiating the controllers
		self.landingpagecontroller = LandingPageController(Application)
		self.studentplacementstatpagecontroller = StudentPlacementStatPageController(Application)

		#instantiating all the views
		self.landingpageview = LandingPageView(self.landingpagecontroller)
		self.studentplacementstatpageview = StudentPlacementStatPageView(self.studentplacementstatpagecontroller)

		self.exec()#start the event loop

	def displayView(self,viewIndex):
		#use this function to show appropriate view
		pass

app = Application()