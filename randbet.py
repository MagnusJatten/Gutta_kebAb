import numpy as np
'''
Innfører randbetingelser i stivhetsmatrisen ved å sette rotasjonfjærer 
med høy stivhet i punkter som egentlig er fast innspent
'''

def randbet(punkt, npunkt, K):
    for i in range(npunkt):
        if punkt[i][2] == 1: #Fast innspent ####FEIL FEIL FEIL
            K[i][i] += 1e69 # Setter stor stivhet for fast innspent knutepunkt
    return K

