from PySide6.QtWidgets import QDialog,QLabel,QVBoxLayout,QDialogButtonBox

class DatabaseIncompleteModal(QDialog):

	def __init__(self,parent=None):
		super().__init__(parent)

		self.setWindowTitle("Incomplete Database")

		button = QDialogButtonBox.Ok

		self.buttonBox = QDialogButtonBox(button)

		self.buttonBox.accepted.connect(self.accept)

		self.layout = QVBoxLayout()
		message = QLabel("Please make sure all required files are present")

		self.layout.addWidget(message)
		self.layout.addWidget(self.buttonBox)
		self.setLayout(self.layout)