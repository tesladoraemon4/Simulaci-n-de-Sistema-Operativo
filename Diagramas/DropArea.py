# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlHardware.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
from PyQt4 import QtCore, QtGui, Qt
from PyQt4.QtCore import Qt, QMimeData
import copy
import ListOperation


from PyQt4.QtGui import QApplication, QDrag, QFrame, QMainWindow, QLabel

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

class Linea(QtGui.QWidget):
    def __init__(self, parent,xo,yo,xd,yd):
        QtGui.QWidget.__init__(self, parent)
        geoP = parent.geometry()
        self.setGeometry(QtCore.QRect(geoP.x(), geoP.y(), geoP.width(), geoP.height()))
        self.xo = xo
        self.yo = yo
        self.xd = xd
        self.yd = yd

    def paintEvent(self, event):
        qp = QtGui.QPainter()
        qp.begin(self)
        pen = QtGui.QPen(QtCore.Qt.black, 2, QtCore.Qt.SolidLine)
        qp.setPen(pen)
        qp.drawLine(self.xo,self.yo,self.xd,self.yd)
        qp.end()
    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin información
        if event.mimeData().hasText():
            event.acceptProposedAction()



        



class DropArea(QtGui.QScrollArea):
    def __init__(self, parent):
        QtGui.QScrollArea.__init__(self, parent)
        self.setAcceptDrops(True)  # Aceptar objetos
        self.setStyleSheet("background-color: #E6E6E6;")
        self.setGeometry(QtCore.QRect(140, 0, 441, 471))
        self.setStyleSheet(_fromUtf8("background-color:qconicalgradient(cx:0.5, cy:0.5, angle:0, stop:0 rgba(13, 57, 178, 255), stop:0.161905 rgba(50, 102, 145, 255), stop:0.225 rgba(41, 61, 166, 255), stop:0.285 rgba(74, 90, 204, 255), stop:0.345 rgba(108, 102, 235, 255), stop:0.415 rgba(112, 222, 245, 255), stop:0.52 rgba(76, 200, 209, 255), stop:0.57 rgba(51, 187, 173, 255), stop:0.635 rgba(42, 168, 164, 255), stop:0.695 rgba(68, 71, 202, 255), stop:0.75 rgba(86, 126, 218, 255), stop:0.815 rgba(73, 185, 208, 255), stop:0.88 rgba(51, 173, 187, 255), stop:0.935 rgba(105, 26, 137, 255), stop:1 rgba(2, 119, 128, 255));"))
        self.setWidgetResizable(True)
        self.setObjectName(_fromUtf8("deskScrollArea"))
        self.setAcceptDrops(True)
        self.scrollAreaWidgetContents_2 = QtGui.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 437, 467))
        self.scrollAreaWidgetContents_2.setObjectName(_fromUtf8("scrollAreaWidgetContents_2"))
        self.setWidget(self.scrollAreaWidgetContents_2)
        self.listaItems = {}

    def dibujarLinea(self,xo,yo,xd,yd):
        line = Linea(self,xo,yo,xd,yd)

    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin información
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dropEvent(self, event):
        # Establecer el widget en una nueva po
        pos = event.pos()
        item = event.source()
        print "lista de items"
        print self.listaItems
        if(self.listaItems.has_key(item)):
            print "la contiene"
            item = item
            geoAux = item.geometry()
            item.setGeometry(pos.x(), pos.y(),geoAux.width(),geoAux.height())
            item.show()
        else:
            if item.valStr != "----->":

                item = item.clone()

                item.id = len(self.listaItems) 

                item.setParent(self)
                geoAux = item.geometry()
                item.setGeometry(pos.x(), pos.y(),geoAux.width(),geoAux.height())
                self.listaItems[item] = 1
                item.show()
                print type(item)


        event.acceptProposedAction()

