

class LandingPageController():

	_currentCardIndex = 0

	def __init__(self,app):
		self.app = app

	def showModuleWindow(self,event):
		#contains code to show the module that has been clicked
		#this function can't change show or hide views by itself and has to call an application function to do so
		self.app.displayView(self._currentCardIndex)

	def setCurrentCardIndex(self, index):
		if index < 0 or index > 2:
			pass
		else:
			self._currentCardIndex = index


	def getCurrentCardIndex(self):
		return self._currentCardIndex