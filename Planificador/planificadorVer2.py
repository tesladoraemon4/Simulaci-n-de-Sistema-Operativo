# -*- coding: utf-8 -*-
import sys
sys.path.append('./Planificador')
sys.path.append('./Procesador')
sys.path.append('./')

import Proceso
import HiloNotificaciones as Hn
import sys
from principalWindow2 import *
import Procesador


sys.path.append('ManejadorGUI')
import ManejadorGUI as mgaGUI




CARGAMAX = 20
TEMPMAX = 40
CARGAPORPROCESO = 5
TEMOPORPROCESO = 10

COL_PID = 0
COL_NOMBRE = 1
COL_TIEMPO = 2
COL_NUCLEO = 3
COL_EDO = 4
class Planificador(object):
	def __init__(self,numProc = 1,procesadores = [Procesador.Procesador(0,.5,CARGAMAX,TEMPMAX)],procesos=[],timeProce=1,GUI = None,notificaciones=None ):
		super(Planificador, self).__init__()
		self.procesadores = procesadores
		self.procesos = procesos
		self.numProc = numProc
		self.timeProce = timeProce 
		self.notificaciones = notificaciones 
		self.tablePart1 = GUI.tablePart1 
		self.GUI = GUI
		self.nucleoActualUsado =  procesadores[0]
		self.manejadorGUI = mgaGUI.ManejadorGUI()

		"""  Este no va solo fue de pruebas
		self.proc = Proceso.Proceso(1,'UI 1',tiempo = 0,edo = "R",nucleo = self.getProcesador())
		self.crearFilaProceso(self.proc,GUI)
		"""

	"""
		Busca el procesador que esta disponible 
		para ejecutar el proceso.
		RETURN 
			None, si no hay procesadores disponibles
	"""
	def getProcesador(self):
		"""Busca el procesador que esta disponible para ejecutar el proceso.
			Parámetros:
				(void)
			Retorno:
				(None | Procesador)
				retorna None si no hay un procesador disponible
				retorna Procesador en caso contrario
		"""
		x = self.nucleoActualUsado 
		if x.carga <= x.cargaMax and  x.temp <= x.tempMax:
			return x

		for x in self.procesadores:
			if x.carga <= x.cargaMax and  x.temp <= x.tempMax:
				self.nucleoActualUsado = x
				return x
		return None
	
	"""
		Manda un proceso a algun procesador para su creacion.
	"""
	def planificarProceso(self,proceso):
		"""Planifica el proceso que fue lanzado.
		    Parámetros:
		        (proceso:Proceso)
		        proceso => es el proceso que se requiere lanzar
		    Retorno:
		    	void | None

		"""
		procesador = self.getProcesador()
		if procesador== None:
			print "No hay procesadores disponibles"
			return None
		vivo = procesador.isAlive()
		proceso.nucleo = procesador
		procesador.agregarProceso(proceso)
		if not vivo:
			procesador.start()
		#procesador.join()
	"""
		Mueve el proceso con pid que esta en el nucleo origen al nucleo destino
		nucleoO nunca es vacio 
		nucleoD este siempre se busca 
	"""
	def moverProceso(self,pid,nucleoO = None,nucleoD=None):
		"""Mueve el proceso con pid que esta en el nucleo origen al nucleo destino.
		    Parámetros:
		        (pid:int,nucleoO = None:Nucleo,nucleoD=None:Nucleo)
		        pid => es el proceso que se requiere lanzar
		        nucleoO => es el nucleo que contiene el proceso que se quiere cambiar
		        NucleD => es el nucleo en que se va a recibir el proceso que se quiere cambiar
		    Retorno:
		    	void
		"""
		if nucleoD == None:
			nucleoD = self.getProcesador()
		if nucleoO.hashIdProcesos.has_key(pid) and nucleoD != nucleoO:
			proceso = nucleoO.hashIdProcesos[pid]
			if (nucleoO.terminarProceso(pid)):
				nucleoD.agregarProceso(proceso)

	def buscarNucleoMasVacio(self):
		"""Mueve el proceso con pid que esta en el nucleo origen al nucleo destino.
		    Parámetros:
		        (pid:int,nucleoO = None:Nucleo,nucleoD=None:Nucleo)
		        pid => es el proceso que se requiere lanzar
		        nucleoO => es el nucleo que contiene el proceso que se quiere cambiar
		        NucleD => es el nucleo en que se va a recibir el proceso que se quiere cambiar
		    Retorno:
		    	void
		"""
		menor = 100
		procVacio = None
		for x in self.procesadores:
			tam = len(x.hashIdProcesos)
			if tam >= 1:
				if tam < menor:
					menor = tam
					procVacio = x
		return procVacio


	def BuscarNucleoContienePid(self,pid):
		for x in self.procesadores:
			if x.hashIdProcesos.has_key(int(pid)):
				return x
		return None


"""
def crearProcesadores(nProc):
	procesadores = []
	for x in range(nProc):
		proc = Procesador.Procesador(x,.5,CARGAMAX,TEMPMAX)
		procesadores.append(proc)
	return procesadores



n = int(input("Numero de procesos y nucleos"))
p = Planificador( procesadores = crearProcesadores(n))
for x in range(0,n):
	proc = Proceso.Proceso(x,'proc'+str(x),tiempo = 0,edo = "R")
	p.planificarProceso(proc)

pid = int(input())
nucleo = p.BuscarNucleoContienePid(pid)
if nucleo != None:
	nucleo.terminarProceso(pid)

"""
