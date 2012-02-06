# For implementing the 'delete' reference option.

import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from deleteref import Ui_Dialog
from global_sql import *


class Startdeleteref(QtGui.QDialog):
    code = ''
    def __init__(self, a, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.code = a
        self.setref()
        self.setpath()
        
        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)
        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        self.setPalette(palette2)

        
        QtCore.QObject.connect(self.ui.deletebutton, QtCore.SIGNAL("clicked()"), self.deleted)
        QtCore.QObject.connect(self.ui.references, QtCore.SIGNAL("currentIndexChanged(int)"), self.setpath)

        self.ui.deletebutton.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.ui.references.setStyleSheet('selection-background-color: rgb(85, 85, 255); selection-color: rgb(255, 255, 255)')            


	# Setting the path in the gui.

    def setpath(self):
        t = (self.code, str(self.ui.references.currentText()), )
        cur.execute("select * from referencess where subjectcode1 = ? and reference = ?", t)
        for row in cur:
            self.ui.referencepath.setText(row[2])
	
	# Deleting the reference from the database.

    def deleted(self):
        t = (self.code, str(self.ui.references.currentText()), )
        
        cur.execute("delete from referencess where subjectcode1 = ? and reference = ?", t)
        con.commit()
        self.close()

	# Setting up the existing references in the gui scroll down option	
	
    def setref(self):
        t = (self.code, )
        
        cur.execute("select * from referencess where subjectcode1 = ?", t)
        a = cur.fetchall()
        
        b = []
        
        for sublist in a:
            b.append(str(sublist[1]))
            
        self.ui.references.clear()
        self.ui.references.addItems(b)

