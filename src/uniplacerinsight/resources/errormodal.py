from PySide6.QtWidgets import QDialog,QLabel,QVBoxLayout,QDialogButtonBox

class ErrorModal(QDialog):

	def __init__(self,parent=None):
		super().__init__(parent)

		self.windowtitle = ""
		self.messageText = ""

		self.setWindowTitle(self.windowtitle)

		button = QDialogButtonBox.Ok

		self.buttonBox = QDialogButtonBox(button)

		self.buttonBox.accepted.connect(self.accept)

		self.layout = QVBoxLayout()
		
		self.message = QLabel(self.messageText)

		self.layout.addWidget(self.message)
		self.layout.addWidget(self.buttonBox)

		self.setLayout(self.layout)

	def exec(self):
		self.message.setText(self.messageText)

		return super().exec()
		

	def setWindowTitleText(self,title):
		self.setWindowTitle(title) 

	def setErrorText(self,text):
		self.messageText = text
