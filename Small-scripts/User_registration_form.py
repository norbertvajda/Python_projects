import os.path
import sys

from PyQt5 import QtWidgets, QtGui, uic

app = QtWidgets.QApplication([])
win = uic.loadUi('User_registration_form.ui')


def validator():
    if len(win.le_username.text()) > 0 and \
       len(win.le_password.text()) > 0 and \
       len(win.le_password_2.text()) > 0:

        if win.le_password.text() != win.le_password_2.text():
            win.lbl_error.setText("Passwords don't match!")
        else:
            win.lbl_error.setText("")
            win.pb_registration.setEnabled(True)
    else:
        win.pb_registration.setEnabled(False)


win.le_username.textChanged.connect(validator)
win.le_password.textChanged.connect(validator)
win.le_password_2.textChanged.connect(validator)

win.show()
sys.exit(app.exec())
