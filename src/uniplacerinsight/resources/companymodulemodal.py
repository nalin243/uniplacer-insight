from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt,QSize,QRect
from PySide6.QtWidgets import QTableView,QDialog

import pandas as pd

from uniplacerinsight.models.tablemodel import TableModel

class DataTable(QDialog):
    def __init__(self,viewmodel,parent=None):
        super().__init__(parent)

        self.setWindowTitle("List of Companies")

        self.tableview = QTableView(self)

        self.viewmodel = viewmodel

        self.tableview.setGeometry(QRect(0,0,750,600))
        self.tableview.setWindowFlags(Qt.WindowStaysOnTopHint)

    def exec(self):

        self.tableview.setModel(self.viewmodel.getTableData())
        self.tableview.resizeColumnsToContents()

        for row in range(0,self.viewmodel.getTableData().rowCount()):
            self.tableview.setRowHeight(row,50)

        widgetWidth = self.tableview.columnWidth(0) + self.tableview.columnWidth(1)

        totalRowHeight = 0
        if(self.viewmodel.getTableData().rowCount()<18 and self.viewmodel.getTableData().rowCount()>2):
            for row in range(0,self.viewmodel.getTableData().rowCount()):
                totalRowHeight = totalRowHeight + self.tableview.rowHeight(row)

            self.tableview.setGeometry(QRect(0,0,widgetWidth+50,totalRowHeight+5))
            self.setMinimumSize(QSize(widgetWidth+50,totalRowHeight+5))
            self.setMaximumSize(QSize(widgetWidth+50,totalRowHeight+5))
        elif(self.viewmodel.getTableData().rowCount()<2):
            for row in range(0,self.viewmodel.getTableData().rowCount()):
                totalRowHeight = totalRowHeight + self.tableview.rowHeight(row)

            self.tableview.setGeometry(QRect(0,0,widgetWidth+50,totalRowHeight+50))
            self.setMinimumSize(QSize(widgetWidth+50,totalRowHeight+50))
            self.setMaximumSize(QSize(widgetWidth+50,totalRowHeight+50))
        else:
            self.tableview.setGeometry(QRect(0,0,widgetWidth+50,600))
            self.setMinimumSize(QSize(widgetWidth+50,600))
            self.setMaximumSize(QSize(widgetWidth+50,600))


        return super().exec()
