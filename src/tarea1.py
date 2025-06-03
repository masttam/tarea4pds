import numpy as np
from scipy.signal import square, sawtooth
from src.utils.grapher import graficar_senal

def crear_senales(frecuencia=2, intervalo_muestreo=0.01):
    tiempo_continuo = np.linspace(-1, 5, 1000)
    tiempo_discreto = np.arange(-1, 5, intervalo_muestreo)

    # Onda senoidal
    senal1_cont = np.sin(2 * np.pi * frecuencia * tiempo_continuo)
    senal1_disc = np.sin(2 * np.pi * frecuencia * tiempo_discreto)

    # Onda exponencial con función escalón
    escalon_cont = np.where(tiempo_continuo >= 0, 1, 0)
    escalon_disc = np.where(tiempo_discreto >= 0, 1, 0)
    senal2_cont = np.exp(-2 * tiempo_continuo) * escalon_cont
    senal2_disc = np.exp(-2 * tiempo_discreto) * escalon_disc

    # Onda triangular (versión simétrica)
    senal3_cont = sawtooth(2 * np.pi * frecuencia * tiempo_continuo, width=0.5)
    senal3_disc = sawtooth(2 * np.pi * frecuencia * tiempo_discreto, width=0.5)

    # Onda cuadrada
    senal4_cont = square(2 * np.pi * frecuencia * tiempo_continuo)
    senal4_disc = square(2 * np.pi * frecuencia * tiempo_discreto)

    return (
        (tiempo_continuo, senal1_cont, tiempo_discreto, senal1_disc),
        (tiempo_continuo, senal2_cont, tiempo_discreto, senal2_disc),
        (tiempo_continuo, senal3_cont, tiempo_discreto, senal3_disc),
        (tiempo_continuo, senal4_cont, tiempo_discreto, senal4_disc)
    )
