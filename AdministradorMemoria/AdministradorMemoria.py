# -*- coding: utf-8 -*-
import Memoria as m
import Swap as s
import Fisica as f
import sys
import  datetime as time
import re
sys.path.append('..')
import Proceso as pro


import random as r


class AdministradorMemoria(object):
	"""Clase que hace la simulacion de la administracion de memoria.
		Ocupa la paginacion para realizar la simulacion de la memoria.
	    Constructor:
	    	procesos:{
	    		self.procesos[p.ide] = {
	    		"proceso": p,
	    		"memoria": memoria,
	    		"tamMemoria":tamMemoria,
	    		"posMemoria":posMemoria,
	    		"fecha":fecha
	    		},
	    		....
	    	},swap:Swap, fisica:Fisica, tablaPagina:{}

		    procesos			=> Contiene los procesos que estan siendo administrados por el administrador de memoria
		    swap 				=> Es la memoria swap que tienes el administrador
		    fisica 				=> Es la memoria fisica que tienes el administrador
		    tablaPagina			=> Es la tabla de paginas utilizada para implementar la paginacion

	"""
	def __init__(self, procesos = {} ,swap = s.Swap(), fisica = f.Fisica(), tablaPagina={}):
		super(AdministradorMemoria, self).__init__()
		self.swap = swap
		self.fisica = fisica
		self.tablaPagina = tablaPagina
		self.procesos = procesos
	def agregarProceso(self,p):
		"""Agrega un proceso al administrador de memoria.
			Parámetros:
				(p:Proceso)
			Retorno:
				True en caso de exito
				None en caso de que las memorias esten llenas

		"""
		#variables del proceso 
		memoria = None
		posMemoria = []
		tamProcesoMemoria = 3
		fecha = time.datetime.now().microsecond#obtenemos la fecha actual del proceso 
		if isinstance(p,int) or isinstance(p,str):
			p = pro.Proceso(ide=int(p),nom="Proceso")

		if not re.match(r'Navegador.*',p.nom):
			tamProcesoMemoria = 1
		vacioFisica = len(self.fisica.posMarcosVacios)
		memoria = self.fisica

		#Validamos que no este llena la memoria swap
		if len(self.swap.posPaginasVacias) < tamProcesoMemoria and len(self.fisica.posMarcosVacios) < tamProcesoMemoria:
			return None
		if vacioFisica >= tamProcesoMemoria:
			#podemos agregar a la memoria fisica el proceso
			marcosVaciosPos = self.fisica.posMarcosVacios;
			cont = 1
			for pos in marcosVaciosPos:
				if cont > tamProcesoMemoria:
					break
				#agregamos a los marcos
				self.fisica.marcos[pos] = p.ide
				posMemoria.append(pos)
				#agregamos las posiciones ocupadas
				self.fisica.posMarcosOcupados.append(pos)
				cont += 1
			#quitamos los marcos disponibles de la memoria fisica
			for x in posMemoria:
				del self.fisica.posMarcosVacios[self.fisica.posMarcosVacios.index(x)]

			self.procesos[p.ide] = {"proceso": p,"memoria": memoria,"tamMemoria":tamProcesoMemoria,"posMemoria":posMemoria,"fecha":fecha}
			return True
		else:
			#Hacemos espacio en la memoria fisica 
			while  len(self.fisica.posMarcosVacios) < tamProcesoMemoria:
			#Buscamos el proceso mas viejo 
				print "swap = "+self.swap.toString()+" \nfisica = "+self.fisica.toString()
				(ide,val) = self.buscarProcesoMasViejo(whereMemoria = self.fisica)
				print "proceso viejo "+str(type(val['memoria']))
				if self.moverProcesoA(val['proceso'],self.swap)==True:
					print "proceso movido"
				else:
					print "algo se chingo"
				print  "tamaño de los marcos vacios "+str( len(self.fisica.posMarcosVacios) )
			return self.agregarProceso(p)
	def buscarProcesoMasNuevo(self,whereMemoria = None,opciones = {}):
		"""Busca el proceso mas nuevo.
			whereMemoria es la memoria donde sera buscado el proceso.
			None para buscar en ambas memorias.
		"""
		items = self.procesos.items()
		(key,val) = (None,None)
		if whereMemoria == None:
			(key,val) = items[0]
			for (k,v) in items:
				if v['fecha'] > val['fecha']:
					(key,val) = (k,v)
		elif isinstance(whereMemoria, s.Swap):
			cont = 0
			for (k,v) in items:
				if isinstance(v['memoria'], s.Swap):
					if cont == 0:
						(key,val) = (k,v)
						cont += 1
					if v['fecha'] > val['fecha']:
						(key,val) = (k,v)
		elif isinstance(whereMemoria, f.Fisica):
			cont = 0
			for (k,v) in items:
				if isinstance(v['memoria'], f.Fisica):
					if cont == 0:
						(key,val) = (k,v)
						cont += 1
					if v['fecha'] > val['fecha']:
						(key,val) = (k,v)
		return (key,val)

	def buscarProcesoMasViejo(self,whereMemoria = None):
		"""Busca el proceso mas viejo.
			whereMemoria es la memoria donde sera buscado el proceso.
			None para buscar en ambas memorias.
		"""
		items = self.procesos.items()
		(key,val) = (None,None)
		if whereMemoria == None:
			(key,val) = items[0]
			for (k,v) in items:
				if v['fecha'] < val['fecha']:
					(key,val) = (k,v)
		elif isinstance(whereMemoria, s.Swap):
			cont = 0
			for (k,v) in items:
				if isinstance(v['memoria'], s.Swap):
					if cont == 0:
						(key,val) = (k,v)
						cont += 1
					if v['fecha'] < val['fecha']:
						(key,val) = (k,v)
		elif isinstance(whereMemoria, f.Fisica):
			cont = 0
			for (k,v) in items:
				if isinstance(v['memoria'], f.Fisica):
					if cont == 0:
						(key,val) = (k,v)
						cont += 1
					if v['fecha'] < val['fecha']:
						(key,val) = (k,v)
		return (key,val)

	def buscarProceso(self,p):
		"""Busca un proceso en el administrador de memoria.
		La busqueda se hace con el ide del proceso.
			Parámetros:
				(p:Proceso)
			Retorno:
				{
	    			proceso:Proceso,
	    			memoria: Memoria,
	    			posMemoria:[]
	    		}
	    		En caso de error el retorno seria None
		"""
		print "p"+str(type(p))
		if isinstance(p,int):
			if(self.procesos.has_key(p)):
				return self.procesos[p]
		elif isinstance(p,str):
			if(self.procesos.has_key(int(p))):
				return self.procesos[int(p)]
		else:
			if(self.procesos.has_key(p.ide)):
				return self.procesos[p.ide]


	def moverProcesoA(self,p,memoria):
		"""Mueve un proceso p a otra memoria.
			El proceso debe de estar en alguna memoria
			Parámetros:
				(p:Proceso,memoria:Memoria)
			Retorno:
				boolean
		"""
		procesoDic = self.buscarProceso(p)
		print str(type(procesoDic['memoria']))+str(procesoDic["proceso"].nom)+"---> "+str(type(memoria))
		if isinstance(memoria, s.Swap):#mover procesos a swap
			print "posiciones de memoria "
			print procesoDic["posMemoria"]

			for pos in procesoDic["posMemoria"]:
				procesoDic["memoria"].marcos[pos] = 0#marcamos los marcos como disponibles
				self.fisica.posMarcosVacios.append(pos)
				del self.fisica.posMarcosOcupados[self.fisica.posMarcosOcupados.index(pos)]
			#buscamos en la memoria mas paginas vacias 
			posDisponiblesSwap =  memoria.posPaginasVacias
			posNoDIsp = []#arreglo para paginas no disponibles
			cont = 0
			print "disponibles de la swap"
			print posDisponiblesSwap
			for x in posDisponiblesSwap:
				if cont == procesoDic["tamMemoria"]:
					break
				print str(x)+",",
				memoria.paginas[x] = p.ide
				posNoDIsp.append(x)
				cont +=1
			for x in posNoDIsp:
				del posDisponiblesSwap[posDisponiblesSwap.index(x)]

			memoria.posPaginasOcupadas += posNoDIsp

			##actualizamos el proceso
			procesoDic["memoria"] = self.swap
			procesoDic["posMemoria"] = []
			procesoDic["posMemoria"] = posNoDIsp
			procesoDic["fecha"] = time.datetime.now().microsecond

			return True
		elif isinstance(memoria, f.Fisica):
			posMemoria = procesoDic["posMemoria"]
			memoriaSwap = procesoDic["memoria"]
			for pos in posMemoria:
				memoriaSwap.paginas[pos] = 0
				self.swap.posPaginasVacias.append(pos)
				del self.swap.posPaginasOcupadas[self.swap.posPaginasOcupadas.index(pos)]
			self.agregarProceso(p)
			return True
	def actualizarFisica(self):
		##buscar el proceso de la swap mas nuevo 
		#y que quepa en la memoria fisica
		while len(self.fisica.posMarcosVacios) >= 1:
			cont = 0
			#buscar el de mayor tiempo (mas nuevo)
			items = self.procesos.items()
			(key,val) = (None,None)
			for (k,v) in items:
				if isinstance(v['memoria'], s.Swap):
					if cont == 0:
						(key,val) = (k,v)
						cont += 1
					if v['fecha'] > val['fecha'] and v["tamMemoria"] <= len(self.fisica.posMarcosVacios):
						(key,val) = (k,v)
			if key != None:#encontramos el proceso
				self.moverProcesoA(self.procesos[key]["proceso"],self.fisica)
			else:
				break




	def matarProceso(self,p):
		""" Mata un proceso tomando en cuenta el ide del proceso.
			Elimina un proceso de la memoria
		"""
		procesoDic = self.buscarProceso(p)
		print "procesos matar"+str(procesoDic)
		posicionesVacias = []
		if isinstance(procesoDic["memoria"],f.Fisica):
			for x in procesoDic["posMemoria"]:
				self.fisica.marcos[x] = 0
				del self.fisica.posMarcosOcupados[self.fisica.posMarcosOcupados.index(x)]
				posicionesVacias.append(x)
			self.fisica.posMarcosVacios += posicionesVacias
			posDisponibles = procesoDic["posMemoria"]
			del self.procesos[procesoDic["proceso"].ide]
			self.actualizarFisica()

			return True
		if isinstance(procesoDic["memoria"],s.Swap):
			self.moverProcesoA(p,self.fisica)
			self.matarProceso(p)
			"""
			for x in procesoDic["posMemoria"]:
				self.swap.paginas[x] = 0
				del self.swap.posPaginasOcupadas[self.swap.posPaginasOcupadas.index(x)]
				posicionesVacias.append(x)
			self.swap.posPaginasVacias += posicionesVacias
			del self.procesos[p.ide]
			return Trueme
			"""
	def dormirProceso(self):
		pass
	def despertarProceso(self):
		pass



"""
	
	self.procesos[p.ide] = {
	"proceso": p,
	"memoria": memoria,
	"tamMemoria":tamMemoria,
	"posMemoria":posMemoria,
	"fecha":fecha
	},
"""
def imprimirProcesos(admon):
	items = admon.procesos.items()
	print "PROCESOS______________________"
	for (k,v) in items:
		print "*********************************************+"
		print "\tide "+str(k)
		print "\tmemoria "+str(v["memoria"])
		#print "\ttamMemoria "+str(v["tamMemoria"])
		print "\tposMemoria "+str(v["posMemoria"])
		print "\tfecha "+str(v["fecha"])
		#print "\tnombre "+str(v["proceso"].nom)
	print "Estado memorias _________________"
	print "swap : "+admon.swap.toString()
	print admon.swap.paginas
	print "fisica : "+admon.fisica.toString()
	print admon.fisica.marcos





nombres = ["Navegador","Otro","ManProceso"]
dicProcesos = {}


def test():
	admon = AdministradorMemoria()
	num = int(input("numero de procesos"))
	for x in range(1,num):
		dicProcesos[x] = pro.Proceso(ide=x,nom=nombres[x%3])
		admon.agregarProceso(dicProcesos[x])
	
	while True:
		print "\n"*10
		imprimirProcesos(admon)
		opt = int(input("1) crea un procesos \n 2)mover proceso \n 3) eliminar proceso\n"))
		if opt == 1:
			crearProcesos(admon)
		elif opt == 2:
			mover(admon)
		elif opt == 3:
			eliminar(admon)


def crearProcesos(admon):
	while True:

		print "\n"*10
		imprimirProcesos(admon)
		pid = int(input("pid del proceso -1 terminar"))
		if pid == -1:
			break
		dicProcesos[pid] = pro.Proceso(ide=pid,nom=nombres[pid%3])
		admon.agregarProceso(dicProcesos[pid])

	
def mover(admon):
	while True:

		print "\n"*10
		imprimirProcesos(admon)
		pos =int(input("posicion del proceso a mover"))
		memoria =int(input("1 a fisica 2 swap -1 para dejar de mover"))
		if memoria == -1:
			break
		if memoria == 1:
			admon.moverProcesoA(dicProcesos[pos],admon.fisica)
		else:
			admon.moverProcesoA(dicProcesos[pos],admon.swap)
		imprimirProcesos(admon)

def eliminar(admon):
	while True:
		print "\n"*10
		imprimirProcesos(admon)
		pos =int(input("ide del proceso a matar -1 terminar"))
		if pos==-1:
			break
		admon.matarProceso(dicProcesos[pos])
		print "proceso matado"










"""
test()
pi = a[3]
print "proceso pi.ide"
print pi.ide
admon.moverProcesoA(pi,admon.swap)
pi = a[4]
print "proceso pi.ide"
print pi.ide
admon.moverProcesoA(pi,admon.swap)

imprimirProcesos(admon)
"""