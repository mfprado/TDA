def Mergesort(lista, iters):
	largo=len(lista)
	iters+=largo+2
	if largo<2:
		return lista, iters
	medio=largo/2
	iters+=2
	izq, iters1=Mergesort(lista[:medio], 0)
	der, iters2= Mergesort(lista[medio:], 0)
	iters+=iters1+iters2
	return merge(izq,der, iters)

def merge(l1,l2, iters):
	resultado=[]
	largo1=len(l1)
	largo2=len(l2)
	iters+=1+largo1+largo2+2
	while largo1>0 and largo2>0:
		if l1[0] < l2[0]: #cuenta como 3
			resultado.append(l1.pop(0))
		else:
			resultado.append(l2.pop(0))
		largo1=len(l1)
		largo2=len(l2)
		iters+=4+largo1+largo2+2
	resultado+=l1
	resultado+=l2
	iters+=2+4
	return resultado, iters
