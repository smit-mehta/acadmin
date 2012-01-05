# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'timetable.ui'
#
# Created: Sat Sep 24 18:58:27 2011
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
        window.resize(602, 354)
        self.centralwidget = QtGui.QWidget(window)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tt = QtGui.QTableWidget(self.centralwidget)
        self.tt.setGeometry(QtCore.QRect(2, 20, 570, 256))
        self.tt.setObjectName(_fromUtf8("tt"))
        self.tt.setColumnCount(0)
        self.tt.setRowCount(0)
        self.sem = QtGui.QComboBox(self.centralwidget)
        self.sem.setGeometry(QtCore.QRect(167, 290, 51, 30))
        self.sem.setObjectName(_fromUtf8("sem"))
        self.edit = QtGui.QToolButton(self.centralwidget)
        self.edit.setGeometry(QtCore.QRect(240, 290, 121, 30))
        self.edit.setObjectName(_fromUtf8("edit"))
        window.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(window)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        window.setStatusBar(self.statusbar)

        self.retranslateUi(window)
        QtCore.QMetaObject.connectSlotsByName(window)

    def retranslateUi(self, window):
        window.setWindowTitle(QtGui.QApplication.translate("window", "Timetable", None, QtGui.QApplication.UnicodeUTF8))
        self.edit.setText(QtGui.QApplication.translate("window", "Make Changes", None, QtGui.QApplication.UnicodeUTF8))

