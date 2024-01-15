from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from views.landingPageView_UI import Ui_MainWindow

class LandingPage(QMainWindow,Ui_MainWindow):

	def __init__(self,Application):
		super().__init__()
		self.setupUi(self)
		Application.currentPage = 9

		print(Application.currentPage)