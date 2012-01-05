# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reminder.ui'
#
# Created: Sat Sep 24 18:58:20 2011
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
        Dialog.resize(394, 206)
        Dialog.setStyleSheet(_fromUtf8("color: rgb(85, 0, 0);"))
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(10, 10, 130, 17))
        self.label_5.setStyleSheet(_fromUtf8("font: 75 12pt \"Ubuntu\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(84, 12, 300, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 69, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.sub = QtGui.QComboBox(Dialog)
        self.sub.setGeometry(QtCore.QRect(110, 63, 85, 27))
        self.sub.setObjectName(_fromUtf8("sub"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 106, 101, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.desc = QtGui.QLineEdit(Dialog)
        self.desc.setGeometry(QtCore.QRect(110, 100, 271, 27))
        self.desc.setObjectName(_fromUtf8("desc"))
        self.add = QtGui.QToolButton(Dialog)
        self.add.setGeometry(QtCore.QRect(60, 150, 80, 25))
        self.add.setObjectName(_fromUtf8("add"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 38, 67, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.date = QtGui.QLabel(Dialog)
        self.date.setGeometry(QtCore.QRect(110, 39, 121, 17))
        self.date.setObjectName(_fromUtf8("date"))
        self.add_3 = QtGui.QToolButton(Dialog)
        self.add_3.setGeometry(QtCore.QRect(220, 150, 101, 25))
        self.add_3.setObjectName(_fromUtf8("add_3"))
        self.tasksaved = QtGui.QLabel(Dialog)
        self.tasksaved.setGeometry(QtCore.QRect(120, 184, 141, 17))
        self.tasksaved.setText(_fromUtf8(""))
        self.tasksaved.setObjectName(_fromUtf8("tasksaved"))

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.add_3, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Add Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Subject :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Description :", None, QtGui.QApplication.UnicodeUTF8))
        self.add.setText(QtGui.QApplication.translate("Dialog", "Add Task", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Date :", None, QtGui.QApplication.UnicodeUTF8))
        self.date.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.add_3.setText(QtGui.QApplication.translate("Dialog", "Done Adding", None, QtGui.QApplication.UnicodeUTF8))

