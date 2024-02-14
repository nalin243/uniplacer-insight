from views.companyPlacementStatisticsView_UI import Ui_MainWindow
from resources.companymodulemodal import DataTable
from resources.companyhiredtablemodal import HiredDataTable

from PySide6.QtWidgets import QMainWindow,QGraphicsView
from PySide6.QtCharts import QCategoryAxis, QLineSeries,QHorizontalBarSeries,QSplineSeries,QPieSeries,QChart,QPieSlice,QLegend,QBarSeries,QBarSet,QBarCategoryAxis,QValueAxis,QChartView
from PySide6.QtCore import QPoint, Qt,QEasingCurve,QPointF
from PySide6.QtGui import QCloseEvent, QPainter,QColor,QFont,QPen

import functools



class CompanyPlacementStatisticsView(Ui_MainWindow, QMainWindow):

    def __init__(self, controller, viewmodel):
        super().__init__()

        self.setupUi(self)

        self.controller = controller
        self.viewmodel = viewmodel

        self.companymodulemodal = DataTable(self.viewmodel,self.centralwidget)
        self.companyhiredtablemodal = HiredDataTable(self.viewmodel, self.centralwidget)

        self.tableButton.mousePressEvent = self.showTableViewModal
        self.hiredTableButton.mousePressEvent = self.showHiredTableViewModal

        self.typeOfJobCombobox.currentTextChanged.connect(self.filterChanged)
        self.sectorCombobox.currentTextChanged.connect(self.filterChanged)
        self.ctcCombobox.currentTextChanged.connect(self.filterChanged)
        self.levelOfJobCombobox.currentTextChanged.connect(self.filterChanged)
        self.batchComboBox.currentTextChanged.connect(self.filterChanged)

        self.batchComboBox.currentTextChanged.connect(self.barAndLineChartFiltersChanged)

    def closeEvent(self, event):
        self.controller.returnToLanding()
        return super().closeEvent(event)

    def show(self):

        self.jobTypeFilter = None if self.typeOfJobCombobox.currentText() == "Job Type(All)" else self.typeOfJobCombobox.currentText()
        self.jobSectorFilter = None if self.sectorCombobox.currentText() == "Job Sector(All)" else self.sectorCombobox.currentText()
        self.ctcFilter = None if self.ctcCombobox.currentText() == "CTC Range(All)" else self.ctcCombobox.currentText()
        self.companyLevelFilter = None if self.levelOfJobCombobox.currentText() == "Job Level(All)" else self.levelOfJobCombobox.currentText()
        self.batchFilter = None if self.batchComboBox.currentText() == "All" else self.batchComboBox.currentText()

        self.controller.changeFilter(self.jobTypeFilter, self.jobSectorFilter, self.ctcFilter, self.companyLevelFilter, self.batchFilter)

        self.totalCompaniesLabel.setText(str(self.viewmodel.getCompanyAggregates()[0]))
        self.companiesVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[1]))
        self.companiesNotVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[2]))
        self.companiesHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[3]))
        self.companiesNotHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[4]))

        self.visitedData = [['Visited', self.viewmodel.totalVisited],['Not Visited', self.viewmodel.totalNotVisited]]
        self.hiredData = [['Hired',self.viewmodel.companiesHired],['Not Hired',self.viewmodel.companiesNotHired]]
        self.initPieChart(self.visitedData,self.hiredData)

        self.controller.updateBarAndLineChartValues(self.batchFilter)
        (lpaRanges,companiesInRange) = self.viewmodel.getBarChartData()
        self.initBarChart(lpaRanges,companiesInRange)
        (months,companiesArriving) = self.viewmodel.getLineChartData()
        self.initLineChart(months,companiesArriving,self.batchFilter)

        self.viewmodel.setTableData(self.jobTypeFilter,self.jobSectorFilter,self.ctcFilter,self.companyLevelFilter, self.batchFilter)

        super().show()

    def showTableViewModal(self, event):
        self.companymodulemodal.exec()

    def showHiredTableViewModal(self, event):
        self.companyhiredtablemodal.exec()

    def initLineChart(self,months,companiesArriving,batchFilter):

        self.lineChart = QChart()
        self.lineChart.setAnimationOptions(QChart.AllAnimations)
        self.lineChart.setAnimationDuration(2000)

        self.lineGraphView.setChart(self.lineChart)

        axis_x = QCategoryAxis()
        axis_y = QValueAxis()

        axis_x.setTitleText("Months")
        axis_y.setTitleText("Number of Visits")

        axis_y.setRange(0,max(companiesArriving)+1)
        axis_y.setLabelFormat("%d")

        series = QLineSeries()
        series.setPointsVisible(True)
        series.setPointLabelsVisible(True)
        series.setPointLabelsFormat("@yPoint")
        series.setPointLabelsFont(QFont("Serif", 12, QFont.Medium))

        series.setName("Companies Visiting in {}-{}".format(int(batchFilter)-1,int(batchFilter)))
        axis_x.setRange(0, (len(months)*10))

        #do this so we can put dot in middle of the month grid
        for index,month in enumerate(months):
            axis_x.append(month,(index+1)*10)

        for index,amount in enumerate(companiesArriving):
            series.append(QPoint(((index+1)*10)-5,amount))

        self.lineChart.addAxis(axis_y,Qt.AlignLeft)

        self.lineChart.addSeries(series)
        series.attachAxis(axis_y)

        self.lineChart.setAxisX(axis_x,series)
        self.lineChart.legend().setVisible(True)



    def initBarChart(self,lpaRanges,companiesInRange):
        self.barChart = QChart()
        self.barGraphView.setChart(self.barChart)
        self.sectorsHired = None 

        axis_y =  QBarCategoryAxis()
        axis_y.setLabelsFont(QFont("Serif", 10, QFont.Bold))
        axis_y.setTitleFont(QFont("Serif", 12, QFont.Bold))
        axis_y.setTitleVisible(True)
        axis_y.setTitleText("Lpa Ranges")

        axis_x = QValueAxis()
        axis_x.setTitleVisible(True)
        axis_x.setTitleFont(QFont("Serif", 12, QFont.Bold))
        axis_x.setLabelsFont(QFont("Serif", 8, QFont.Bold))
        axis_x.setTitleText("Number of Companies")
        axis_x.setLabelFormat("%d")

        self.companiesInRange = QBarSet("Companies Hired")
        self.companiesInRange.setColor(QColor("#4e79a7"))

        self.companiesInRange.append(companiesInRange)

        self.series = QHorizontalBarSeries()

        self.series.hovered.connect(self.barHovered)

        self.series.append(self.companiesInRange)

        self.barChart.addSeries(self.series)
        self.barChart.setAnimationOptions(QChart.AllAnimations)

        axis_y.append(lpaRanges)
        self.barChart.addAxis(axis_y,Qt.AlignLeft)
        self.series.attachAxis(axis_y)

        axis_x.setRange(0,max(companiesInRange)+2)

        self.barChart.addAxis(axis_x,Qt.AlignBottom)
        self.series.attachAxis(axis_x)

        self.barChart.legend().setVisible(True)
        self.barChart.legend().setAlignment(Qt.AlignTop)

    def barHovered(self, status, index, barset):
        if status:
            self.series.setLabelsVisible(True)
        else:
            self.series.setLabelsVisible(False)

    def initPieChart(self,visitedData,hiredData):

        self.pieChart.removeAllSeries()
        self.pieChart.setAnimationOptions(QChart.SeriesAnimations)
        self.pieChart.setAnimationEasingCurve(QEasingCurve.OutQuint)
        self.pieChart.setAnimationDuration(2000)

        self.outerSeries = QPieSeries()
        self.outerSeries.setHoleSize(0.05)
        # self.outerSeries.setPieSize(0.71)

        self.innerSeries = QPieSeries()
        self.innerSeries.setHoleSize(0.50)
        self.innerSeries.setPieSize(0.70)

        self.sliceshovered = []

        self.outerColors = ["#2ecc71","#e67e22"]
        self.innerColors = ["#3498db","#808080"]

        for self.item in visitedData:
            self.outerSeries.append(QPieSlice(self.item[0],self.item[1]))

        for self.item in hiredData:
            self.innerSeries.append(QPieSlice(self.item[0],self.item[1]))

        for index,self.slice in enumerate(self.outerSeries.slices()):

            self.color = QColor(self.outerColors[index])

            if(self.slice.label() == "Visited"):
                self.innerSeries.setPieEndAngle(self.slice.percentage()*360)
                self.slice.setLabelPosition(QPieSlice.LabelInsideNormal)
                self.slice.setLabel("{:.0f}%".format(round(self.slice.percentage()*100),2))
                self.slice.setLabelBrush(QColor("#006400"))
                self.slice.setColor(self.color)
                self.slice.setLabelVisible(True)
                self.slice.setLabelFont(QFont("Serif", 13, QFont.Medium))
                continue

            self.slice.setLabel("{:.0f}%".format(round(self.slice.percentage()*100),2))
            self.slice.setLabelArmLengthFactor(0.05)
            self.slice.setLabelBrush(self.color)
            self.slice.setColor(self.color)
            self.slice.setBorderWidth(1)
            # self.color.setAlpha(100)
            self.slice.setBorderColor(QColor("black"))
            self.slice.setExplodeDistanceFactor(0.001)
            self.slice.setExploded(True)
            self.slice.setLabelVisible(True)
            self.slice.setLabelFont(QFont("Serif", 13, QFont.Medium))
            # self.slice.hovered.connect(functools.partial(self.pieSliceHovered,self.slice))

        for index,self.slice in enumerate(self.innerSeries.slices()):

            self.color = QColor(self.innerColors[index])
            self.slice.setLabel("{:.2f}%".format(round(self.slice.percentage()*100),2))
            self.slice.setLabelArmLengthFactor(0.05)
            self.slice.setLabelBrush(self.color)
            self.slice.setExploded(True)
            self.slice.setLabelVisible(True)
            self.slice.setExplodeDistanceFactor(0.001)
            self.slice.setLabelFont(QFont("Serif", 13, QFont.Medium))
            self.slice.setColor(self.color)
            self.slice.hovered.connect(functools.partial(self.pieSliceHovered,self.slice))

        self.pieChart.addSeries(self.outerSeries)
        self.pieChart.addSeries(self.innerSeries)
        
        self.pieChart.legend().setFont(QFont("Serif", 12, QFont.Normal))
        self.pieChart.legend().setMarkerShape(QLegend.MarkerShapeCircle)

        self.pieChart.legend().markers()[2].setLabel(self.hiredData[0][0])
        self.pieChart.legend().markers()[3].setLabel(self.hiredData[1][0])

        self.pieChart.legend().markers()[0].setLabel(self.visitedData[0][0])
        self.pieChart.legend().markers()[1].setLabel(self.visitedData[1][0])

        # self.pieChart.legend().markers()[2].setLabel(self.visitedData[2][0])


        self.pieChart.legend().setAlignment(Qt.AlignBottom)
        self.pieChartView.setRenderHint(QPainter.Antialiasing)

    def pieSliceHovered(self,pieSlice,state):
        self.pieChart.zoom(2.0)
        if(state):
            pieSlice.setExplodeDistanceFactor(0.1)
        else:
            pieSlice.setExplodeDistanceFactor(0.001)

    def barAndLineChartFiltersChanged(self):
        self.batchFilter = None if self.batchComboBox.currentText()=="All" else self.batchComboBox.currentText()

        self.controller.updateBarAndLineChartValues(self.batchFilter)
        (lpaRanges,companiesInRange) = self.viewmodel.getBarChartData()
        self.initBarChart(lpaRanges,companiesInRange)
        (months,companiesArriving) = self.viewmodel.getLineChartData()
        self.initLineChart(months,companiesArriving,self.batchFilter)

    def filterChanged(self):

        self.jobTypeFilter = None if self.typeOfJobCombobox.currentText() == "Job Type(All)" else self.typeOfJobCombobox.currentText()
        self.jobSectorFilter = None if self.sectorCombobox.currentText() == "Job Sector(All)" else self.sectorCombobox.currentText()
        self.ctcFilter = None if self.ctcCombobox.currentText() == "CTC Range(All)" else self.ctcCombobox.currentText()
        self.companyLevelFilter = None if self.levelOfJobCombobox.currentText() == "Job Level(All)" else self.levelOfJobCombobox.currentText()
        self.batchFilter = None if self.batchComboBox.currentText() == "All" else self.batchComboBox.currentText()

        self.controller.changeFilter(self.jobTypeFilter, self.jobSectorFilter, self.ctcFilter, self.companyLevelFilter, self.batchFilter)

        self.totalCompaniesLabel.setText(str(self.viewmodel.getCompanyAggregates()[0]))
        self.companiesVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[1]))
        self.companiesNotVisitedLabel.setText(str(self.viewmodel.getCompanyAggregates()[2]))
        self.companiesHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[3]))
        self.companiesNotHiredLabel.setText(str(self.viewmodel.getCompanyAggregates()[4]))

        self.visitedData = [['Visited', self.viewmodel.totalVisited],['Not Visited', self.viewmodel.totalNotVisited]]
        self.hiredData = [['Hired',self.viewmodel.companiesHired],['Not Hired',self.viewmodel.companiesNotHired]]
        self.initPieChart(self.visitedData,self.hiredData)
