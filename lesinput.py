import numpy as np

def lesinput():

    # Åpner inputfilen
    fid = open("input.txt", "r")

    # Leser totalt antall punkt
    comlin = fid.readline()            #  Leser kommentarlinje. 
    npunkt = int(fid.readline())       # Antall knutepunkt
    #print(f'npunkt = {npunkt}')
    # x- og y-koordinater til knutepunktene og grensebetingelse
    # Knutepunktnummer tilsvarer radnummer
    # x-koordinat lagres i kolonne 1, y-koordinat i kolonne 2
    # Grensebetingelse lagres i kolonne 3; 1 = fast innspent og 0 = fri rotasjon
    comlin = fid.readline() 
    punkt = np.loadtxt(fid, dtype = int, max_rows = npunkt)      # Array med knutepunkt
    #print(f'punkt = {punkt}')
    

    # Leser antall elementer
    comlin = fid.readline() 
    nelem = int(fid.readline()) #Antall element
    #print(f'nelem = {nelem}')
    comlin = fid.readline() 
    # Kolonne 1 og 2: Elementkonnektivitet, dvs. sammenheng mellom elementfrihetsgrader og systemfrihetsgrader
    # Kolonne 3: E-modul
    # Kolonne 4: Tverrsnittstype
    # Elementnummer tilsvarer radnummer
    # Systemfrihetsgrad for lokal frihetsgrad 1 lagres i kolonne 1
    # Systemfrihetsgrad for lokal frihetsgrad 2 lagres i kolonne 2
    # Det anbefales at nummerering av systemfrihetsgrad starter på 0, slik at det samsvarerer med indeksering i Python
    elem = np.loadtxt(fid, dtype = int, max_rows = nelem) #Elemntinfo 
    comlin = fid.readline() 
    # Elementkonnektivitetstabell
    # Kolonne 1: Systemfrihetsgrad for elementfrihetsgrad 1
    # Kolonne 2: Systemfrihetsgrad for elementfrihetsgrad 2
    elemkonn = elem[0:nelem,0:2]
    #print(f'elemkonn = {elemkonn}')
    # Tverrsnittsdata
    # Kolonne 1: E-modul
    # Kolonne 2: Tverrsnittstype, I-profil=1 og rørprofil=2
    tvsnitt = elem[0:nelem,2:4]
    #print(f'tvsnitt = {tvsnitt}')
    
    comlin = fid.readline() 
  

    # Leser geometridata for tverrsnittstypene
    geom = np.loadtxt(fid, dtype = float, max_rows = nelem) #Array med geometri
    #print(geom)
    #print(f'geom = {geom}')
    # Leser antall laster som virker på rammen
    comlin = fid.readline() 
    nlast = int(fid.readline())
    #print(f'nlast = {nlast}')
    comlin = fid.readline() 
    
    # Leser lastdata
    lastdata = np.loadtxt(fid, dtype = float, max_rows = nlast)    

    #print(f'lastdata = {lastdata}')
    # Lukker input-filen
    fid.close()
    

    return npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata

lesinput()