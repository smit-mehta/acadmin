import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ttdetailsex import Startttdetailsex
from global_sql import *

class Starttimetableedit(QtGui.QWidget):

    def __init__(self, parent=None, flags = 1):
        QtGui.QWidget.__init__(self, parent)
        
        self.ttdetails = Startttdetailsex()
        
        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)
        cur.execute("select * from days")
        a = cur.fetchone()

        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        self.setPalette(palette2)

        self.setStyleSheet('color: rgb(85, 0, 0);')
        
        self.period = []
        self.timeslotslabel = []
        self.dayslabel = [QtGui.QLabel('     '), QtGui.QLabel('Monday'), QtGui.QLabel('Tuesday'), QtGui.QLabel('Wednesday'), QtGui.QLabel('Thursday'), QtGui.QLabel('Friday'), QtGui.QLabel('Saturday'), QtGui.QLabel('Sunday'), ]
        
        self.semcombobox = QtGui.QComboBox()
    
        self.setsem()
        mainvbox = QtGui.QVBoxLayout()
        self.mainhbox = QtGui.QHBoxLayout()
        self.setWindowTitle('Edit timetable')        
        self.dayslabelbox = QtGui.QVBoxLayout()
    
        self.loop4()
    
        self.mainhbox.addLayout(self.dayslabelbox)
            
        sembox = QtGui.QHBoxLayout()
        self.timebox = []
           
        self.semlabel = QtGui.QLabel("Semester   :")
        self.semlabel.setVisible(False)   
            
        self.semcombobox.setFixedSize(40, 30)
        self.semcombobox.setVisible(False)
        self.genlabel1 = QtGui.QLabel(" You must click save after making the changes")

        self.save = QtGui.QToolButton()
        self.save.setText('Save')
        
        self.editslot = QtGui.QToolButton()
        self.editslot.setText('Edit slots and days')
        
        
        sembox.addWidget(self.semlabel)
        sembox.addWidget(self.semcombobox)
        sembox.addWidget(self.genlabel1)
        sembox.addWidget(self.editslot)
        sembox.addWidget(self.save)
      
        
        self.loop3()
                
        self.loop1()
   
        self.settimetable()        
        
        mainvbox.addLayout(sembox)
   
        mainvbox.addLayout(self.mainhbox)
        
        self.setLayout(mainvbox)

        QtCore.QObject.connect(self.semcombobox, QtCore.SIGNAL("currentIndexChanged(int)"), self.loop2)
        QtCore.QObject.connect(self.save, QtCore.SIGNAL("clicked()"), self.saved)
        QtCore.QObject.connect(self.editslot, QtCore.SIGNAL("clicked()"), self.editsloted)
        
        self.save.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.editslot.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')

        
    def editsloted(self):
        
        self.ttdetails.show()
        QtCore.QObject.connect(self.ttdetails.done, QtCore.SIGNAL("clicked()"), self.close)
        
    
    def loop4(self):
        cur.execute("select * from days")
        a = cur.fetchone()
        d = 0
        if a[0]==0:
            d = 6
        if a[0]==1:
            d = 7
        if a[0]==2:
            d = 8
        
        i = 0;
        
        while(i<d):
            self.dayslabel[i].setFixedSize(90, 30)
            self.dayslabelbox.addWidget(self.dayslabel[i])
            i = i+1
        
    def loop3(self):
        cur.execute("select * from timeslots")

        i = 0
        for row in cur:
            self.timeslotslabel.append(QtGui.QLabel('          '+row[0]+'          '))
            self.timeslotslabel[i].setFixedSize(90, 30)
            self.timebox.append(QtGui.QVBoxLayout())
            self.timebox[i].addWidget(self.timeslotslabel[i])
            i = i+1
        
    def loop2(self):
        
        a = self.countdays()
        
        m = 0
        
        cur.execute("select * from timeslots")
        
        for row in cur:
            m = m+1
        
        
        k = 0;
        i = 0;
        
        while k<m:
            i = 0
            while(i<a):
                self.setsub(k, i)
                i = i+1
            k = k+1
        
        self.settimetable()
        
        
        
    def loop1(self):
        
        a = self.countdays()
        
        k = 0
        m = 0
        
        cur.execute("select * from timeslots")
        
        for row in cur:
            m = m+1
        
        while k<m:
            
            self.period.append([])
            i = 0
            while i<a:
            
                self.period[k].append(QtGui.QComboBox())
                self.period[k][i].setFixedSize(90, 30)
                self.setsub(k, i)
                i = i+1
            k = k+1
            
        cur.execute("select * from timeslots")
 
        k = 0
        i = 0
        
        for row in cur:
            i = 0
            while (i<a):
                self.timebox[k].addWidget(self.period[k][i])
                i = i+1
            k = k+1
            
        cur.execute("select * from timeslots")
        
        k = 0;
        
        for row in cur:
            self.mainhbox.addLayout(self.timebox[k])
            k = k+1
    
    def setsub(self, k, i):
        
        self.period[k][i].clear()
        c = (int(self.semcombobox.currentText()), )
        
        cur.execute("select subjectcode from acads where semester = ?", c)
        a = cur.fetchall()
        b = ['', ]
        
        for sublist in a:
            b.append(str(sublist[0]))
        
        self.period[k][i].addItems(b)
            
    def setsem(self):
        
        cur.execute("select distinct semester from acads")
        a = cur.fetchall()
        
        b = []
        
        for sublist in a:
            b.append(str(sublist[0]))
            
        self.semcombobox.clear()
        self.semcombobox.addItems(b)

        cur.execute("select * from defsem")
        a = cur.fetchone()

        if a!=None:
            self.semcombobox.setCurrentIndex(self.semcombobox.findText(str(a[0])))

        
    def countdays(self):
        
        cur.execute("select * from days")
        a = cur.fetchone()
        
        if a[0]==0:
            return 5
        if a[0]==1:
            return 6
        return 7
        
    def saved(self):
        
        t = (int(self.semcombobox.currentText()), )
        
        cur.execute("delete from timetable where semester = ?", t)
        con.commit()
        
        
        a = self.countdays()
        
        k = 0
        m = 0
        
        cur.execute("select * from timeslots")
        
        for row in cur:
            m = m+1
        
        while k<m:
            i = 0
            while i<a:
                t = (i, k, str(self.period[k][i].currentText()), int(self.semcombobox.currentText()), )
                cur.execute("insert into timetable values(?, ?, ?, ?)", t)
                con.commit()
                i = i+1
            k = k+1
        
        
        self.close()

    def settimetable(self):
        
        a = (int(self.semcombobox.currentText()), )
        
        cur.execute("select * from timetable where semester = ?", a)
        
        for row in cur:
            
            k = int(row[1])
            i = int(row[0])
            idx = self.period[k][i].findText(str(row[2]))
            self.period[k][i].setCurrentIndex(idx)
            

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  panel = Starttimetableedit()
  panel.show()
  sys.exit(app.exec_())
