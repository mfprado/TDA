from collections import deque
from heapq import heappush, heappop

class Grafo (object):
	
	def __init__(self):
		self.vertices_residual = {}
		self.vertices_completo = {}
	
	def agregar_arista(self,vertice_1,vertice_2,peso = 0):
		if not vertice_1 in self.vertices_completo:
			self.vertices_residual[vertice_1] = {}
			self.vertices_completo[vertice_1] = {}
		if not vertice_2 in self.vertices_completo:
			self.vertices_residual[vertice_2] = {}
			self.vertices_completo[vertice_2] = {}

		self.vertices_completo[vertice_1][vertice_2] = peso
		self.vertices_completo[vertice_2][vertice_1] = 0
		self.vertices_residual[vertice_2][vertice_1] = 0
		
	def camino_minimo(self,origen = '0',destino = '1'):
		"""if destino!= None:
			if not origen in self.vertices or not destino in self.vertices:
				raise KeyError()"""
		
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
		print self.vertices_residual	
		print self.vertices_completo
		
	def Ford(self, origen, destino):
		camino,pesos = self.camino_minimo('s','t')
		
		while camino != None:
			#actualizacion de los pesos
			minimo = min(pesos)
			while len(camino) > 1:
				vertice_1 = camino[0]
				vertice_2 = camino[1]
				nuevo_peso_arista_1_2 = self.vertices_completo[vertice_1][vertice_2] - minimo
				self.vertices_completo[vertice_1][vertice_2] = nuevo_peso_arista_1_2
				nuevo_peso_arista_2_1 = self.vertices_completo[vertice_1][vertice_2] + minimo
				self.vertices_completo[vertice_2][vertice_1] = nuevo_peso_arista_2_1
				
				if vertice_2 in self.vertices_residual[vertice_1]:
					self.vertices_residual[vertice_1][vertives_2] = nuevo_peso_arista_1_2
				else:
					self.vertices_residual[vertice_2][vertice_1] = nuevo_peso_arista_2_1
					
				camino = camino[1:]
			camino,pesos = self.camino_minimo('s','t')
			
		print "Los ejes a vigilar son: ",self.aritas_de_mayor_flujo()
		
		
		
		
	def aritas_de_mayor_flujo(self):
		aritas = []
		
		for vertice_1 in self.vertices_residual:
			for vertice_2,peso in self.vertices_residual[vertice_1].items():
				heappush(aritas, ((-1)*peso, (vertice_2,vertice_1)))
				
		flujo_1 = heappop(aritas)[1]
		flujo_2 = heappop(aritas)[1]
		 
		return flujo_1,flujo_2
				
							


def main():
	grafo = Grafo()
	grafo.agregar_arista('s','a',9)
	grafo.agregar_arista('a','c',8)
	grafo.agregar_arista('c','t',10)
	grafo.agregar_arista('s','b',9)
	grafo.agregar_arista('b','d',3)
	grafo.agregar_arista('d','t',7)
	grafo.agregar_arista('a','b',10)
	grafo.agregar_arista('b','c',1)
	grafo.agregar_arista('d','c',8)
	grafo.imprimir_grafo()
	print grafo.Ford('s','t')

main()
