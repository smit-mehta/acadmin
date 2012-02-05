# For setting the 'default sem' tab.

import sys
from PyQt4 import QtCore, QtGui
from defaultsem import Ui_Dialog
from global_sql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *



class Startdefaultsem(QtGui.QDialog):
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)
        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))


        self.setPalette(palette2)
        self.setStyleSheet('color: rgb(85, 0, 0);')
        self.ui.okay.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        
        self.setsem()
        QtCore.QObject.connect(self.ui.okay, QtCore.SIGNAL("clicked()"), self.okayed)

	# Setting the selected sem as default sem.	
	
    def okayed(self):
        cur.execute("delete from defsem")
        cur.execute("insert into defsem values(?)", (int(self.ui.sem.currentText()), ))
        con.commit()
        self.close()
        
    # Setting the already saved semester into the options.
    
    def setsem(self):
        cur.execute("select distinct semester from acads")
        a = cur.fetchall()
        
        b = []
        
        for sublist in a:
            b.append(str(sublist[0]))
            
        self.ui.sem.clear()
        self.ui.sem.addItems(b)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startdefaultsem()
    myapp.show()
    sys.exit(app.exec_())
