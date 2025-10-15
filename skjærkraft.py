import numpy as np 

'''
Beregner skjærkraftverdier for alle element ved endene
'''


def skjær(nelem, lastdata, M_verdier, elemlen):
    Q_verdier = np.zeros((nelem, 2))
    for i in range(nelem):
        L = elemlen[i]

        #Fra endemomenter  
        Q_verdier[i,0] = (M_verdier[i,0] - M_verdier[i,1]) / L 
        Q_verdier[i,1] = Q_verdier[i,0]  

        #Punktlast 
        if lastdata[i,3] == 1: 
            P = lastdata[i,1]  
            a = lastdata[i,4]
            if a != 0 and a != L: #Punktlast ikke i bjelkeende
                b = L - a
                Q_verdier[i,0] += P*b / L
                Q_verdier[i,1] += P*a / L
        elif lastdata[i,3] == 2: #Fordelt last
            q1, q2 = lastdata[i,1], lastdata[i,2]

            #Bidrag fra jevnt fordelt last
            Q_verdier[i,0] += min(q1,q2)*L/2
            Q_verdier[i,1] -= min(q1,q2)*L/2

            #Bidrag fra lineært fordelt last 
            if min(q1,q2) == q2: #maks i ende 1
                q = q1 -q2 
                Q_verdier[i,0] += q*L/3 
                Q_verdier[i,1] -= q*L/6

            else: #maks i ende 2
                q = q2 - q1
                Q_verdier[i,0] += q*L/6
                Q_verdier[i,1] -= q*L/3
    
    return Q_verdier



