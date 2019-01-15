# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'py.ui'
#
# Created: Sun Apr 26 21:40:58 2015
#      by: PyQt4 UI code generator 4.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Tf_dialog(object):
    def setupUi(self, Tf_dialog):
        Tf_dialog.setObjectName(_fromUtf8("Tf_dialog"))
        Tf_dialog.resize(618, 384)
        self.Tf_button = QtGui.QPushButton(Tf_dialog)
        self.Tf_button.setGeometry(QtCore.QRect(490, 20, 101, 31))
        self.Tf_button.setObjectName(_fromUtf8("Tf_button"))
        self.Tf_table = QtGui.QTextBrowser(Tf_dialog)
        self.Tf_table.setGeometry(QtCore.QRect(30, 80, 561, 271))
        self.Tf_table.setObjectName(_fromUtf8("Tf_table"))
        self.Tf_text = QtGui.QLineEdit(Tf_dialog)
        self.Tf_text.setGeometry(QtCore.QRect(50, 19, 421, 31))
        self.Tf_text.setObjectName(_fromUtf8("Tf_text"))

        self.retranslateUi(Tf_dialog)
        #QtCore.QObject.connect(self.Tf_button, QtCore.SIGNAL(_fromUtf8("clicked()")), self.Tf_table.show)
        QtCore.QMetaObject.connectSlotsByName(Tf_dialog)

    def retranslateUi(self, Tf_dialog):
        Tf_dialog.setWindowTitle(_translate("Tf_dialog", "TFTable", None))
        self.Tf_button.setText(_translate("Tf_dialog", "Generate Table", None))

