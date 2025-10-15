import numpy as np

'''
 Beregner systemlastvektor ved å addere knutepunktskrefter
og -momenter og trekke fra fastinnspenningsmomenter
'''

def syslast(R,S_fim,elemkonn, lastdata, elemlen):
    for i in range(len(elemlen)):
        #Knutepunktskrefter og momenter
        R[elemkonn[i,0]] += lastdata[i,1]
        R[elemkonn[i,1]] += lastdata[i,2]

        #Fastinnspenningsmomenter
        R[elemkonn[i,0]] -= S_fim[i,0]
        R[elemkonn[i,1]] -= S_fim[i,1]
    return R