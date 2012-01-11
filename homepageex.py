import os
#os.chdir('/usr/share/acadmin/')
import sys
from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from homepage import Ui_window2
from cgpaex import Startcgcalc
from gradeex import Startgrade
from editsemex import Starteditsem
from timetableex import Starttimetable
from addrefex import Startaddref
from referenceframeex import Startframe
from editsubex import Starteditsub
from timetableex2 import Starttimetableedit
from ttdetailsex import Startttdetailsex
from calendarex import Startcalendar
from defaultsemex import Startdefaultsem
from aboutex import Startabout
from helpex import Starthelp
from global_sql import *
import datetime

class Startmain(QtGui.QMainWindow):

    
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_window2()
        self.ui.setupUi(self)
        self.setWindowTitle('acadmin - Academic Management Tool')

        icon = QtGui.QIcon()
        b = QtGui.QPixmap("./pics/logo.png")
        icon.addPixmap(b)

        self.setWindowIcon(icon)

        
        self.setFixedWidth(931)
        self.setFixedHeight(668)
        
        b = QtGui.QPixmap("./pics/hide.png")
        self.ui.hide.setPixmap(QtGui.QPixmap(b))
        
        self.subtabWidget = QtGui.QTabWidget()
        
        self.dummybutton2 = QtGui.QToolButton()

        self.setdate()
        self.setsem()
        self.setallwidgets()
        self.setsub()
        self.setmaintabwidget()
        self.checkdb()
        
        self.setpics()
        self.settoolbar()

        self.setstickynote()

        self.editsub = Starteditsub()

        QtCore.QObject.connect(self.ui.maintabWidget, QtCore.SIGNAL("currentChanged(int)"), self.timetabletab)     
        QtCore.QObject.connect(self.editsub.ui.change, QtCore.SIGNAL("clicked()"), self.setsub)        
        QtCore.QObject.connect(self.ui.cgcalc, QtCore.SIGNAL("clicked()"), self.showcg)
        QtCore.QObject.connect(self.ui.calendar, QtCore.SIGNAL("clicked()"), self.showcalendar)
        QtCore.QObject.connect(self.ui.home, QtCore.SIGNAL("clicked()"), self.showhome)
        QtCore.QObject.connect(self.ui.timetable, QtCore.SIGNAL("clicked()"), self.showtimetable)
        QtCore.QObject.connect(self.ui.editsem, QtCore.SIGNAL("clicked()"), self.showeditsem)
        QtCore.QObject.connect(self.ui.defsem, QtCore.SIGNAL("clicked()"), self.defaultsem)
        QtCore.QObject.connect(self.ui.about, QtCore.SIGNAL("clicked()"), self.showabout)
        QtCore.QObject.connect(self.ui.help, QtCore.SIGNAL("clicked()"), self.showhelp)
        
        self.clickflag = 0
        self.clickflag2 = 0
        self.ttflag = 0
        self.cgflag = 0
        
    def showhelp(self):
        self.help = Starthelp()
        self.help.show()
    def checkdb(self):
        cur.execute("select * from acads")
        a = cur.fetchone()
        
        if a==None:
	    self.ui.maintabWidget.setCurrentIndex(1)
            message = QtGui.QMessageBox(self)
            message.setText('Welcome to "acadmin". Start by adding a subject.')
            message.setWindowTitle('Acadmin alert')
            message.setIcon(QtGui.QMessageBox.Information)
            message.exec_()
	    
	
    def showabout(self):
        self.showabt = Startabout()
        self.showabt.show()
        
    def showcalendar(self):
        self.ui.maintabWidget.setCurrentIndex(2)

    def showhome(self):
        self.ui.maintabWidget.setCurrentIndex(0)

    def showeditsem(self):
        self.ui.maintabWidget.setCurrentIndex(1)

    def showtimetable(self):
        self.ui.maintabWidget.setCurrentIndex(3)
        if self.clickflag!=1:
            self.clickflag = 1
            self.ui.timetable.click()
                
    def showcg(self):
        self.ui.maintabWidget.setCurrentIndex(4)
        if self.clickflag2!=1:
            self.clickflag2 = 1
            self.ui.cgcalc.click()
        
    
    
    def defaultsem(self):
        cur.execute("select * from acads")
        a = cur.fetchone()
        
        if a==None:
            self.showmessage('Add a subject first')
	    self.ui.editsem.click()
        else:
            self.setdefaultsem = Startdefaultsem()
            self.setdefaultsem.show()
            QtCore.QObject.connect(self.setdefaultsem.ui.okay, QtCore.SIGNAL("clicked()"), self.setdefsemandclose)
           
    def setdefsemandclose(self):
        self.setsem()
        self.close()

    def timetabletab(self):
        a = self.ui.maintabWidget.currentIndex()

        b = self.ttflag
        c = self.cgflag        
                
        if a==3:        
            if b==0:
                self.settimetable()
            
            if self.ui.maintabWidget.count()>5:
                self.ui.maintabWidget.removeTab(4)
        
        if a==4:
            if c==0:
                self.cgcalc()
                
            if self.ui.maintabWidget.count()>5:
                self.ui.maintabWidget.removeTab(5)
        
    def setallwidgets(self):
        if self.ui.sem.text()=='':
            sem = None
        else :
            sem = int(self.ui.sem.text())

        self.editsem = Starteditsem()        
        self.calendar = Startcalendar(sem)        

    def setmaintabwidget(self):
        self.notrequired = QtGui.QWidget()
        self.notrequired2 = QtGui.QWidget()
        self.ui.maintabWidget.clear()
        self.ui.maintabWidget.insertTab(0, self.subtabWidget, 'Home')
        self.ui.maintabWidget.insertTab(1, self.editsem, 'Add/Delete Subjects')
        self.editsemsignals()
        self.ui.maintabWidget.insertTab(2, self.calendar, 'Calendar')
        self.calendarsignals()
        self.ui.maintabWidget.insertTab(3, self.notrequired, 'Timetable')
        self.ui.maintabWidget.insertTab(4, self.notrequired2, 'Grades')
        
    def cgcalc(self):
        
        cur.execute("select * from grades")
        a = cur.fetchone()

        
        if a==None:
            self.showmessage('Set default grading system first')

            self.gradingsystem = Startgrade()
            self.gradingsystem.show()
            QtCore.QObject.connect(self.gradingsystem.ui.done, QtCore.SIGNAL("clicked()"), self.cgcalc)
            
        else:
            cur.execute("select * from acads")
            a = cur.fetchone()
            
            if a==None:
                self.showmessage('Add a subject first')
            else:

                self.cgcalc2 = Startcgcalc()
                self.ui.maintabWidget.insertTab(4, self.cgcalc2, 'Grades')
                self.cgflag = 1
                cur.execute("insert into cgflag values(1)")
                con.commit()
        
    def settimetable(self):

        cur.execute("select max(day) from timetable")
        a = cur.fetchone()
        
        
        if a[0]==None:
            cur.execute("select * from days")
            b = cur.fetchone()

            if b==None:
                self.showmessage('Set timeslots and Days first')
                self.ttdetails = Startttdetailsex()
                self.ttdetails.show()
                QtCore.QObject.connect(self.ttdetails.done, QtCore.SIGNAL("clicked()"), self.settimetable)
                QtCore.QObject.connect(self.ttdetails.cancel, QtCore.SIGNAL("clicked()"), self.settimetable)
            
            else:
                cur.execute("select * from acads")
                a = cur.fetchone()
                if a==None:
                    self.showmessage('Add a subject first')
                    
            
                else:
                    self.showmessage('Set the periods and save')
                    self.ttedit = Starttimetableedit()
                    self.ttedit.show()
                    
                    QtCore.QObject.connect(self.ttedit.save, QtCore.SIGNAL("clicked()"), self.settimetable)
        
        else:

            self.timetable = Starttimetable()
            
            self.ui.maintabWidget.insertTab(3, self.timetable, 'Timetable')
            self.ttflag = 1
            cur.execute("insert into timetableflag values(1)")
            con.commit()
                        
    def calendarsignals(self):

        QtCore.QObject.connect(self.calendar.savebunk, QtCore.SIGNAL("clicked()"), self.setsub)
        QtCore.QObject.connect(self.calendar.t.ui.add, QtCore.SIGNAL("clicked()"), self.setstickynote)
        QtCore.QObject.connect(self.calendar.dummybutton, QtCore.SIGNAL("clicked()"), self.setstickynote)
        
    def editsemsignals(self):

        QtCore.QObject.connect(self.editsem.ui.add, QtCore.SIGNAL("clicked()"), self.setsub2)
        QtCore.QObject.connect(self.editsem.ui.delete_2, QtCore.SIGNAL("clicked()"), self.setsub2)

    def setsub(self):
   
        self.subtabWidget.clear()
        self.startframe = []

        if self.ui.sem.text()!='':
            c = (int(self.ui.sem.text()),)
            cur.execute("select * from acads where semester = ?", c)
        
            i=0
            k = 0
        
            subcode = []
            subname = []
            credits = []
            bunksleft = []
            classes = []
            attendance = []
        
            for row in cur:
                subcode.append(row[1])
                subname.append(row[2])
                credits.append(row[3])
                bunksleft.append(row[5]-row[6])
                classes.append(row[7])
                attendance.append(row[8])
                k = k+1
        
            for i in range(0, k):
                self.startframe.append(Startframe(str(subcode[i]), classes[i], attendance[i]))
                a = self.subtabWidget.insertTab(i, self.startframe[i], subcode[i])
                self.startframe[i].subjectname.setText(subname[i])
                self.startframe[i].credits.setText(str(credits[i]))
                self.startframe[i].subjectcode.setText(str(subcode[i]))
                self.startframe[i].bunksleft.setText(str(bunksleft[i]))
                QtCore.QObject.connect(self.startframe[i].editsubject.ui.change, QtCore.SIGNAL("clicked()"), self.setsub3)
                QtCore.QObject.connect(self.startframe[i].addref.ui.add, QtCore.SIGNAL("clicked()"), self.setsub3)
                QtCore.QObject.connect(self.startframe[i].deleteref.ui.deletebutton, QtCore.SIGNAL("clicked()"), self.setsub3)
                i = i+1
        

        self.ui.maintabWidget.removeTab(0)
        self.ui.maintabWidget.insertTab(0, self.subtabWidget, 'Home')

    def setsub3(self):
        self.setsub()
        self.ui.home.click()

    def setsub2(self):
        
        flag = 0
        
        cur.execute("select * from acads")
        
        for row in cur:
        	flag = flag+1
        
        self.setsem()
        self.setsub()
        self.calendar.setbunkclasses()
        self.calendar.setbunkticks()
        self.ui.home.click()
        
        if flag==1:
        	self.ui.defsem.click()
        
    
    def setsem(self):
        cur.execute("select * from defsem")
        a = cur.fetchone()
        
        if a!=None:
            self.ui.sem.setText(str(a[0]))



    def showmessage(self, a):
        message = QtGui.QMessageBox(self)
        message.setText(a)
        message.setWindowTitle('Acadmin alert')
        message.setIcon(QtGui.QMessageBox.Warning)
        message.exec_()

    def setdate(self):

        self.date = datetime.datetime.now()
        self.month = [None, 'Jan.', 'Feb.', 'March', 'April', 'May', 'June', 'July', 'Aug.', 'Sept.', 'Oct.', 'Nov.', 'Dec.', ]
        
        self.ui.day.setText("<span style=\" font-size:48pt; font-weight:600; color:#ffff00;\">"+ str(self.date.day) + "</span>")
        self.ui.monthyear.setText("<span style=\" font-size:12pt; font-weight:600; color:#ffff00;\">"+ self.month[self.date.month] + "  " + str(self.date.year) + "</span>")
        self.ui.day.setAlignment(Qt.AlignHCenter)
        self.ui.monthyear.setAlignment(Qt.AlignHCenter)

    def setstickynote(self):
        
        stickylist=QtGui.QWidget()
        stickylist.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        stickylistgrid = QtGui.QGridLayout()

        stickylistgrid.addWidget(QtGui.QLabel("        "), 0, 0)        
        stickylistgrid.addWidget(QtGui.QLabel("<b>.  Today's Tasks :</b>"), 1, 0)
        
        todaytask = []
        i=0
        t = (self.date.day, self.date.month, self.date.year, )
        cur.execute("select * from reminder where day = ? and month = ? and year = ?", t)
        a = cur.fetchone()
        
        
        if a==None:
            stickylistgrid.addWidget(QtGui.QLabel("<i>.    No assignments</i>"), 2, 0)

        else:

            cur.execute("select * from reminder where day = ? and month = ? and year = ?", t)
            for row in cur:
                todaytask.append(QtGui.QLabel('   ' + str(i+1)+'. '+str(row[0])+' - '+str(row[1])))
                stickylistgrid.addWidget(todaytask[i], i+2, 0)
                i = i+1


        stickylistgrid.addWidget(QtGui.QLabel("<b>.  Tomorrow's Tasks :</b>"), i+3, 0)

        today = QtCore.QDate(self.date.year, self.date.month, self.date.day)
        tomorrow = today.addDays(1)
        
        tommtask = []
        j = i+3
        t = (tomorrow.day(), tomorrow.month(), tomorrow.year(), )
        cur.execute("select * from reminder where day = ? and month = ? and year = ?", t)
        a = cur.fetchone()
        if a==None:
       
            stickylistgrid.addWidget(QtGui.QLabel("<i>.    No assignments</i>"), j+1, 0)
       
        else:
       
            cur.execute("select * from reminder where day = ? and month = ? and year = ?", t)
            q=0
            for row in cur:
                tommtask.append(QtGui.QLabel('   '+str(q+1)+'. '+str(row[0])+' - '+str(row[1])))
                stickylistgrid.addWidget(tommtask[q], j+1, 0)
                q = q+1
                j = j+1

        stickylistgrid.addWidget(QtGui.QLabel("        "), j+2, 0)        
        stickylist.setLayout(stickylistgrid)
        self.ui.stickynote.setWidget(stickylist)

    def setpics(self):
                
        self.ui.home.setIcon(QtGui.QIcon('./pics/home.png'))
        self.ui.calendar.setIcon(QtGui.QIcon('./pics/calendar.png'))
        self.ui.timetable.setIcon(QtGui.QIcon('./pics/timetable.png'))
        self.ui.cgcalc.setIcon(QtGui.QIcon('./pics/grades.png'))
        self.ui.editsem.setIcon(QtGui.QIcon('./pics/editsem.png'))
        self.ui.about.setIcon(QtGui.QIcon('./pics/about.png'))
        self.ui.defsem.setIcon(QtGui.QIcon('./pics/default.png'))
        self.ui.help.setIcon(QtGui.QIcon('./pics/help.png'))
        
        palette = QtGui.QPalette()
        palette.setBrush(self.backgroundRole(), QBrush(QImage("./pics/sticky note.png")))


        palette3 = QtGui.QPalette()
        palette3.setBrush(self.backgroundRole(), QBrush(QImage("./pics/calender.png")))

        palette2 = QtGui.QPalette()
        palette2.setBrush(self.backgroundRole(), QBrush(QImage("./pics/background2.jpg")))

        self.setPalette(palette2)
        self.ui.stickynote.setPalette(palette)
        
        
        
        self.ui.calender.setPalette(palette3)


    def settoolbar(self):
        self.ui.toolBar.addWidget(self.ui.home)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.ui.calendar)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.ui.timetable)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.ui.cgcalc)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.ui.editsem)
        self.ui.toolBar.addSeparator()
        
        aha = QtGui.QWidget()
        aha.setFixedWidth(40)
        aha.setFixedHeight(30)
        

        self.ui.toolBar.addWidget(aha)
        
        self.ui.toolBar.addWidget(self.ui.defsem)
        self.ui.toolBar.addSeparator()

        aha2 = QtGui.QWidget()
        aha.setFixedWidth(40)
        aha.setFixedHeight(30)


        self.ui.toolBar.addWidget(aha2)
        
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.ui.about)
        self.ui.toolBar.addSeparator()
        self.ui.toolBar.addWidget(self.ui.help)
        self.ui.toolBar.addSeparator()        
 


        self.ui.home.setToolTip('Home')
        self.ui.calendar.setToolTip('Calendar')
        self.ui.timetable.setToolTip('Timetable')
        self.ui.cgcalc.setToolTip('Grades')
        self.ui.editsem.setToolTip('Add / Delete Subjects')
        self.ui.about.setToolTip('About')
        self.ui.defsem.setToolTip('Set Default Semester')
        self.ui.help.setToolTip('Help')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Startmain()
    myapp.show()
    sys.exit(app.exec_())
