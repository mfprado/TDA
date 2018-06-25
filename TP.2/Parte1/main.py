from crear_grafo import cargar_en_grafo
from grafo import Grafo
ARCHIVO_MAPA = "mapa.coords"

def main (argv, distancia, ejercicio):
	try:
		if len(argv) !=4: #main.py , pos espia 1, pos espia 2, pos aeropuerto
			print "Error: no se pasaron la cantidad de parametros esperados"
			return
		grafo,pos_espia_1,pos_espia_2,pos_aeropuerto = cargar_en_grafo(ARCHIVO_MAPA, int(argv[1]),int(argv[2]),int(argv[3]),distancia)
		if (pos_espia_1<0 or pos_espia_2<0 or pos_aeropuerto<0):
			print "Error: una de las posiciones pasadas no existe"
			raise ValueError
		ejercicio(grafo,pos_espia_1,pos_espia_2,pos_aeropuerto)
	except:
		print "Dado un error en el programa, el mismo no se ejecutara"