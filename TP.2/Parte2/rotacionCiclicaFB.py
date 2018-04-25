def esRotacionCiclicaFB(s1, s2) :
    rotacionPrevia = s2
    ultimoIndice = len(s2) - 1
    for i in range(0,len(s2)) :
        if s1 == rotacionPrevia :
            return True
        rotacionPrevia = (rotacionPrevia[ultimoIndice] + rotacionPrevia[0 : ultimoIndice])
    return False


print (esRotacionCiclicaFB("DABRAABRACA","ABRACADABRA"))
