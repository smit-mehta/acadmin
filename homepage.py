# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homepage.ui'
#
# Created: Sat Sep 24 18:58:08 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_window2(object):
    def setupUi(self, window2):
        window2.setObjectName(_fromUtf8("window2"))
        window2.resize(931, 668)
        window2.setAutoFillBackground(False)
        window2.setStyleSheet(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(window2)
        self.centralwidget.setStyleSheet(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 80, 481, 16))
        self.line.setFrameShadow(QtGui.QFrame.Raised)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 131, 31))
        self.label_2.setStyleSheet(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.maintabWidget = QtGui.QTabWidget(self.centralwidget)
        self.maintabWidget.setGeometry(QtCore.QRect(20, 150, 580, 470))
        self.maintabWidget.setStyleSheet(_fromUtf8("color: rgb(85, 0, 0);\n"
"background-color: rgb(188, 223, 245);\n"
"alternate-background-color: rgb(64, 163, 255);"))
        self.maintabWidget.setObjectName(_fromUtf8("maintabWidget"))
        self.timetable = QtGui.QToolButton(self.centralwidget)
        self.timetable.setGeometry(QtCore.QRect(630, 420, 170, 25))
        self.timetable.setObjectName(_fromUtf8("timetable"))
        self.editsem = QtGui.QToolButton(self.centralwidget)
        self.editsem.setGeometry(QtCore.QRect(630, 480, 171, 25))
        self.editsem.setObjectName(_fromUtf8("editsem"))
        self.cgcalc = QtGui.QToolButton(self.centralwidget)
        self.cgcalc.setGeometry(QtCore.QRect(630, 450, 171, 25))
        self.cgcalc.setObjectName(_fromUtf8("cgcalc"))
        self.calendar = QtGui.QToolButton(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(630, 390, 171, 25))
        self.calendar.setStyleSheet(_fromUtf8(""))
        self.calendar.setObjectName(_fromUtf8("calendar"))
        self.stickynote = QtGui.QScrollArea(self.centralwidget)
        self.stickynote.setGeometry(QtCore.QRect(620, 210, 205, 190))
        self.stickynote.setFrameShape(QtGui.QFrame.NoFrame)
        self.stickynote.setLineWidth(1)
        self.stickynote.setWidgetResizable(True)
        self.stickynote.setObjectName(_fromUtf8("stickynote"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 205, 190))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.stickynote.setWidget(self.scrollAreaWidgetContents)
        self.defsem = QtGui.QToolButton(self.centralwidget)
        self.defsem.setGeometry(QtCore.QRect(630, 510, 171, 25))
        self.defsem.setStyleSheet(_fromUtf8(""))
        self.defsem.setObjectName(_fromUtf8("defsem"))
        self.sem = QtGui.QLabel(self.centralwidget)
        self.sem.setGeometry(QtCore.QRect(149, 123, 40, 30))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.sem.setFont(font)
        self.sem.setStyleSheet(_fromUtf8("color: rgb(85, 0, 0);"))
        self.sem.setText(_fromUtf8(""))
        self.sem.setTextFormat(QtCore.Qt.AutoText)
        self.sem.setObjectName(_fromUtf8("sem"))
        self.home = QtGui.QToolButton(self.centralwidget)
        self.home.setGeometry(QtCore.QRect(630, 360, 171, 25))
        self.home.setStyleSheet(_fromUtf8(""))
        self.home.setObjectName(_fromUtf8("home"))
        self.about = QtGui.QToolButton(self.centralwidget)
        self.about.setGeometry(QtCore.QRect(630, 540, 171, 25))
        self.about.setAutoFillBackground(False)
        self.about.setStyleSheet(_fromUtf8(""))
        self.about.setObjectName(_fromUtf8("about"))
        self.help = QtGui.QToolButton(self.centralwidget)
        self.help.setGeometry(QtCore.QRect(630, 570, 171, 25))
        self.help.setAutoFillBackground(False)
        self.help.setStyleSheet(_fromUtf8(""))
        self.help.setObjectName(_fromUtf8("help"))
        self.hide = QtGui.QLabel(self.centralwidget)
        self.hide.setGeometry(QtCore.QRect(15, 150, 590, 29))
        self.hide.setObjectName(_fromUtf8("hide"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 179, 580, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.calender = QtGui.QScrollArea(self.centralwidget)
        self.calender.setGeometry(QtCore.QRect(650, 40, 131, 141))
        self.calender.setFrameShape(QtGui.QFrame.NoFrame)
        self.calender.setWidgetResizable(True)
        self.calender.setObjectName(_fromUtf8("calender"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 131, 141))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.day = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.day.setGeometry(QtCore.QRect(0, 20, 130, 80))
        self.day.setObjectName(_fromUtf8("day"))
        self.monthyear = QtGui.QLabel(self.scrollAreaWidgetContents_2)
        self.monthyear.setGeometry(QtCore.QRect(0, 100, 130, 40))
        self.monthyear.setObjectName(_fromUtf8("monthyear"))
        self.calender.setWidget(self.scrollAreaWidgetContents_2)
        window2.setCentralWidget(self.centralwidget)
        self.toolBar = QtGui.QToolBar(window2)
        self.toolBar.setIconSize(QtCore.QSize(50, 50))
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        window2.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar)
        self.home_2 = QtGui.QAction(window2)
        self.home_2.setCheckable(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/homepage/Screenshot.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.home_2.setIcon(icon)
        self.home_2.setObjectName(_fromUtf8("home_2"))

        self.retranslateUi(window2)
        self.maintabWidget.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(window2)

    def retranslateUi(self, window2):
        window2.setWindowTitle(QtGui.QApplication.translate("window2", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("window2", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600; color:#550000;\">Semester :</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.timetable.setText(QtGui.QApplication.translate("window2", "Time Table", None, QtGui.QApplication.UnicodeUTF8))
        self.editsem.setText(QtGui.QApplication.translate("window2", "Add/Delete subjects", None, QtGui.QApplication.UnicodeUTF8))
        self.cgcalc.setText(QtGui.QApplication.translate("window2", "Grades", None, QtGui.QApplication.UnicodeUTF8))
        self.calendar.setText(QtGui.QApplication.translate("window2", "Calendar", None, QtGui.QApplication.UnicodeUTF8))
        self.defsem.setText(QtGui.QApplication.translate("window2", "Set Default sem", None, QtGui.QApplication.UnicodeUTF8))
        self.home.setText(QtGui.QApplication.translate("window2", "Home", None, QtGui.QApplication.UnicodeUTF8))
        self.about.setText(QtGui.QApplication.translate("window2", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.help.setText(QtGui.QApplication.translate("window2", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.hide.setText(QtGui.QApplication.translate("window2", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.day.setText(QtGui.QApplication.translate("window2", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.monthyear.setText(QtGui.QApplication.translate("window2", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("window2", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.home_2.setText(QtGui.QApplication.translate("window2", "home", None, QtGui.QApplication.UnicodeUTF8))
        self.home_2.setToolTip(QtGui.QApplication.translate("window2", "Home", None, QtGui.QApplication.UnicodeUTF8))

