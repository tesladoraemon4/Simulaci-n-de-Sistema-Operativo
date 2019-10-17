# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShellUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!


from PyQt4 import QtCore, QtGui
import TarjetasUi as tUi
import sys
import re
sys.path.append('../Navegador')

import ChecadorTarjetas as ct
import Tarjeta as t
import Navegador as n

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

class CheckTarjetas(QtGui.QMainWindow):
    """Checador Tarjetas.
    Padre:
        QtGui.QMainWindow
    Constructores:
        Shell(planifi=None,parent=None)
        inicializa una shell por defecto.
    """
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui= tUi.Ui_Form()
        self.ui.setupUi(self)
        #iniciamos la captura de eventos 
        self.ui.pushButton.clicked.connect(self.lanzarChequeo)
        self.checador = ct.ChecadorTarjetas()
        #Agregamos un navegador a la pestaña
        nav = n.Navegador(title = "Informacion tarjetas",urlInit="https://es.wikipedia.org/wiki/Algoritmo_de_Luhn")
        self.ui.infoTab.insertTab(1,nav,"Informacion")

        #https://www.pcihispano.com/como-funcionan-las-tarjetas-de-pago-parte-i-pan-primary-account-number/


    def lanzarChequeo(self):
        """Funcion que se ejecuta cuanto se requiere chequear una tarjeta.
            Obtiene los parametros necesarios para hacer el chequeo de una tarjeta.
            Parámetros:
                (void)
            Retorno:
                void
        """
        numeroTarjeta =  self.ui.lineEdit.text()
        print "numero tar"+str(numeroTarjeta)
        if(re.match(r'[0-9]+',numeroTarjeta)):
            tarjeta = t.Tarjeta(numero = self.ui.lineEdit.text())
            
            tarjeta.consultarCaracteristicas()
            listaValores = tarjeta.toString().split('\n')
            self.ui.listWidget.clear()
            for x in listaValores:
                item = QtGui.QListWidgetItem(x)
                self.ui.listWidget.addItem(item)
        else:
            self.ui.listWidget.clear()
            item = QtGui.QListWidgetItem("Introdujo mal el numero de se tarjeta")
            self.ui.listWidget.addItem(item)





if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = CheckTarjetas()
    myapp.show()
    sys.exit(app.exec_())
"""
"""