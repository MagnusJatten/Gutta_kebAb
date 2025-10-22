import numpy as np

def lesinput():
    """
    Leser inputfil og returnerer grunnleggende data i ulike numpy-arrays.
    """
    
    def next_data_line(fid):
        '''
        Sørger for at tommme linjer og kommentarer hoppes
        over, og  returner neste datalinje.
        '''
        while True:
            line = fid.readline()
            if line == "":
                return None
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            return line

    with open("input.txt", "r") as fid:
        #Antall knutepunkt
        npunkt = int(next_data_line(fid))
        punkt = []
        
        #Knutepunktsdata
        for i in range(npunkt):
            punkt.append([float(x) for x in next_data_line(fid).split()])
        punkt = np.array(punkt)

        # Antall elementer
        nelem = int(next_data_line(fid))
        elem = []
        
        #Elementsdata
        for i in range(nelem):
            elem.append([int(x) for x in next_data_line(fid).split()])
        elem = np.array(elem)
        elemkonn = elem[:, 0:2]  #Konnektivitetstabell
        tvsnitt = elem[:, 2:4]   #E-modul og profiltype

        #Geometri
        geom = []
        for i in range(nelem):
            geom.append([float(x) for x in next_data_line(fid).split()])
        geom = np.array(geom)

        #Antall ytre laster
        nlast = int(next_data_line(fid))
        lastdata = []

        #Lastdata
        for i in range(nlast):
            lastdata.append([float(x) for x in next_data_line(fid).split()])
        lastdata = np.array(lastdata)

    return npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata


