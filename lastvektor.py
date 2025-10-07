import numpy as np 

'''
Beregner fastinnspenningsmomenter for alle elementer basert på elementlengder og lastdata
'''

def FIM(elemlen, lastdata):
    S_fim = np.zeros((len(elemlen), 2))
    for i in range(len(elemlen)):
        L = elemlen[i]
        for ilast in lastdata:
           if ilast[0] == i: #Sjekker om lasten virker på element i
                if ilast[1] == 0: #Moment
                    M = ilast[4]
                    S_fim[i,0] += M
                    S_fim[i,1] += -M
                elif ilast[1] == 1: #Punktlast
                    P = ilast[4]  
                    a = ilast[2]
                    b = ilast[3]
                    S_fim[i,0] += ((P*a*b**2)/(L**2)) #m1
                    S_fim[i,1] += ((P*a**2*b)/(L**2)) #m2
                elif ilast[1] == 2: #Jevnt Fordelt last
                    q = ilast[4] 
                    S_fim[i,0] += (-1/12 * q * L**2) #m1
                    S_fim[i,1] += (1/12* q*L**2) #m2
                elif ilast[1] == 3: #Lineært fordelt last
                    q = ilast[4]
                    S_fim[i,0] += (-1/30 * q * L**2) #m1
                    S_fim[i,1] += (1/20 * q * L**2) #m2
    return S_fim
