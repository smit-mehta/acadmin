# Implementing reminder / task saver in calendar tab.

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
from reminder import Ui_Dialog
from global_sql import *


class Startaddreminder(QtGui.QMainWindow):
    def __init__(self, date, sem, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)

        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)
                
        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        self.setPalette(palette2)
        
        self.ui.add_3.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        
        self.ui.add.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')                

        self.date = date
        self.sem = sem
        
        self.ui.date.setText(date.toString())
        
        self.setsub()
        
        
        QtCore.QObject.connect(self.ui.add, QtCore.SIGNAL("clicked()"), self.tasksave)
        
    # Saving the task into the database.

    def tasksave(self):

        day = self.date.day()
        month = self.date.month()
        year = self.date.year()
        
        t = (str(self.ui.sub.currentText()), str(self.ui.desc.text()), day, month, year, )
        
        cur.execute("insert into reminder values(?, ?, ?, ?, ?)", t)
        con.commit()
        
        self.ui.tasksaved.setText("Task added")
        self.ui.desc.clear()

    # Setting the subjects of the current semester.

    def setsub(self):
        
        self.ui.sub.clear()
 
        t = (self.sem, )
        cur.execute("select subjectcode from acads where semester = ?", t)
        a = cur.fetchall()
        b = []
        
        for sublist in a:
            b.append(str(sublist[0]))
            
        b.append("Other")
        self.ui.sub.addItems(b)
               
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startaddreminder()
    myapp.show()
    sys.exit(app.exec_())
