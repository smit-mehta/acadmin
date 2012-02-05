# For implementing the 'calendar' along with its ui.

import sys, random
from PyQt4 import QtCore, QtGui
from reminderex import Startaddreminder
from global_sql import *

class Startcalendar(QtGui.QWidget):
  
    def __init__(self, a, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
		# Setting the current semester		
		
        self.sem = a
        
        # UI
        
        self.setGeometry(300, 400, 350, 280)
        self.setWindowTitle('Calendar')

        self.a = calendar()
        self.a.setSelectionMode(1)
        
        self.scroll = QtGui.QScrollArea()
        self.bunkscroll = QtGui.QScrollArea()
        
        self.addtask = QtGui.QToolButton()
        self.addtask.setText("Add")
        hbox = QtGui.QHBoxLayout()
        hbox.addWidget(self.addtask)

        self.savebunk = QtGui.QToolButton()
        self.savebunk.setText("Save Bunks")
        
        hbox2 = QtGui.QHBoxLayout()
        hbox2.addWidget(self.bunkscroll)
        hbox2.addWidget(self.savebunk)

        self.dummybutton = QtGui.QToolButton()
                
        self.initial()
        self.setbunkclasses()
        self.settasks()

        hboxcal = QtGui.QHBoxLayout()
        sidelabel1 = QtGui.QLabel('                 ')
        sidelabel2 = QtGui.QLabel('                 ')

        hboxcal.addWidget(sidelabel1)
        hboxcal.addWidget(self.a)
        hboxcal.addWidget(sidelabel1)
        
        vbox = QtGui.QVBoxLayout()
        vbox.addLayout(hboxcal)
        vbox.addWidget(self.scroll)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)    

        self.savebunk.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.addtask.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')

		
		# Signals and slots		
		
        QtCore.QObject.connect(self.a, QtCore.SIGNAL("clicked(const QDate&)"), self.settasks)
        QtCore.QObject.connect(self.addtask, QtCore.SIGNAL("clicked()"), self.addtaskopen)        
        QtCore.QObject.connect(self.savebunk, QtCore.SIGNAL("clicked()"), self.savebunks)        

        
        self.setLayout(vbox)


	# Setting the ticks on bunks for the subject which is already there in the database.
        
    def setbunkticks(self):
        
        for i in self.tick:
            i.setChecked(False)

        date = self.a.selectedDate()
        
        day = date.day()
        month = date.month()
        year = date.year()
                
        t = (day, month, year, self.sem)

        cur.execute("select * from bunk where day = ? and month = ? and year = ? and semester = ?", t)
        
        for row in cur:
            for i in self.tick:
                if i.text()==row[0]:
                    i.setChecked(True)                        


	# Saving the bunks into the database.
        
    def savebunks(self):
        date = self.a.selectedDate()
        
        day = date.day()
        month = date.month()
        year = date.year()
                
        t = (day, month, year, self.sem)

                
        cur.execute("delete from bunk where day = ? and month = ? and year = ? and semester = ?", t)
        con.commit()
        
        
        for i in self.tick:
            if i.isChecked()==True:
                l = (str(i.text()), day, month, year, self.sem)
                cur.execute("insert into bunk values(?, ?, ?, ?, ?)", l)
                con.commit()

        self.setbunkintoacads()
    
    
    # Updating the number of bunks into the main database table to calculate the number of bunks left.
    
    def setbunkintoacads(self):
        cur.execute("select distinct subjectcode from bunk")
        a = cur.fetchall()
        
        for i in a:
            t = (i[0], self.sem, )
            cur.execute("select count(subjectcode) from bunk where subjectcode = ? and semester = ?", t)
            o = cur.fetchall()
            h = (o[0][0], i[0], self.sem, )
            cur.execute("update acads set bunksdone=? where subjectcode = ? and semester = ?", h)
            con.commit()

	# Calling the class for adding reminder.

    def initial(self):
            self.t = Startaddreminder(self.a.selectedDate(), self.sem)

	# Adding the tasks.
	
    def addtaskopen(self):
            
            self.t.date = self.a.selectedDate()
            self.t.ui.date.setText(self.t.date.toString())
            self.t.ui.tasksaved.setText('')
            self.t.show()        
            QtCore.QObject.connect(self.t.ui.add, QtCore.SIGNAL("clicked()"), self.settasks)
    
    # Setting the classes.
    
    def setbunkclasses(self):
        if self.sem!=None:        
            self.bunklist = QtGui.QWidget()
            self.bunklist.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
            self.bunklistgrid = QtGui.QGridLayout()
            self.bunklistgrid.setVerticalSpacing(0)
            self.bunklist.setLayout(self.bunklistgrid)
            
            t = (self.sem, )
            cur.execute("select subjectcode from acads where semester = ?", t)
            
            self.tick=[]
            i=0
            for row in cur:
                self.tick.append(QtGui.QCheckBox(row[0]))
                self.bunklistgrid.addWidget(self.tick[i], int(i/2), i%2)
                i = i+1
    
            
            self.bunkscroll.setWidget(self.bunklist)
            

    # Setting the tasks.
    
    def settasks(self):
        if self.sem!=None:
            self.setbunkticks()
            
        date = self.a.selectedDate()
        
        day = date.day()
        month = date.month()
        year = date.year()
                
        t = (day, month, year, )
        
        self.tasklist = QtGui.QWidget()
        self.tasklist.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        self.tasklistgrid = QtGui.QGridLayout()
        self.tasklist.setLayout(self.tasklistgrid)
        self.tasklistgrid.setColumnMinimumWidth(0, 270)

        
        cur.execute("select * from reminder where day = ? and month = ? and year = ?", t)
        
        self.tasks = []
        self.deletetasks = []
        i=0
        
        for row in cur:
            self.tasks.append(QtGui.QLabel(str(i+1)+'. '+str(row[0])+' - '+str(row[1])))
            self.deletetasks.append(QtGui.QToolButton())
            self.deletetasks[i].setIcon(QtGui.QIcon("./pics/deleteButton.png"))
            QtCore.QObject.connect(self.deletetasks[i], QtCore.SIGNAL("clicked()"), self.deletetaskl)        
            self.tasklistgrid.addWidget(self.tasks[i], i, 0)
            self.tasklistgrid.addWidget(self.deletetasks[i], i, 1)
            i = i+1 
        
        self.totaltasks = i
        
        if i==0:
            self.tasklistgrid.addWidget(QtGui.QLabel("No Tasks Added."), 0 , 0)
            
        self.scroll.setWidget(self.tasklist)
        
    # Provision for deleting the task
        
    def deletetaskl(self):
        delbutton = self.sender()

        k = 0
        
        for i in self.deletetasks:
            if i == delbutton:
                break
            
            k = k+1
        
        date = self.a.selectedDate()

        day = date.day()
        month = date.month()
        year = date.year()
                
        t = (day, month, year, )

        cur.execute("select * from reminder where day = ? and month = ? and year = ?", t)
        
        m = 0
        
        for row in cur:
            m = m+1
            if m==k+1:
                break


        t = (row[0], row[1], row[2], row[3], row[4], )       
        cur.execute("delete from reminder where subjectcode = ? and description = ? and day = ? and month = ? and year = ?", t)        
        con.commit()
        self.settasks()

        self.dummybutton.click()        
                
class calendar(QtGui.QCalendarWidget):
  
    def __init__(self):
        super(calendar, self).__init__()
        
        
        self.setGeometry(300, 300, 350, 280)
        

    def paintCell(self, painter, rect, date):
    
        QtGui.QCalendarWidget.paintCell(self, painter, rect, date)
        
        g = QtGui.QFont()
        g.setBold(True)
        g.setOverline(True)
        g.setUnderline(True)
        
        f = QtGui.QTextCharFormat()
        f.setFont(g)
        
        color = QtGui.QColor(22, 38, 50, 61)
        
        
        cur.execute("select * from bunk")
        
        for row in cur:
            if date==QtCore.QDate(row[3], row[2], row[1]):
                self.setDateTextFormat(date, f)    
        
        cur.execute("select * from reminder")
        
        for row in cur:
            if date==QtCore.QDate(row[4], row[3], row[2]):
                painter.fillRect(rect, color)
    
       
            
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startcalendar(1)
    myapp.show()
    sys.exit(app.exec_())
