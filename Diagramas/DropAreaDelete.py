# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlHardware.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui, Qt
import DropArea as d
from PyQt4.QtCore import Qt, QMimeData
import copy,DragItem
from PyQt4.QtGui import QApplication, QDrag, QFrame, QMainWindow, QLabel
import ListOperation

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


class DropAreaDelete(d.DropArea):
    def __init__(self, parent,dropAreaContains = None):
        d.DropArea.__init__(self, parent)
        self.setStyleSheet("background-color: rgb(255, 0, 0);")
        self.setGeometry(QtCore.QRect(0, 0, 50, 50))
        self.dropAreaContains = dropAreaContains

    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin información
        if event.mimeData().hasText():
            event.acceptProposedAction()
    def dropEvent(self, event):
        val = event.source()
        if val.borrado != 1:
            return 
        dic = val.parentWidget().listaItems
        dic[val] = -1
        val.setParent(None)

        #event.acceptProposedAction()
 