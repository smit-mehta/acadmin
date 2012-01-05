import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from global_sql import *


class Startttdetailsex(QtGui.QDialog):
    slotslabel = []
    slots = []
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        
        self.setWindowTitle('Give timeslots and days')        
        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        self.setPalette(palette2)

        self.setStyleSheet('color: rgb(85, 0, 0);')

        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)
        
        self.grid = QtGui.QGridLayout()
        self.hbox = QtGui.QHBoxLayout()
        self.vbox = QtGui.QVBoxLayout()
        
        
        self.timeslotlabel = QtGui.QLabel("No. of timeslots required :")
        
        self.timeslots = QtGui.QComboBox()
        self.timeslots.setFixedSize(40, 30)
        b = ['3', '4', '5', '6', '7', '8', '9', '10', ]
        self.timeslots.clear()
        self.timeslots.addItems(b)
        
        self.dayslabel = QtGui.QLabel ("Days :")
        
        self.days = QtGui.QComboBox()
        days = ['Mon - Fri', 'Mon - Sat', 'Mon - Sun', ]
        self.days.clear()
        self.days.addItems(days)
        
        self.grid.addWidget(self.timeslotlabel, 1, 0)
        self.grid.addWidget(self.timeslots, 1 , 1) 
        self.createlineedits()

        QtCore.QObject.connect(self.timeslots, QtCore.SIGNAL("currentIndexChanged(int)"), self.createlineedits)

        self.done = QtGui.QToolButton()
        self.done.setText('Done')
        self.done.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        
        self.hbox.addWidget(self.done)
        
        self.cancel = QtGui.QToolButton()
        self.cancel.setText('Cancel')
        
        self.hbox.addWidget(self.cancel)
        
        QtCore.QObject.connect(self.done, QtCore.SIGNAL("clicked()"), self.doned)
        QtCore.QObject.connect(self.cancel, QtCore.SIGNAL("clicked()"), self.close)

        self.cancel.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')

        self.vbox.addLayout(self.grid)
        self.vbox.addLayout(self.hbox)

        self.setLayout(self.vbox)

    def createlineedits(self):
        a = int(self.timeslots.currentText())
        
        k = 0
        
        for i in self.slotslabel:
            self.grid.removeWidget(self.slotslabel[k])
            self.grid.removeWidget(self.slots[k])
            self.slotslabel[k].close()
            self.slots[k].close()
            k = k+1
        
        self.slotslabel = []
        self.slots = []

        self.slotslabel.append(QtGui.QLabel('Timeslot 1 : (For Eg. : 8.00-9.00 AM)'))
        self.slots.append(QtGui.QLineEdit())
        self.grid.addWidget(self.slotslabel[0], 2, 0)
        self.grid.addWidget(self.slots[0], 2, 1)
                
        
        
        for i in range(1, a):
            self.slotslabel.append(QtGui.QLabel('Timeslot '+str(i+1)))
            self.slots.append(QtGui.QLineEdit())
        
            self.grid.addWidget(self.slotslabel[i], i+2, 0)
            self.grid.addWidget(self.slots[i], i+2, 1)
        
        self.grid.addWidget(self.dayslabel, a+2 , 0)
        self.grid.addWidget(self.days, a+2 , 1)

    def doned(self):
        cur.execute("delete from timeslots")
        cur.execute("delete from days")
        con.commit()
        a = int(self.timeslots.currentText())
        
        for i in range(0, a):
            t = (str(self.slots[i].text()), )
            cur.execute("insert into timeslots values(?)", t)
            con.commit()
        s = (int(self.days.currentIndex()), )

        cur.execute("insert into days values(?)", s)
        con.commit()
        
        cur.execute("delete from timetable")
        con.commit()
        
        self.close()


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  panel = Startttdetailsex()
  panel.show()
  sys.exit(app.exec_())
