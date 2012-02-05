# Setting the grades of all the semesters in 'cgpa' secondary tab.

import sys
from PyQt4 import QtGui, QtCore
from global_sql import *



class Startgradeframe(QtGui.QWidget):
    numeqdict = {}    
    
    def setnumeqdict(self):
        cur.execute("select * from grades")
        for row in cur:
            self.numeqdict[row[0]] = row[1]
    

    def __init__(self, a, parent=None):

        QtGui.QWidget.__init__(self, parent)
        sublist = QtGui.QWidget()
        sublist.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sublistgrid = QtGui.QGridLayout()
        sublist.setLayout(sublistgrid)

        sublistscrollarea = QtGui.QScrollArea()
        
        self.setnumeqdict()
        subject = []
        grade = []
        dash = []
        
        t = (a, )
        i=0
        
        cur.execute("select * from acads where semester = ? and grade<>'null'", t)
        
        for row in cur:
            subject.append(QtGui.QLabel(row[1]))
            grade.append(QtGui.QLabel(row[4]))
            dash.append(QtGui.QLabel(" --- "))
            subject[i].setBuddy(dash[i])
            dash[i].setBuddy(grade[i])
            sublistgrid.addWidget(subject[i], i, 0)
            sublistgrid.addWidget(dash[i], i, 2)
            sublistgrid.addWidget(grade[i], i, 4)
            i = i+1
            
            
        sublistscrollarea.setWidget(sublist)

        mainvbox = QtGui.QVBoxLayout()
        mainvbox.addWidget(sublistscrollarea)
        self.setLayout(mainvbox)
        
    # Calculating the gpa.
    
    def calc_gpa(self, a):
        t = (a, )
        cur.execute("select * from acads where semester = ? and grade<>'null'", t)
        
        gpat = 0
        creditsum = 0
        
        for row in cur:
            gpat = gpat + row[3]*self.numeqdict[row[4]]
            creditsum = creditsum + row[3]
        
        return float(gpat)/creditsum
        
    # Calculating the number of credits.
    
    def creditsum(self, a):
        t = (a, )
        cur.execute("select * from acads where semester = ? and grade<>'null'", t)
        
        creditsum = 0
        
        for row in cur:
            creditsum = creditsum + row[3]
        
        return creditsum
        
        
if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  panel = Startgradeframe()
  panel.show()
  sys.exit(app.exec_())
