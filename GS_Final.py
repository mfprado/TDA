from Cargar_preferencias import obtener_preferencias
from Creacion_de_archivos import crear_archivos

cantJugadores = 200 #cant de elementos
cantEquipos = 20
vacantesPorEquipo =10

def Gale_Shapley(jugadores,equipos):
	jugadores = [[j[0],j[1],-1] for j in jugadores]
	vacantes = dict()
	s = []
	for p in range(cantEquipos):
		vacantes[p] = vacantesPorEquipo
	vacantesTotales=cantEquipos*vacantesPorEquipo;
	while vacantesTotales>0:
		for equipo in equipos:
			if vacantes[equipo[0]]==0:
				continue
			for j in equipo[1]:
				jugador = jugadores[j]
				if vacantes[equipo[0]]==0:
					break;
				if(jugador[2]<0):
					 jugador[2]=equipo[0]
					 vacantesTotales-=1;
					 vacantes[equipo[0]]-=1
				else:
					otroEquipo = jugador[2]
					preferencia = jugador[1]
					if(preferencia.index(otroEquipo)>preferencia.index(equipo[0])):
						jugador[2]=equipo[0]
   					 	vacantes[equipo[0]]-=1
						vacantes[otroEquipo]+=1
	s=[(j[0],j[2]) for j in jugadores]
	for contrato in s:
		print str(contrato[0]) + " " + str(contrato[1])
	return vacantes


def main():
	crear_archivos()
	jug,eqi= obtener_preferencias()
	jug.sort()
	eqi.sort()
	print Gale_Shapley(jug,eqi)

main()
