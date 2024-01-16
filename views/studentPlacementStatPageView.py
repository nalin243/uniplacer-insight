from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from views.studentPlacementStatPageView_UI import Ui_MainWindow


class StudentPlacementStatPageView(QMainWindow,Ui_MainWindow):

	def __init__(self,controller):
		super().__init__()

		self.setupUi(self)