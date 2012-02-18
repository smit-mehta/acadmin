# Setting the grades and their numeric equivalence.

import sys
from PyQt4 import QtCore, QtGui
from grade import Ui_Dialog
from global_sql import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *


class Startgrade(QtGui.QDialog):
    grade = ()
    num = ()
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

        
        self.grade = (self.ui.grade1, self.ui.grade2, self.ui.grade3, self.ui.grade4, self.ui.grade5, self.ui.grade6, self.ui.grade7, self.ui.grade8, )
        self.num = (self.ui.num1, self.ui.num2, self.ui.num3, self.ui.num4, self.ui.num5, self.ui.num6, self.ui.num7, self.ui.num8, )
        
        self.setall()        
        
        
        QtCore.QObject.connect(self.ui.done, QtCore.SIGNAL("clicked()"), self.doned)
        
    # Saving the new grade format.

    def doned(self):
        
        cur.execute("update acads set grade = ?", (None, ))
        con.commit()
        
        cur.execute("delete from grades")
        con.commit()
        
        self.close()
        
        i = 0
        
        while(i<8):
            if self.grade[i].text()!='':
                t = (str(self.grade[i].text()), self.num[i].value(), )
                cur.execute("insert into grades values(?, ?)", t)
                con.commit()
            i = i+1
 
        cur.execute("select * from grades")
        a = cur.fetchone()
        
    # Showing the grade scheme already in the database.

    def setall(self):
        
        i=0
        while(i<8):
            self.grade[i].clear()
            self.num[i].setValue(0)
            i = i+1
        cur.execute("select * from grades")
        a = cur.fetchall()
               
        i=0
        
        cur.execute("select * from grades")
        
        for row in cur:
            self.grade[i].setText(row[0])
            self.num[i].setValue(row[1])
            i = i+1
            
        
        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startgrade()
    myapp.show()
    sys.exit(app.exec_())
