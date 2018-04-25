cantEstudiantes = 200 #cant de elementos
cantPasantias = 20
vacantesPorPasantia =10
estudiantes = [ (i, list(np.random.permutation(range(cantPasantias*vacantesPorPasantia)))) \
               for i in xrange(cantEstudiantes) ]
pasantias = [ (i, list(np.random.permutation(range(cantEstudiantes)))) \
             for i in xrange(cantPasantias) ]*vacantesPorPasantia
vacantes = dict()
for p in range(cantPasantias):
    vacantes[p]=vacantesPorPasantia
    s = []
    while len(estudiantes) > 0:
        e = estudiantes.pop()
        empleado=False
        for p in pasantias:
            if(vacantes[p[0]]>0):
                vacantes[p[0]]-=1
                s+=[(e,p)]
                break;
            for i in range(len(s)):
                contrato = s[i]
                if(contrato[1]==p):
                    eprima=contrato[0]
                    preferencias = contrato[1][1]
                    id_e = e[0]
                    id_eprima = eprima[0]
                    if(preferencias.index(id_e)<preferencias.index(id_eprima)):
                        s.remove(contrato)
                        s+=[(e,p)]
                        estudiantes+=[eprima]
                        empleado=True
                        break
            if empleado: break
