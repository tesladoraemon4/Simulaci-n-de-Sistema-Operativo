# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministradorProc.ui'
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

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName(_fromUtf8("StackedWidget"))
        StackedWidget.resize(341, 121)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.scrollArea = QtGui.QScrollArea(self.page)
        self.scrollArea.setGeometry(QtCore.QRect(-1, -2, 341, 121))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName(_fromUtf8("scrollArea"))
        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 337, 117))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))
        self.tableWidget = QtGui.QTableWidget(self.scrollAreaWidgetContents)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 341, 121))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        StackedWidget.addWidget(self.page)
        self.page1 = QtGui.QWidget()
        self.page1.setObjectName(_fromUtf8("page1"))
        self.scrollArea_2 = QtGui.QScrollArea(self.page1)
        self.scrollArea_2.setGeometry(QtCore.QRect(0, 0, 341, 121))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName(_fromUtf8("scrollArea_2"))
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 337, 117))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        StackedWidget.addWidget(self.page1)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(_translate("StackedWidget", "StackedWidget", None))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("StackedWidget", "pid", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("StackedWidget", "Nom Proceso", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("StackedWidget", "Núcleo", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("StackedWidget", "Estado", None))

