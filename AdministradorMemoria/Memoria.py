# -*- coding: utf-8 -*-

class Memoria(object):
	"""Clase que abstrae una memoria.
	    Constructor:
			tamanio
		    tamanio=20 				=> Es el tamaño de la memoria medido en mb
	"""
	def __init__(self, tamanio=20):
		super(Memoria, self).__init__()
		self.tamanio = tamanio


