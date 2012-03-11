# For implemention of 'about' tab.
# Displays information about the app.

import sys
from PyQt4 import QtCore, QtGui
from about import Ui_Dialog
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Startabout(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)

        self.setPalette(palette2)
        self.setStyleSheet('color: rgb(85, 0, 0);')
        self.ui.close.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        

        b = QtGui.QPixmap("./pics/acadmin.png")
        self.ui.acadmin.setPixmap(QtGui.QPixmap(b))

        b = QtGui.QPixmap("./pics/shaastra.png")
        self.ui.shaastra.setPixmap(QtGui.QPixmap(b))

        QtCore.QObject.connect(self.ui.close, QtCore.SIGNAL("clicked()"), self.close)
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startabout()
    myapp.show()
    sys.exit(app.exec_())
