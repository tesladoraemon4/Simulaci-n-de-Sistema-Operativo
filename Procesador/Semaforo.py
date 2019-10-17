# -*- coding: utf-8 -*-

import threading as t

class Semaforo(t.Thread):
	"""Semaforo donde puedes obtener los atributos dle mismo"""
	def __init__(self):
		super(Semaforo, self).__init__()
		self.val = 1
		self.sem = t.Lock()
	def bloquear(self):
		self.val+=1
		self.sem.acquire()

	def desBloquear(self):
		self.val-=1
		self.sem.release()


