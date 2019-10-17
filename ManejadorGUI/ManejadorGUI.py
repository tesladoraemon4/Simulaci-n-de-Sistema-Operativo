# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AdministradorProc.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!
import sys
sys.path.append('./')
import HiloNotificaciones as Hn
import VentanaPrincipal as pw
import Proceso


from PyQt4 import QtCore, QtGui

COL_PID = 0
COL_NOMBRE = 1
COL_TIEMPO = 2
COL_NUCLEO = 3
COL_EDO = 4


COL_TEMP = 0
COL_CARGA = 1
COL_NUMPROC = 2



class ManejadorGUI(object):
	"""Es el driver entre la GUI y la logica de negocio.
	Ocupa el patron de diseño singleton.
	"""
	class __ManejadorGUI:
		"""Clase interna privada que realiza las operaciones.
		"""
		def __init__(self):
			self.GUI = None#pw.VentanaPrincipal()
			self.hiloNotificaciones = None#Hn.HiloNotificaciones(self.GUI.ui.notificaciones)
			self.ventanaPrincipal = None
		def __str__(self):
			return `self` + ' ' + self.nombre
		def mostrarNotificacion(self,mensaje):
			"""Muestra una notificacion en area de notificaciones.
				Parámetros:
					(mensaje:str)
				Retorno:
					void
			"""
			self.hiloNotificaciones.encolarNotificacion(mensaje)

		def killPid(self,pid):
			"""Elimina las entradas de la tabla de GUI del area de notificaciones.
				Parámetros:
					(pid:int)
					pid => es el pid del proceso que se desea eliminar.
				Retorno:
					boolean
					Retorna un True en caso de exito o False en caso de error.
			"""
			nucConPid = self.GUI.planificador.BuscarNucleoContienePid(pid)
			if nucConPid != None:
				termino = nucConPid.terminarProceso(pid)
				if termino:
					print "termino el pid"
					self.removerFilaProceso(Proceso.Proceso(pid,""),self.GUI.ui)
					lista = self.GUI.ui.mdiArea.subWindowList()
					print "FIla ui removida"
					if lista == []:
						return False
					for x in lista:
						if x.widget().ide == pid:
							self.GUI.ui.mdiArea.removeSubWindow(x)
							print "removeSubWindow"
							return True

		def buscarFilaNombre(self,nombre,gui):
			"""Busca la posicion de una fila utilizando el valor que tiene el nombre.
				Parámetros:
					(nombre,gui)
					nombre => nombre de la fila que se desea eliminar
					gui => el contenedor que contiene la tabla del planificador de procesos
				Retorno:
					None|int
					None en caso de que no exista la fila
					int en que es el numero de fila de la tabla
			"""
			tabla1AdmonProc = gui.tablePart1
			numFilas = tabla1AdmonProc.rowCount()
			for filaI in range(numFilas):
				if( tabla1AdmonProc.item(filaI,COL_NOMBRE).text() == str(nombre)):
					return filaI
			return None

		def buscarFilaId(self,id,gui):
			"""Busca la posicion de una fila utilizando el valor que tiene el id.
			Parámetros:
				(id,gui)
				id => id de la fila que se desea eliminar
				gui => el contenedor que contiene la tabla del planificador de procesos
			Retorno:
				None|int
				None en caso de que no exista la fila
				int en que es el numero de fila de la tabla
			"""
			tabla1AdmonCores = gui.edo_cores
			numFilas = tabla1AdmonCores.rowCount()
			for filaI in range(numFilas):
				if( int(tabla1AdmonCores.verticalHeaderItem(filaI).text()[6:]) == int(id)):
					return filaI
			return None

		def buscarFilaPid(self,pid,gui):
			"""Busca la posicion de la fila que contiene el pid de un proceso.
				Parámetros:
					(pid,gui)
					pid => pid de la fila que se desea eliminar
					gui => el contenedor que contiene la tabla  del planificador de procesos
				Retorno:
					None|int
					None en caso de que no exista la fila
					int en que es el numero de fila de la tabla
			"""
			tabla1AdmonProc = gui.tablePart1
			numFilas = tabla1AdmonProc.rowCount()
			for filaI in range(numFilas):
				if( tabla1AdmonProc.item(filaI,COL_PID).text() == str(pid)):
					return filaI
			return None


		def inicializarGuiMemorias(self):
			"""Agrega elementos a la gui de las memorias.
				Parámetros:
					(void)
				Retorno:
					void
			"""
			print "inicializad"
			#instancia de la ventana
			pWVent = self.ventanaPrincipal
			gui = pWVent.ui
			admonMemoria = pWVent.administradorMemoria
			fisicaGui = gui.listWidgetMarcos
			swapGui = gui.listWidgetPaginas
			##Agregamos los cambios en la GUI
			for x in admonMemoria.fisica.marcos:
				item = QtGui.QListWidgetItem("  ")
				fisicaGui.addItem(item)
			for x in admonMemoria.swap.paginas:
				item = QtGui.QListWidgetItem("   ")
				swapGui.addItem(item)




		def actualizarMemorias(self,admonMemoria):
			"""Actualiza la gui de la memoria del sistema.
				Parámetros:
					(void)
				Retorno:
					void
			"""
			#instancia de la ventana
			pWVent = self.ventanaPrincipal
			gui = pWVent.ui
			admonMemoria = pWVent.administradorMemoria
			fisicaGui = gui.listWidgetMarcos
			swapGui = gui.listWidgetPaginas
			##Agregamos los cambios en la GUI
			cont = 0
			for x in admonMemoria.fisica.marcos:
				item = fisicaGui.item(cont)
				if str(x) == "0":
					item.setText("") 
				else:
					item.setText("Id proceso "+str(x)) 
				#fisicaGui.addItem(item)
				cont += 1

			cont = 0
			for x in admonMemoria.swap.paginas:
				item = swapGui.item(cont)
				if str(x) == "0":
					item.setText("") 
				else:
					item.setText("Id proceso "+str(x)) 
				#swapGui.addItem(item)
				cont += 1






		def swapFila(self,gui,filaO,filaD):
			"""Intercambia la fila origen con la fila destino.
				Parámetros:
					(gui,filaO:int,filaD:int)
					pid => pid de la fila que se desea eliminar
					filaO => posicion de la fila origen que se quiere intercambiar
					filaD => posicion de la fila destino que se quiere intercambiar
				Retorno:
					void
			"""
			tabla1AdmonProc = gui.tablePart1
			numCols = tabla1AdmonProc.columnCount()
			filaLo = []
			for x in range(numCols):
				filaLo.append(tabla1AdmonProc.takeItem(filaO,x))
			filaLd = []
			for x in range(numCols):
				filaLd.append(tabla1AdmonProc.takeItem(filaD,x))
			for x in range(numCols):
				tabla1AdmonProc.setItem(filaD,x,filaLo[x])
				tabla1AdmonProc.setItem(filaO,x,filaLd[x])
			tabla1AdmonProc.show()

		def removerFilaProcesoPorNombre(self,nombre,gui):
			"""Remove la fila del proceso usando el nombre del proceso.
				Parámetros:
					(nombre:str,gui)
					nombre => nombre de la fila que se desea eliminar
					gui => el contenedor que contiene la tabla  del planificador de procesos
				Retorno:
					int
				Retorna el pid del proceso eliminado
			"""
			tabla1AdmonProc = gui.tablePart1
			numCols = 5
			#buscar la fila que tiene el pid del procesos
			filaConElPid = self.buscarFilaNombre(nombre,gui)
			if filaConElPid != None:
				numCols = tabla1AdmonProc.columnCount()
				pid = str(tabla1AdmonProc.item(filaConElPid,COL_PID).text())

				#Eliminar las filas 
				for x in range(numCols):
					tabla1AdmonProc.setItem(filaConElPid, x,None)



				#Recorrer el contenido de las filas inferiores a filaConElPid
				for x in range(filaConElPid,numCols):
					self.swapFila(gui,x+1,x)
				tabla1AdmonProc.setRowCount(tabla1AdmonProc.rowCount()-1)
				tabla1AdmonProc.show()
				self.mostrarNotificacion("Se ah removido el proceso: "+str(nombre))
				return pid

		def removerFilaProceso(self,proceso,gui):
			"""Remove la fila del proceso.
				Parámetros:
					(proceso:Proceso)
					proceso => referencia del objeto proceso que se desea remover.
					gui => el contenedor que contiene la tabla  del planificador de procesos
				Retorno:
					void
			"""
			tabla1AdmonProc = gui.tablePart1
			numCols = 5
			#buscar la fila que tiene el pid del procesos
			filaConElPid = self.buscarFilaPid(proceso.ide,gui)
			numCols = tabla1AdmonProc.columnCount()
			#Eliminar las filas 
			for x in range(numCols):
				tabla1AdmonProc.setItem(filaConElPid, x,None)
			#Recorrer el contenido de las filas inferiores a filaConElPid
			for x in range(filaConElPid,numCols):
				self.swapFila(gui,x+1,x)
			tabla1AdmonProc.setRowCount(tabla1AdmonProc.rowCount()-1)
			tabla1AdmonProc.show()
			self.mostrarNotificacion("Se ah removido el proceso: "+str(proceso.nom)+"\nCon pid: "+str(proceso.ide))
		def actualizarFilaProceso(self,proceso,gui):
			"""Actualiza la fila del administrador de procesos.
				Actualiza la fila del proceso utilizando los atributos del objeto mandado como parametro,
				 esta actualizacion se realiza en la tabla del administrador de procesos. 
				Parámetros:
					(proceso:Proceso,gui)
					proceso => referencia del objeto proceso que se desea actualizar.
					gui => el contenedor que contiene la tabla  del planificador de procesos
				Retorno:
					void
			"""
			tabla1AdmonProc = gui.tablePart1
			#buscar la fila que tiene el pid del procesos
			filaConElPid = self.buscarFilaPid(proceso.ide,gui)
			if(filaConElPid != None):
				item = QtGui.QTableWidgetItem(str(proceso.edo))
				tabla1AdmonProc.setItem(filaConElPid, COL_EDO,item)
				item = QtGui.QTableWidgetItem(str(proceso.tiempo))
				tabla1AdmonProc.setItem(filaConElPid, COL_TIEMPO,item)
				item = QtGui.QTableWidgetItem(str(proceso.ide))
				tabla1AdmonProc.setItem(filaConElPid, COL_PID,item)
				item = QtGui.QTableWidgetItem(str(proceso.nucleo.idNum))
				tabla1AdmonProc.setItem(filaConElPid, COL_NUCLEO,item)
				item = QtGui.QTableWidgetItem(str(proceso.nom))
				tabla1AdmonProc.setItem(filaConElPid, COL_NOMBRE,item)



		def crearFilaProceso(self,proceso,gui):
			"""Crea la fila del administrador de procesos.
				Crea la fila del proceso utilizando los atributos del objeto mandado como parametro,
				 esta actualizacion se realiza en la tabla del administrador de procesos. 
				Parámetros:
					(proceso:Proceso,gui)
					proceso => referencia del objeto proceso que se desea crear.
					gui => el contenedor que contiene la tabla  del planificador de procesos
				Retorno:
					void
			"""
			tabla1AdmonProc = gui.tablePart1
			tabla1AdmonProc.setRowCount(tabla1AdmonProc.rowCount()+1)
			item = QtGui.QTableWidgetItem(str(""))
			tabla1AdmonProc.setVerticalHeaderItem(tabla1AdmonProc.rowCount()-1, item)
			proceso.row = tabla1AdmonProc.rowCount()-1
			item = QtGui.QTableWidgetItem(str(proceso.ide))
			tabla1AdmonProc.setItem(tabla1AdmonProc.rowCount()-1,COL_PID, item)
			item = QtGui.QTableWidgetItem(str(proceso.nom))
			tabla1AdmonProc.setItem(tabla1AdmonProc.rowCount()-1,COL_NOMBRE, item)
			item = QtGui.QTableWidgetItem(str(proceso.tiempo))
			tabla1AdmonProc.setItem(tabla1AdmonProc.rowCount()-1,COL_TIEMPO, item)
			item = QtGui.QTableWidgetItem(str(proceso.nucleo.idNum))
			tabla1AdmonProc.setItem(tabla1AdmonProc.rowCount()-1,COL_NUCLEO, item)
			item = QtGui.QTableWidgetItem(str(proceso.edo))
			tabla1AdmonProc.setItem(tabla1AdmonProc.rowCount()-1,COL_EDO, item)
			tabla1AdmonProc.show()
			return proceso



		def actualizarFilaNucleo(self,nucleo,gui):
			"""Actualiza la tabla del administrador de procesos.
				Actualiza la fila del proceso utilizando los atributos del objeto mandado como parametro,
				 esta actualizacion se realiza en la tabla del administrador de procesos. 
				Parámetros:
					(nucleo:Nucleo,gui)
					nucleo => referencia del objeto nucleo que se desea actualizar.
					gui => el contenedor que contiene la tabla  del planificador de procesos
				Retorno:
					void
			"""
			tabla1AdmonProc = gui.edo_cores
			#buscar la fila que tiene el pid del nucleos
			filaConElPid = self.buscarFilaId(nucleo.idNum,gui)
			if(filaConElPid != None):
				item = QtGui.QTableWidgetItem(str(nucleo.temp))
				tabla1AdmonProc.setItem(filaConElPid, COL_TEMP,item)
				item = QtGui.QTableWidgetItem(str(nucleo.carga))
				tabla1AdmonProc.setItem(filaConElPid, COL_CARGA,item)
				item = QtGui.QTableWidgetItem(str(nucleo.lCircular.tam))
				"""
				tabla1AdmonProc.setItem(filaConElPid, COL_NUMPROC,item)
				tabla1AdmonProc.show()
				"""



		def crearFilaNucleos(self,procesador,gui):
			"""Crea una nueva entrada en la tabla del administrador de procesos.
				Crea la fila del proceso utilizando los atributos del objeto mandado como parametro,
				 esta actualizacion se realiza en la tabla del administrador de procesos. 
				Parámetros:
					(procesador:Procesador,gui)
					procesador => referencia del objeto procesador que se desea crear.
					gui => el contenedor que contiene la tabla  del planificador de procesos
				Retorno:
					void
			"""
			#Tabla de los cores 
			tablaNucleos = gui.edo_cores
			tablaNucleos.setRowCount(tablaNucleos.rowCount()+1)

			item = QtGui.QTableWidgetItem(str("Nucleo"+str(tablaNucleos.rowCount()-1)))
			tablaNucleos.setVerticalHeaderItem(tablaNucleos.rowCount()-1, item)

			item = QtGui.QTableWidgetItem(str(procesador.temp))
			tablaNucleos.setItem(tablaNucleos.rowCount()-1,COL_TEMP, item)

			
			item = QtGui.QTableWidgetItem(str(procesador.carga))
			tablaNucleos.setItem(tablaNucleos.rowCount()-1,COL_CARGA, item)
			
			"""

			item = QtGui.QTableWidgetItem(str(procesador.procesos.tam))
			tablaNucleos.setItem(tablaNucleos.rowCount()-1,COL_NUMPROC, item)
			"""


			tablaNucleos.show()
			return procesador
		def mostrarNotificacion(self,mensaje):
			"""Muestra una notificacion en la barra de notificaciones.
				Parámetros:
					(mensaje:str)
					mensaje => mensaje que se desea mostrar
				Retorno:
					void
			"""
			self.hiloNotificaciones.encolarNotificacion(mensaje)

	instance = None
	def __new__(cls):
		if not ManejadorGUI.instance:
			ManejadorGUI.instance = ManejadorGUI.__ManejadorGUI()
		return ManejadorGUI.instance

	def __getattr__(self, nombre):
		return getattr(self.instance, nombre)
	def __setattr__(self, nombre, valor):
		return setattr(self.instance, nombre, valor)

	
