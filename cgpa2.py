# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cgpa2.ui'
#
# Created: Sat Sep 24 18:56:50 2011
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
        Dialog.resize(751, 466)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 350, 17))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.textBrowser = QtGui.QTextBrowser(Dialog)
        self.textBrowser.setGeometry(QtCore.QRect(0, 10, 741, 51))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setGeometry(QtCore.QRect(40, 120, 291, 251))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 380, 171, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 400, 221, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(370, 100, 71, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gpa = QtGui.QLabel(Dialog)
        self.gpa.setGeometry(QtCore.QRect(260, 380, 67, 17))
        self.gpa.setObjectName(_fromUtf8("gpa"))
        self.semcredits = QtGui.QLabel(Dialog)
        self.semcredits.setGeometry(QtCore.QRect(260, 400, 67, 17))
        self.semcredits.setObjectName(_fromUtf8("semcredits"))
        self.cgpa = QtGui.QLabel(Dialog)
        self.cgpa.setGeometry(QtCore.QRect(460, 100, 67, 17))
        self.cgpa.setObjectName(_fromUtf8("cgpa"))
        self.netcredits = QtGui.QLabel(Dialog)
        self.netcredits.setGeometry(QtCore.QRect(460, 120, 67, 17))
        self.netcredits.setObjectName(_fromUtf8("netcredits"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(370, 120, 81, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.graph = QtGui.QLabel(Dialog)
        self.graph.setGeometry(QtCore.QRect(380, 160, 341, 270))
        self.graph.setObjectName(_fromUtf8("graph"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "CGPA Analysis", None, QtGui.QApplication.UnicodeUTF8))
        self.textBrowser.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"> -- All CGPA calculations are done on the basis of following. To Edit, go back and enter/edit concerned subjects in concerned semetsers </p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "GPA for this semester :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Total credits for this semester :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Net CGPA :", None, QtGui.QApplication.UnicodeUTF8))
        self.gpa.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.semcredits.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.cgpa.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.netcredits.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "Net Credits :", None, QtGui.QApplication.UnicodeUTF8))
        self.graph.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

