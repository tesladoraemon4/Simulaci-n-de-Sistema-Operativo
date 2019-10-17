# -*- coding: utf-8 -*-
import Memoria as m
class Swap(m.Memoria):

	"""Clase que abstrae una memoria fisica.
	    Constructor:
			tamanio = 50 , paginas, posPaginasVacios, posPaginasOcupados
		    tamanio=50 				=> Es el tamaño de la memoria medido en mb
		    paginas 				=> Es un arreglo que tiene todos los paginas de la memoria.
		    posPaginasVacias 		=> Es un arreglo que tiene las posiciones donde hay paginas disponibles en el arreglo de paginas.
		    posPaginasOcupados 		=> Es un arreglo que tiene las posiciones donde hay paginas utilizados en el arreglo de paginas.

	"""
	def __init__(self, tamanio = 3 , paginas = [], posPaginasVacias = [], posPaginasOcupadas = []):
		super(Swap, self).__init__()
		self.paginas = [0 for x in range(tamanio)]
		self.posPaginasVacias = [x for x in range(tamanio)]
		self.posPaginasOcupadas = posPaginasOcupadas
		self.tamanio = tamanio


	def toString(self):
		return "paginasDisponibles: "+str(len(self.posPaginasVacias))+"\tpaginasOcupadas: "+str(len(self.posPaginasOcupadas))


