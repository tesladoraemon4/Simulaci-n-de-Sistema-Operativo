# -*- coding: utf-8 -*-
import random as r
class Nodo(object):
	def __init__(self, val=None,sig=None):
		self.val = val
		self.sig = sig
class listaCircular(object):
	"""Collacircular para el administrador de procesos"""
	def __init__(self, arg=None):
		super(listaCircular, self).__init__()
		self.arg = arg
		self.primero = None
		self.ultimo = None
		self.tam = 0

	def vacia(self,lista):
		return (lista.primero == None and lista.ultimo == None)
	def vacia(self):
		return (self.primero == None and self.ultimo == None)
	def agregar(self,val):
		if self.vacia():
			self.primero = Nodo(val)
			self.ultimo = self.primero
			self.primero.sig = self.primero
		else:
			nodo = Nodo(val,self.ultimo)
			nodo.sig = self.ultimo
			self.ultimo = nodo
			self.primero.sig = self.ultimo
		self.tam += 1

	def recorrer(self,lista = None,nVeces=1):
		if lista == None:
			lista = self
		for x in range(nVeces):
			nodoI = lista.primero.sig
			while nodoI != lista.primero:
				print "valor del nodo "+str(nodoI.val)
				nodoI = nodoI.sig
			print "valor del nodo "+str(nodoI.val)
			print "*"*10

	def eliminarProcesoId(self,id):
		"""Elimina de la lista circular un proceso por el ID.
		    Parámetros:
		        (id:int)
		    Retorno:
		        obj:Procesador | None
		    Retorna el procesador al que pertenecia el proceso, en caso de fracaso retorna None
		"""
		nodoI = self.primero.sig
		nodoA = self.primero
		while nodoI != self.primero:
			if(id == nodoI.val.ide):
				nu = nodoI.val.nucleo
				nodoA.sig = nodoI.sig
				self.tam -= 1
				return nu
			nodoI = nodoI.sig
			nodoA = nodoA.sig

		if(id == nodoI.val.ide):
			nu = nodoI.val.nucleo
			#nodoA.sig = nodoI.sig
			self.primero = nodoI.sig
			self.tam -= 1
			return nu


	def eliminar(self,val):
		"""Elimina de la lista circular un objeto.
		    Parámetros:
		        (val:void)
		    Retorno:
		        Boolean
		    Retorna el True en caso se exito, en caso de fracaso retorna False.
		"""
		nodoI = self.primero.sig
		nodoA = self.primero
		while nodoI != self.primero:
			if(val == nodoI.val):
				nodoA.sig = nodoI.sig
				self.tam -= 1
				return True
			nodoI = nodoI.sig
			nodoA = nodoA.sig

		if(val == nodoI.val):
			#nodoA.sig = nodoI.sig
			self.primero = nodoI.sig
			self.tam -= 1
			return True
		return False

"""
valList = int(input())
l = listaCircular()

for x in range(valList):
	l.agregar(r.randint(0,valList*10))
l.recorrer()


for x in range(valList):
	l.agregar(r.randint(0,valList*10))
l.recorrer()

bad = l.eliminar(int(input()))
print bad
l.recorrer()
bad = l.eliminar(int(input()))
print bad
l.recorrer()
bad = l.eliminar(int(input()))
print bad
l.recorrer()


"""
