# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addref.ui'
#
# Created: Sat Sep 24 18:55:40 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName(_fromUtf8("window"))
        window.resize(429, 186)
        window.setStyleSheet(_fromUtf8("color: rgb(85, 0, 0);"))
        self.centralwidget = QtGui.QWidget(window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.subjectcode = QtGui.QLabel(self.centralwidget)
        self.subjectcode.setGeometry(QtCore.QRect(140, 20, 251, 17))
        self.subjectcode.setObjectName(_fromUtf8("subjectcode"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.browse = QtGui.QToolButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(350, 90, 71, 21))
        self.browse.setObjectName(_fromUtf8("browse"))
        self.path2 = QtGui.QLabel(self.centralwidget)
        self.path2.setGeometry(QtCore.QRect(20, 80, 51, 17))
        self.path2.setObjectName(_fromUtf8("path2"))
        self.add = QtGui.QToolButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(170, 150, 41, 25))
        self.add.setObjectName(_fromUtf8("add"))
        self.reference = QtGui.QLineEdit(self.centralwidget)
        self.reference.setGeometry(QtCore.QRect(140, 50, 141, 21))
        self.reference.setObjectName(_fromUtf8("reference"))
        self.referencepath = QtGui.QTextBrowser(self.centralwidget)
        self.referencepath.setGeometry(QtCore.QRect(70, 80, 270, 50))
        self.referencepath.setObjectName(_fromUtf8("referencepath"))
        window.setCentralWidget(self.centralwidget)
        self.label_3.setBuddy(self.reference)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(QtGui.QApplication.translate("window", "Add Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("window", "Course Code :", None, QtGui.QApplication.UnicodeUTF8))
        self.subjectcode.setText(QtGui.QApplication.translate("window", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("window", "Reference title :", None, QtGui.QApplication.UnicodeUTF8))
        self.browse.setText(QtGui.QApplication.translate("window", "Browse", None, QtGui.QApplication.UnicodeUTF8))
        self.path2.setText(QtGui.QApplication.translate("window", "Path :", None, QtGui.QApplication.UnicodeUTF8))
        self.add.setText(QtGui.QApplication.translate("window", "Add", None, QtGui.QApplication.UnicodeUTF8))
        self.referencepath.setHtml(QtGui.QApplication.translate("window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Please click on the browse button and select a file.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

