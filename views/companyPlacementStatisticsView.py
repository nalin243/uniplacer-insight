from views.companyPlacementStatisticsView_UI import Ui_MainWindow

from PySide6.QtWidgets import QMainWindow,QGraphicsView
from PySide6.QtCharts import QCategoryAxis, QLineSeries,QSplineSeries, QPieSeries,QChart,QPieSlice,QLegend,QBarSeries,QBarSet,QBarCategoryAxis,QValueAxis,QChartView
from PySide6.QtCore import QPoint, Qt,QEasingCurve
from PySide6.QtGui import QCloseEvent, QPainter,QColor,QFont,QPen

import functools



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

        self.visitedData = [['Visited', self.viewmodel.totalVisited],['Not Visited', self.viewmodel.totalNotVisited]]
        self.hiredData = [['Hired',self.viewmodel.companiesHired],['Not Hired',self.viewmodel.companiesNotHired]]
        self.initPieChart(self.visitedData,self.hiredData)

        self.controller.updateBarAndLineChartValues(self.batchFilter)
        (sectorsHired,barChartYaxisRange,sectors) = self.viewmodel.getBarChartData()
        # self.initBarChart(sectorsHired,sectors,barChartYaxisRange)
        (months,companiesArriving) = self.viewmodel.getLineChartData()
        self.initLineChart(months,companiesArriving)

        super().show()

    def initLineChart(self,months,companiesArriving):

        self.lineChart = QChart()
        self.lineGraphView.setChart(self.lineChart)

        axis_x = QCategoryAxis()
        axis_y = QValueAxis()

        axis_y.setRange(0,max(companiesArriving)+1)

        series = QLineSeries()
        series.setPointsVisible(True)
        series.setPointLabelsVisible(True)
        series.setPointLabelsFormat("@yPoint")
        series.setPointLabelsFont(QFont("Serif", 10, QFont.Medium))

        series.setName("Companies Visiting")

        for index,month in enumerate(months):
            axis_x.append(month,index)

        for index,amount in enumerate(companiesArriving):
            series.append(QPoint(index,amount))

        self.lineChart.addAxis(axis_y,Qt.AlignLeft)

        self.lineChart.addSeries(series)
        series.attachAxis(axis_y)

        self.lineChart.setAxisX(axis_x,series)
        self.lineChart.legend().setVisible(True)
        # self.lineChart.addAxis(axis_x,Qt.AlignBottom)



    # def initBarChart(self,sectorsHired=[],categories=[],barChartYaxisRange=0):
    #     self.barChart = QChart()
    #     self.barGraphView.setChart(self.barChart)
    #     self.sectorsHired = None 

    #     self.axis_x =  QBarCategoryAxis()
    #     self.axis_x.setLabelsFont(QFont("Serif", 10, QFont.Bold))
    #     self.axis_x.setTitleFont(QFont("Serif", 12, QFont.Bold))
    #     self.axis_x.setTitleVisible(True)
    #     self.axis_x.setTitleText("Job Sectors")

    #     self.axis_y = QValueAxis()
    #     self.axis_y.setTitleVisible(True)
    #     self.axis_y.setTitleFont(QFont("Serif", 12, QFont.Bold))
    #     self.axis_y.setLabelsFont(QFont("Serif", 8, QFont.Bold))
    #     self.axis_y.setTitleText("Hired Students")

    #     self.sectorsHired = QBarSet("Hired")

    #     self.sectorsHired.append(sectorsHired)

    #     self.series = QBarSeries()

    #     self.series.hovered.connect(self.barHovered)

    #     self.series.append(self.sectorsHired)

    #     self.barChart.addSeries(self.series)
    #     self.barChart.setAnimationOptions(QChart.SeriesAnimations)

    #     self.categories = categories

    #     self.axis_x.append(self.categories)

    #     self.barChart.addAxis(self.axis_x,Qt.AlignBottom)
    #     self.series.attachAxis(self.axis_x)

    #     self.axis_y.setRange(0,barChartYaxisRange)

    #     self.barChart.addAxis(self.axis_y,Qt.AlignLeft)
    #     self.series.attachAxis(self.axis_y)

    #     self.barChart.legend().setVisible(True)
    #     self.barChart.legend().setAlignment(Qt.AlignTop)

    # def barHovered(self, status, index, barset):
    #     if status:
    #         self.series.setLabelsVisible(True)
    #     else:
    #         self.series.setLabelsVisible(False)

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
        (sectorsHired,barChartYaxisRange,sectors) = self.viewmodel.getBarChartData()
        # self.initBarChart(sectorsHired,sectors,barChartYaxisRange)

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

        self.visitedData = [['Visited', self.viewmodel.totalVisited],['Not Visited', self.viewmodel.totalNotVisited]]
        self.hiredData = [['Hired',self.viewmodel.companiesHired],['Not Hired',self.viewmodel.companiesNotHired]]
        self.initPieChart(self.visitedData,self.hiredData)