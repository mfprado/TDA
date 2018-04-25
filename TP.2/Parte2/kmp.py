
def kmp(s1, s2):
    largoS2 = (len(s2))
    for i in range(largoS2) :
        pos = (largoS2 - i)
        if (s1 == (s2[pos : largoS2] + s2[0 : pos])) :
            return True
    return False

print (kmp("DABRAABRACA","ABRACADABRA"))
