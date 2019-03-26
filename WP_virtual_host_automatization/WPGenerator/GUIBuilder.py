import os.path
import sys

from PyQt5 import QtWidgets, QtGui, uic


class GUIBuilder:

    def __init__(self):
        self.app = QtWidgets.QApplication([])

        QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Light.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Regular.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Bold.ttf")
        QtGui.QFontDatabase.addApplicationFont("assets/fonts/Lato/Lato-Hairline.ttf")

        self.win = uic.loadUi('GUI.ui')
        self.win.show()

    def show_window(self):
        sys.exit(self.app.exec())
