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
	for i in range(0,10):
		lista=[]
		for x in range(0,10000):
			lista.append(random.randint(0,INF))
		sets.append(lista)
	return sets
	
def promedio (lista):
	suma = 0
	for i in lista:
		
		for j in i:
			suma += j[0]
	return suma/len(lista)

def main():
	sets = diezSets()
	cantidad = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]
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
			Seleccion(nuevoSet, i)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			
			nuevoSet = set[0:i]
			tiempoIni=time()
			Insercion (nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)

			nuevoSet = set[0:i]
			tiempoIni=time()
			Heapsort(nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)

			nuevoSet = set[0:i]
			tiempoIni=time()
			Mergesort(nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)

			tiemposDelSet.append(tiemposDeCantidad)
		tiempos.append(tiemposDelSet)
	print len(tiempos)
	return tiempos

main()
