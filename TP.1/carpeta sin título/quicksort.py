def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux
	
def Quicksort (lista,ini,fin, iters):
	iters+=1
	if ini < fin:
		p,iters = particion(lista, ini, fin, iters)
		iters+=3
		Quicksort(lista, ini, p -1, iters)
		Quicksort(lista, p + 1,  fin, iters)
	return iters
	
def particion(lista,ini,fin, iters):
	pivot = lista[fin - 1]
	i = ini -1
	iters+=6
	for j in range (ini, fin -1):
		iters+=3
		if lista[j] < pivot:
			i = i +1
			swap(lista,i,j)
			iters+=7
	swap(lista,i+1,fin-1)
	return i+1, iters+7
	
