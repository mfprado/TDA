from crear_grafo import cargar_en_grafo
from Grafo import Grafo
ARCHIVO_MAPA = "redsecreta.map"

def main ():
	try:
		grafo = cargar_en_grafo(ARCHIVO_MAPA)
		grafo_sabotaje = cargar_en_grafo(ARCHIVO_MAPA)
		flujo_maximo, arista_1, arista_2 = grafo.Ford('0','1') #0 es la fuente, 1 es el sumidero		
		flujo_maximo_sabotaje = grafo_sabotaje.flujo_maximo_despues_de_sabotaje(arista_1, arista_2)
		print "Los ejes a vigilar son: ",arista_1, " y ", arista_2
		print "El flujo maximo de la red es: ", flujo_maximo
		print "Si el grafo fuese saboteado, el flujo maximo seria: ", flujo_maximo_sabotaje
	except:
		print "Dado un error en el programa, el mismo no se ejecutara"
main()