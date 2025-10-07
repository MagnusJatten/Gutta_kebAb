import numpy as np 
'''
Beregner bøyestivhet EI for alle elementer basert på tverrsnittsdata og geometridata
'''
def boyestivhet(tvsnitt, geom):
    EI = np.zeros(len(tvsnitt))
    for i in range(len(tvsnitt)):
        E = tvsnitt[i,0]
        if tvsnitt[i,1] == 1: #I-profil
            h = geom[0] #totalt høyde
            b = geom[1] #flensbredde
            ts = geom[2] #tykkelse på steg
            tf = geom[3] #tykkelse på flens
            I = (b*h**3 - (b - ts)*(h - 2*tf)**3)/12
            EI[i] = E*I
        elif tvsnitt[i,1] == 2: #rørprofil
            D = geom[0] #ytre diameter
            d = geom[1] #indre diameter
            I = (np.pi/64)*(D**4 - d**4)
            EI[i] = E*I
    return EI 