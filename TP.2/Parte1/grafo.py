from heapq import heappush, heappop
from collections import deque

class Grafo (object):
	
	def __init__(self):
		self.vertices ={}
	
	def agregar_arista(self,cord_x,cord_y,peso = 1):
		if not cord_x in self.vertices:
			self.vertices[cord_x] = []
		if not cord_y in self.vertices:
			self.vertices[cord_y] = []
		self.vertices[cord_x].append((cord_y,peso))
	
	def camino_minimo(self,origen,destino,con_camino = False):
		if destino!= None:
			if not origen in self.vertices or not destino in self.vertices:
				raise KeyError()
		
		vecinos = []
		vuelta = {}
		costos = {}
		heappush(vecinos, (0, origen))
		vuelta[origen] = None
		costos[origen] = 0

		while vecinos:
			actual = heappop(vecinos)[1]
			if actual == destino:
				break
			for v,peso in self.vertices[actual]:
				
				#if v in self.vertices:
				nuevo_costo = costos[actual] + peso

				if not v in costos or nuevo_costo < costos[v]:
					costos[v] = nuevo_costo
					heappush(vecinos,(nuevo_costo, v))
					vuelta[v] = actual
		if not destino in costos:
			return None, -1
		if con_camino == True:
			return self.reconstruir_camino(vuelta, origen, destino),costos[destino] 
		else:
			return costos[destino]
	
	def obtener_camino(self,origen1,origen2,destino, con_camino = False):
		camino_1 = None
		camino_2 = None
		if origen1 == destino:
			camino_1 = [origen1]
		if origen2 == destino:
			camino_2 = [origen2]
		
		padre, orden = self.bfs(destino)
		if camino_1 != [origen1]:
			camino_1 = self.reconstruir_camino(padre,destino,origen1)
		if camino_2 !=  [origen2]:
			camino_2 = self.reconstruir_camino(padre,destino,origen2)
		
		if con_camino == True:
			return camino_1,camino_2
		else:
			if camino_1 != None and camino_2 != None:
				return len(camino_1),len(camino_2)
			elif camino_1 == None and camino_2 != None:
				return -1,len(camino_2)
			elif camino_2 == None and camino_1 != None:
				return len(camino_1),-1
			else:
				return -1,-1
	
	def bfs(self, inicio = None):
		if inicio == None:
			inicio = self.vertices.keys()[0]
		cola = deque([inicio])
		padre = {inicio: None}
		orden = {inicio: 0}
		visitados = []

		while len(cola) > 0:
			v = cola.popleft()
			visitados.append(v)

			for vertice,peso in self.vertices[v]:
				if not vertice in visitados:
					cola.append(vertice)
					padre[vertice] = v
					orden[vertice] = orden[v] + 1
					visitados.append(vertice)

		return padre,orden
	
	def reconstruir_camino(self, vuelta, origen, destino):
		if not destino in vuelta:
			return None
		camino = []
		while destino != origen:
			camino.append(destino)
			destino = vuelta[destino]
		camino.append(destino)
		camino.reverse()
		return camino
	
	def imprimir_grafo(self):
		print self.vertices
