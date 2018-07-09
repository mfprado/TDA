from AttackStrategy import *
from itertools import permutations
import numpy
import itertools

class DinamicAttack(AttackStrategy):

	def __init__(self, shuttlesCount, board):
		AttackStrategy.__init__(self, shuttlesCount, board)

		barcosLista = board.getShips()
		self.barcos=[]
		for i in range(0, len(barcosLista)):
			barco = barcosLista[i]
			self.barcos.append(barco.life)

		#self.turnsToKillShip = {}
		self.ataques = {} #(vidas, columna) = (ataqueOptimo, puntosTotales)
		self.listaAtaques = numpy.array(list(self.partitions(shuttlesCount, len(self.barcos))))
		self.calcularAtaqueOptimo(self.barcos, 0, board)

	def partitions(self, n, b):
		masks = numpy.identity(b, dtype=int)
		for c in itertools.combinations_with_replacement(masks, n): 
			yield sum(c)

	def barcosVivos(self, barcos):
		contador=0
		for vida in barcos:
			if vida>0:
				contador+=1
		return contador

	def calcularAtaqueOptimo(self, barcos, turno, board):
		if (self.barcosVivos(barcos))<0:
			return ([0]*len(self.barcos), 0)
		posicion = turno%(board.columnsCount())
		if ((tuple(barcos), posicion) in self.ataques):
			return self.ataques[(tuple(barcos),posicion)]

		for ataque in self.listaAtaques:
			barcosAAtacar = barcos
			barcosAtacados = self.atacar(barcosAAtacar, board, posicion, ataque)
			(ataqueOptimo , puntosOptimo) = self.calcularAtaqueOptimo(barcosAtacados, turno+1, board)
			puntos = self.barcosVivos(barcosAtacados) + puntosOptimo
			if (barcos, posicion) in self.ataques:
				if self.ataques[(tuple(barcos), posicion)][1]>puntos:
					self.ataques[(tuple(barcos), posicion)] = (ataque, puntos)
			else:
				self.ataques[(tuple(barcos), posicion)] = (ataque, puntos)
		return self.ataques[(tuple(barcos), posicion)]

	def atacar(self, barcos, board, columna, ataque):
		for i in range(0, len(barcos)):
			barcos[i]-= ataque[i]*board.cells[i][columna].damage
			if barcos[i]<0:
				barcos[i]=0
		return barcos

	def attack(self, board):
		columna = board.shipsActualColumn
		ataqueOptimo, puntosOptimos = self.ataques[(self.barcos, columna)]
		self.barcos=self.atacar(self.barcos, board, columna, ataqueOptimo)
		for i in range(0, len(ataqueOptimo)):
			cantidadLanzaderas = ataqueOptimo[i]
			j=0
			cellToAttack = board.cells[i][columna]
			barco = cellToAttack.getShip()
			print("Ataque a celda (" + str(i) + " ," + str(columna) + ") con " + cantidadLanzaderas + " lanzaderas\n")
			while j<cantidadLanzaderas:
				barco.receiveAttack(cellToAttack.damage)
				j+=1