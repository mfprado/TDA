def swap(lista,a,b):
	aux = lista[a]
	lista [a] = lista [b]
	lista [b] = aux  	
	
def downheap(lista,ini,fin):
	if ini >= fin:
		return
	p_hijo_d = (ini*2) + 2
	p_hijo_i = (ini*2) + 1
	p_hijo_mayor = ini
	padre = lista[ini]
	hijo_d = None
	hijo_i = None
	
	comparacion = 0;
	if(p_hijo_i < fin and cmp(lista[ini],lista[p_hijo_i])<0):
		p_hijo_mayor = p_hijo_i
	
	if(p_hijo_d < fin and cmp(lista[p_hijo_mayor],lista[p_hijo_d])<0):
		p_hijo_mayor = p_hijo_d
	if p_hijo_mayor != ini:
		swap(lista,ini,p_hijo_mayor)
		downheap(lista,p_hijo_mayor,fin)

def heapify(lista,largo):
	for i in range(largo/2,-1,-1):
		downheap(lista,i,largo)
	
def Heapsort(lista):
	if lista == None or lista ==[]:
		return
	largo = len(lista)  
	heapify(lista,largo)

	for i in range(largo-1,0,-1):
		swap(lista,i,0)
		downheap(lista,0,i)