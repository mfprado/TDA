from grafo import Grafo

MSJ_ERROR = "Error: "
MSJ_IOERROR = "No se pudo acceder al archivo: "
MSJ_INDEXERROR = "Error de datos en el archivo: "

def cargar_en_grafo(archivoMapa):
	'''Carga el mapa en un grafo
	Si se produjo un error con el archivoMapa se informa '''
	grafo = Grafo()
	try:
		archivo = open(archivoMapa)
		for linea in archivo:#vertice1 vertice2 pesoDev1Av2
			datos = linea.split(' ') #datos=['v1','v2','peso']
			grafo.agregar_arista(datos[0],datos[1], datos[2])
	except IOError,e:
		print MSJ_ERROR,e
		print MSJ_IOERROR, archivoMapa
		raise IOError
	except IndexError, e:
		archivo.close()
		print MSJ_ERROR,e
		print MSJ_INDEXERROR, archivoMapa
		raise IndexError
	finally:
		archivo.close()
	return grafo