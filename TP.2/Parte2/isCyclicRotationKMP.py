def KMPTable(pattern):
    result = [None]
    for i in range(0, len(pattern)):
        j = i
        while True:
            if j == 0:
                result.append(0)
                break
            if pattern[result[j]] == pattern[i]:
                result.append(result[j] + 1)
                break
            j = result[j]
    return [-1] + result[1:len(result)-1]


def KMP(pattern, text):
    table = KMPTable(pattern)
    k = 0
    i = 0
    while k + i < len(text):
        if text[k + i] == pattern[i]:
            i = i + 1
            if i == len(pattern):
                return k
        else:
            if i == 0:
                k = k + 1
            else:
                k = k + i - table[i]
                i = table[i]

#Algoritmo identico al de Fuerza Bruta pero en la igualdad define con KMP
def isCyclicRotation(s1, s2):

    n = (len(s2))
    for i in range(n) :
        j = (n - i)
        if (KMP(s1, (s2[j : n] + s2[0 : j])) == 0 ) :
            return True
    return False

print (isCyclicRotation("DABRAABRACA","ABRACADABRA"))

#Algoritmo con unica iteracion KMP
def isCyclicRotationKMP(s1,s2):
    s = s1 + s1
    return (KMP(s2,s) >= 0)

print (isCyclicRotationKMP("DABRAABRACA","ABRACADABRA"))
