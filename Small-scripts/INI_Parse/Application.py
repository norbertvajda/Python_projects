import configparser
import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.config = configparser.ConfigParser()
        self.config.read('settings.ini')

        self.title = 'Config parser'

        self.left = int(self.config['program'].get('x'))
        self.top = int(self.config['program'].get('y'))
        self.height = int(self.config['program'].get('height'))
        self.width = int(self.config['program'].get('width'))

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.statusBar().showMessage('This is a test')
        self.show()

    def closeEvent(self, a0: QtGui.QCloseEvent) -> None:
        self.config['program']['x'] = str(self.geometry().x())
        self.config['program']['y'] = str(self.geometry().y())
        self.config['program']['height'] = str(self.geometry().height())
        self.config['program']['width'] = str(self.geometry().width())

        with open('settings.ini', 'w') as configfile:  # save
            self.config.write(configfile)

        a0.accept()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(application.exec_())
