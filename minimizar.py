'''
CLASE DEDICADA A LA MINIMIZACION DE UN AFD
'''

import copy

#Clase para minimizacion de automatas finitos deterministas
class minimizar (object):
	#Declarar variables en relación al AFD
	def __init__(self, estadosAFD, estados_finalesAFD, estado_inicialesAFD, simbolosAFD, afd):
		self.estadosAFD = estadosAFD
		self.estados_finalesAFD = estados_finalesAFD
		self.estado_inicialAFD = estado_inicialesAFD
		self.simbolosAFD = simbolosAFD
		self.afd = afd
		self.dfa_minimizado = None

	#Establecer todas las variables para la minimizacion
	def new_estados(self, estadosAFD):
		tabla = ""
		estadosAFD  = estadosAFD.split(",")
		for estado in estadosAFD:
			estado = estado.split("\n")[0]
			if estado != '' :
				self.estadosAFD.append(estado)

	def new_simbolos(self, simbolosAFD):
		simbolosAFD  = simbolosAFD.split(",")
		for simbolo in simbolosAFD:
			simbolo = simbolo.split("\n")[0]
			if simbolo != '' :
				self.simbolosAFD.append(simbolo)

	def new_estado_inicial(self, estado_inicialAFD):
		self.estado_inicialAFD = str(estado_inicialAFD).split("\n")[0]

	def new_estados_finales(self, estadosAFD):
		estadosAFD  = estadosAFD.split(",")
		for estado in estadosAFD:
			estado = estado.split("\n")[0]
			if estado != '' :
				self.estados_finalesAFD.append(estado)

	#Tabla de estado para agrupar
	def contruir(self, tabla):
		transiciones = tabla.split("\n")
		for transicion in transiciones:
			f = transicion.split(",")
			if len(f) == 3:
				origen = f[0].split(" ")[0]
				simbolo = f[1].split(" ")[0]
				destino = f[2].split(" ")[0]
				self.transicion(origen, simbolo, destino)
	#Actualizar los estados
	def transicion(self, origen, simbolo, destino):
		indice_tupla = None
		ind = 0
		for state in self.afd: 
			if state[0]== origen and state[1]== simbolo and state[2] == destino: indice_tupla = ind
			ind += 1
		if not indice_tupla: self.afd.append((origen, simbolo, destino)) 

		""" 		if self.afd in (origen):
			self.afd[origen].update({simbolo :  destino})
		else:
			self.afd[origen] = {simbolo : destino} """
	
	def new_afd(self, estado, simbolo):
		estado_resultante = None
		cont = 0
		while len(self.afd)>cont and not estado_resultante:
			if self.afd[cont][0] == estado and self.afd[cont][1] == simbolo:
				estado_resultante = self.afd[cont][2]
			cont += 1
		return estado_resultante
		""" if estado in self.estadosAFD:
		 	if self.afd[estado] in (simbolo):
		 		return self.afd[estado][simbolo]
		return None """

	def estados_alcanzables(self):
		alcanzables = [self.estado_inicialAFD]
		a_verificar = [self.estado_inicialAFD]

		while a_verificar:
			estado = a_verificar.pop(0)
			for simbolo in self.simbolosAFD:
				alcanzado  = self.new_afd(estado, simbolo)
				if alcanzado and alcanzado not in alcanzables:
					a_verificar.append(alcanzado)
					alcanzables.append(alcanzado)
		
		return alcanzables

	def dic_distinguidas(self, clases_distinguidas):
		estados = {}
		for i in range(len(clases_distinguidas)):
			clave = ''.join(clases_distinguidas[i])
			estados.update({clave : clases_distinguidas[i]})
		return estados

	def nuevos_estados_finales(self, dic_distinguidas):
		finales = []
		
		for estado in self.estados_finalesAFD:
			nuevo_final = self.indice_nueva_clase(estado, dic_distinguidas)
			if nuevo_final != None and nuevo_final not in finales:
				finales.append(nuevo_final)

		return finales

	def nuevo_estado_inicial(self, dic_distinguidas):
		return self.indice_nueva_clase(self.estado_inicialAFD, dic_distinguidas)

	def nuevos_estados(self, dic_distinguidas):
		estados = []
		
		for estado in self.estadosAFD:
			estado_nuevo = self.indice_nueva_clase(estado, dic_distinguidas)
			if estado_nuevo != None and estado_nuevo not in estados:
				estados.append(estado_nuevo)

		return estados

	def nueva_afd(self, min_dfa, dic_distinguidas):
		
		for estado in dic_distinguidas.keys():
			
			viejo_estado = dic_distinguidas[estado][0] if dic_distinguidas[estado] else estado

			for simbolo in self.simbolosAFD:
				viejo_destino = self.new_afd(viejo_estado, simbolo)
				nuevo_destino = self.indice_nueva_clase(viejo_destino, dic_distinguidas)
				min_dfa.transicion(estado, simbolo, nuevo_destino)

	def indice_nueva_clase(self, simbolo, dic_distinguidas):
		for k in dic_distinguidas.keys():
			if simbolo in dic_distinguidas[k]:
				return k
		return None

	def particiones_sucesivas(self, p0):
		p1 = self.distingue(p0)
		if p1 == p0:
			return p1
		else:
			return self.particiones_sucesivas(p1)

	#Elementos distinguibles dentro de una clase de equivalencia
	def distingue(self, p0):
		nueva_particion = []
		particion = copy.deepcopy(p0)

		for clase_equivalencia in particion:
			if len(clase_equivalencia) > 1:

				nueva_clase = [clase_equivalencia.pop(0)]
				elementos_a_comparar = [nueva_clase[0], clase_equivalencia.pop(0)]
				
				while len(elementos_a_comparar) == 2:
					a = elementos_a_comparar.pop(0)
					b = elementos_a_comparar.pop(0)

					distinguible = False

					for simbolo in self.simbolosAFD:
						estado_a = self.new_afd(a, simbolo)
						estado_b = self.new_afd(b, simbolo)

						if estado_a == None or estado_b == None:
							continue
						elif self.indice(estado_a, p0) != self.indice(estado_b, p0):
							nueva_particion.append([b])
							distinguible = True
						
					if not distinguible:
						nueva_clase.append(b)
						
					if clase_equivalencia:
						elementos_a_comparar.append(a)
						elementos_a_comparar.append(clase_equivalencia.pop(0))	

				nueva_particion.append(nueva_clase)

			else:
				nueva_particion.append(clase_equivalencia)
		
		return nueva_particion

	def indice(self, elemento, particion):
		for i in range(len(particion)):
			clase = particion[i]
			if elemento in clase:
				return i
		return -1

	#Juntar todo para la impresion
	def reIstanciate(self):
		alcanzables = set([ estado for item in self.estados_alcanzables() for estado in item]) # alcanzables
		estadosAFD = list(alcanzables & set(self.estadosAFD))
		estados_finalesAFD = list(alcanzables | set(self.estados_finalesAFD)) #Ver lo de la intersección de estados

		p0 = [estados_finalesAFD, list(set(estadosAFD) - set(estados_finalesAFD))]
		
		clases_distinguidas = self.particiones_sucesivas(p0)
		clases_distinguidas = self.dic_distinguidas(clases_distinguidas)
		nuevos_estados = self.nuevos_estados(clases_distinguidas)
		nuevos_finales = self.nuevos_estados_finales(clases_distinguidas)
		nuevo_inicial = self.nuevo_estado_inicial(clases_distinguidas)
		
		self.dfa_minimizado = minimizar(nuevos_estados, nuevos_finales, nuevo_inicial, self.simbolosAFD, self.afd)

		self.nueva_afd(self.dfa_minimizado, clases_distinguidas)
		
		lista = estados_finalesAFD
		print('\nAFD minimizado')

""" 	def fixEstadosResultantes(self, lista):
			new_estados = []
			for estados in lista: new_estados.extend(estados.split("Q"))
			new_estados = [f'Q{num_estado}' for num_estado in new_estados] """
 
	