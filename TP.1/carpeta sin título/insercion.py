def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux  

def Insercion (lista, iters):
	i=1
	largo = len(lista)
	iters+=3+largo
	while i < largo:
		#print i
		j = i
		while j > 0 and lista[j-1] > lista[j]:
			swap(lista,j,j-1)
			j = j - 1
			iters+=11 #incluye el swap
		i += 1
		iters+=8 #j=i, j>0, lista[j-1]>lista[j], i+=1, i<largo siguiente
		#print iters
	return iters

