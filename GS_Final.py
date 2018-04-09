from Cargar_preferencias import obtener_preferencias
from Creacion_de_archivos import crear_archivos

cantJugadores = 200 #cant de elementos
cantEquipos = 20
vacantesPorEquipo =10

def Gale_Shapley(jugadores,equipos):
	vacantes = dict()
	s = []
	for p in range(cantEquipos):
		vacantes[p] = vacantesPorEquipo
	for p in range(cantEquipos):
		
		while len(jugadores) > 0:
			#print "vuelta"
			e = jugadores.pop()
			empleado = False
			for p in equipos:
				#print p
				if(vacantes[p[0]] > 0):
					vacantes[p[0]] -= 1
					s += [(e,p)]
					break;
				for i in range(len(s)):
					contrato = s[i]
					if(contrato[1] == p):
						eprima = contrato[0]
						preferencias = contrato[1][1]
						id_e = e[0]
						id_eprima = eprima[0]
						if(preferencias.index(id_e) < preferencias.index(id_eprima)):
							s.remove(contrato)
							s+=[(e,p)]
							jugadores += [eprima]
							empleado = True
							break
				if empleado: break
	print s
	for contrato in s:
		print str(contrato[0][0]) + " " + str(contrato[1][0])
	return vacantes


def main():
	crear_archivos()
	jug,eqi= obtener_preferencias()
	jug.sort()
	eqi.sort()
	print Gale_Shapley(jug,eqi)
	
main()

