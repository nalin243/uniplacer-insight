from PySide6 import QtWidgets
from PySide6.QtWidgets import QWidget,QApplication
from PySide6.QtCore import QPropertyAnimation,QRect,Qt


class CardOutLineWidget(QWidget):

	def __init__(self,parent=None):

		super(CardOutLineWidget,self).__init__(parent)

		self.enterAnimation = QPropertyAnimation(self,b"geometry")
		self.enterAnimation.setDuration(50)
		self.enterAnimation.setStartValue(QRect(468, 62, 334, 404))
		self.enterAnimation.setEndValue(QRect(468, 51, 334, 404))

		self.leaveAnimation = QPropertyAnimation(self,b"geometry")
		self.leaveAnimation.setDuration(50)
		self.leaveAnimation.setStartValue(QRect(468, 51, 334, 404))
		self.leaveAnimation.setEndValue(QRect(468, 62, 334, 404))


	def enterEvent(self,event):
		self.enterAnimation.start()


	def leaveEvent(self,event):
		self.leaveAnimation.start()


