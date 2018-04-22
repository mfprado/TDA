def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux  	
	
def downheap(lista,ini,fin, iters):
	iters+=1
	if ini >= fin:
		return iters
	p_hijo_d = (ini*2) + 2
	p_hijo_i = (ini*2) + 1
	p_hijo_mayor = ini
	padre = lista[ini]
	hijo_d = None
	hijo_i = None
	
	comparacion = 0;
	iters+=21

	if(p_hijo_i < fin and cmp(lista[ini],lista[p_hijo_i])<0):
		p_hijo_mayor = p_hijo_i
		iters+=1
	
	if(p_hijo_d < fin and cmp(lista[p_hijo_mayor],lista[p_hijo_d])<0):
		p_hijo_mayor = p_hijo_d
		iters+=1
	if p_hijo_mayor != ini:
		swap(lista,ini,p_hijo_mayor)
		iters = 5 + downheap(lista,p_hijo_mayor,fin,iters)
	return iters

def heapify(lista,largo, iters):
	iters+=1
	for i in range(largo/2,-1,-1):
		iters = 1 + downheap(lista,i,largo, iters)
	return iters
	
def Heapsort(lista, iters):
	iters+=2
	if lista == None or lista ==[]:
		return iters
	largo = len(lista)
	iters+=largo+1
	iters = heapify(lista,largo, iters)
	iters+=1

	for i in range(largo-1,0,-1):
		
		swap(lista,i,0)
		iters = 6 + downheap(lista,0,i, iters)
	return iters
