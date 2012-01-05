import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from editsub import Ui_Dialog
from global_sql import *



class Starteditsub(QtGui.QDialog):
    
    a = '0'
    
    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        
        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/genback.png")))

        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)
        self.setWindowIcon(icon)
        self.setPalette(palette2)
        self.ui.attendance.setMaximum(100)
        self.ui.change.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        
        self.ui.toolButton_2.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        

        QtCore.QObject.connect(self.ui.change, QtCore.SIGNAL("clicked()"), self.changed)

    def changed(self):

        bunksallowed = int(self.ui.classes.value()+1)-int((self.ui.classes.value()*self.ui.attendance.value()/100))

        s = (str(self.ui.subjectcode.text()), str(self.ui.subjectname.text()), self.ui.credits.value(), self.ui.attendance.value(), self.ui.classes.value(), bunksallowed, self.a, )



        cur.execute("update acads set subjectcode = ?, subjecttitle = ?, credits = ?, attendance = ?, totalclasses = ?, bunksallowed = ? where subjectcode = ?", s)

        t = (str(self.ui.subjectcode.text()), self.a, )
        cur.execute("update referencess set subjectcode1 = ? where subjectcode1 = ?", t)
        
        con.commit()
        self.close()

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Starteditsub()
    myapp.show()
    sys.exit(app.exec_())
