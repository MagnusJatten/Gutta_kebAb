import numpy as np 
'''
Beregner bøyestivhet EI for alle elementer basert på tverrsnittsdata og geometridata
'''
def boyestivhet(tvsnitt, geom):
    EI = np.zeros(len(tvsnitt))
    for i in geom[0]: #hvert element (0 = elemnr)
        E = tvsnitt[i,0]
        if tvsnitt[i,1] == 1: #I-profil
            h = geom[1] #totalt høyde
            b = geom[2] #flensbredde
            ts = geom[3] #tykkelse på steg
            tf = geom[4] #tykkelse på flens
            I = (b*h**3 - (b - ts)*(h - 2*tf)**3)/12
            EI[i] = E*I
        elif tvsnitt[i,1] == 2: #rørprofil
            D = geom[1] #ytre diameter
            d = geom[2] #indre diameter
            I = (np.pi/64)*(D**4 - d**4)
            EI[i] = E*I
    return EI 