import numpy as np

def lesinput():
    """
    Leser inputfilen 'input.txt' og returnerer:
    npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata
    Robust mot kommentarer (#) og tomme linjer.
    """
    
    def next_data_line(fid):
        """Hopp over tomme linjer og kommentarer, returner neste datalinje."""
        while True:
            line = fid.readline()
            if line == "":  # EOF
                return None
            line = line.strip()
            if line == "" or line.startswith("#"):
                continue
            return line

    with open("input.txt", "r") as fid:
        # Antall knutepunkt
        npunkt = int(next_data_line(fid))
        punkt = []
        for _ in range(npunkt):
            punkt.append([float(x) for x in next_data_line(fid).split()])
        punkt = np.array(punkt)

        # Antall elementer
        nelem = int(next_data_line(fid))
        elem = []
        for _ in range(nelem):
            elem.append([int(x) for x in next_data_line(fid).split()])
        elem = np.array(elem)
        elemkonn = elem[:, 0:2]  # Første to kolonner
        tvsnitt = elem[:, 2:4]   # Neste to kolonner

        # Geometri
        geom = []
        for _ in range(nelem):
            geom.append([float(x) for x in next_data_line(fid).split()])
        geom = np.array(geom)

        # Laster
        nlast = int(next_data_line(fid))
        lastdata = []
        for _ in range(nlast):
            lastdata.append([float(x) for x in next_data_line(fid).split()])
        lastdata = np.array(lastdata)

    return npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata


# ==============================
# Test kjøring
# ==============================
if __name__ == "__main__":
    npunkt, punkt, nelem, elemkonn, tvsnitt, geom, lastdata = lesinput()
    
    print("Antall knutepunkt:", npunkt)
    print("Knutepunkter:\n", punkt)
    print("Antall elementer:", nelem)
    print("Elementkoblinger:\n", elemkonn)
    print("Tverrsnitt:\n", tvsnitt)
    print("Geometri:\n", geom)
    print("Lastdata:\n", lastdata)
