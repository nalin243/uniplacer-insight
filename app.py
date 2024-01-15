from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication

from views.landingPageView import LandingPage
from views.studentPlacementStatView import StudentPlacementStatPage

class Application(QApplication):

	__currentPage = 0

	def __init__(self):
		super(Application,self).__init__([])

		self.landingpage = LandingPage(self)
		self.studentplacementstatpage = StudentPlacementStatPage(self)

		# self.landingpage.show()
		# self.studentplacementstatpage.show()

		self.exec()

app = Application()