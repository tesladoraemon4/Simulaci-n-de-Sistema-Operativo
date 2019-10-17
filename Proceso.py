class Proceso(object):
	def __init__(self,ide,nom,tiempo=None,edo=None,nucleo=None,row=None,col=None):
		super(Proceso, self).__init__()
		self.ide = ide
		self.nom = nom
		self.nucleo = nucleo
		self.tiempo = tiempo
		self.edo = edo
		self.row = row
		self.col = col

	def toString(self):
		return "id#"+str(self.ide)+"\edo:\t"+str(self.edo)+"\NucleoID:"+str(self.nucleo.idNum)+"\n"
