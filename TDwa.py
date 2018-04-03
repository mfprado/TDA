#! /usr/bin/python

#Para ejecutar si dice "permiso denegado" poner "chmod 777 TDa.py" y despues volver a ejecutar con "./TDa.py"
from heapsort import Heapsort
from quicksort import Quicksort
from insercion import Insercion
from seleccion import Seleccion
from merge import Mergesort

import random
from time import time
INF = 9999999

def diezSets():
	sets=[]
	for i in range(0,2):
		lista=[]
		for x in range(0,10):
			lista.append(random.randint(0,INF))
		sets.append(lista)
	return sets
	
def promedio (lista):
	promedios = []
	pr = []
	print len(lista)
	for i in range (3):
		for j in range (2):
			suma = 0
			for k in range (2):
				suma += lista[j][i][k]
			promedios.append(suma/10)
		pr.append(promedios)
	print pr
	

def main():
	sets = diezSets()
	cantidad = [1,5,10]
	tiempos = []
	for set in sets:
		tiemposDelSet = []
		for i in cantidad:
			tiemposDeCantidad = []
			nuevoSet = set[0:i]
			
			tiempoIni=time()
			Quicksort(nuevoSet,0, i)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			
			nuevoSet = set[0:i]
			tiempoIni=time()
			Heapsort(nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			
			"""nuevoSet = set[0:i]
			tiempoIni=time()
			Mergesort(nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			
			
			nuevoSet = set[0:i]
			tiempoIni=time()
			Seleccion(nuevoSet, i)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			print len(tiemposDeCantidad)
			
			nuevoSet = set[0:i]
			tiempoIni=time()
			Insercion (nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			print len(tiemposDeCantidad), "fin"""
			tiemposDelSet.append(tiemposDeCantidad)
		tiempos.append(tiemposDelSet)
	promedio(tiempos)
	return tiempos

main()
