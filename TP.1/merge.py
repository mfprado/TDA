def Mergesort(lista):
	if len(lista)<2:
		return lista
	medio=len(lista)/2
	izq=Mergesort(lista[:medio])
	der= Mergesort(lista[medio:])
	return merge(izq,der)

def merge(l1,l2):
	resultado=[]
	while len(l1)>0 and len(l2)>0:
		if l1[0] < l2[0]:
			resultado.append(l1.pop(0))
		else:
			resultado.append(l2.pop(0))
	resultado+=l1
	resultado+=l2
	return resultado
