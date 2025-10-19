import numpy as np

'''
 Beregner systemlastvektor ved å addere knutepunktskrefter
og -momenter og trekke fra fastinnspenningsmomenter
'''

def syslast(S_fim,elemkonn, lastdata, npunkt):
    R = np.zeros((npunkt,1))

    #Fastinnspenningsmomenter
    for i in range(len(elemkonn)):
        punkt1 = elemkonn[i,0]
        punkt2 = elemkonn[i,1]
        R[punkt1] -= S_fim[i,0]
        R[punkt2] -= S_fim[i,1]
        

    #Knutepunktskrefter og momenter
    #for i in range(len(lastdata)):
        #element = int(lastdata[i,0])
        #R[elemkonn[element,0]] += lastdata[i,1]
        #R[elemkonn[element,1]] += lastdata[i,2]


    return R

