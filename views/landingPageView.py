from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow,QFileDialog
from PySide6.QtGui import QPixmap
from PySide6.QtCore import QPropertyAnimation,QRect,QSize

from views.landingPageView_UI import Ui_MainWindow
from resources.errormodal import ErrorModal

import images

class LandingPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller):
		super().__init__()

		self.setupUi(self)
		self.setWindowTitle("Uniplacer Insight")

		self.controller = controller

		self.updatePageStatus()

		self.CardNextButton.mousePressEvent = self.nextModuleCard
		self.CardPrevButton.mousePressEvent = self.previousModuleCard

		self.stackedWidgetForCards.currentChanged.connect(self.updatePageStatus)
		self.stackedWidgetForCards.mousePressEvent = self.controller.showModuleWindow
		self.uploadButton.mousePressEvent = self.selectFolder


	def selectFolder(self,event):
		self.dir = self.dialog.getExistingDirectory(None,caption="Select folder containing excel sheets")
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


	def test(self,event):
		print("lol")