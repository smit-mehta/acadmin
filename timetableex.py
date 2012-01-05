import sys
from PyQt4 import QtCore, QtGui
from timetable import Ui_window
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from global_sql import *
from timetableex2 import Starttimetableedit
from ttdetailsex import Startttdetailsex


class Starttimetable(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_window()
        self.ui.setupUi(self)
        

        
        self.setedit = Starttimetableedit()
        self.ttdetails = Startttdetailsex()
        
        self.ui.sem.setVisible(False)
        self.setsem()
        self.setcolrow()
        self.settimetable()
        
        
        
        QtCore.QObject.connect(self.setedit.ttdetails.done, QtCore.SIGNAL("clicked()"), self.close)
        QtCore.QObject.connect(self.ui.sem, QtCore.SIGNAL("currentIndexChanged(int)"), self.settimetable)
        QtCore.QObject.connect(self.ui.edit, QtCore.SIGNAL("clicked()"), self.setedited)

        self.ui.edit.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        
        
    def setedited(self):
        
        self.setedit.show()
        QtCore.QObject.connect(self.setedit.save, QtCore.SIGNAL("clicked()"), self.settimetable)
    
        
    def settimetable(self):
        
        i=0
        
        
        while i<=self.row:
            k=0
            while k<=self.col:
                
                item = QtGui.QTableWidgetItem()
                self.ui.tt.setItem(i, k, item)    
                self.ui.tt.item(i, k).setText('')
                k = k+1
            i = i+1
            
        a = (int(self.ui.sem.currentText()), )
        cur.execute("select * from timetable where semester = ?", a)
        
        for row in cur:
            
            k = int(row[1])
            i = int(row[0])
            item = QtGui.QTableWidgetItem()
            self.ui.tt.setItem(i, k, item)    
            self.ui.tt.item(i, k).setText(row[2])
        
        
    
    def setcolrow(self):
        self.dayslabel = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', ]

        cur.execute("select max(day) from timetable")
        a = cur.fetchone()
        
        self.row = a[0]
        
        
        self.ui.tt.setRowCount(a[0]+1)        
        
        k = 0
        while k<(a[0]+1):
            item = QtGui.QTableWidgetItem()
            self.ui.tt.setVerticalHeaderItem(k, item)    
            self.ui.tt.verticalHeaderItem(k).setText(self.dayslabel[k])        
            k = k+1
        

        cur.execute("select max(slot) from timetable")        
        a = cur.fetchone()
        
        self.col = a[0]
        self.ui.tt.setColumnCount(a[0]+1)
        
        cur.execute("select * from timeslots")
        
        k = 0
        for row in cur:
            item = QtGui.QTableWidgetItem()
            self.ui.tt.setHorizontalHeaderItem(k, item)    
            self.ui.tt.horizontalHeaderItem(k).setText(str(row[0]))        
            k = k+1
        

    def setsem(self):
        
        cur.execute("select distinct semester from acads")
        a = cur.fetchall()
        
        b = []
        
        for sublist in a:
            b.append(str(sublist[0]))
            
        self.ui.sem.clear()
        self.ui.sem.addItems(b)
        
        cur.execute("select * from defsem")
        a = cur.fetchone()


        if a!=None:
            self.ui.sem.setCurrentIndex(self.ui.sem.findText(str(a[0])))

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Starttimetable()
    myapp.show()
    sys.exit(app.exec_())
