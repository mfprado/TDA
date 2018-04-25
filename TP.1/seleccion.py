def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux  

def Seleccion(lista, n):
	for i in range (n):
		minimo = i
		for j in range (i+1,n):
			if lista[j] < lista[minimo]:
				minimo = j
		swap (lista,minimo,i)
	#print lista