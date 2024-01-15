from PySide6 import QtWidgets
from PySide6.QtWidgets import QMainWindow

from views.studentPlacementStatView_UI import Ui_MainWindow


class StudentPlacementStatPage(QMainWindow,Ui_MainWindow):

	def __init__(self,Application):
		super().__init__()

		self.setupUi(self)