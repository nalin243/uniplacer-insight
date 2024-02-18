#This is the main controller file that will create instantiate all the controllers and views. 

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QSplashScreen
from mysql.connector import errorcode
from PySide6.QtCore import Slot,QObject
from PySide6.QtGui import QPixmap

from views.landingPageView import LandingPageView
from views.studentPlacementStatPageView import StudentPlacementStatPageView
from views.companyPlacementStatisticsView import CompanyPlacementStatisticsView

from resources.errormodal import ErrorModal
from resources.loginmodal import LoginModal
from resources.loadinganimationdialog import LoadingAnimationDialog

from controllers.landingPageController import LandingPageController
from controllers.studentPlacementStatPageController import StudentPlacementStatPageController
from controllers.companyPlacementStatPageController import CompanyPlacementStatPageController

from models.studentPlacementStatPageViewModel import StudentPlacementStatPageViewModel
from models.companyPlacementStatPageViewModel import CompanyPlacementStatPageViewModel

from data.datamanager import DataManager
from data.normalizeworker import NormalizeWorker
from data.appstorage import AppStorage

from data.loginauth import LoginAuth

from functools import partial

import images
import time

class Application(QApplication):

	_currentPage = -1      # -1 indidcates that current page is landing page

	def __init__(self,args):
		super(Application,self).__init__([])

		self.DEVELOPER_MODE = args.dev

		self.setQuitOnLastWindowClosed(False)

		try:
			from ctypes import windll
			appid = "customcompany.uniplacerinsight.app.version1"
			windll.shell32.SetCurrentProcessExplicitAppUserModelID(appid)
		except ImportError:
			pass

		self.splashscreen = QSplashScreen(pixmap=QPixmap(":/icons/splashscreen.png"))

		self.loadinganimationdialog = LoadingAnimationDialog()

		self.appstorage = AppStorage()

		self.loginauth = LoginAuth(self.appstorage)

		self.datamanager = DataManager(self,self.appstorage,self.loadinganimationdialog)

		#instantiating the models
		self.studentplacementstatpageviewmodel = StudentPlacementStatPageViewModel(self.datamanager)
		self.companyplacementstatpageviewmodel = CompanyPlacementStatPageViewModel(self.datamanager)

		#instantiating the controllers
		self.landingpagecontroller = LandingPageController(self,self.datamanager)
		self.studentplacementstatpagecontroller = StudentPlacementStatPageController(self,self.studentplacementstatpageviewmodel)
		self.companyplacementstatpagecontroller = CompanyPlacementStatPageController(self,self.companyplacementstatpageviewmodel)

		#instantiating all the views
		self.landingpageview = LandingPageView(self.landingpagecontroller)
		self.studentplacementstatpageview = StudentPlacementStatPageView(self.studentplacementstatpagecontroller,self.studentplacementstatpageviewmodel)
		self.companyplacementstatpageview = CompanyPlacementStatisticsView(self.companyplacementstatpagecontroller, self.companyplacementstatpageviewmodel)

		self.dialog = ErrorModal(self.landingpageview.widget)
		self.loginmodal = LoginModal(self.loginauth,self.landingpageview.widget)

		self.splashscreen.show()
		time.sleep(3)
		self.splashscreen.close()

		self.displayView(-1)#first page is always landing page

		self.exec()#start the event loop

	def setDbConfig(self,username,password,name,host):

		self.datamanager.setDbConfig(username,password,name,host)
		self.appstorage.storeDbCredentials(username,password,name,host)

	def showErrorModal(self,code):
		if(code==5):
			self.dialog.setWindowTitleText("Localization support error")
			self.dialog.setErrorText("No localization support for language eng, check database server")
			self.dialog.exec()
		if(code==4):
			self.dialog.setWindowTitleText("Connection Refused")
			self.dialog.setErrorText("Host does not have permission to connect to database")
			self.dialog.exec()
		if(code==3):
			self.dialog.setWindowTitleText("Can't connect to database")
			self.dialog.setErrorText("Make sure database credentials are correct and database is up")
			self.dialog.exec()
		if(code==2):
			self.dialog.setWindowTitleText("Database Connection Refused")
			self.dialog.setErrorText("Make sure database is reachable")
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

		if(self.DEVELOPER_MODE):
			self.landingpageview.show()
			match Application._currentPage:
				case 0:
					self.landingpageview.hide()
					self.studentplacementstatpageview.show()
				case 1:
					self.landingpageview.hide()
					self.companyplacementstatpageview.show()
				case 2:
					pass
		else:
			if(Application._currentPage == -1):
				self.landingpageview.show()
			elif(Application._currentPage != -1):
				if(dbConnStatus==2):#check if there is any error first
					self.showErrorModal(2)
				elif(dbConnStatus==1):
					self.showErrorModal(1)
				elif(dbConnStatus==3):
					self.showErrorModal(3)
				elif(dbConnStatus==4):
					self.showErrorModal(4)
				elif(dbConnStatus==5):
					self.showErrorModal(5)
				elif(dbConnStatus==0):
					self.loginmodal.signInButton.clicked.connect(partial(self.checkAuth, dbConnStatus))
					self.loginmodal.confirmCredButton.clicked.connect(partial(self.newCredentials, dbConnStatus))
					self.loginmodal.stackedWidget.setCurrentIndex(0)
					self.loginmodal.show()

	

	def checkAuth(self,dbConnStatus):  # Function to show the modules once authentication check is True

		self.loginauth.establishConn()

		username = self.loginmodal.userNameInput.text()
		password = self.loginmodal.passwordInput.text()

		authStatus = self.loginauth.checkAuth(username, password)

		if(authStatus): 
			self.loginmodal.close()
			match Application._currentPage:
				case 0:
					self.landingpageview.hide()
					self.studentplacementstatpageview.show()
				case 1:
					self.landingpageview.hide()
					self.companyplacementstatpageview.show()
				case 2:
					pass

		else:
			self.loginmodal.wrongCredLabel.setText("Wrong Credentials")

	def newCredentials(self, dbConnStatus):
		self.loginauth.establishConn()
		newMail = self.loginmodal.emailInput.text()
		confirmPass = self.loginmodal.confirmPasswordInput.text()

		if(self.loginauth.newCredentials(newMail, confirmPass)):
			if(dbConnStatus == 0):
				self.loginmodal.wrongCredLabel.setText("")
				self.loginmodal.stackedWidget.setCurrentIndex(0)