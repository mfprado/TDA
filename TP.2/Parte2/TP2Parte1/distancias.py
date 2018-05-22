from math import sqrt
def distancia_euclidea(punto1, punto2):
	return sqrt((punto1[1]-punto1[0])**2 + (punto2[1]-punto2[0])**2)

def sin_distancia(punto1,punto2):
	return 1