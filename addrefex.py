import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from addref import Ui_window
from global_sql import *

class Startaddref(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_window()
        self.ui.setupUi(self)
        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)
        self.setPalette(palette2)

        QtCore.QObject.connect(self.ui.browse, QtCore.SIGNAL("clicked()"), self.browsed)
        QtCore.QObject.connect(self.ui.add, QtCore.SIGNAL("clicked()"), self.added)
    
        self.ui.browse.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.ui.add.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
    
    def browsed(self):
        fd = QtGui.QFileDialog(self)
        self.path = fd.getOpenFileName()
        self.ui.referencepath.setText(self.path)
        
    
    def added(self):
        if (self.ui.reference.text()=='') or (self.ui.referencepath.toPlainText()==''):
            self.showmessage()
        
        else :
            s = (str(self.ui.subjectcode.text()), str(self.ui.reference.text()), str(self.path), )
        
            cur.execute("insert into referencess values (?, ?, ?)", s)
            con.commit()
            self.close()
   
    def showmessage(self):
        message = QtGui.QMessageBox(self)
        message.setText('Either of reference title or reference path is not filled')
        message.setWindowTitle('acadmin Error')
        message.setIcon(QtGui.QMessageBox.Critical)
        message.exec_()

               
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startaddref()
    myapp.show()
    sys.exit(app.exec_())
