# Pakker
import numpy as np

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


def main():

    #Leser inputdata
    npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata = lesinput()

    #Beregner elementlengder
    elemlen = lengder(punkt, elemkonn)

    #Beregner bøyestivhet for alle elementer
    EI, I, zc = boyestivhet(tvsnitt, geom, nelem)

    #Bygger systemlastvektor
   
  
        # -----Beregner elementlastvektor S_fim m/fastinnspenningsmomenter for elementer med ytre last
        # Lag funksjonen selv
    S_fim = FIM(elemlen, lastdata)

    R = syslast(S_fim, elemkonn, lastdata, npunkt)
        # -----Adderer elementlastvektor S_fim inn i systemlastvektor R vha. elementkonnektivitet
        # Lag funksjonen selv
        # R = elemlast_til_syslast(R, S_fim, elemkonn )


    # ------Bygger systemstivhetsmatrisen ved å innaddere elementstivhetsmatriser vha. elementkonnektivitet
    # Lag funksjonen selv
    K = stivmat(nelem, npunkt, elemkonn, elemlen, EI)

    # ------Innfører grensebetingelser
    # Lag funksjonen selv basert på valgt metode for innføring av grensebetingelser
    K_med_rand = randbet(punkt, npunkt, K)

    # -----Løser ligningssystemet------
    #r = np.zeros_like(R), må kanskje initialisere r her?
    r = np.linalg.solve(K_med_rand, R)
    
    #------Beregner momentverdier for alle element ved endene, 
    #------og ved midtpunkt for fordelt last og under punktlaster
    #------vha. superposisjonsprinsippet
    # Lag funksjonen selv
    M_verdier= moment(nelem,EI, elemlen, r,S_fim,lastdata )


    #------Beregner skjærkraftverdier for alle element ved endene
    #------vha. enkel derivasjon (Q=dM/ds) for Q-bidrag fra moment pga.
    #------bjelkeenderotasjoner, og bruker superposisjonsprinsippet
    #------for å addere til Q-bidrag fra ytre last
    # Lag funksjonen selv
    Q_verdier  = skjær(nelem, lastdata, M_verdier, elemlen)

    #------Beregner bøyespenning for alle element ved endene, 
    #------og ved midtpunkt for fordelt last og under punktlaster
    # Lag funksjonen selv
    sigma_M = boyespenning(M_verdier, I, zc, nelem)

    #-----Printer bøyespenninger for alle elementene
    print("Bøyespenninger:")
    print(sigma_M)

    #-----Printer momentverdier for alle elementer
    print("Momentverdier for tegning av M-diagram (for hånd):")
    print(M_verdier)

    #-----Printer skjærkraftverdier ved endene for alle elementer
    print("Skjærkraftverdier for tegning av Q-diagram (for hånd):")
    print(Q_verdier)

main()