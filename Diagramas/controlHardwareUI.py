# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlHardware.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import  DropArea  
import  DropAreaDelete 
import  DragItem as d  

from PyQt4 import QtCore, QtGui, Qt

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

class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName(_fromUtf8("Frame"))
        Frame.resize(580, 470)
        Frame.setFrameShape(QtGui.QFrame.StyledPanel)
        Frame.setFrameShadow(QtGui.QFrame.Raised)
        self.dragItemScrollArea = QtGui.QScrollArea(Frame)
        self.dragItemScrollArea.setGeometry(QtCore.QRect(0, 0, 141, 471))
        self.dragItemScrollArea.setStyleSheet(_fromUtf8("background-color: qradialgradient(spread:repeat, cx:0.5, cy:0.5, radius:0.077, fx:0.5, fy:0.5, stop:0 rgba(0, 169, 255, 147), stop:0.497326 rgba(0, 0, 0, 147), stop:1 rgba(0, 169, 255, 147))"))
        self.dragItemScrollArea.setWidgetResizable(True)
        self.dragItemScrollArea.setObjectName(_fromUtf8("dragItemScrollArea"))

        self.scrollAreaWidgetContents = QtGui.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 137, 467))
        self.scrollAreaWidgetContents.setObjectName(_fromUtf8("scrollAreaWidgetContents"))

        self.verticalLayoutWidget = QtGui.QWidget(self.scrollAreaWidgetContents)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1, 1, 141, 471))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))


        self.verticalLayout = QtGui.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))

        #Agregamos los items a la lista izquierda 
        item = d.DragItem(0,"----->",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem(0,"Inicio",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem(0,"Condicion",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem(0,"Instrucion",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem(0,"STD out",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem(0,"STD in",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem(0,"Fin",Frame)
        self.verticalLayout.addWidget(item)



        self.dragItemScrollArea.setWidget(self.scrollAreaWidgetContents)
        """
        item = d.DragItem("Inicio",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem("Condicion",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem("Instrucion",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem("STD out",Frame)
        self.verticalLayout.addWidget(item)
        item = d.DragItem("STD in",Frame)
        self.verticalLayout.addWidget(item)
        """

        self.deskScrollArea = DropArea.DropArea(Frame)
        self.dropAreaDelete = DropAreaDelete.DropAreaDelete(self.deskScrollArea.scrollAreaWidgetContents_2,dropAreaContains = self.deskScrollArea)
        self.retranslateUi(Frame)
        

        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        Frame.setWindowTitle(_translate("Frame", "Frame", None))

