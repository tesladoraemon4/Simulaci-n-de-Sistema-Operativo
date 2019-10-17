# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tarjetasUI.ui'
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
        Form.resize(579, 470)
        self.infoTab = QtGui.QTabWidget(Form)
        self.infoTab.setGeometry(QtCore.QRect(0, 0, 581, 471))
        self.infoTab.setStyleSheet(_fromUtf8("background-color: qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(63, 219, 233, 255), stop:0.143495 rgba(48, 26, 137, 255), stop:0.469194 rgba(99, 7, 177, 255), stop:0.649289 rgba(57, 73, 255, 255), stop:0.867299 rgba(34, 255, 244, 255));"))
        self.infoTab.setObjectName(_fromUtf8("infoTab"))
        self.infoTabPage1_2 = QtGui.QWidget()
        self.infoTabPage1_2.setObjectName(_fromUtf8("infoTabPage1_2"))
        self.pushButton = QtGui.QPushButton(self.infoTabPage1_2)
        self.pushButton.setGeometry(QtCore.QRect(440, 50, 97, 27))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.lineEdit = QtGui.QLineEdit(self.infoTabPage1_2)
        self.lineEdit.setGeometry(QtCore.QRect(50, 50, 341, 25))
        self.lineEdit.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.infoTabPage1_2)
        self.label.setGeometry(QtCore.QRect(50, 10, 331, 31))
        self.label.setStyleSheet(_fromUtf8("background-color: rgb(255, 255, 255);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.listWidget = QtGui.QListWidget(self.infoTabPage1_2)
        self.listWidget.setGeometry(QtCore.QRect(30, 140, 501, 241))
        self.listWidget.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(0, 0, 0, 255), stop:0.19397 rgba(0, 0, 0, 255), stop:0.202312 rgba(122, 97, 0, 255), stop:0.495514 rgba(2, 0, 211, 255), stop:0.504819 rgba(49, 68, 255, 255), stop:0.79 rgba(255, 13, 13, 255), stop:1 rgba(255, 69, 69, 255));"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.label_2 = QtGui.QLabel(self.infoTabPage1_2)
        self.label_2.setGeometry(QtCore.QRect(40, 90, 171, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.infoTab.addTab(self.infoTabPage1_2, _fromUtf8(""))

        self.retranslateUi(Form)
        self.infoTab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.infoTab.setToolTip(_translate("Form", "<html><head/><body><p>QAOI{FLJASpf{ASFASfAS</p></body></html>", None))
        self.infoTabPage1_2.setWhatsThis(_translate("Form", "<html><head/><body><p>agasdfasdfasdf</p><p><br/></p></body></html>", None))
        self.pushButton.setText(_translate("Form", "Validar", None))
        self.label.setText(_translate("Form", "Inserte el numero de la tarjeta", None))
        self.label_2.setText(_translate("Form", "Caracteristicas", None))
        self.infoTab.setTabText(self.infoTab.indexOf(self.infoTabPage1_2), _translate("Form", "Validador", None))

