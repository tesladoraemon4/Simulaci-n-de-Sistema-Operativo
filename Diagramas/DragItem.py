# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DragItemUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt4 import *
from PyQt4.QtCore import Qt, QMimeData
import nodoConect

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
class DragItem(QtGui.QLabel):
    def __init__(self,borrado=0, valStr="value",parent=None,id=None):
        self.parent = parent
        QtGui.QLabel.__init__(self,parent)
        self.setText(valStr)
        self.setupUi(self)
        self.borrado = borrado
        self.valStr = valStr
        self.id = id
        self.vertices = []
        self.setAcceptDrops(True)  # Aceptar objetos

    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(127, 75)
        self.setStyleSheet("background-color: white;")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
    def mousePressEvent(self, event):
        # Inicializar el arrastre con el botón derecho
        if event.button() == Qt.LeftButton:
            self.drag_start_position = event.pos()
        
    def mouseMoveEvent(self, event):
        # Chequear que se esté presionando el botón derecho
        if not (event.buttons() and Qt.LeftButton):
            return
        
        # Verificar que sea una posición válida
        if ((event.pos() - self.drag_start_position).manhattanLength()
            < QApplication.startDragDistance()):
            return
        
        drag = QDrag(self)
        mime_data = QMimeData()
        
        # Establecer el contenido del widget como dato
        mime_data.setText(self.text())
        drag.setMimeData(mime_data)
        
        # Ejecutar la acción
        self.drop_action = drag.exec_(Qt.CopyAction | Qt.MoveAction)
    
    def dragEnterEvent(self, event):
        # Ignorar objetos arrastrados sin información
        if event.mimeData().hasText():
            event.acceptProposedAction()
    def dropEvent(self, event):
        # Sueltan una flecha
        item = event.source()
        if item.text() != "----->":
            return

        dicNodos = self.parentWidget().listaItems
        nodos = []
        for (k,v) in dicNodos.items():
            print v
            if v!=-1:
                   nodos.append(k)
        print "lista de nodos "

        ventana = nodoConect.nodoConect(nodoO=self,nodos=nodos)
        if ventana.exec_() != QtGui.QDialog.Accepted:
            return 

        no = ventana.POST['NO']
        nd = ventana.POST['ND']
        print no
        idNo = int(no[no.index('(')+1:no.index(')')])
        idNd = int(nd[nd.index('(')+1:nd.index(')')])
        print "id nodo origen "+str(idNo)
        print "id nodo destino "+str(idNd)

        #buscamos los items 

        listaItems = self.parentWidget().listaItems.items()
        nodoO = None
        nodoD = None

        for (k,v) in listaItems:
            if v!=-1:
                if k.id == idNo:
                    nodoO = k
                if k.id == idNd:
                    nodoD = k

        gOrigenX = nodoO.geometry().x()
        gOrigenY = nodoO.geometry().y()


        gDestinoX = nodoD.geometry().x()
        gDestinoY = nodoD.geometry().y()

        linea = QtCore.QLine(gOrigenX,gOrigenY,gDestinoX,gDestinoY)
        linea.show()





    def destroy(self):
        self = None

    def clone(self):
        copia = DragItem(1,self.text(),self.parent)
        return copia


"""
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = DragItem()31

    myapp.show()
    sys.exit(app.exec_())
"""
