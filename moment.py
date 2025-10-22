import numpy as np
'''
Beregner momentverdier for alle element ved endene
'''


def moment(nelem, EI, elemlen, rot, fim, lastdata, elemkonn):
    M_verdier = np.zeros((nelem,3))
    for i in range(nelem):
        k = np.array([[4, 2], [2, 4]]) # Lokal stivhetsmatrise for hvert element
        L = elemlen[i]
        k = k* ((EI[i])/(L)) #Skalerer med EI/L
        th1 = rot[elemkonn[i,0]]
        th2 = rot[elemkonn[i,1]]

        #Ende 1 
        kr = k @ np.array([th1, th2])
        M1, M2 = kr + fim[i,:]
        M_verdier[i,0] =- M1

        #Ende 2 
        M_verdier[i,2] = M2

        #Midtpunkt ved fordelt last/under last ved punktlast
        M_tot = (M1-M2)/2
        M_verdier[i,1] += M_tot
    
    
        for ilast in lastdata: 
            element = int(ilast[0])
            if element == i:
                type_last = ilast[3]

                if type_last == 1:  # Punktlast
                    P = ilast[1]
                    a = ilast[4]
                    if a != 0 and  a != L:
                        M_verdier[i,1] = 0 # Nullstiller tidligere beregnet moment ved midtpunkt
                        b = L - a
                        Mp = (P*a*b)/L
                        M_under_last = M1 + ((M1-M2)/L * a) + Mp
                        M_verdier[i,1] += M_under_last
                
                elif type_last == 2:  # Fordelt last
                    M_mid = 0
                    q1, q2 = ilast[1], ilast[2]
                    q = min(q1,q2)
                    M_mid += (q*L**2)/8
                    q = abs(q1 - q2)
                    x = L/2
                    M_mid += (q*x)/(6*L) *(2*L**2 -3*L*x + x**2)
                    M_verdier[i,1] += M_mid
    

    return M_verdier