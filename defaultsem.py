# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'defaultsem.ui'
#
# Created: Sat Sep 24 18:57:12 2011
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(368, 168)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(110, 20, 71, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.sem = QtGui.QComboBox(Dialog)
        self.sem.setGeometry(QtCore.QRect(220, 15, 51, 27))
        self.sem.setObjectName(_fromUtf8("sem"))
        self.okay = QtGui.QToolButton(Dialog)
        self.okay.setGeometry(QtCore.QRect(150, 70, 71, 25))
        self.okay.setObjectName(_fromUtf8("okay"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 352, 44))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Default semester", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Semester :", None, QtGui.QApplication.UnicodeUTF8))
        self.okay.setText(QtGui.QApplication.translate("Dialog", "Okay", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">** Clicking on okay after selecting the semester will close the app. Reopen it for further use.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

