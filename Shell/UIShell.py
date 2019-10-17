# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShellUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(426, 224)
        Form.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);"))
        self.prompt = QtGui.QLabel(Form)
        self.prompt.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.prompt.setObjectName(_fromUtf8("prompt"))
        self.stdin = QtGui.QLineEdit(Form)
        self.stdin.setGeometry(QtCore.QRect(170, 0, 261, 41))
        self.stdin.setAutoFillBackground(False)
        self.stdin.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.37619, y1:1, x2:0.37619, y2:0, stop:0.12381 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.stdin.setObjectName(_fromUtf8("stdin"))
        self.stdout = QtGui.QLabel(Form)
        self.stdout.setGeometry(QtCore.QRect(0, 49, 421, 181))
        self.stdout.setStyleSheet(_fromUtf8("background-color: rgb(0, 1, 0);"))
        self.stdout.setObjectName(_fromUtf8("stdout"))


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.prompt.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt; color:#00ff00;\">torMoSO@usuario</span></p></body></html>", None))
        self.stdout.setText(_translate("Form", "<html><head/><body><p><br/></p></body></html>", None))

