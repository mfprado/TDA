#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv

def pasar_valores2(listas):
	archivo = open("tiempos_algoritmos_promedios.csv","w")
	archivo_csv = csv.writer(archivo)
	for lista in listas:
		archivo_csv.writerow(lista)

def main():
	i = 0
	lista_final = []
	try:
		with open("tiempos_algoritmos.csv") as arch:
			arch_csv = csv.reader(arch)
			lista = []
			for pre in arch_csv:
				suma = 0
				for val in pre:
					suma += float(val)
					print suma
				lista.append(suma/10.0)
				i += 1
				if i%5 == 0:
					lista_final.append(lista)
					lista = []
	except IOError:
		raise IOError("No se encuntra el archivo")
	print lista_final
	pasar_valores2(lista_final)
	
	

main()
