from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QPen,QFont,QColor,QMovie
from PySide6.QtWidgets import QApplication,QMainWindow,QWidget,QLabel,QGraphicsScene
from PySide6.QtCore import QRect,QSize,QPropertyAnimation

import images

# class LoadingBarInnerBox(QWidget):

# 	def __init__(self,parent=None):
# 		super().__init__(parent)

# 		self.displayLabel = QLabel(self)
# 		self.setMaximumSize(QSize(40,35))

# 		self.canvas = QtGui.QPixmap(40,35)

# 		pen = QPen()
# 		pen.setWidth(5)

# 		self.painter = QtGui.QPainter(self.canvas)

# 		self.painter.setPen(pen)

# 		self.painter.fillRect(0,0,40,35,QColor("black"))

# 		self.painter.end()

# 		self.displayLabel.setPixmap(self.canvas)


class LoadingAnimationDialog(QMainWindow):

	def __init__(self,parent=None):

		super().__init__(parent)

		# loadingbarinnerbox = LoadingBarInnerBox(self)
		# loadingbarinnerbox.setGeometry(QRect(30,35,390,35))

		# self.moveAcrossAnimation = QPropertyAnimation(loadingbarinnerbox,b"geometry")
		# self.moveAcrossAnimation.setDuration(950)
		# self.moveAcrossAnimation.setStartValue(QRect(30, 35, 390, 35))
		# self.moveAcrossAnimation.setEndValue(QRect(379, 35, 390, 35))
		# self.moveAcrossAnimation.setLoopCount(50)
		
		self.displayLabel = QLabel(self)
		self.displayLabel.setGeometry(QRect(0,0,350,100))
		self.setWindowFlag(Qt.FramelessWindowHint)
		self.setAttribute(Qt.WA_TranslucentBackground,True)
		self.setWindowModality(Qt.WindowModal)

		movie = QMovie(":/icons/loading-animation.gif")
		self.displayLabel.setMovie(movie)
		movie.start()

		# self.canvas = QtGui.QPixmap(450,120)
		# self.setCentralWidget(self.displayLabel)

		# self.displayLabel.setPixmap(self.canvas)

		# pen = QPen()
		# pen.setWidth(5)

		# self.painter = QtGui.QPainter(self.canvas)

		# self.painter.setPen(pen)

		# self.painter.drawRect(30,35,390,35)
		# self.painter.end()

		# self.displayLabel.setPixmap(self.canvas)
		# self.moveAcrossAnimation.start()


	def show(self):


		return super().show()