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

print (KMPTable("ABRACADABRA"))
print (KMPTable("DABRAABRACA"))

def KMP(pattern, text):
    tf = KMPTable(pattern)
    k = 0
    i = 0
    while k + i < len(text):
        print (k, i)
        if text[k + i] == pattern[i]:
            i = i + 1
            if k == len(pattern):
                return k
        else:
            if i == 0:
                k = k + 1
            else:
                k = k + i - tf[i]
                i = tf[i]
    return None


print(KMP('ABRACADABRA','ABRACADAPA ABRACADABRA'))
