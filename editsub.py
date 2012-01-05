# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editsub.ui'
#
# Created: Mon Sep 26 13:22:15 2011
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
        Dialog.resize(393, 207)
        Dialog.setStyleSheet(_fromUtf8("color: rgb(85, 0, 0);"))
        self.subjectname = QtGui.QLineEdit(Dialog)
        self.subjectname.setGeometry(QtCore.QRect(110, 47, 271, 27))
        self.subjectname.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.subjectname.setObjectName(_fromUtf8("subjectname"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(7, 83, 56, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(7, 15, 92, 17))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(7, 51, 97, 17))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.change = QtGui.QToolButton(Dialog)
        self.change.setGeometry(QtCore.QRect(80, 170, 61, 25))
        self.change.setObjectName(_fromUtf8("change"))
        self.toolButton_2 = QtGui.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(230, 170, 71, 25))
        self.toolButton_2.setObjectName(_fromUtf8("toolButton_2"))
        self.label_9 = QtGui.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(9, 113, 151, 17))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog)
        self.label_10.setGeometry(QtCore.QRect(9, 143, 161, 17))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.classes = QtGui.QSpinBox(Dialog)
        self.classes.setGeometry(QtCore.QRect(180, 110, 59, 27))
        self.classes.setObjectName(_fromUtf8("classes"))
        self.attendance = QtGui.QDoubleSpinBox(Dialog)
        self.attendance.setGeometry(QtCore.QRect(180, 140, 62, 27))
        self.attendance.setObjectName(_fromUtf8("attendance"))
        self.subjectcode = QtGui.QLabel(Dialog)
        self.subjectcode.setGeometry(QtCore.QRect(110, 15, 67, 17))
        self.subjectcode.setObjectName(_fromUtf8("subjectcode"))
        self.credits = QtGui.QSpinBox(Dialog)
        self.credits.setGeometry(QtCore.QRect(110, 80, 59, 27))
        self.credits.setObjectName(_fromUtf8("credits"))
        self.label_6.setBuddy(self.subjectname)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.toolButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.subjectname, self.classes)
        Dialog.setTabOrder(self.classes, self.attendance)
        Dialog.setTabOrder(self.attendance, self.change)
        Dialog.setTabOrder(self.change, self.toolButton_2)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Edit subject", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Credits :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Course Code :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Dialog", "Course Name :", None, QtGui.QApplication.UnicodeUTF8))
        self.change.setText(QtGui.QApplication.translate("Dialog", "Change", None, QtGui.QApplication.UnicodeUTF8))
        self.toolButton_2.setText(QtGui.QApplication.translate("Dialog", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Dialog", "Total No. of Classes :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("Dialog", "% attendance required :", None, QtGui.QApplication.UnicodeUTF8))
        self.subjectcode.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))

