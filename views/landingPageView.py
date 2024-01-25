from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow,QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QPropertyAnimation,QRect,QSize

from views.landingPageView_UI import Ui_MainWindow
from resources.dbcredentialsformmodal import DbCredentialsFormModal

import images

class LandingPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller):
		super().__init__()

		self.setupUi(self)
		self.setWindowTitle("Uniplacer Insight")

		self.controller = controller
		self.dbcredentialmodal = DbCredentialsFormModal(self.widget)

		self.updatePageStatus()

		self.CardNextButton.mousePressEvent = self.nextModuleCard
		self.CardPrevButton.mousePressEvent = self.previousModuleCard

		self.stackedWidgetForCards.currentChanged.connect(self.updatePageStatus)
		self.stackedWidgetForCards.mousePressEvent =  self.controller.showModuleWindow

		self.uploadButton.mousePressEvent = self.selectFolder
		self.dbSettingsButton.mousePressEvent = self.showDbCredModal

		self.dbcredentialmodal.submitButton.clicked.connect(self.updateDbAuth)


	def updateDbAuth(self,event):

		username = self.dbcredentialmodal.dbUserInputBox.text()
		password = self.dbcredentialmodal.dbPassInputBox.text()
		name = self.dbcredentialmodal.dbNameInputBox.text()
		host = self.dbcredentialmodal.dbHostInputBox.text()

		self.dbcredentialmodal.close()
		
		self.controller.updateDbAuth(username,password,name,host)


	def showDbCredModal(self,event):
		self.dbcredentialmodal.exec()


	def selectFolder(self,event):
		self.dir = self.fileUploadDialog.getExistingDirectory(None,caption="Select folder containing excel sheets")
		self.controller.setDirPath(self.dir)

	def nextModuleCard(self, event):
		#contains code to move to the next card
		self.controller.setCurrentCardIndex(self.controller.getCurrentCardIndex()+1)	
		self.stackedWidgetForCards.slideToNextWidget()

	def previousModuleCard(self, event):
		#contains code to move to the previous card
		self.controller.setCurrentCardIndex(self.controller.getCurrentCardIndex()-1)
		self.stackedWidgetForCards.slideToPreviousWidget()

	def updatePageStatus(self):
		match self.controller.getCurrentCardIndex():
			case 0:
				self.CardPrevButton.setPixmap(QPixmap(u""))
				self.radio1.setCheckable(True)
				self.radio1.setChecked(True)

				self.radio2.setCheckable(False)
				self.radio3.setCheckable(False)

			case 1:	
				self.CardPrevButton.setPixmap(QPixmap(u":/icons/arrow2.png"))
				self.CardNextButton.setPixmap(QPixmap(u":/icons/arrow.png"))
				self.radio2.setCheckable(True)
				self.radio2.setChecked(True)

				self.radio1.setCheckable(False)
				self.radio3.setCheckable(False)

			case 2:
				self.CardNextButton.setPixmap(QPixmap(u""))
				self.radio3.setCheckable(True)
				self.radio3.setChecked(True)

				self.radio1.setCheckable(False)
				self.radio2.setCheckable(False)
