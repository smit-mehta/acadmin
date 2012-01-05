import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from cgpa2 import Ui_Dialog
from cgpaframeex import Startgradeframe
from global_sql import *

class Startcgpa2(QtGui.QDialog):
    tabindex = {}
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.tabWidget.clear()
        
        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)

        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        self.setPalette(palette2)
        self.setStyleSheet('color: rgb(85, 0, 0);')

        
        b = QtGui.QPixmap("./graph.png")        
        
        a = b.scaled(341, 270, Qt.IgnoreAspectRatio, 1)
        
        self.ui.graph.setPixmap(QtGui.QPixmap(a))
                
        QtCore.QObject.connect(self.ui.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.setall)
        
        
        self.startgradeframe = []
        cur.execute("select distinct semester from acads where grade<>'NULL'")
        
        k=0
        sem = []
        
        for row in cur:
            sem.append(row[0])
            k = k+1
        
        
        i = 0
        for i in range(0, k):
            self.tabindex[i] = sem[i]
            self.startgradeframe.append(Startgradeframe(sem[i]))
            self.ui.tabWidget.insertTab(i, self.startgradeframe[i], 'Sem '+str(sem[i]))
            i = i+1
        
        self.setall()
        self.setcgpa()
        
    def setall(self):
        i = self.ui.tabWidget.currentIndex()
        a = self.tabindex[i]
        

        self.ui.semcredits.setText(str(self.startgradeframe[i].creditsum(a)))
        self.ui.gpa.setText(str(self.startgradeframe[i].calc_gpa(a)))
                
    def setcgpa(self):
        
        cgpat = 0
        netcredits = 0
        k = 0
        i = len(self.startgradeframe)

        while(k<i):
            cgpat = cgpat + self.startgradeframe[k].calc_gpa(self.tabindex[k]) * self.startgradeframe[k].creditsum(self.tabindex[k])
            netcredits = netcredits + self.startgradeframe[k].creditsum(self.tabindex[k])
            k = k+1    
        
        cgpat = float(cgpat)/netcredits
	cg = "%.2f" % (cgpat)
        self.ui.cgpa.setText(str(cg))
	self.ui.netcredits.setText(str(netcredits))
        
            
    def showmessage(self, a):
        message = QtGui.QMessageBox(self)
        message.setText(a)
        message.setWindowTitle('acadmin Error')
        message.setIcon(QtGui.QMessageBox.Critical)
        message.exec_()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startcgpa2()
    myapp.show()
    sys.exit(app.exec_())
