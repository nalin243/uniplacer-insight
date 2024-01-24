from PySide6.QtCore import QRunnable


class NormalizeWorker(QRunnable):


	def __init__(self,func,checkDb,setExcelFilePaths):
		super().__init__()

		self.fn = func
		self.checkDb = checkDb
		self.setExcelFilePaths = setExcelFilePaths

	def run(self):
		try:
			self.fn()
			if(self.checkDb()==0):
				self.setExcelFilePaths()

		except Exception as e:
			print(e,"normalizeworker")
			#This throws a type error when we click on the module card after uploading table
			#This only happens when we just uploaded the folder and does not happen after closing and reopening the application 
			#when the table is already present