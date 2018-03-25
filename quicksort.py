def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux  
	
def Quicksort (lista,ini,fin):
	if ini < fin:
		p = particion(lista, ini, fin)
		Quicksort(lista, ini, p -1)
		Quicksort(lista, p + 1,  fin)
	
def particion(lista,ini,fin):
	pivot = lista[fin - 1]
	i = ini -1
	for j in range (ini, fin -1):
		if lista[j] < pivot:
			i = i +1
			swap(lista,i,j)
	swap(lista,i+1,fin-1)
	return i+1