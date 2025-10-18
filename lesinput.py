import numpy as np

def lesinput():

    # Åpner inputfilen
    fid = open("input.txt", "r")

    #Knutepunktsdata
    comlin = fid.readline()            
    npunkt = int(fid.readline())       

    comlin = fid.readline() 
    punkt = np.loadtxt(fid, dtype = int, max_rows = npunkt)      
    
    #Elementdata
    comlin = fid.readline() 
    nelem = int(fid.readline()) #Antall element
    comlin = fid.readline() 
   

    elem = np.loadtxt(fid, dtype = int, max_rows = nelem) #Elemntinfo 
    comlin = fid.readline() 
    
    elemkonn = elem[0:nelem,0:2]
    
    tvsnitt = elem[0:nelem,2:4]
    comlin = fid.readline() 
  

    #Geometridata
    geom = np.loadtxt(fid, dtype = float, max_rows = nelem) #Array med geometri
    comlin = fid.readline() 

    #Lastdata
    nlast = int(fid.readline())
    comlin = fid.readline() 

    lastdata = np.loadtxt(fid, dtype = float, max_rows = nlast)    

    # Lukker input-filen
    fid.close()
    
    return npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata

lesinput()