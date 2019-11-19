import sys

from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QIcon
from PyQt5.QtQml import QQmlApplicationEngine
from PyQt5.QtWidgets import QApplication


def run():
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load('PyQt5_example_qml.qml')
    app.setWindowIcon(QIcon('image.png'))

    if not engine.rootObjects():
        return -1

    return app.exec_()


if __name__ == "__main__":
    sys.exit(run())
