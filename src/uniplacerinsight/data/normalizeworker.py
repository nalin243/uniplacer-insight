from PySide6.QtCore import QRunnable,Signal,QObject


class NormalizeWorker(QRunnable,QObject):

	startSignal = Signal(bool)
	endSignal = Signal(bool)


	def __init__(self,normalizeandpush,checkDb,setExcelFilePaths):
		super().__init__()
		QObject.__init__(self)

		self.normalizeandpush = normalizeandpush
		self.checkDb = checkDb
		self.setExcelFilePaths = setExcelFilePaths

	def run(self):
		self.startSignal.emit(True)
		try:
			self.normalizeandpush()
			self.endSignal.emit(True)			

		except Exception as e:
			print(e,"normalizeworker")
			#This throws a type error when we click on the module card after uploading table
			#This only happens when we just uploaded the folder and does not happen after closing and reopening the application 
			#when the table is already present