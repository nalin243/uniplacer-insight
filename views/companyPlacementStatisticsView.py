from views.companyPlacementStatisticsView_UI import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow


class CompanyPlacementStatisticsView(Ui_MainWindow, QMainWindow):

    def __init__(self, controller, viewmodel):
        super().__init__()

        self.setupUi(self)

        self.controller = controller
        self.viewmodel = viewmodel

        
