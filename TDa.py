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
	promedios = []
	prom_aux = []
	i = 0
	j = 0
	k = 0
	cont = 0
	suma = 0
	while cont < len(lista)*len(lista[0])*len(lista[0][0]):
		if k == len(lista[i][j]) :
			j += 1
			k = 0
			promedios.append(prom_aux)
			prom_aux = []
		suma += lista[i][j][k]
		i +=1
		if i == len(lista):
			prom_aux.append(suma)
			i = 0
			k +=1
			suma = 0
		cont+=1
	promedios.append(prom_aux)
		
	return promedios 

def setOrdenado():
	lista=list(range(10000))
	return lista

def setNrosIguales():
	lista=[]
	for x in range(0,10000):
		lista.append(1)
	return lista

def ordenarSets(sets):
	cantidad = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]
	tiempos = []
	for seti in sets:
		tiemposDelSet = []
		for i in cantidad:
			#print i
			tiemposDeCantidad = []
			nuevoSet = seti[0:i]
			
			'''tiempoIni=time()
			Quicksort(nuevoSet,0, i)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			
			nuevoSet = seti[0:i]'''
			tiempoIni=time()
			Seleccion(nuevoSet, i)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			
			nuevoSet = seti[0:i]
			tiempoIni=time()
			Insercion (nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)

			nuevoSet = seti[0:i]
			tiempoIni=time()
			Heapsort(nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)

			nuevoSet = seti[0:i]
			tiempoIni=time()
			Mergesort(nuevoSet)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)

			tiemposDelSet.append(tiemposDeCantidad)
		tiempos.append(tiemposDelSet)
	return tiempos

def main():
	sets = diezSets()
	tiempoDiezSets = ordenarSets(sets)
	print "termino los 10 sets"
	#tiempoDiezSets = [[[Q,S,I,H,M],[Q,S,I,H,M],[],[],[],[],[],[],[],[]],  [],  [],  [],  [],  [],  [],  [],  [],  []]
	#tiempoDiezSets = [[[50 de largo],[largo 100],[largo 500],[largo 1000],[largo 2000],[largo 3000],...,[largo 10000]],  [],...,   []]
	ordenado =setOrdenado()
	sets = [ordenado, ordenado[::-1], setNrosIguales()]
	tiempoPeoresCasos = ordenarSets(sets)

#Para graficar en Jupyter seria algo asi:
'''import matplotlib.pyplot as plot
longitudes = [50, 100, 500, 1000, 2000, 3000, 4000, 5000, 7500, 10000]
algoritmos = ["QuickSort", "Seleccion", "Insercion", "HeapSort", "MergeSort"] #titulos que habria que ponerle a cada subplot
for set_lista in tiemposSets:
	tiempos_juntados_por_algoritmo = zip(set_lista[0],set_lista[1],set_lista[2],set_lista[3],set_lista[4],set_lista[5],set_lista[6],set_lista[7],set_lista[8],set_lista[9])
	plot.figure()
	i=1
	color = ['r', 'g', 'b', 'k', 'y']
	for algoritmo in tiempos_juntados_por_algoritmo:
		plot.subplot(2,2,i)
		plot.plot(longitudes, algoritmo,color[i-1])
		i++
	plot.show()'''

main()
#setDesordenado()
