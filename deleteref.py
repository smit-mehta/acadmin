# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteref.ui'
#
# Created: Sat Sep 24 18:57:26 2011
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
        Dialog.resize(400, 173)
        Dialog.setStyleSheet(_fromUtf8("color: rgb(85, 0, 0);"))
        self.path2 = QtGui.QLabel(Dialog)
        self.path2.setGeometry(QtCore.QRect(20, 80, 51, 17))
        self.path2.setObjectName(_fromUtf8("path2"))
        self.deletebutton = QtGui.QToolButton(Dialog)
        self.deletebutton.setGeometry(QtCore.QRect(150, 140, 71, 25))
        self.deletebutton.setObjectName(_fromUtf8("deletebutton"))
        self.subjectcode = QtGui.QLabel(Dialog)
        self.subjectcode.setGeometry(QtCore.QRect(140, 20, 251, 17))
        self.subjectcode.setObjectName(_fromUtf8("subjectcode"))
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 17))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 111, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.references = QtGui.QComboBox(Dialog)
        self.references.setGeometry(QtCore.QRect(140, 46, 231, 27))
        self.references.setObjectName(_fromUtf8("references"))
        self.referencepath = QtGui.QTextBrowser(Dialog)
        self.referencepath.setGeometry(QtCore.QRect(90, 80, 280, 50))
        self.referencepath.setObjectName(_fromUtf8("referencepath"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Delete References", None, QtGui.QApplication.UnicodeUTF8))
        self.path2.setText(QtGui.QApplication.translate("Dialog", "Path :", None, QtGui.QApplication.UnicodeUTF8))
        self.deletebutton.setText(QtGui.QApplication.translate("Dialog", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.subjectcode.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "Course Code :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Reference title :", None, QtGui.QApplication.UnicodeUTF8))

