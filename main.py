# Pakker
import numpy as np
import matplotlib.pyplot as plt

# Funksjoner
from lesinput import lesinput
from lengder import lengder
from boyestivhet import boyestivhet
from lastvektor import syslast
from FIM import FIM
from stivmat import stivmat
from randbet import randbet
from moment import moment
from skjærkraft import skjær
from boyespenning import boyespenning
from resultat import resultat_tabeller

def main():

    #Leser inputdata
    npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata = lesinput()
    #Beregner elementlengder
    elemlen = lengder(punkt, elemkonn)

    #Beregner bøyestivhet for alle elementer
    EI, I, zc = boyestivhet(tvsnitt, geom, nelem)
  
    #Beregner elementlastvektor S_fim m/fastinnspenningsmomenter for elementer med ytre last    
    S_fim = FIM(elemlen, lastdata)

    #Bygger systemlastvektor
    R = syslast(S_fim, elemkonn, lastdata, npunkt)

    #Bygger systemstivhetsmatrisen ved å innaddere elementstivhetsmatriser vha. elementkonnektivitet

    K = stivmat(nelem, npunkt, elemkonn, elemlen, EI)
    
    #Innfører grensebetingelser
    K_med_rand = randbet(punkt, npunkt, K)

    #Løser ligningssystemet
    r = np.linalg.solve(K_med_rand, R)
    
    #Beregner momentverdier for alle element ved endene, 
    #og ved midtpunkt for fordelt last og under punktlaster  
    M_verdier= moment(nelem,EI, elemlen, r,S_fim,lastdata )
    
    #Beregner skjærkraftverdier for alle element ved endene
    Q_verdier  = skjær(nelem, lastdata, M_verdier, elemlen)

    #Beregner bøyespenning for alle element ved endene, 
    #og ved midtpunkt for fordelt last og under punktlaster
    sigma_M = boyespenning(M_verdier, I, zc, nelem)
    

    #Resultater
    Moment = np.round(M_verdier/1e6,2) #Konverting til kNm  og avrunding for utskrift
    Skjær = np.round(Q_verdier/1e3,2)  #Konverting til kN og avrunding for utskrift
    sigma_M = np.round(sigma_M,2)      #Avrunding for utskrift
    
    resultat_tabeller(Moment, Skjær, sigma_M)


main()