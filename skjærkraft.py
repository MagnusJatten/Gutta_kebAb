import numpy as np 

'''
Beregner skjærkraftverdier for alle element ved endene
vha. superposisjonsprinsippet
'''

def skjær(npunkt, lastdata, moment, elemlen):
    Q_verdier = np.zeros((npunkt, 2))
    for i in range(npunkt):
        L = elemlen[i] 
        # Bidrag fra endemomenter  
        Q_verdier[i,0] = (moment[i,0] + moment[i,1]) / L  # Ende 1
        Q_verdier[i,1] = Q_verdier[i,0]                   # Ende 2

        # Bidrag fra ytre laster
        mask = np.where(lastdata[:,0] == i)[0]  # Finn alle rader som gjelder element i
        for idx in mask:
            # Punktlast 
            if lastdata[idx,3] == 1: 
                P = lastdata[idx,1]  
                a = lastdata[idx,4]
                if a != 0 and a != L:  # Punktlast ikke i bjelkeende
                    Q_verdier[i,1] += P*a / L
                    Q_verdier[i,0] += P - Q_verdier[i,1]

            # Fordelt last       
            elif lastdata[idx,3] == 2: 
                q1, q2 = lastdata[idx,1], lastdata[idx,2]

                # Bidrag fra jevnt fordelt last
                Q_verdier[i,0] += min(q1,q2)*L/2
                Q_verdier[i,1] -= min(q1,q2)*L/2

                # Bidrag fra lineært fordelt last 
                if max(q1,q2) == q1:  # maks i ende 1
                    q = q1 - q2 
                    Q_verdier[i,0] += q*L/3 
                    Q_verdier[i,1] -= q*L/6
                else:  # maks i ende 2
                    q = q2 - q1
                    Q_verdier[i,0] += q*L/6
                    Q_verdier[i,1] -= q*L/3
        
    return Q_verdier
