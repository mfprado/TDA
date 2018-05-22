#Algoritmo por fuerza bruta
def isCyclicRotation(s1, s2):
    # Como dice el enunciado ambas cadenas de texto son de igual tamano, n.
    n = (len(s2))
    for i in range(n) :
        j = (n - i)
        if (s1 == (s2[j : n] + s2[0 : j])) :
            return True
    return False


print (esRotacionCiclicaFB("DABRAABRACA","ABRACADABRA"))
