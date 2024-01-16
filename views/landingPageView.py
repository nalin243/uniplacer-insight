from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from views.landingPageView_UI import Ui_MainWindow

class LandingPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller):
		super().__init__()

		self.setupUi(self)
		

	def nextModuleCard(self):
		#contains code to move to the next card
		pass

	def previousModuleCard(self):
		#contains code to move to the previous card
		pass
