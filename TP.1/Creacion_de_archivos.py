import random
import csv
import os
import shutil

def creacion(cant,cant2,cadena,cadena_direc):
	try:
		os.mkdir(cadena_direc)
	except:
		shutil.rmtree(cadena_direc)
		os.mkdir(cadena_direc)
	lista = lista=list(range(0,cant2))
	
	for i in range(0,cant):
		random.shuffle(lista,random.random)
		nom_archivo = "./"+ cadena_direc +"/"+ cadena + str(i) + ".prf"
		archivo = open(nom_archivo,"w")
		primer_linea = cadena+str(i)
		archivo_csv = csv.writer(archivo)
		archivo_csv.writerow([primer_linea])
		for j in lista:
			archivo_csv.writerow([str(j)])
	archivo.close()

def crear_archivos():
	creacion(20,200,"Equipo_","Equipos")
	creacion(200,20,"Jugador_","Jugadores")

