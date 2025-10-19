import numpy as np
'''
Beregner momentverdier for alle element ved endene
'''


def moment(nelem,EI, elemlen, rot, fim, lastdata,elemkonn):
    M_verdier = np.zeros((nelem,3))

    for i in range(nelem):
        k = np.array([[4, 2], [2, 4]]) # Lokal stivhetsmatrise for hvert element
        L = elemlen[i]
        k = k*((EI[i])/(elemlen[i])) #Skalerer med EI/L
        #Ende 1 
        kr = k[0,0] * rot[elemkonn[i,0]] + k[0,1]*rot[elemkonn[i,1]]  # Ende 1
        M1 = kr + fim[i,0]
        M_verdier[i,0] = M1

        #Ende 2
        kr = k[1,0] * rot[elemkonn[i,0]] + k[1,1]*rot[elemkonn[i,1]]  # Ende 2
        M2 = kr + fim[i,1]
        M_verdier[i,2] = M2
        
        #Midtpunkt 
        M_tot = (M1-M2)/2
        M_verdier[i,1] = M_tot

        element = i
        mask = np.where(lastdata[:,0] == element)[0]  # Finn rader som gjelder dette elementet

        for idx in mask:
            type_last = lastdata[idx,3]
            if type_last == 1:  # Punktlast
                P = lastdata[idx,1]
                a = lastdata[idx,4]
                b = L - a
                Mp = (P*a*b)/L
                M_under_last = M1 - (M2+M1)/L * a + Mp
                M_verdier[i,1] += M_under_last
            elif type_last == 2:  # Fordelt last
                M_mid = 0
                q1, q2 = lastdata[idx,1], lastdata[idx,2]
                M_mid += (q1*L**2)/8
                q = abs(q1 - q2)
                x = L/2
                M_mid += (q*x)/(6*L) *(2*L**2 -3*L*x + x**2)
                M_mid += M_tot
                M_verdier[i,1] += M_mid
    return M_verdier