from PySide6.QtCore import QAbstractTableModel,Qt

class TableModel(QAbstractTableModel):
    def __init__(self, data):
        super().__init__()
        self._data = data

    def updateData(self,newdata):
        self._data = newdata

    def data(self, index, role=0):
        if role == Qt.ItemDataRole.DisplayRole:
            #returns the text value to be presented in given row and column, for dataframe we are using iloc
            item = self._data.iloc[index.row(), index.column()]
            return str(item)

    def rowCount(self, parent=None):
        #returns the row count in current data
        return self._data.shape[0]

    def columnCount(self, parent=None):
        #returns column count in current data
        return self._data.shape[1]

    def headerData(self, section, orientation, role=0):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])
