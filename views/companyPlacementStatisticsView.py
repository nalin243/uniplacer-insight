from views.companyPlacementStatisticsView_UI import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow


class CompanyPlacementStatisticsView(Ui_MainWindow, QMainWindow):

    def __init__(self, controller, viewmodel):
        super().__init__()

        self.setupUi(self)

        self.controller = controller
        self.viewmodel = viewmodel

        self.typeOfJobCombobox.currentTextChanged.connect(self.filterChanged)
        self.sectorCombobox.currentTextChanged.connect(self.filterChanged)
        self.ctcCombobox.currentTextChanged.connect(self.filterChanged)
        self.levelOfJobCombobox.currentTextChanged.connect(self.filterChanged)
        self.batchComboBox.currentTextChanged.connect(self.filterChanged)

    def closeEvent(self, event):
        self.controller.returnToLanding()
        return super().closeEvent(event)

    def show(self):

        self.jobTypeFilter = None if self.typeOfJobCombobox.currentText() == "All" else self.typeOfJobCombobox.currentText()
        self.jobSectorFilter = None if self.sectorCombobox.currentText() == "All" else self.sectorCombobox.currentText()
        self.ctcFilter = None if self.ctcCombobox.currentText() == "All" else self.ctcCombobox.currentText()
        self.companyLevelFilter = None if self.levelOfJobCombobox.currentText() == "All" else self.levelOfJobCombobox.currentText()
        self.batchFilter = None if self.batchComboBox.currentText() == "All" else self.batchComboBox.currentText()

        self.controller.changeFilter(self.jobTypeFilter, self.jobSectorFilter, self.ctcFilter, self.companyLevelFilter, self.batchFilter)

        self.totalCompaniesLabel.setText(str(self.viewmodel.getCompanyAggregates()[0]))
        self.companiesVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[1]))
        self.companiesNotVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[2]))
        self.companiesHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[3]))
        self.companiesNotHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[4]))

        super().show()

    def filterChanged(self):

        self.jobTypeFilter = None if self.typeOfJobCombobox.currentText() == "All" else self.typeOfJobCombobox.currentText()
        self.jobSectorFilter = None if self.sectorCombobox.currentText() == "All" else self.sectorCombobox.currentText()
        self.ctcFilter = None if self.ctcCombobox.currentText() == "All" else self.ctcCombobox.currentText()
        self.companyLevelFilter = None if self.levelOfJobCombobox.currentText() == "All" else self.levelOfJobCombobox.currentText()
        self.batchFilter = None if self.batchComboBox.currentText() == "All" else self.batchComboBox.currentText()

        self.controller.changeFilter(self.jobTypeFilter, self.jobSectorFilter, self.ctcFilter, self.companyLevelFilter, self.batchFilter)

        self.totalCompaniesLabel.setText(str(self.viewmodel.getCompanyAggregates()[0]))
        self.companiesVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[1]))
        self.companiesNotVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[2]))
        self.companiesHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[3]))
        self.companiesNotHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[4]))