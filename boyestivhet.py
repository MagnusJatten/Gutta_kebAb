import numpy as np 
'''
Beregner bøyestivhet EI for alle elementer basert på tverrsnittsdata og geometridata
'''
def boyestivhet(tvsnitt, geom, nelem):
    EI = np.zeros(len(tvsnitt))
    I = np.zeros(len(tvsnitt))
    zc = np.zeros(len(tvsnitt)) 
    for i in range(nelem): #hvert element 
        E = tvsnitt[i,0]
        if tvsnitt[i,1] == 2: #I-profil
            h = geom[i,1] #totalt høyde
            b = geom[i,2] #flensbredde
            ts = geom[i,3] #tykkelse på steg
            tf = geom[i,4] #tykkelse på flens
            I_i = (b*h**3 - (b - ts)*(h - 2*tf)**3)/12
            EI[i] = E*I_i
            I[i] = I_i
            zc[i] = h/2 #nøytralakse, husk å forklare i rapport
        else: #rørprofil
            D = geom[i,1] #ytre diameter
            d = geom[i,2] #indre diameter
            I_i = (np.pi/64)*(D**4 - d**4)
            EI[i] = E*I_i
            I[i] = I_i
            zc[i] = D/2 #nøytralakse
    return EI, I, zc  