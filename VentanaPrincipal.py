# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministradorProc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
from probando import *

sys.path.append('AdministradorMemoria')
import AdministradorMemoria as admon

sys.path.append('Planificador')
import planificadorVer2 as p
sys.path.append('ManejadorGUI')
import ManejadorGUI as mgaGUI
sys.path.append('Procesador')
import HiloNotificaciones as Hn
import listaCircular
import Proceso
sys.path.append('Tarjetas')
sys.path.append('Navegador')
import Procesador
import CheckTarjetas
import random as r
import  time as t

CARGAMAX = 20
TEMPMAX = 40    
CARGAPORPROCESO = 5
TEMOPORPROCESO = 10


COL_PID = 0
COL_NOMBRE = 1
COL_TIEMPO = 2
COL_NUCLEO = 3
COL_EDO = 4
sys.path.append('Diagramas')
sys.path.append('Navegador')
sys.path.append('Shell')
import controlHardware
import Shell 
import Navegador



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
class VentanaPrincipal(QtGui.QMainWindow):

    __instance = None

    @staticmethod
    def getInstance():
        """Obtiene la instancia ya creada de la ventana principal.
            Parámetros:
                (void)
            Retorno:
                VentanaPrincipal
        """
        if VentanaPrincipal.__instance == None:
            VentanaPrincipal()
        return VentanaPrincipal.__instance 
    def __init__(self, parent=None):
        if VentanaPrincipal.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            QtGui.QWidget.__init__(self,parent)
            self.ui=Ui_MainWindow()
            self.ui.setupUi(self)
            self.hiloNotificaciones = Hn.HiloNotificaciones(self.ui.notificaciones)
            self.dicWindowMDI = []
            self.cont = 0
            ##pruebas 1
            QtCore.QObject.connect(self.ui.probar1,QtCore.SIGNAL("clicked()"),self.iniciarShell)
            ##pruebas 2
            QtCore.QObject.connect(self.ui.pushButton,QtCore.SIGNAL("clicked()"),self.funTest)
            #iniciar shell
            QtCore.QObject.connect(self.ui.actionShell,QtCore.SIGNAL("triggered()"),self.iniciarShell)
            #iniciar navegador
            QtCore.QObject.connect(self.ui.actionNavegador,QtCore.SIGNAL("triggered()"),self.iniciarNavegador)
             #iniciar control hard
            QtCore.QObject.connect(self.ui.actionControl_Hardware,QtCore.SIGNAL("triggered()"),self.iniciarControlHard)
            #inicia las tarjetas
            QtCore.QObject.connect(self.ui.actionValidadorTarjetas,QtCore.SIGNAL("triggered()"),self.iniciarValidador)
            #creamos el planificador con n procesadores 
            procecs = self.crearProcesadores(int(sys.argv[1]))
            self.planificador = p.Planificador(procesadores = procecs,
                GUI = self.ui,
                notificaciones = self.hiloNotificaciones )
            self.administradorMemoria = admon.AdministradorMemoria()

            #damos a cada procesador su propio planificador
            for x in self.planificador.procesadores:
                x.planificador = self.planificador
            #planifica los procesos para el primer hilo
            self.manejadorGUI = mgaGUI.ManejadorGUI()
            self.manejadorGUI.ventanaPrincipal = self

            self.band = False
            VentanaPrincipal.__instance = self
            #inicializamos la gui de las memorias
            self.manejadorGUI.inicializarGuiMemorias()

            self.procesosInitSO()

    def crearProcesadores(self,nProc):
        """Crea un numero n de procesadores.
            Parámetros:
                (nProc:int)
            Retorno:
                [procesador,....]
        """
        procesadores = []
        for x in range(nProc):
            proc = Procesador.Procesador(x,.5,CARGAMAX,TEMPMAX)
            procesadores.append(proc)
        return procesadores
    def procesosInitSO(self):
        """Crea los procesos para inicializar el SO.
            Parámetros:
                (nProc:int)
            Retorno:
                procesadores:[]
        """
        procesosInit = []
        proc = Proceso.Proceso(int(t.time()+3)%1000,"UI",tiempo = 0,edo = "R")
        procesosInit.append(proc)
        for x in procesosInit:
            self.planificador.planificarProceso(x)
            #iniciamos la administracion de memoria 
            self.administradorMemoria.agregarProceso(x)
            t.sleep(1)
            self.manejadorGUI.actualizarMemorias(self.administradorMemoria)


        procesadores = self.planificador.procesadores
        for proc in procesadores:
            #        def crearFilaNucleos(self,procesador,gui):
            self.manejadorGUI.crearFilaNucleos(proc,self.ui)




    def iniciarValidador(self):
        """Inicia el validador de tarjetas.
            Parámetros:
                (void)
            Retorno:
                void
        """
        self.addSubwindow("ValidadorTarjetas")
        self.updateNotificaciones("Validador tarjetas lanzada")

    def iniciarShell(self):
        """Inicia la ventana Shell.
            Parámetros:
                (void)
            Retorno:
                void
        """
        self.addSubwindow("Shell")
        self.updateNotificaciones("Shell lanzada")
    def iniciarNavegador(self):
        """Inicia la ventana Navegador.
            Parámetros:
                (void)
            Retorno:
                void
        """
        self.addSubwindow("Navegador")
        self.updateNotificaciones("Navegador lanzado")
    def iniciarControlHard(self):
        """Inicia la ventana ControlHardware.
            Parámetros:
                (void)
            Retorno:
                void
        """
        self.addSubwindow("Control de hardware")
        self.updateNotificaciones("Control de hardware lanzado")
    def updateNotificaciones(self,mensaje):
        """Actualiza las notificaciones del panel de notificaciones.
            Parámetros:
                (mensaje:str)
            Retorno:
                void
        """
        if not self.band:
            self.manejadorGUI.GUI = VentanaPrincipal.getInstance()
            self.manejadorGUI.hiloNotificaciones = Hn.HiloNotificaciones.getInstance()
            self.band = True

        self.manejadorGUI.mostrarNotificacion(mensaje)

    def addSubwindow(self,nombre):
        """Añade una subventana al MDIAREA de la ventana principal.
            Parámetros:
                (nombre:str)
            Retorno:
                void
        """
        proc = Proceso.Proceso(int(t.time()+3)%1000,nombre,tiempo = 0,edo = "R")
        proc.nom = nombre+str(proc.ide)
        bandAgregado = self.administradorMemoria.agregarProceso(proc)
        if bandAgregado == True:
            if nombre == "Shell":
                terminal = Shell.Shell(planifi=self.planificador)
                terminal.ide = proc.ide
                terminal.setWindowTitle(nombre+str(proc.ide))
                ventanitaActual = self.ui.mdiArea.addSubWindow(terminal)
                self.dicWindowMDI.append(ventanitaActual.widget().windowTitle())
                QtCore.QObject.connect(ventanitaActual,QtCore.SIGNAL("destroyed()"),self.cerrarSubventana)
                terminal.show()
            elif nombre == "Navegador":
                navegador = Navegador.Navegador()
                navegador.ide = proc.ide
                navegador.setWindowTitle(nombre+str(proc.ide))
                ventanitaActual = self.ui.mdiArea.addSubWindow(navegador)
                self.dicWindowMDI.append(ventanitaActual.widget().windowTitle())
                QtCore.QObject.connect(ventanitaActual,QtCore.SIGNAL("destroyed()"),self.cerrarSubventana)
                navegador.show()
            elif nombre == "ValidadorTarjetas":
                principalWindow = CheckTarjetas.CheckTarjetas()
                principalWindow.ide = proc.ide
                principalWindow.setWindowTitle(nombre+str(proc.ide))
                ventanitaActual = self.ui.mdiArea.addSubWindow(principalWindow)
                #ventanitaActual.windowStateChanged
                self.dicWindowMDI.append(ventanitaActual.widget().windowTitle())
                QtCore.QObject.connect(ventanitaActual,QtCore.SIGNAL("destroyed()"),self.cerrarSubventana)
                principalWindow.show()
            else:
                principalWindow = controlHardware.ventanaPrincipal()
                principalWindow.ide = proc.ide
                principalWindow.setWindowTitle(nombre+str(proc.ide))
                ventanitaActual = self.ui.mdiArea.addSubWindow(principalWindow)
                #ventanitaActual.windowStateChanged
                self.dicWindowMDI.append(ventanitaActual.widget().windowTitle())
                QtCore.QObject.connect(ventanitaActual,QtCore.SIGNAL("destroyed()"),self.cerrarSubventana)
                principalWindow.show()

                self.planificador.planificarProceso(proc)
                self.manejadorGUI.actualizarMemorias(self.administradorMemoria)

        else:
            ret = QtGui.QMessageBox.critical(self, "Las memorias esta llenas", 
            '''Memorias llenas
            ''', QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
            




    def cerrarSubventana(self):
        """Elimina la ventana de la subWindowList del mdiArea y elimina el proceso del planificador de procesos.
            Precondición:
                *lanzar la signal destroyed() desde la subventana.
            Parámetros:
                (void)
            Retorno:
                void
        """
        ventanasActuales = self.ui.mdiArea.subWindowList() 
        dicActuales = {}
        for x in ventanasActuales:
            dicActuales[x.widget().windowTitle()] = 1
        diferente = None
        cont = 0
        for x in self.dicWindowMDI:
            if not dicActuales.has_key(x):
                diferente = x
                del self.dicWindowMDI[cont]
                break
            cont +=1
        ##Funciona =)
        pid = self.manejadorGUI.removerFilaProcesoPorNombre( diferente, self.ui );
        #pid = self.planificador.removerFilaProcesoPorNombre( diferente, self.ui )
        ##bUSCAR NUCLEO
        print "PID proceso "+str(pid)
        if(pid == None):
            return
        band = self.planificador.BuscarNucleoContienePid(pid)
        if band!=None:  
            rs = band.terminarProceso(pid)
            print self.administradorMemoria.matarProceso(pid)
            self.manejadorGUI.actualizarMemorias(self.administradorMemoria)
            if rs==True:  
                print "*"*50
                print "Termino el prceso =)"*8


    """
        def  hasWindowInMdi(self,nombre):
            win = self.ui.mdiArea.subWindowList()
            if win == []:
                return None
            for x in win:
                if x.widget().windowTitle() == nombre:
                    return True
            return False
    """

    #No la ocupas
    def funTest(self):
        edo = self.ui.checkBox.checkState()
        print edo
        if  edo != 1:
            self.ui.checkBox.setStyleSheet(_fromUtf8("background-color: rgb(0, 255, 8);"))
            self.ui.checkBox.setCheckState(edo+1)
        else:
            self.ui.checkBox.setStyleSheet(_fromUtf8(""))
            self.ui.checkBox.setCheckState(edo-1)
        self.ui.checkBox.show()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = VentanaPrincipal()
    myapp.show()
    sys.exit(app.exec_())