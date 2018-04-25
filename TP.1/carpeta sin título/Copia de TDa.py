#! /usr/bin/python

#Para ejecutar si dice "permiso denegado" poner "chmod 777 TDa.py" y despues volver a ejecutar con "./TDa.py"
from heapsort import Heapsort
from quicksort import Quicksort
from insercion import Insercion
from seleccion import Seleccion
from merge import Mergesort

import random
import csv
import sys
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

def calcular_promedios_csv():
	tiempos = []
	i = 0
	j = 0
	k = 0
	cont = 0
	suma = 0
	archivo = open("tiempos_algoritmos_promedio.csv","w")
	archivo_csv = csv.writer(archivo)
	for lista in listas:
		for tiempo in listas:
			for tiem in tiempo:
				archivo_csv.writerow(tiem)

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
	iteracionesLista = []
	for seti in sets:
		tiemposDelSet = []
		iteracionesDelSet = []
		for i in cantidad:
			print i
			tiemposDeCantidad = []
			iteracionesDeCantidad = []
			
			nuevoSet = seti[0:i]
			iteraciones=0
			tiempoIni=time()
			iteraciones = Quicksort(nuevoSet,0, i, iteraciones)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			iteracionesDeCantidad.append(iteraciones)
			
			nuevoSet = seti[0:i]
			iteraciones=0
			tiempoIni=time()
			iteraciones = Seleccion(nuevoSet, i, iteraciones)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			iteracionesDeCantidad.append(iteraciones)
			
			nuevoSet = seti[0:i]
			iteraciones=0
			tiempoIni=time()
			iteraciones = Insercion (nuevoSet, iteraciones)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			iteracionesDeCantidad.append(iteraciones)

			nuevoSet = seti[0:i]
			iteraciones=0
			tiempoIni=time()
			iteraciones =Heapsort(nuevoSet, iteraciones)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			iteracionesDeCantidad.append(iteraciones)

			nuevoSet = seti[0:i]
			iteraciones=0
			tiempoIni=time()
			iteraciones = Mergesort(nuevoSet, iteraciones)
			tiempoFin=time()
			tiemposDeCantidad.append(tiempoFin-tiempoIni)
			iteracionesDeCantidad.append(iteraciones[1])

			tiemposDelSet.append(tiemposDeCantidad)
			iteracionesDelSet.append(iteracionesDeCantidad)
		tiempos.append(tiemposDelSet)
		iteracionesLista.append(iteracionesDelSet)
	return tiempos, iteracionesLista

def pasar_valores(listas,nombre_archivo):
	tiempos = []
	i = 0
	j = 0
	k = 0
	cont = 0
	suma = 0
	archivo = open(nombre_archivo + ".csv","w")
	archivo_csv = csv.writer(archivo)
	while cont < len(listas)*len(listas[0])*len(listas[0][0]):
		if k == len(listas[i][j]) :
			j += 1
			k = 0

		tiempos.append(listas[i][j][k])
		i +=1
		if i == len(listas):
			archivo_csv.writerow(tiempos)
			i = 0
			k +=1
			tiempos = []
		cont+=1
	tiempos.append(tiempos)
	
def pasar_valores2(listas,nombre_archivo):
	archivo = open(nombre_archivo+".csv","w")
	archivo_csv = csv.writer(archivo)
	for lista in listas:
		for lis in lista:
			archivo_csv.writerow(lis)
				
def pasar_valores3(listas):
	archivo = open("tiempos_algoritmos_promedio.csv","w")
	archivo_csv = csv.writer(archivo)
	for tiempo in listas:
		archivo_csv.writerow(tiempo)


def main():
	"""sets = diezSets()
	tiempoDiezSets,iters = ordenarSets(sets)
	pasar_valores(tiempoDiezSets,"tiempos_algoritmos")
	pasar_valores2(tiempoDiezSets,"tiempos_algoritmos_2")
	#promedios = promedio(tiempoDiezSets)
	#pasar_valores2(promedios,"prom")
	
	pasar_valores(iters,"tiempos_algoritmos_iter")
	pasar_valores2(iters,"tiempos_algoritmos_2_iter")
	#promedios_i = promedio(iters)
	#pasar_valores2(promedios_i,"prom_iter")"""
	
	#print "termino los 10 sets"
	#tiempoDiezSets = [[[Q,S,I,H,M],[Q,S,I,H,M],[],[],[],[],[],[],[],[]],  [],  [],  [],  [],  [],  [],  [],  [],  []]
	#tiempoDiezSets = [[[50 de largo],[largo 100],[largo 500],[largo 1000],[largo 2000],[largo 3000],...,[largo 10000]],  [],...,   []]
	ordenado = setOrdenado()
	sets = [ordenado, ordenado[::-1], setNrosIguales()]
	sys.setrecursionlimit(INF)
	tiempoPeoresCasos,iters = ordenarSets(sets)
	pasar_valores2(tiempoPeoresCasos,"tiempos_algoritmos_peores_casos")
	pasar_valores2(iters,"tiempos_algoritmos_peores_casos_iters")


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
