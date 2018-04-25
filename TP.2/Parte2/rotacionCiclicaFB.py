def esRotacionCiclicaFB(s1, s2) :
    rotacionPrevia = s2
    largo = len(s2) - 1
    for i in range(0,len(s2)) :
        if s1 == (rotacionPrevia[largo] + rotacionPrevia[0 : largo]) :
            return True
        rotacionPrevia = (rotacionPrevia[largo] + rotacionPrevia[0 : largo])
    return False


print (esRotacionCiclicaFB("DABRAABRACA","ABRACADABRA"))
