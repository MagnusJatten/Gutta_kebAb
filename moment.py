import numpy as np
'''
Beregner momentverdier for alle element ved endene
'''


def moment(nelem,EI, elemlen, rot, fim,lastdata ):
    M_verdier = np.zeros((nelem,3))
    k = np.array([[4, 2], [2, 4]]) # Lokal stivhetsmatrise for hvert element
    for i in range(nelem):
        L = elemlen[i]
        k = k*(EI[i]/elemlen[i]) #Skalerer med EI/L
        r = k*rot[i] #Rotasjon pga. bjelkeendemomenter
        #Ende 1 
        M1 = r + fim[i,0] 
        M_verdier[i,0] = M1
        #Ende 2 
        M2 = r + fim[i,1]
        M_verdier[i,2] = M2
        #Midtpunkt
        type_last = lastdata[i,4]
        if type_last == 1: #Punktlast
            P  = lastdata[i,1]
            a = lastdata[i,5]
            b = L - a
            M_mid = P*a*b/L
            M_verdier[i,1] = M_mid
        elif type_last == 2: #Fordelt last
            M_mid = 0
            q1, q2 = lastdata[i,1], lastdata[i,2]

            #Bidrag fra jevnt fordelt last
            M_mid += (q1*L**2)/8

            #Bidrag fra lineært fordelt last
            q = abs(q1 - q2)
            x = L/2
            M_mid += (q*x)/(6*L) *(2*L**2 -3*L*x + x**2) 
            M_verdier[i,1] = M_mid

    return M_verdier