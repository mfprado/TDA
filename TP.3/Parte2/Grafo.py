from collections import deque
from heapq import heappush, heappop

class Grafo (object):
	
	def __init__(self):
		self.vertices_simil_residual = {} #grafo simil residual = grafo residual sin las aristas originales
		self.vertices_completo = {} #grafo resifual
	
	def agregar_arista(self,vertice_1,vertice_2,peso = 0):
		'''Se agrega al grafo completo la arista que une al vertice_1 con el vertice_2, 
		la cual tendra peso 'peso'.
		Se agrega al grafo simil residual y al completo la arista que une al vertice_2 
		con el vertice_1, la cual tendra peso cero.
		'''
		if not vertice_1 in self.vertices_completo:
			self.vertices_simil_residual[vertice_1] = {}
			self.vertices_completo[vertice_1] = {}
		if not vertice_2 in self.vertices_completo:
			self.vertices_simil_residual[vertice_2] = {}
			self.vertices_completo[vertice_2] = {}

		self.vertices_completo[vertice_1][vertice_2] = int(peso)
		self.vertices_completo[vertice_2][vertice_1] = 0
		self.vertices_simil_residual[vertice_2][vertice_1] = 0
		
	def camino_minimo(self,origen = '0',destino = '1'):
		'''Devuelde una lista con el seguimiento del camino minimo entre origen y destino.
		Tambien devuelve una lista con los pesos de las aristas recorridas, estos pesos no se devuelven
		en el orden de recorrido necesariamente'''
		vecinos = []
		vuelta = {}
		costos = {}
		heappush(vecinos, (0, origen))
		vuelta[origen] = None
		costos[origen] = 0
		pesos = []

		while vecinos:
			actual = heappop(vecinos)[1]
			if actual == destino:
				break
			for v,peso in self.vertices_completo[actual].items():
				nuevo_costo = costos[actual] + peso
				if peso != 0 and (not v in costos or nuevo_costo < costos[v]):
					costos[v] = nuevo_costo
					heappush(vecinos,(nuevo_costo, v))
					vuelta[v] = (actual,peso)
		
		return self.reconstruir_camino(vuelta, origen, destino)
		
	def reconstruir_camino(self, vuelta, origen, destino):
		'''Devuelde una lista con el seguimiento del camino entre origen y destino.
		Tambien devuelve una lista con los pesos de las aristas recorridas, estos pesos no se devuelven
		en el orden de recorrido, sino en sentido contrario'''
		if not destino in vuelta:
			return None,0
		camino = []
		pesos = []
		destino = (destino,0)
		while destino[0] != origen:
			camino.append(destino[0])
			pesos.append(destino[1])
			destino = vuelta[destino[0]]
		camino.append(destino[0])
		pesos.append(destino[1])
		pesos.pop(0)
		camino.reverse()
		return camino,pesos
		
	def imprimir_grafo(self):
		'''Imprime el grafo simil residual, el cual es como el grafo residual sin las aristas originales (vertices_simil_residual), 
		que se expresa en forma de diccionario:
			vertices_simil_residual={vertice_1:{vertice_2:'peso1a2', vertice_5:'peso1a5'}, vertice_3:{vertice_4:'peso3a4'},...}
		Imprime el grafo residual (vertices_completo), que se expresa en forma de diccionario como el grafo simi residual'''
		print self.vertices_simil_residual	
		print self.vertices_completo
		
	def Ford(self, origen, destino):
		'''Recibe por parametro la fuente (origen) y el sumidero (destino).
		Se aplica el algoritmo Ford Fulkerson al grafo, luego se devuelve el flujo maximo del grafo
		y las dos aristas con mayor flujo'''
		camino,pesos = self.camino_minimo('0','1')
		flujo_maximo = 0
		while camino != None:
			#actualizacion de los pesos
			minimo = min(pesos)
			flujo_maximo += minimo #se suman los 'cuellos de botella'
			while len(camino) > 1:
				vertice_1 = camino[0]
				vertice_2 = camino[1]
				nuevo_peso_arista_1_2 = self.vertices_completo[vertice_1][vertice_2] - minimo
				self.vertices_completo[vertice_1][vertice_2] = nuevo_peso_arista_1_2
				nuevo_peso_arista_2_1 = self.vertices_completo[vertice_1][vertice_2] + minimo
				self.vertices_completo[vertice_2][vertice_1] = nuevo_peso_arista_2_1
				
				if vertice_2 in self.vertices_simil_residual[vertice_1]:
					self.vertices_simil_residual[vertice_1][vertives_2] = nuevo_peso_arista_1_2
				else:
					self.vertices_simil_residual[vertice_2][vertice_1] = nuevo_peso_arista_2_1
					
				camino = camino[1:]
			camino,pesos = self.camino_minimo('0','1')
		arista_flujo_max = self.arista_max_flujo()
		return flujo_maximo, arista_flujo_max #flujo_maximo, arista_max_flujo	

	def arista_max_flujo(self):
		'''Devuelve la arista del grafo simil residual (vertices_simil_residual) por la cual 
		pasa mayor flujo'''
		arista = (0, (0,0))
		
		for vertice_1 in self.vertices_simil_residual:
			for vertice_2, peso in self.vertices_simil_residual[vertice_1].items():
				if peso>arista[0]:
					arista = (peso, (vertice_2,vertice_1))

		return arista[1]

	def eliminar_arista(self, arista):
		'''Elimina el peso de la arista pasada por parametro.
		arista = (vertice_1, vertice_2)'''
		self.vertices_completo[arista[0]][arista[1]] = 0

	def flujo_maximo_despues_de_sabotaje(self, arista_1, arista_2):
		'''Recibe las dos aristas de mayor flujo de la forma (vertice_1,vertice_2), ya que si 
		hay sabotaje se roba la informacion que pasa por esas aristas.
		Se le pone peso cero a las dos aristas pasadas por parametro. Para saber el flujo maximo
		luego del sabotaje, el grafo al que se le debe aplicar esta funcion es al grafo original.
		Se le aplica Ford Fulkerson al grafo para objeter el flujo maximo.'''
		#arista_1 = (vertice_1, vertice_2)
		self.eliminar_arista(arista_1)
		self.eliminar_arista(arista_2)
		flujo_maximo, arista = self.Ford('0','1')
		return flujo_maximo
