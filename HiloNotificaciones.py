# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministradorProc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import threading as t
import time
class HiloNotificaciones(t.Thread):
	"""docstring for HiloNotificaciones 
		Hilo para ejecutar la actualizacion de notificaciones
	"""
	# Here will be the instance stored.
	__instance = None
	@staticmethod
	def getInstance():
		""" Static access method. """
		if HiloNotificaciones.__instance == None:
			__instance = HiloNotificaciones()
		return HiloNotificaciones.__instance 

	def __init__(self,widget ,lista = []):
		
		""" Virtually private constructor. """
		if HiloNotificaciones.__instance != None:
			HiloNotificaciones.__instance = self
		else:
			super(HiloNotificaciones, self).__init__()
			self.lista = lista
			self.widget = widget
			self.lock = t.Lock()
			self.enEjecucion = False
			HiloNotificaciones.__instance = self

	def encolarNotificacion(self,notifiStr):
		"""Manda un mensaje a la ventana de notificaciones para que sea mostrado.
			Manda a ala cola prioridad un mensaje para que este pueda ser mostrado.
		    Parámetros:
		        (notifiStr:str)
		    Retorno:
		        void
		"""
		self.lock.acquire()
		self.lista.append(notifiStr)
		self.lock.release()
		self.lanzarHilo()


	def encolarNotificaciones(self,notifiesStr):
		"""Manda mensajes a la ventana de notificaciones para que sean mostrados.
			Manda a ala cola prioridad mensajes para que estos pueda ser mostrados.
		    Parámetros:
		        (notifiesStr:[]str)
		    Retorno:
		        void
		"""
		self.lock.acquire()
		for x in notifiesStr:
			self.lista.append(x)
		self.lock.release()
		self.lanzarHilo()

	def modificarHilo(self,widget,lista):
		"""Manda mensajes a la ventana de notificaciones para que sean mostrados.
			Manda a ala cola prioridad mensajes para que estos pueda ser mostrados.
		    Parámetros:
		        (notifiesStr:[]str)
		    Retorno:
		        void
		"""
		super(HiloNotificaciones, self).__init__()
		self.lista = lista
		self.widget = widget
		self.lock = t.Lock()
		self.enEjecucion = False
		HiloNotificaciones.__instance = self

	def lanzarHilo(self):
		if not self.enEjecucion and not self.isAlive():
			self = self.crearNuevoHilo(self.widget,self.lista)
			self.start()
		

	def crearNuevoHilo(self,widget ,lista = []):
		super(HiloNotificaciones, self).__init__()
		self.lista = lista
		self.widget = widget
		self.lock = t.Lock()
		self.enEjecucion = False
		HiloNotificaciones.__instance = self
		return self
	def run(self):
		self.enEjecucion = True
		self.lista.append("")
		while self.lista != []:
			lenNotifi = len(self.lista)
			self.widget.setText(self.lista.pop())
			if lenNotifi == 1:
				time.sleep(3)
			elif lenNotifi > 1 and lenNotifi < 4:
				time.sleep(2)
			elif lenNotifi > 3 and lenNotifi < 6:
				time.sleep(1)
			elif lenNotifi > 5:
				time.sleep(0)
		self.enEjecucion = False



		




