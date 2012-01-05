# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addref.ui'
#
# Created: Thu Jan  5 14:46:23 2012
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_window(object):
    def setupUi(self, window):
        window.setObjectName("window")
        window.resize(429, 251)
        window.setStyleSheet("color: rgb(85, 0, 0);")
        self.centralwidget = QtGui.QWidget(window)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.label.setObjectName("label")
        self.subjectcode = QtGui.QLabel(self.centralwidget)
        self.subjectcode.setGeometry(QtCore.QRect(140, 20, 251, 17))
        self.subjectcode.setObjectName("subjectcode")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.label_3.setObjectName("label_3")
        self.browse = QtGui.QToolButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(350, 90, 71, 21))
        self.browse.setObjectName("browse")
        self.path2 = QtGui.QLabel(self.centralwidget)
        self.path2.setGeometry(QtCore.QRect(20, 80, 51, 17))
        self.path2.setObjectName("path2")
        self.add = QtGui.QToolButton(self.centralwidget)
        self.add.setGeometry(QtCore.QRect(170, 150, 41, 25))
        self.add.setObjectName("add")
        self.reference = QtGui.QLineEdit(self.centralwidget)
        self.reference.setGeometry(QtCore.QRect(140, 50, 141, 21))
        self.reference.setObjectName("reference")
        self.referencepath = QtGui.QTextBrowser(self.centralwidget)
        self.referencepath.setGeometry(QtCore.QRect(70, 80, 270, 50))
        self.referencepath.setObjectName("referencepath")
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(28, 182, 370, 55))
        self.textBrowser_2.setObjectName("textBrowser_2")
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
        self.textBrowser_2.setHtml(QtGui.QApplication.translate("window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">-- Please make sure that the file name or in the path of the file,</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\"> there is no blank space used. For example, &quot;Wrong example.pdf&quot; </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt;\">and &quot;home/documents/imp notes/notes.pdf&quot; are invalid.</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

