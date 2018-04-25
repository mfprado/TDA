def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux

def Seleccion(lista, n, iters):
	for i in range (n):
		minimo = i
		for j in range (i+1,n):
			iters+=4
			if lista[j] < lista[minimo]:
				minimo = j
				iters+=1
		swap (lista,minimo,i)
		iters+=8 #minimo=i + swap
	return iters
