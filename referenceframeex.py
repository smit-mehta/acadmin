import os
import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from global_sql import *
from addrefex import Startaddref
from editsubex import Starteditsub
from deleterefex import Startdeleteref
from pysqlite2 import dbapi2 as sqlite


class Startframe(QtGui.QWidget):
    code = ''

    def a(self):
    	link = self.sender()
    	
    	k = 0
        
        for i in self.references:
            if i == link:
                break
            
            k = k+1
	
        t = (self.code, k+1)
        cur.execute("select referencepath from referencess where subjectcode1 = ? and ROWID = ?", t)
        
        for row in cur:
	        path = str(row[0])
        os.system("xdg-open '"+path+"'")

    	
    	
   	
    def __init__(self, a, b, c, parent=None):

        QtGui.QWidget.__init__(self, parent)
        sublist = QtGui.QWidget()
        sublist.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sublistgrid = QtGui.QGridLayout()
        sublist.setLayout(sublistgrid)


        
        self.code = a
        self.classes = c
        self.attendance = b
        
        
        sublistscrollarea = QtGui.QScrollArea()
        
        
        self.editsubject = Starteditsub()
        self.addref = Startaddref()
        self.deleteref = Startdeleteref(a)

        self.addrefbutton = QtGui.QToolButton()
        self.addrefbutton.setText('Add References')    
        
        self.addrefbutton.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        
            
        self.editsub = QtGui.QToolButton()
        self.editsub.setText('Edit Subject')    

        self.editsub.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        

        self.delete = QtGui.QToolButton()
        self.delete.setText('Delete References')    

        self.delete.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')

        QtCore.QObject.connect(self.addrefbutton, QtCore.SIGNAL("clicked()"), self.addrefbuttoned)
        QtCore.QObject.connect(self.editsub, QtCore.SIGNAL("clicked()"), self.editsubed)
        QtCore.QObject.connect(self.delete, QtCore.SIGNAL("clicked()"), self.deleted)
        
        
        self.subjectname = QtGui.QLabel('')
        self.credits = QtGui.QLabel('')
        self.subjectcode = QtGui.QLabel('')
        self.bunksleft = QtGui.QLabel('')

        self.subjectname2 = QtGui.QLabel("Subject's Name : ")
        self.credits2 = QtGui.QLabel('Credits :')
        self.subjectcode2 = QtGui.QLabel("Subject's Code : ")
        self.bunksleft2 = QtGui.QLabel("Bunks Left : ")


        i=0
        
        t = (self.code, )
        cur.execute("select * from referencess where subjectcode1 = ?", t)
                
        number = []
        self.references = []
        
        for row in cur:
            
            number.append(QtGui.QLabel(str(i+1)+'. '))
            self.references.append(QtGui.QLabel('<a href =' + row[2] + ' > ' + row[1] + '</a>'))
#            references[i].setOpenExternalLinks(True)
            QtCore.QObject.connect(self.references[i], QtCore.SIGNAL("linkActivated(const QString&)"), self.a)
            sublistgrid.addWidget(number[i], i, 0)
            sublistgrid.addWidget(self.references[i], i, 1)
            i = i+1
        
        sublistscrollarea.setWidget(sublist)

        mainvbox = QtGui.QVBoxLayout()
        mainh1box = QtGui.QHBoxLayout()
        mainh2box = QtGui.QHBoxLayout()
        mainh3box = QtGui.QHBoxLayout()
        mainh4box = QtGui.QHBoxLayout()
        mainh5box = QtGui.QHBoxLayout()

        mainh1box.addWidget(self.subjectcode2)
        mainh1box.addWidget(self.subjectcode)
        
        mainh2box.addWidget(self.subjectname2)
        mainh2box.addWidget(self.subjectname)

        mainh3box.addWidget(self.credits2)
        mainh3box.addWidget(self.credits)
        
        mainh4box.addWidget(self.bunksleft2)
        mainh4box.addWidget(self.bunksleft)


        mainvbox.addLayout(mainh1box)
        mainvbox.addLayout(mainh2box)
        mainvbox.addLayout(mainh3box)
        mainvbox.addLayout(mainh4box)
        
        mainvbox.addWidget(sublistscrollarea)
        
        mainh5box.addWidget(self.addrefbutton)
        mainh5box.addWidget(self.delete)
        mainh5box.addWidget(self.editsub)

        mainvbox.addLayout(mainh5box)

        self.setLayout(mainvbox)
        
        
    def addrefbuttoned(self):

        self.addref.show()
        self.addref.ui.subjectcode.setText(self.subjectcode.text())


    def editsubed(self):

        self.editsubject.show()
        self.editsubject.a = str(self.subjectcode.text())
        self.editsubject.ui.subjectcode.setText(self.subjectcode.text())
        self.editsubject.ui.subjectname.setText(self.subjectname.text())
        self.editsubject.ui.credits.setValue(int(self.credits.text()))
        self.editsubject.ui.classes.setValue(self.classes)
        self.editsubject.ui.attendance.setValue(self.attendance)

    def deleted(self):
    
        self.deleteref.show()
        self.deleteref.ui.subjectcode.setText(self.subjectcode.text())
	
	def gen(a, self):
			print a


if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  panel = Startframe()
  panel.show()
  sys.exit(app.exec_())
