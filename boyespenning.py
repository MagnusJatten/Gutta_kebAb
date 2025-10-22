import numpy as np 
'''
Beregner bøyespenning for alle element ved endene og midtpunkt ved fordelt last
'''
def boyespenning(M_verdier, I, zc,nelem):
    sigma_m = np.zeros((nelem, 3))
    for i in range(nelem):
        sigma_m[i,0] = M_verdier[i,0]*zc[i]/I[i]
        sigma_m[i,1] = M_verdier[i,1]*zc[i]/I[i]
        sigma_m[i,2] = M_verdier[i,2]*zc[i]/I[i]
    return sigma_m