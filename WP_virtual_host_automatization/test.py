from PyQt5 import QtWidgets, QtGui, uic
 
import sys
 


app = QtWidgets.QApplication([])

QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Light.ttf")
QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Regular.ttf")
QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Bold.ttf")
QtGui.QFontDatabase.addApplicationFont("assets/fonts/Lato/Lato-Hairline.ttf")

win = uic.loadUi("GUI.ui")
win.show()
 
sys.exit(app.exec())
