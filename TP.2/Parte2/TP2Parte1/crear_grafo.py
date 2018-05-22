from grafo import Grafo

MSJ_ERROR = "Error:"
MSJ_IOERROR = "No se pudo acceder al archivo:"
MSJ_INDEXERROR = "Error de datos en el archivo:"

def cargar_en_grafo(archivoMapa, lineaEspia1, lineaEspia2, lineaAeropuerto, distancia):
	'''Carga el mapa en un grafo, y devuelve los puntos donde se encuentran el espia 1, 2 y el aeropuerto.
	Si se produjo un error con el archivoMapa se informa '''
	pos_espia_1 = -1
	pos_espia_2 = -1
	pos_aeropuerto = -1
	grafo = Grafo()
	try:
		archivo = open(archivoMapa)
		nroLinea = 0
		for linea in archivo:#'p1.x p1.y - p2.x p2.y'
			puntos = linea.split(' - ')#['p1.x p1.y','p2.x p2.y']
			coordenadas = [puntos[0].split(), puntos[1].split()] #[['p1.x','p1.y'],['p2.x','p2.y']
			punto1 = (int(coordenadas[0][0]),int(coordenadas[0][1]))
			punto2 = (int(coordenadas[1][0]),int(coordenadas[1][1]))
			peso = distancia(punto1, punto2)
			grafo.agregar_arista(punto1,punto2, peso)
			if (nroLinea == lineaEspia1):
				pos_espia_1 = punto1
			if (nroLinea == lineaEspia2):
				pos_espia_2 = punto1
			if (nroLinea == lineaAeropuerto):
				pos_aeropuerto = punto1
			nroLinea += 1
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
	return grafo, pos_espia_1, pos_espia_2, pos_aeropuerto