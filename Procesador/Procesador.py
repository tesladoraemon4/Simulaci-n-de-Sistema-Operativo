# -*- coding: utf-8 -*-
import listaCircular as l
import threading as t
import sys
sys.path.append('./ManejadorGUI')
import ManejadorGUI as mgaGUI
import Proceso, time,Semaforo

CARGAMAX = 20
TEMPMAX = 40
CARGAPORPROCESO = 5
TEMOPORPROCESO = 10
class Procesador(t.Thread):
	"""Clase que abstrae a un nucleo de un procesador.
	    Constructores:
			
			idNum,velocidad,cargaMax,tempMax,temp=0,carga=0,procesos=l.listaCircular(),timeProce=.3,hiloNotificaciones=None,planificador=None

		    idNum 							=> Identificador del procesador
		    velocidad 						=> Velocidad del procesador
		    cargaMax 						=> cargaMax maxima que puede tener el procesador para mandar la carga hacia otro nucleo
		    tempMax 						=> Temperatura maxima si la temperatura maxima es excedida se mandan los procesos a otro núcleo
		    temp=0 							=> Temperatura actual del microprocesador
		    carga=0 						=> Carga actual del microprocesador
		    procesos=l.listaCircular() 		=> Cola circular de procesos 
		    timeProce=.3 					=> Tiempo que el microprocesador va a dar a cada proceso en ejecutarce
		    hiloNotificaciones=None 		=> Hilo que se usa para comunicarce con el area de notificaciones
		    planificador=None 				=> Se encarga de planificar los procesos del sistema
	"""
	def __init__(self,idNum,velocidad,cargaMax,tempMax,temp=0,carga=0,procesos=l.listaCircular(),timeProce=.3,hiloNotificaciones=None,planificador=None):
		t.Thread.__init__(self)		
		self.idNum = idNum
		self.temp = temp
		self.velocidad = velocidad
		self.carga = carga
		self.procesos = procesos
		self.cargaMax = cargaMax
		self.hiloNotificaciones = hiloNotificaciones
		self.tempMax = tempMax
		self.planificador = planificador
		self.timeProce = timeProce
		self.lCircular = l.listaCircular()
		#Manejador para controlar la GUI
		self.manejadorGUI = mgaGUI.ManejadorGUI()
		self.lock = t.Lock()


		self.hashIdProcesos = {}


	

	
	"""
		Da turno de ejecucion a un proceso 
	"""
	def darTurnoProc(self,proceso):
		"""Da turno de ejecucion a un proceso.
			Parámetros:
				(proceso:Proceso)
			Retorno:
				void
		"""
		if(proceso.edo == "R"):
			proceso.edo = "E"
			self.manejadorGUI.actualizarFilaProceso(proceso,self.planificador.GUI)
			time.sleep(self.timeProce)
			proceso.edo = "R"
			proceso.tiempo += self.timeProce
			self.manejadorGUI.actualizarFilaProceso(proceso,self.planificador.GUI)

	"""
	Termina un proceso si lo termina manda un true sino un false
	"""
	def terminarProceso(self,idProc):
		"""Termina la ejecucion de un proceso en el microprocesador con el id que fue pasado como parametro.
			Parámetros:
				(idProc:int)
			Retorno:
				void
		"""
		print "****************************************************************+"*10
		print self.lCircular
		self.lock.acquire()
		nucleo = self.lCircular.eliminarProcesoId(idProc)
		self.lock.release()
		print nucleo
		if(nucleo != None):
			nucleo.temp -= TEMOPORPROCESO
			nucleo.carga -= CARGAPORPROCESO
			del self.hashIdProcesos[idProc]
			return True
		return False

	"""
		agrega un proceso a la cola de prioridad 
	"""
	def agregarProceso(self,proceso):
		"""Agrega un proceso a la lista circular.
			Parámetros:
				(proceso:Proceso)
			Retorno:
				void
		"""
		print "proceso agregador Procesador "+str(proceso.ide)
		self.manejadorGUI.crearFilaProceso(proceso,self.planificador.GUI)
		self.carga += CARGAPORPROCESO
		self.temp += TEMOPORPROCESO
		self.lock.acquire()
		self.lCircular.agregar(proceso)
		self.hashIdProcesos[proceso.ide] = proceso
		self.lock.release()
		self.manejadorGUI.actualizarFilaNucleo(self,self.planificador.GUI)
		
	def run(self):
		"""Ejecuta la lista circular.
			Parámetros:
				(void)
			Retorno:
				void
		"""
		self.lock.acquire()
		nodoI = self.lCircular.primero.sig
		self.lock.release()
		while(True):
			#time.sleep(self.timeProce)
			self.darTurnoProc(nodoI.val)
			#print "despues de ejecucion id cola "
			#print nodoI.val.toString()+" Num proc "+str(self.lCircular.tam)
			self.lock.acquire()
			nodoI = nodoI.sig
			self.lock.release()
			#print "*"*10





