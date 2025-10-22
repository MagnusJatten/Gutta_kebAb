import matplotlib.pyplot as plt
import numpy as np

def resultat_tabeller(M_verdier, Q_verdier, sigma_m):
  
    # Kolonne- og radtitler
    M_og_sigma_kolonner = ["Ende 1", "Midtpunkt/Under punktlast", "Ende 2"]
    Q_kolonner = ["Ende 1", "Ende 2"]
    rows = ["Element " + str(i) for i in range(M_verdier.shape[0])]

    # Subplots for tabellene
    fig, axes = plt.subplots(3, 1, figsize=(8, 18))
    tabeller = [
        (M_verdier, M_og_sigma_kolonner, "Momentverdier [kNm])"), 
        (Q_verdier, Q_kolonner , "Skjærkraftverdier [kN]"), 
        (sigma_m, M_og_sigma_kolonner, "Bøyespenning [MPa]")]
    

    # Slå av akser og legg inn tabeller
    for ax, (data, kolonner, tittel) in zip(axes, tabeller):
        ax.axis("off")  # Skjul akser
        tabell = ax.table(cellText=data, rowLabels=rows, colLabels = kolonner, loc="center")
        tabell.auto_set_font_size(False)
        tabell.set_fontsize(9)      
        tabell.scale(1.3, 1.6)       
        ax.set_title(tittel, fontsize=12, fontweight='bold', pad = -40)

    plt.tight_layout()
    plt.show()

