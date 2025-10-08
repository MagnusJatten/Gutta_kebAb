import numpy as np

def systemstivhetsmatrise(nelem, elem, elementlengder, EI, npunkt):
    # Initialiserer systemstivhetsmatrise
    K = np.zeros((npunkt, npunkt)) # Systemstivhetsmatrise med dimensjon (npunkt x npunkt)
    k = np.array([[4, 2], [2, 4]]) # Lokal stivhetsmatrise for hvert element
    L = elementlengder # Elementlengder

    for i in range(nelem):
        EI_L = ((EI[i]) / L[i]) # E-modul delt på elementlengde
        k_ij = EI_L * k # For hver element, skaler lokal stivhetsmatrise med EI/L
        
        K[int(elem[i, 0]), int(elem[i, 0])] += k_ij[0, 0] 
        K[int(elem[i, 0]), int(elem[i, 1])] += k_ij[0, 1]  
        K[int(elem[i, 1]), int(elem[i, 0])] += k_ij[1, 0]
        K[int(elem[i, 1]), int(elem[i, 1])] += k_ij[1, 1] 

    return K