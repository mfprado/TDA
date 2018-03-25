def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux  

def Insercion (lista):
	i=1
	while i < len(lista):
		j = i
		while j > 0 and lista[j-1] > lista[j]:
			swap(lista,j,j-1)
			j = j - 1
		i += 1 
	#print lista