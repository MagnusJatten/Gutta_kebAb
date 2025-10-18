import numpy as np
'''
Beregner momentverdier for alle element ved endene
'''


def moment(nelem,EI, elemlen, rot, fim, lastdata):
    M_verdier = np.zeros((nelem,3))
    for i in range(nelem):
        k = np.array([[4, 2], [2, 4]]) # Lokal stivhetsmatrise for hvert element
        L = elemlen[i]
        k = k*((EI[i])/(elemlen[i])) #Skalerer med EI/L
        #Ende 1 
        kr = k[0,0] * rot[i] + k[0,1]*rot[i]
        M1 = kr + fim[i,0]
        M_verdier[i,0] = M1
        #Ende 2 
        kr =  k[1,0] * rot[i] + k[1,1]*rot[i]
        M2 = kr + fim[i,1]
        M_verdier[i,2] = M2
        #Midtpunkt 
        M_tot = (M1-M2)/2
        element = i
        while element in lastdata[:, 0]: #Inkluderer elementer med flere ytre laster
            type_last = lastdata[i,3]
            if type_last == 1: #Punktlast, rett under last
                P  = lastdata[i,1]
                a = lastdata[i,4]
                b = L - a
                Mp = (P*a*b)/L #Superpos
                M_under_last = M1 - (M2+M1)/L * a + Mp
                M_verdier[i,1] = M_under_last
                
            elif type_last == 2: #Fordelt last
                M_mid = 0
                q1, q2 = lastdata[i,1], lastdata[i,2]

                #Bidrag fra jevnt fordelt last
                M_mid += (q1*L**2)/8

                #Bidrag fra lineært fordelt last
                q = abs(q1 - q2)
                x = L/2
                M_mid += (q*x)/(6*L) *(2*L**2 -3*L*x + x**2)
                M_mid += M_tot
                M_verdier[i,1] = M_mid 
            element += 1
    return M_verdier