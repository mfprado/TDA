from os import listdir
import csv

#en la ruta tambien puede ir ".", si los archivos estan en la misma ubicacion que el .py

def obtener_nro(cadena):
	cadena_aux = ""
	for letra in cadena:
		if letra.isdigit():
			cadena_aux = cadena_aux + letra
	return cadena_aux

def cargar_preferencias(ruta):
	lista_prefe = []
	for arch in listdir(ruta):
		cadena = ruta +"/" + str(arch)
		if arch == ".DS_Store":
			continue
		try:
			with open(cadena) as preferencias:
				preferencias_csv = csv.reader(preferencias)
				prefe = int(obtener_nro(arch))
				lista = []
				for pre in preferencias_csv:
					if pre[0].isdigit():
						pref = pre[0]
						lista.append(int(pref))
				lista_prefe.append((prefe,lista))
				
		except IOError:
			raise IOError("No se encuntra el archivo")
	return lista_prefe


def obtener_preferencias():
	pref_jugadores = cargar_preferencias("./Jugadores")
	pref_equipos = cargar_preferencias("./Equipos")
	return pref_jugadores, pref_equipos

