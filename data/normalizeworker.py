from PySide6.QtCore import QRunnable, Slot


class NormalizeWorker(QRunnable):


	def __init__(self,func,tableExists,setExcelFilePaths,app):
		super().__init__()

		self.fn = func
		self.app = app
		self.tableExists = tableExists
		self.setExcelFilePaths = setExcelFilePaths

	@Slot()
	def run(self):
		try:
			self.fn()
			if(self.tableExists()):
				self.setExcelFilePaths()

		except Exception as e:
			pass
			# print(e.__class__.__name__)
			#This throws a type error when we click on the module card after uploading table
			#This only happens when we just uploaded the folder and does not happen after closing and reopening the application 
			#when the table is already present