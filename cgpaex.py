import os
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from cgpa import Ui_window
from gradeex import Startgrade
from cgpa2ex import Startcgpa2
from global_sql import *


class Startcgcalc(QtGui.QMainWindow):

    sub = ()
    credit = ()
    grade = ()
    numeqdict = {}
    
    def setsem(self):
        cur.execute("select distinct semester from acads")
        a = cur.fetchall()
        
        b = []
        
        for sublist in a:
            b.append(str(sublist[0]))
            
        self.ui.sem.clear()
        self.ui.sem.addItems(b)
        cur.execute("select * from defsem")
        a = cur.fetchone()


        if a!=None:
            self.ui.sem.setCurrentIndex(self.ui.sem.findText(str(a[0])))

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_window()
        self.ui.setupUi(self)
        self.editgrades = Startgrade()
        

        self.setsem()
        self.ui.sem.setVisible(False)
        self.sub = (self.ui.sub1, self.ui.sub2, self.ui.sub3, self.ui.sub4, self.ui.sub5, self.ui.sub6, self.ui.sub7, self.ui.sub8, self.ui.sub9, self.ui.sub10, )
        
        self.credit = (self.ui.credit1, self.ui.credit2, self.ui.credit3, self.ui.credit4, self.ui.credit5, self.ui.credit6, self.ui.credit7, self.ui.credit8, self.ui.credit9, self.ui.credit10, )

        self.grade = (self.ui.grade1, self.ui.grade2, self.ui.grade3, self.ui.grade4, self.ui.grade5, self.ui.grade6, self.ui.grade7, self.ui.grade8, self.ui.grade9, self.ui.grade10, ) 
        
        self.gradeinvisible()
        self.clear()
        self.setgrade1()
        self.setsub()

        self.setnumeqdict()
        self.setgrade2()
        
        for i in range(0, 10):
            self.grade[i].setStyleSheet('selection-background-color: rgb(85, 85, 255); selection-color: rgb(255, 255, 255)')            
        
        QtCore.QObject.connect(self.ui.sem, QtCore.SIGNAL("currentIndexChanged(int)"), self.setsub)
        QtCore.QObject.connect(self.ui.cgpa_button, QtCore.SIGNAL("clicked()"), self.calc_cgpa)
        QtCore.QObject.connect(self.ui.gpa_button, QtCore.SIGNAL("clicked()"), self.calc_gpa)
        QtCore.QObject.connect(self.ui.editgrades, QtCore.SIGNAL("clicked()"), self.editgradesed)
        QtCore.QObject.connect(self.ui.save, QtCore.SIGNAL("clicked()"), self.saved)

        self.ui.cgpa_button.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.ui.gpa_button.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')
        self.ui.editgrades.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        
        self.ui.save.setStyleSheet('background-color: rgb(0, 147, 203); color: rgb(255, 255, 255);')        
                

    def creditsum(self, a):
        t = (a, )
        cur.execute("select * from acads where semester = ? and grade<>'null'", t)
        
        creditsum = 0
        
        for row in cur:
            creditsum = creditsum + row[3]
        
        return creditsum

    
    def calc_cgpa(self):

        cur.execute("select distinct semester from acads")
        
        flag = 0
        
        for row in cur:
            if self.creditsum(int(row[0]))==0:
                flag = 1
                break;

        if flag==0:
            os.system("python './graph.py'")
            self.cgpa = Startcgpa2()
            self.cgpa.show()
    
        else :
            self.showmessage("One of the semester's credit sum is 0 ")

    def saved(self):
        if self.ui.sem.currentText()!='':
            
            c = (int(self.ui.sem.currentText()),)
            
            cur.execute("select count(subjectcode) from acads where semester = ?", c)
            a = cur.fetchone()
            con.commit()
            i=0
            while(i<a[0]):
                if self.grade[i].currentIndex()!=0:
                    t= (str(self.grade[i].currentText()), str(self.sub[i].text()), int(self.ui.sem.currentText()), )
                    cur.execute("update acads set grade = ? where subjectcode = ? and semester = ?", t)
                    con.commit()
            
                    
                else :
                    t= (None, str(self.sub[i].text()), int(self.ui.sem.currentText()), )
                    cur.execute("update acads set grade = ? where subjectcode = ? and semester = ?", t)
                    con.commit()
                i = i+1
        
    def calc_gpa(self):
        
            gpat = 0
            creditsum = 0
            c = (int(self.ui.sem.currentText()),)
            cur.execute("select count(subjectcode) from acads where semester = ?", c)
            a = cur.fetchone()

            i = 0;
            while(i<a[0]):
                if self.grade[i].currentIndex()!=0:
                    gpat = gpat + int(self.credit[i].text())*self.numeqdict[str(self.grade[i].currentText())]
                    creditsum = creditsum + int(self.credit[i].text())
                i = i+1
            
            self.ui.crthsem.setText(str(creditsum))
            
            if creditsum!=0:
                
                gpa = float(gpat)/creditsum
                
                self.ui.gpa.setText(str(gpa))
            
            else:
                self.showmessage('Credit sum is 0')

                        
    def showmessage(self, a):
        message = QtGui.QMessageBox(self)
        message.setText(a)
        message.setWindowTitle('acadmin Error')
        message.setIcon(QtGui.QMessageBox.Critical)
        message.exec_()



    def gradeinvisible(self):
        i = 0
        
        while(i<10):
            self.grade[i].setVisible(False)
            i= i+1
    
    def setsub(self):
            
        if self.ui.sem.currentText()!='':
            c = (int(self.ui.sem.currentText()),)
            
            cur.execute("select * from acads where semester = ?", c)
        
            i=0
            while(i<10):
                self.sub[i].clear()
                self.credit[i].clear()
                self.grade[i].setVisible(False)
                i = i+1
            self.ui.crthsem.clear()
            self.ui.gpa.clear()
            i=0
            for row in cur:
                self.sub[i].setText(row[1])
                self.credit[i].setText(str(row[3]))
                self.grade[i].setVisible(True)
                
                if row[4]!=None:
                    a = self.grade[i].findText(row[4],Qt.MatchExactly)
                    self.grade[i].setCurrentIndex(a)
                else:
                    self.grade[i].setCurrentIndex(0)

                i = i+1;
    
    
    def clear(self):
        i=0
        while(i<10):
            self.sub[i].clear()
            self.credit[i].clear()
            self.grade[i].clear()
            i = i+1
        
    
    def setgrade1(self):
        cur.execute("select grade from grades")
        
        a = cur.fetchall()
        
        b = ['']
        
        for sublist in a:
            b.append(str(sublist[0]))
        
        i = 0
        while (i<10):
            self.grade[i].addItems(b)
            i = i+1
        
    def setnumeqdict(self):
        cur.execute("select * from grades")
        for row in cur:
            self.numeqdict[row[0]] = row[1]
            
    def editgradesed(self):
        self.editgrades.show()
    
    
    def setgrade2(self):
        if self.ui.sem.currentText()!='':
            c = (int(self.ui.sem.currentText()),)
            
            cur.execute("select * from acads where semester = ?", c)
            
            
    
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startcgcalc()
    myapp.show()
    sys.exit(app.exec_())
