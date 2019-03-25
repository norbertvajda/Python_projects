from PyQt5 import QtWidgets, QtGui, uic
 
import sys
 
app = QtWidgets.QApplication([])

# get font family 
# _id = QtGui.QFontDatabase.addApplicationFont("assets/fonts/Lato/Lato-Light.ttf")
# print(QtGui.QFontDatabase.applicationFontFamilies(_id))

QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Light.ttf")
QtGui.QFontDatabase.addApplicationFont("assets/fonts/Quicksand/Quicksand-Regular.ttf")
QtGui.QFontDatabase.addApplicationFont("assets/fonts/Lato/Lato-Hairline.ttf")

win = uic.loadUi("GUI.ui") #specify the location of your .ui file

#win.gb_url.setStyleSheet("QGroupBox { background-color: rgb(255, 255,\
#255); border:1px solid rgb(255, 170, 255); }")

win.gb_lang.setStyleSheet("QGroupBox { background-color: rgb(255, 255, 255); \
border:1px solid rgb(255, 170, 255); \
border-radius: 5px; font: 12pt 'Quicksand'; }")

#win.gb_url.setStyleSheet("QGroupBox {background-color: white;}")
#win.gb_db.setStyleSheet("QGroupBox {background-color: white;}")
#win.gb_pw_setting.setStyleSheet("QGroupBox {background-color: white;}")
# ==================================================================================
label = win.lbl_db_name
label.setStyleSheet('font: 18pt "Lato Hairline";')
# label.setStyleSheet('font: 18pt "Quicksand Light";')
# label.setStyleSheet('font: 18pt "Quicksand";')
# ==================================================================================
 
win.show()
 
sys.exit(app.exec())
