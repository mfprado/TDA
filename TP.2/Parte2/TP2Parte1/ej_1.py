def ejercicio_1(grafo,sky_1,sky_2,airport):
	"sin peso, sin camino"
	largo_1,largo_2 = grafo.obtener_camino(sky_1,sky_2,airport)
	print largo_1,largo_2
	quien_gana(0,0,largo_1,largo_2)

def ejercicio_2(grafo,sky_1,sky_2,airport):
	peso_1 = grafo.camino_minimo(sky_1,airport)
	peso_2 = grafo.camino_minimo(sky_2,airport)
	quien_gana(0,0,peso_1, peso_2)

def ejercicio_4_a(grafo,sky_1,sky_2,airport):
	camino_1,camino_2 = grafo.obtener_camino(sky_1,sky_2,airport,True)
	if camino_1==None or camino_2==None:
		quien_gana(camino_1, camino_2, 0, 0)
	else:
		quien_gana(camino_1, camino_2, len(camino_1), len(camino_2))
	
def ejercicio_4_b(grafo,sky_1,sky_2,airport):
	camino_1,peso_1 = grafo.camino_minimo(sky_1,airport,True)
	camino_2,peso_2 = grafo.camino_minimo(sky_2,airport,True)
	quien_gana(camino_1, camino_2, peso_1, peso_2)

def quien_gana(camino_1, camino_2, peso_1, peso_2):
	if camino_2 == None or peso_2 == -1 :
		print "El espia 1 logro escapar"
	elif camino_1 == None or peso_1 == -1 :
		print "El espia 1 no puede llegar al aeropuerto"
	elif peso_2 <= peso_1:
		print "El espia 2 intercepto al otro espia"
	elif peso_2 > peso_1:
		print "El espia 1 logro escapar"
	if camino_1 != 0 and camino_2!= 0:
		print "Camino del espia 1: ", camino_1
		print "Camino del espia 2: ", camino_2
