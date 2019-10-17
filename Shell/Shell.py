# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ShellUI.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

import sys
sys.path.append('../ManejadorGUI')
import ManejadorGUI as mgaGUI
from PyQt4 import QtCore, QtGui
import UIShell as s
import re
import shutil, os

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

ROOT = "/home/david/Documentos/proyectos/ProyectoSO/ROOT/"
HOME = "home/"
DIRARCHIVOS = ROOT+HOME



class Shell(QtGui.QMainWindow):
    """Obstrae una  shell para comunicarse con el SO.
    Padre:
        QtGui.QMainWindow
    Constructores:
        Shell(planifi=None,parent=None)
        inicializa una shell por defecto.
    """
    def __init__(self,planifi=None,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui= s.Ui_Form()
        self.ui.setupUi(self)
        self.planifi = planifi
        self.manejadorGUI= mgaGUI.ManejadorGUI()

    def lanzarcoMando(self):
        """Captura los comandos escritos en la Shell y lanza los comando que estan disponibles.
            Parámetros:
                (void)
            Retorno:
                void
        """
        grafica = self.ui
        cadena= str(grafica.stdin.text())
        grafica.stdin.setText("")
        print cadena
        elementosCad = cadena.split(" ")
        cad1 = "<html><head/><body><p><span style=\" font-size:14pt; color:#00ff00;\">"
        cad2 ="</span></p></body></html>"
        if(re.match(r'( )*mkdir .*',cadena)):
            self.mkdir(elementosCad[1])
        elif(re.match(r'( )*touch .*',cadena)):
            self.touch(elementosCad[1])
        elif(re.match(r'( )*rm .*',cadena)):
            self.rm(elementosCad[1])
        elif(re.match(r'( )*cat .*',cadena)):
            rs = self.cat(elementosCad[1])
            grafica.stdout.setText(cad1+rs.replace('\n',"<br>")+cad2)
        elif(re.match(r'( )*kill .*',cadena)):
            self.manejadorGUI.killPid(int(elementosCad[1]))
        elif(re.match(r'( )*ps( )*',cadena)):
            self.ps()
        elif(re.match(r'( )*cp( )+.*( )+',cadena)):
            self.cp(elementosCad[1],elementosCad[2])
        elif(re.match(r'( )*mv( )+.*( )+',cadena)):
            self.mv(elementosCad[1],elementosCad[2])
        elif(re.match(r'( )*correrAplicacion( )+.*( )*',cadena)):
            grafica.stdout(self.correrAplicacion(elementosCad[1]))
        else:
            grafica.stdout.setText(cad1+"Ningun comando coincide"+cad2)

    lanzarcoMando.__doc__ = """Este es un nuevo docstring."""  
    def keyPressEvent(self, event):
        """(SobreEscrita) Se detecta si se escribio enter en la shell.
            Parámetros:
                (*event:QKeyEvent)
            Retorno:
                void
        """
        key = event.key()
        print "evento key "+str(key)
        if(key == 0x01000005):
            self.lanzarcoMando()


    def correrAplicacion(self,nomApplication):
        """Crea un directorio en el SO.
            Hace un directorio en la carpeta interna del SO, la ruta raiz se encuentra guardada en la variable ROOT y la ruta del directorio se encuentra guardada en la variable HOME
            Parámetros:
                (ruta)
            Retorno:
                void
        """
        if(len(nomApplication)==0):
            return "El comando debe ser de la siguiente forma \n correrAplicacion (Shell|Navegador|Control)"
        cad = ""
        if nombre == "Shell":
            self.manejadorGUI.GUI.iniciarShell()
        elif nombre == "Navegador":
            self.manejadorGUI.GUI.iniciarNavegador()
        elif nombre == "Control":
            self.manejadorGUI.GUI.iniciarControlHard()
        else:
            cad += "No se encuentra la aplicacion "+str(nomApplication)
        return cad




    def mkdir(self,ruta):
        """Crea un directorio en el SO.
            Hace un directorio en la carpeta interna del SO, la ruta raiz se encuentra guardada en la variable ROOT y la ruta del directorio se encuentra guardada en la variable HOME
            Parámetros:
                (ruta)
            Retorno:
                void
        """
        global DIRARCHIVOS
        cad = ""
        try:
            os.makedirs(DIRARCHIVOS+ruta)
        except OSError:
            pass
        # si no podemos crear la ruta dejamos que pase
        os.chdir(ruta)
        return cad

    def touch(self,ruta):
        """Crea un archivo en el SO.
            Hace un archivo en la carpeta interna del SO, la ruta raiz se encuentra guardada en la variable ROOT y la ruta del directorio se encuentra guardada en la variable HOME
            Parámetros:
                (ruta)
            Retorno:
                void
        """
        global DIRARCHIVOS

        cad = ""
        arch = None
        try:
            arch = open(DIRARCHIVOS+ruta, "w")

        except OSError:
            pass
        arch.close()
        return cad


    def rm(self,ruta):
        """Remueve un archivo del SO.
            Remueve un archivo en la carpeta interna del SO, la ruta raiz se encuentra guardada en la variable ROOT y la ruta del directorio se encuentra guardada en la variable HOME
            Parámetros:
                (ruta)
            Retorno:
                void
        """
        global DIRARCHIVOS
        cad = ""
        try:
            ObjArchivo = os.remove(DIRARCHIVOS+ruta)
        except OSError:
            print("No se pudo remover el archivo especificado")
        return cad


    def cat(self,ruta):
        """Muestra un archivo de texto ya guardado en el SO.
            Remueve un archivo en la carpeta interna del SO, la ruta raiz se encuentra guardada en la variable ROOT y la ruta del directorio se encuentra guardada en la variable HOME
            Parámetros:
                (ruta)
            Retorno:
                void
        """
        global DIRARCHIVOS
        cad = ""
        try:
            archivo = open(DIRARCHIVOS+ruta, "r")
            for linea in archivo.readlines():
                cad += linea
                print (linea)
            archivo.close() 
        except OSError:
            print("No se pudo mostrar el archivo especificado")
        return cad

    def ps(self):
        """Consulta todos los procesos que se estan ejecutando en el SO.
            Hace la consulta de <Tabla de procesos> del SO. 
            Parámetros:
                (void)
            Retorno:
                resultado:str
        """
        cad = ""
        tabla1AdmonProc = self.planifi.GUI.tablePart1

        #tabla = [[0 for x in range(x)] for y in range(y)]
        ##COnsultamos todas las tablas 
        numFilas = tabla1AdmonProc.rowCount()
        numColumnas = tabla1AdmonProc.columnCount()

        for filaI in range(numFilas):
            for colI in range(numColumnas):
                print tabla1AdmonProc.item(filaI,colI).text()
            print ""

        return cad
    def cp(self,origen,destino):
        """Copia un archivo.
            Copia un archivo de su ruta origen a la ruta destino.
            Parámetros:
                (origen,destino)
            Retorno:
                void
        """
        global DIRARCHIVOS
        origen = DIRARCHIVOS+origen
        destino = DIRARCHIVOS+destino
        if os.path.exists(origen):
            with open(origen, 'rb') as forigen:
                with open(destino, 'wb') as fdestino:
                    shutil.copyfileobj(forigen, fdestino)
                    print("Archivo copiado")

    def mv(self,origen,destino):
        """Mueve un archivo.
            Mueve un archivo de su ruta origen a la ruta destino iniciando como directorio raiz la variable DIRARCHIVOS
            Parámetros:
                (origen,destino)
            Retorno:
                void
        """
        global DIRARCHIVOS
        origen = DIRARCHIVOS+origen
        destino = DIRARCHIVOS+destino
        if os.path.exists(origen):  
            ruta = shutil.move(origen, destino)
            return ('El directorio ha sido movido')
        else:
            return ('El directorio origen no existe')




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Shell()
    myapp.show()
    sys.exit(app.exec_())