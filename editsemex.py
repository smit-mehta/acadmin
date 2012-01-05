import sys
from PyQt4 import QtCore, QtGui
from editsem import Ui_window
from global_sql import *



class Starteditsem(QtGui.QMainWindow):

        
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_window()
        
        
        self.ui.setupUi(self)
        
        self.delete_setsem()
        
        self.ui.semadd.setMinimum(1)
        self.ui.semadd.setMaximum(12)
        self.ui.attendance.setMaximum(100)        
                
        QtCore.QObject.connect(self.ui.add, QtCore.SIGNAL("clicked()"), self.added)
        QtCore.QObject.connect(self.ui.semdelete, QtCore.SIGNAL("currentIndexChanged(int)"), self.delete_setsub)
        QtCore.QObject.connect(self.ui.delete_2, QtCore.SIGNAL("clicked()"), self.deleted)

                 
        self.ui.semdelete.setStyleSheet('selection-background-color: rgb(85, 85, 255); selection-color: rgb(255, 255, 255)')            
        self.ui.subdelete.setStyleSheet('selection-background-color: rgb(85, 85, 255); selection-color: rgb(255, 255, 255)')            

        self.ui.subjectcode.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.ui.subjectname.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.ui.attendance.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.ui.classes.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.ui.semadd.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.ui.credits.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.ui.add.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.ui.delete_2.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.ui.toolButton_2.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.ui.toolButton_3.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        
    def delete_setsub(self):
        
        self.ui.subdelete.clear()
        
        cur.execute("select subjectcode from acads where semester = %d"%(int(self.ui.semdelete.currentText())))
        a = cur.fetchall()
        b = []
        
        for sublist in a:
            b.append(str(sublist[0]))
            
        self.ui.subdelete.addItems(b)
        

    def added(self):
        if self.subject_already_exists()==1:
            self.showmessage()            
            
        else:
            bunksallowed = int(self.ui.classes.value())-int((self.ui.classes.value()*self.ui.attendance.value()/100))
            s = (self.ui.semadd.value(), str(self.ui.subjectcode.text()), str(self.ui.subjectname.text()), self.ui.credits.value(), None, bunksallowed, 0, self.ui.attendance.value(), self.ui.classes.value() )
            cur.execute("insert into acads values (?, ?, ?, ?, ?, ?, ?, ?, ?)", s)
            con.commit()
            
            
            
        self.ui.subjectcode.clear()
        self.ui.subjectname.clear()
        
        
        
    def subject_already_exists(self):
        a = (self.ui.semadd.value(),)
        
        cur.execute("select subjectcode from acads where semester = ?",a)
        
        for row in cur:
            if str(self.ui.subjectcode.text())==row[0] :
                return 1
        return 0
        
    def deleted(self):
        a = (int(self.ui.semdelete.currentText()), str(self.ui.subdelete.currentText()), )
        b = (str(self.ui.subdelete.currentText()),)
        cur.execute("delete from acads where semester = ? and subjectcode = ?", a)

        cur.execute("delete from referencess where subjectcode1 = ?", b)

        cur.execute("delete from bunk where semester = ? and subjectcode = ?", a)
        
        cur.execute("delete from reminder where subjectcode = ?", b)
        

        con.commit()
        a = 1
        cur.execute("select * from acads")
        
       
    def delete_setsem(self):
        
        cur.execute("select distinct semester from acads")
        a = cur.fetchall()
        b = ['']
        
        
        for sublist in a:
            b.append(str(sublist[0]))
            
        self.ui.semdelete.clear()
        self.ui.semdelete.addItems(b)
        
    def showmessage(self):
        message = QtGui.QMessageBox(self)
        message.setText('Subject already exists')
        message.setWindowTitle('acadmin Error')
        message.setIcon(QtGui.QMessageBox.Critical)
        message.exec_()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Starteditsem()
    myapp.show()
    sys.exit(app.exec_())
