from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QPixmap

from views.landingPageView_UI import Ui_MainWindow

import images

class LandingPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller):
		super().__init__()

		self.setupUi(self)

		self.controller = controller

		self.updatePageStatus()

		self.CardNextButton.mousePressEvent = self.nextModuleCard
		self.CardPrevButton.mousePressEvent = self.previousModuleCard

		self.stackedWidgetForCards.currentChanged.connect(self.updatePageStatus)

		self.stackedWidgetForCards.mousePressEvent = self.controller.showModuleWindow

		self.show()
		

	def nextModuleCard(self, event):
		self.controller.setCurrentCardIndex(self.controller.getCurrentCardIndex()+1)
		self.stackedWidgetForCards.setCurrentIndex(self.controller.getCurrentCardIndex())
		#contains code to move to the next card

	def previousModuleCard(self,event):
		self.controller.setCurrentCardIndex(self.controller.getCurrentCardIndex()-1)
		self.stackedWidgetForCards.setCurrentIndex(self.controller.getCurrentCardIndex())
		#contains code to move to the previous card

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

		