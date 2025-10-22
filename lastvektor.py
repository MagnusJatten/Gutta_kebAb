import numpy as np

'''
 Bygger systemlastvektor ved å addere knutepunktsmomenter og trekke fra fastinnspenningsmomenter
'''

def syslast(S_fim,elemkonn, lastdata, npunkt):
    R = np.zeros(npunkt) #Initialiserer systemlastvektor

    #Fastinnspenningsmomenter
    for i in range(len(elemkonn)):
        R[elemkonn[i,0]] += S_fim[i,0]
        R[elemkonn[i,1]] += S_fim[i,1]

    R *= -1 #Inverterer matrisen

    #Konsentrerte knutepunktsmomenter
    for ilast in lastdata:
        if ilast[3] == 0: 
            element = ilast[0]
            R[elemkonn[int(element),0]] += ilast[1]
            R[elemkonn[int(element),1]] += ilast[2]
    
    return R

