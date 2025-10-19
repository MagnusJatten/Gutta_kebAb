import numpy as np

'''
Bygger stivhetsmatrisen for hele systemet ved å innaddere elementstivhetsmatriser
via elementkonnektivitet
'''

def stivmat(nelem, npunkt, elemkonn, elemlen, EI):
    K = np.zeros((npunkt, npunkt)) # Stivhetsmatrise med dimensjon (npunkt x npunkt)
    k = np.array([[4, 2], [2, 4]]) # Lokal stivhetsmatrise for hvert element
    

    for i in range(nelem):
        L = elemlen[i] # Elementlengde   
        EI_L = (EI[i])/L
    
        k_ij = EI_L * k # For hver element, skaler lokal stivhetsmatrise med EI/L
        K[elemkonn[i, 0], elemkonn[i, 0]] += k_ij[0, 0]
        K[elemkonn[i, 0], elemkonn[i, 1]] += k_ij[0, 1]
        K[elemkonn[i, 1], elemkonn[i, 0]] += k_ij[1, 0]
        K[elemkonn[i, 1], elemkonn[i, 1]] += k_ij[1, 1]
    return K