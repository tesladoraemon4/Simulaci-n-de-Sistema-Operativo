# -*- coding: utf-8 -*-
import Tarjeta as t
class ChecadorTarjetas(object):
	"""ChecadorTarjetas.
		Realiza la suma de verificacion de los numeros de tarjetas insertadas.
	"""
	def __init__(self, numero=None, isValida=False):
		self.numero = numero
		self.isValida = isValida
		
	def hacerCheckSum(self,tarjeta):
		"""Hace la comprobacion de una tarjeta.
		Utiliza el algoritmo de Luhn para hacer la comprobacion de tarjetas
			Parámetros:
				(tarjeta:Tarjeta)
			Retorno:
				tarjetaIsValida:boolean
		"""
		self.numero = tarjeta.numero.replace(" ","")
		final = 0
		cont = 0
		for car in self.numero:
			num = int(car)
			"""
			if cont%2 == 0:
				final += num
			else:
				num *= 2 
				if num < 10:
					final += num
				else:
					final += (1 + (num)%10)
			"""
			final += (num)if (cont%2 == 0) else ((num*2)if (num*2 < 10) else (1 + (num*2)%10))
			cont += 1
		tarjeta.isValida = (final % 10 == 0)
		return tarjeta.isValida


	def lanzarTest(self):
		test = ChecadorTarjetas()
		while True:
			numero = str(input())
			if(numero == "-1"):
				break
			"""
			test.numero = numero
			if(test.hacerCheckSum()):
				print "=)"
			else:
				print "=("
				
			"""
			tarjeta = t.Tarjeta(numero)
			tarjeta.consultarCaracteristicas()
			#print tarjeta.toString()
			"""
			if (test.hacerCheckSum(tarjeta)==True):
				pass

			else:
				print "Tarjeta no valida"


			print "*"*10
			"""
"""
a = ChecadorTarjetas()
a.lanzarTest()

"""
