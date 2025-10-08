import numpy as np 

'''
FIM: Beregner fastinnspenningsmomenter for alle elementer 
basert på elementlengder og lastdata
syslast: Beregner systemlastvektor ved å addere knutepunktskrefter
og -momenter og trekke fra fastinnspenningsmomenter
'''

def FIM(elemlen, lastdata):
    S_fim = np.zeros((len(elemlen), 2))
    for i in range(len(elemlen)):
        L = elemlen[i]
        for ilast in lastdata:
           if ilast[0] == i: #Sjekker om lasten virker på element i
                if ilast[3] == 0: #Moment
                    M1 = ilast[1]
                    M2 = ilast[2]
                    S_fim[i,0] += M1
                    S_fim[i,1] += -M2
                elif ilast[3] == 1: #Punktlast
                    P = ilast[1]  
                    a = ilast[4]
                    b = L - a
                    S_fim[i,0] += ((P*a*b**2)/(L**2)) #m1
                    S_fim[i,1] += ((P*a**2*b)/(L**2)) #m2
                elif ilast[3] == 2: #Fordelt last
                    q1 = ilast[1] #startintensitet
                    q2 = ilast[2] #sluttintensitet
                    if q1 == q2: #jevnt fordelt last
                        S_fim[i,0] += (-1/12 * q1 * L**2) #m1
                        S_fim[i,1] += (1/12* q1*L**2) #m2
                    if q2 > q1: #Lineært fordelt last (maks i ende 2)
                        q = q2 - q1
                        S_fim[i,0] += (-1/20 * (ilast[1]*L + q*L/3) * L) #m1
                        S_fim[i,1] += (1/30 * (ilast[1]*L + 2*q*L/3) * L) #m2
                    
                    if q1 > q2: #Lineært fordelt last (maks i ende 1)
                        q = q1 - q2
                        S_fim[i,0] += (-1/30 * q * L**2) #m1
                        S_fim[i,1] += (1/20 * q * L**2) #m2
    return S_fim

def syslast(R,S_fim,elemkonn, lastdata, elemlen):
    for i in range(len(elemlen)):
        #Knutepunktskrefter og momenter
        R[elemkonn[i,0]] += lastdata[i,1]
        R[elemkonn[i,1]] += lastdata[i,2]

        #Legger til fastinnspenningsmomenter
        R[elemkonn[i,0]] -= S_fim[i,0]
        R[elemkonn[i,1]] -= S_fim[i,1]
    return R