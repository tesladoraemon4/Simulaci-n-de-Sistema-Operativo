# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nodoConect.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(242, 181)
        Dialog.setStyleSheet(_fromUtf8("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(63, 219, 233, 255), stop:0.143495 rgba(48, 26, 137, 255), stop:0.469194 rgba(99, 7, 177, 255), stop:0.649289 rgba(57, 73, 255, 255), stop:0.867299 rgba(34, 255, 244, 255))"))
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(10, 130, 221, 41))
        self.buttonBox.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
""))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayoutWidget = QtGui.QWidget(Dialog)
        self.formLayoutWidget.setGeometry(QtCore.QRect(0, 0, 241, 121))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        self.label.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.466667 rgba(21, 26, 221, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        self.label_2.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.466667 rgba(21, 26, 221, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_2)
        self.selectNodoOrigen = QtGui.QComboBox(self.formLayoutWidget)
        self.selectNodoOrigen.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.466667 rgba(21, 26, 221, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.selectNodoOrigen.setObjectName(_fromUtf8("selectNodoOrigen"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.selectNodoOrigen)
        self.selectNodoDestino = QtGui.QComboBox(self.formLayoutWidget)
        self.selectNodoDestino.setMaximumSize(QtCore.QSize(138, 23))
        self.selectNodoDestino.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.466667 rgba(21, 26, 221, 255), stop:1 rgba(255, 255, 255, 255));"))
        self.selectNodoDestino.setObjectName(_fromUtf8("selectNodoDestino"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.selectNodoDestino)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(1, QtGui.QFormLayout.LabelRole, spacerItem)
        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.label.setText(_translate("Dialog", "NO", None))
        self.label_2.setText(_translate("Dialog", "ND", None))

