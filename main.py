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

    K = stivmat(nelem, elemkonn, elemlen, EI)
    
    #Innfører grensebetingelser
    K_med_rand = randbet(punkt, npunkt, K)
    K_med_rand =np.array([[46, 20,  2,  1,  0],
                  [20, 60, 10,  0,  0],
                  [ 2, 10, 48,  2, 10],
                  [ 1,  0,  2, 46, 20],
                  [ 0,  0, 10, 20, 60]])
    #Løser ligningssystemet
    r = np.linalg.solve(K_med_rand, R)
    
    #Beregner momentverdier for alle element ved endene, 
    #og ved midtpunkt for fordelt last og under punktlaster  
    M_verdier= moment(nelem,EI, elemlen, r,S_fim,lastdata, elemkonn)
    
    #Beregner skjærkraftverdier for alle element ved endene
    Q_verdier  = skjær(nelem, lastdata, M_verdier, elemlen)

    #Beregner bøyespenning for alle element ved endene, 
    #og ved midtpunkt for fordelt last og under punktlaster
    sigma_M = boyespenning(M_verdier, I, zc, nelem)
    

    #Resultater
    Moment = np.round(M_verdier,10)#Konverting til kNm  og avrunding for utskrift
    Skjær = np.round(Q_verdier,10)#Konverting til kN og avrunding for utskrift
    sigma_M = np.round(sigma_M,10)      #Avrunding for utskrift
    
    resultat_tabeller(Moment, Skjær, sigma_M)


main()