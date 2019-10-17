# -*- coding: utf-8 -*-
import subprocess
import os
import json
import requests

class Tarjeta(object):
	"""Clase que abstrae a una trajeta de credito.
	"""
	def __init__(self,numero, binBancario = None,entidadBancaria = None,pais = None,numeroCuenta = None):
		self.MIIDic = {
			0:"Industria poco común.",
			1:"Negocios de líneas aéreas.",
			2:"Negocios de líneas aéreas.",
			3:"Entretenimiento y Viajes Negocios.",
			4:"Bancos y Negocios Financieros.",
			5:"Bancos y Negocios Financieros.",
			6:"Merchandising, Comercio y pocos negocios bancarios restantes.",
			7:"Negocios petroleros",
			8:"Telecomunicaciones",
			9:"Organizaciones Nacionales de Trabajo",
		}
		self.numero = numero
		self.binBancario = numero[:6]
		self.numeroCuenta = numero[6:len(numero)-1]
		self.MIITarjeta = self.MIIDic[int(numero[0])]
		self.isValida = False
		self.entidadBancaria = None
		self.pais = None

		self.tipo = None
		self.esquema = None


	def toString(self):
		return "numero \n\t"+str(self.numero)+"\n binBancario \n\t"+str(self.binBancario)+"\n entidadBancaria \n\t"+str(self.entidadBancaria)+"\n pais \n\t"+str(self.pais)+"\n tipo \n\t"+str(self.tipo)+"\n esquema \n\t"+str(self.esquema)+"\n numeroCuenta \n\t"+str(self.numeroCuenta)+"\n isValida \n\t"+str(self.isValida)+"\n MIITarjeta \n\t"+str(self.MIITarjeta)

	def consultarCaracteristicas(self):
		# Creamos la petición HTTP con GET:
		r = requests.get("https://lookup.binlist.net/"+str(self.binBancario))
		# Imprimimos el resultado si el código de estado HTTP es 200 (OK):
		if r.status_code == 200:
			cadJson = r.text
			decoded = json.loads(cadJson)
			print decoded
			
			if decoded['bank'] != {}:
				self.entidadBancaria = decoded['bank']['name']

			if decoded['country'] != {}:
				self.pais = decoded['country']['name']
			
			self.tipo = decoded['type']
			self.esquema = decoded['scheme']




