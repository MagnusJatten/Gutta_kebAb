# -----------------------------------------------------------
# Structure_visualization.py
# Oversatt og tilpasset fra Josef Kiendl sin Matlab-kode.
# Brukes til å vise u-deformert og deformert ramme.
#
# Krever:
#   numpy
#   matplotlib
#   scipy (for CubicSpline)
# -----------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline


# -----------------------------------------------------------
# Lager to figurer (én for initial, én for deformert)
# -----------------------------------------------------------
def setup_plots():
    fig_init, ax_init = plt.subplots()
    fig_def, ax_def = plt.subplots()
    ax_init.set_title("Initial ramme")
    ax_def.set_title("Deformert ramme")
    ax_init.set_aspect("equal", adjustable="box")
    ax_def.set_aspect("equal", adjustable="box")
    return fig_init, ax_init, fig_def, ax_def


# -----------------------------------------------------------
# Tegner den u-deformerte strukturen
# -----------------------------------------------------------
def plot_structure(ax, punkt, elem, show_numbers=True):
    nodes = np.array(punkt[:, 0:2], dtype=float)
    el_nod = np.array(elem[:, 0:2], dtype=int)

    for i, e in enumerate(el_nod):
        n1, n2 = e
        x = [nodes[n1, 0], nodes[n2, 0]]
        z = [nodes[n1, 1], nodes[n2, 1]]
        ax.plot(x, z, "-k", linewidth=2)

        if show_numbers:
            # Skriv elementnummer midt på staven
            xm = (x[0] + x[1]) / 2
            zm = (z[0] + z[1]) / 2
            ax.text(xm, zm, f"e{i+1}", color="red", fontsize=8)

    if show_numbers:
        # Skriv nodenummer
        for i, (x, z) in enumerate(nodes):
            ax.text(x, z, f"n{i+1}", color="blue", fontsize=8)


# -----------------------------------------------------------
# Tegner den deformerte strukturen
# -----------------------------------------------------------
def plot_structure_def(ax, punkt, elem, r, show_numbers=True):
    nodes = np.array(punkt[:, 0:2], dtype=float)
    el_nod = np.array(elem[:, 0:2], dtype=int)

    for i, e in enumerate(el_nod):
        n1, n2 = e
        x1, z1 = nodes[n1]
        x2, z2 = nodes[n2]

        # Elementlengde og vinkel
        dx = x2 - x1
        dz = z2 - z1
        L = np.sqrt(dx**2 + dz**2)
        psi = np.arctan2(dz, dx)

        # Hent nodale rotasjoner fra r
        phi1 = r[n1]
        phi2 = r[n2]

        # Lokal x og z (u-deformert)
        x_local = np.array([0, L])
        z_local = np.array([0, 0])

        # 100 punkter langs elementet
        xx = np.linspace(0, L, 100)

        # Bruk kubisk spline for å lage jevn kurve
        cs = CubicSpline(x_local, z_local, bc_type=((1, -phi1), (1, -phi2)))
        zz = cs(xx)

        # Roter fra lokalt til globalt koordinatsystem
        rot = np.array([[np.cos(psi), -np.sin(psi)],
                        [np.sin(psi),  np.cos(psi)]])
        xxzz = rot @ np.vstack((xx, zz))
        xx_global = xxzz[0, :] + x1
        zz_global = xxzz[1, :] + z1

        ax.plot(xx_global, zz_global, "-k", linewidth=2)

        if show_numbers:
            xm = (xx_global[0] + xx_global[-1]) / 2
            zm = (zz_global[0] + zz_global[-1]) / 2
            ax.text(xm, zm, f"e{i+1}", color="red", fontsize=8)

    if show_numbers:
        for i, (x, z) in enumerate(nodes):
            ax.text(x, z, f"n{i+1}", color="blue", fontsize=8)


# -----------------------------------------------------------
# Eksempel på bruk:
# (Du kan kommentere ut dette når du importerer i ditt prosjekt)
# -----------------------------------------------------------
if __name__ == "__main__":
    # Eksempeldata (du kan endre til å lese fra din egen tekstfil)
    punkt = np.array([
        [0, 0],
        [4, 0],
        [4, 3],
    ])

    elem = np.array([
        [0, 1],
        [1, 2],
    ])

    # Rotasjoner (små vinkler, radianer)
    r = np.array([0.0, 0.01, -0.015])

    # Skalering for å synliggjøre deformasjon
    scale = 50
    r_scaled = r * scale

    # Tegn
    fig_init, ax_init, fig_def, ax_def = setup_plots()
    plot_structure(ax_init, punkt, elem)
    plot_structure_def(ax_def, punkt, elem, r_scaled)

    plt.show()
