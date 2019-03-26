import os
import sys

from PyQt5 import QtWidgets, QtGui


class Validation:

    @staticmethod
    def is_user_root():
        if os.geteuid() != 0:
            app = QtWidgets.QApplication([])
            error_dialog = QtWidgets.QErrorMessage()
            error_dialog.showMessage('Please, run the program as root!')
            app.exec_()
            sys.exit()

    @staticmethod
    def mandatory_text_field(elem):
        pass
