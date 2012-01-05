# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'grade.ui'
#
# Created: Sat Sep 24 18:57:55 2011
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
        Dialog.resize(404, 374)
        self.label = QtGui.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 391, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(100, 50, 67, 17))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(250, 40, 67, 17))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.num1 = QtGui.QDoubleSpinBox(Dialog)
        self.num1.setGeometry(QtCore.QRect(240, 90, 62, 27))
        self.num1.setObjectName(_fromUtf8("num1"))
        self.grade1 = QtGui.QLineEdit(Dialog)
        self.grade1.setGeometry(QtCore.QRect(90, 90, 61, 27))
        self.grade1.setObjectName(_fromUtf8("grade1"))
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(240, 60, 91, 17))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line = QtGui.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(60, 80, 300, 3))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(60, 40, 300, 3))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.line_3 = QtGui.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(196, 40, 3, 290))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.num2 = QtGui.QDoubleSpinBox(Dialog)
        self.num2.setGeometry(QtCore.QRect(240, 120, 62, 27))
        self.num2.setObjectName(_fromUtf8("num2"))
        self.grade2 = QtGui.QLineEdit(Dialog)
        self.grade2.setGeometry(QtCore.QRect(90, 120, 61, 27))
        self.grade2.setObjectName(_fromUtf8("grade2"))
        self.grade3 = QtGui.QLineEdit(Dialog)
        self.grade3.setGeometry(QtCore.QRect(90, 150, 61, 27))
        self.grade3.setObjectName(_fromUtf8("grade3"))
        self.num3 = QtGui.QDoubleSpinBox(Dialog)
        self.num3.setGeometry(QtCore.QRect(240, 150, 62, 27))
        self.num3.setObjectName(_fromUtf8("num3"))
        self.grade4 = QtGui.QLineEdit(Dialog)
        self.grade4.setGeometry(QtCore.QRect(90, 180, 61, 27))
        self.grade4.setObjectName(_fromUtf8("grade4"))
        self.num4 = QtGui.QDoubleSpinBox(Dialog)
        self.num4.setGeometry(QtCore.QRect(240, 180, 62, 27))
        self.num4.setObjectName(_fromUtf8("num4"))
        self.grade5 = QtGui.QLineEdit(Dialog)
        self.grade5.setGeometry(QtCore.QRect(90, 210, 61, 27))
        self.grade5.setObjectName(_fromUtf8("grade5"))
        self.num5 = QtGui.QDoubleSpinBox(Dialog)
        self.num5.setGeometry(QtCore.QRect(240, 210, 62, 27))
        self.num5.setObjectName(_fromUtf8("num5"))
        self.grade6 = QtGui.QLineEdit(Dialog)
        self.grade6.setGeometry(QtCore.QRect(90, 240, 61, 27))
        self.grade6.setObjectName(_fromUtf8("grade6"))
        self.num6 = QtGui.QDoubleSpinBox(Dialog)
        self.num6.setGeometry(QtCore.QRect(240, 240, 62, 27))
        self.num6.setObjectName(_fromUtf8("num6"))
        self.grade7 = QtGui.QLineEdit(Dialog)
        self.grade7.setGeometry(QtCore.QRect(90, 270, 61, 27))
        self.grade7.setObjectName(_fromUtf8("grade7"))
        self.num7 = QtGui.QDoubleSpinBox(Dialog)
        self.num7.setGeometry(QtCore.QRect(240, 270, 62, 27))
        self.num7.setObjectName(_fromUtf8("num7"))
        self.grade8 = QtGui.QLineEdit(Dialog)
        self.grade8.setGeometry(QtCore.QRect(90, 300, 61, 27))
        self.grade8.setObjectName(_fromUtf8("grade8"))
        self.num8 = QtGui.QDoubleSpinBox(Dialog)
        self.num8.setGeometry(QtCore.QRect(240, 300, 62, 27))
        self.num8.setObjectName(_fromUtf8("num8"))
        self.done = QtGui.QToolButton(Dialog)
        self.done.setGeometry(QtCore.QRect(166, 340, 60, 25))
        self.done.setObjectName(_fromUtf8("done"))

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.grade1, self.num1)
        Dialog.setTabOrder(self.num1, self.grade2)
        Dialog.setTabOrder(self.grade2, self.num2)
        Dialog.setTabOrder(self.num2, self.grade3)
        Dialog.setTabOrder(self.grade3, self.num3)
        Dialog.setTabOrder(self.num3, self.grade4)
        Dialog.setTabOrder(self.grade4, self.num4)
        Dialog.setTabOrder(self.num4, self.grade5)
        Dialog.setTabOrder(self.grade5, self.num5)
        Dialog.setTabOrder(self.num5, self.grade6)
        Dialog.setTabOrder(self.grade6, self.num6)
        Dialog.setTabOrder(self.num6, self.grade7)
        Dialog.setTabOrder(self.grade7, self.num7)
        Dialog.setTabOrder(self.num7, self.grade8)
        Dialog.setTabOrder(self.grade8, self.num8)
        Dialog.setTabOrder(self.num8, self.done)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Default Grading System", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-style:italic;\">Add grades in decreasing order of their numeric equivalence</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Grade", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Numeric", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Equivalence", None, QtGui.QApplication.UnicodeUTF8))
        self.done.setText(QtGui.QApplication.translate("Dialog", "Done", None, QtGui.QApplication.UnicodeUTF8))

