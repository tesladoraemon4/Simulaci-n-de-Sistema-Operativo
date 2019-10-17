# -*- coding: utf-8 -*-
import Memoria as m
class Fisica(m.Memoria):
	"""Clase que abstrae una memoria fisica.
	    Constructor:
			tamanio = 20 , marcos, posMarcosVacios, posMarcosOcupados
		    tamanio=20 				=> Es el tamaño de la memoria medido en mb
		    marcos 					=> Es un arreglo que tiene todos los marcos de la memoria.
		    posMarcosVacios 		=> Es un arreglo que tiene las posiciones donde hay marcos disponibles en el arreglo de marcos.
		    posMarcosOcupados 		=> Es un arreglo que tiene las posiciones donde hay marcos utilizados en el arreglo de marcos.

	"""
	def __init__(self, tamanio = 3 , marcos = [], posMarcosVacios = [], posMarcosOcupados = []):
		super(Fisica, self).__init__()
		self.marcos = [0 for x in range(tamanio)]
		self.posMarcosVacios = [x for x in range(tamanio)]
		self.posMarcosOcupados = posMarcosOcupados
		self.tamanio = tamanio
		
	def toString(self):
		return "marcosDisponibles: "+str(len(self.posMarcosVacios))+"\t marcosOcupadas: "+str(len(self.posMarcosOcupados))

