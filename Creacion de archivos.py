import random
import csv

def creacion(cant,cant2,cadena):
	lista = lista=list(range(1,cant2))
	for i in range(1,cant+1):
		random.shuffle(lista,random.random)
		nom_archivo = cadena + str(i) + ".prf.csv"
		archivo = open(nom_archivo,"w")
		primer_linea = cadena+str(i)
		archivo_csv = csv.writer(archivo)
		archivo_csv.writerow([primer_linea])
		for j in lista:
			archivo_csv.writerow([str(j)])
	archivo.close()

def main():
	creacion(20,200,"Equipo_")
	creacion(200,20,"Jugador_")

