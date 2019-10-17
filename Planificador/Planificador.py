# -*- coding: utf-8 -*-

sys.path.append('./Procesador')
import listaCircular
import Proceso
import Procesador
import random as r
import  time as t

CARGAMAX = 20
TEMPMAX = 40

CARGAPORPROCESO = 5
TEMOPORPROCESO = 10

class Planificador(object):
	def __init__(self, procesadores,procesos=[],timeProce=1):
		super(Planificador, self).__init__()
		self.procesadores = procesadores
		self.procesos = procesos
		self.lCircular = listaCircular.listaCircular()
		self.timeProce = timeProce 
	"""
		Busca el procesador que esta disponible 
		para ejecutar el proceso.
		RETURN 
			None, si no hay procesadores disponibles
	"""
	def getProcesador(self):
		for x in self.procesadores:
			if x.carga <= x.cargaMax and  x.temp <= x.tempMax:
				return x
		return None
		
	def agregarProceso(self,proceso):
		procesador = self.getProcesador()
		procesador.carga += CARGAPORPROCESO
		procesador.temp += TEMOPORPROCESO
		self.lCircular.agregar(proceso)

	def darTurnoProc(self,proceso):
		cpu = self.getProcesador()
		if cpu==None:
			print "No hay mas procesadores disponibles"
		proceso.nucleo = cpu
		proceso.edo = "E"
		t.sleep(self.timeProce)
		proceso.tiempo += self.timeProce

	"""
	Termina un proceso si lo termina manda un true sino un false
	"""
	def terminarProceso(self,idProc):
		lista = self.lCircular
		nodoI = lista.primero.sig
		nodoA = lista.primero
		while nodoI != lista.primero:
			if(idProc == nodoI.val.ide):
				nu = nodoI.val.nucleo
				nu.temp -= TEMOPORPROCESO
				nu.carga -= CARGAPORPROCESO
				nodoA.sig = nodoI.sig
				return True
			nodoI = nodoI.sig
			nodoA = nodoA.sig
		if(idProc == nodoI.val.ide):
			nu = nodoI.val.nucleo
			nu.temp -= TEMOPORPROCESO
			nu.carga -= CARGAPORPROCESO
			nodoA.sig = nodoI.sig
			lista.primero = nodoI.sig
			lista.ultimo = lista.primero
			return True
		return False
	def runPlanificador(self):
		nodoI = self.lCircular.primero.sig
		ciclos = int(input("ciclos de procesador"))
		for x in range(ciclos):
		#while(True):
			print "Antes de ejecucion"
			print nodoI.val.toString()
			self.darTurnoProc(nodoI.val)
			print "despues de ejecucion"
			print nodoI.val.toString()
			nodoI.val.edo = None
			nodoI = nodoI.sig
			print "*"*10



"""
NO SIRVE SOLO ERA PARA PRUEBAS
def crearProcesadores(nProc):
	procesadores = []
	for x in range(nProc):
		proc = Procesador.Procesador(x,.5,CARGAMAX,TEMPMAX)
		procesadores.append(proc)
	return procesadores
"""

"""

n = int(input("Numero de procesos y nucleos"))
p = Planificador(crearProcesadores(n))
for x in range(0,n):
	p.agregarProceso(Proceso.Proceso(x,'proc',0,nucleo = p.procesadores[x]))

p.lCircular.recorrer()

while True:
	p.runPlanificador()
	if(p.terminarProceso(int(input("proceso a terminar id"))) == True):
		print "Terminado con exito"

	p.lCircular.recorrer()

	cont = int(input("desea continuar 1 si"))

	if( cont != 1):
		break;
"""
