""" Diccionario de poblados """

class poblado:
	
	def __init__(self, nombre, poblacion):
		self.nombre = nombre
		self.poblacion = poblacion
		inicializar(self)
	
	def inicializar(self): 
		porc_pob_rec_ini = 20 #porcentaje de poblacion reclutable inicial
		self.pob_rec = self.poblacion * porc_pob_rec_ini / 100

	def ocupado(self, ejercito):
		
		
	def pasar_turno(self):
		
		
class ejercito:
	
	def __init__(self, poblado):
		self.ubicacion = poblado
		

