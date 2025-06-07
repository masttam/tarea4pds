import numpy as np
from scipy.signal import square, sawtooth

def crear_senales(frecuencia=2, intervalo_muestreo=0.01):
    """
    Genera 4 señales: senoidal, exponencial escalonada, triangular y cuadrada.
    Devuelve una tupla con pares de señales (continuas y discretas).
    """
    tiempo_continuo = np.linspace(-1, 5, 1000)
    tiempo_discreto = np.arange(-1, 5, intervalo_muestreo)

    # Señal senoidal
    senal1_cont = np.sin(2 * np.pi * frecuencia * tiempo_continuo)
    senal1_disc = np.sin(2 * np.pi * frecuencia * tiempo_discreto)

    # Señal exponencial con escalón
    escalon_cont = np.where(tiempo_continuo >= 0, 1, 0)
    escalon_disc = np.where(tiempo_discreto >= 0, 1, 0)
    senal2_cont = np.exp(-2 * tiempo_continuo) * escalon_cont
    senal2_disc = np.exp(-2 * tiempo_discreto) * escalon_disc

    # Señal triangular
    senal3_cont = sawtooth(2 * np.pi * frecuencia * tiempo_continuo, width=0.5)
    senal3_disc = sawtooth(2 * np.pi * frecuencia * tiempo_discreto, width=0.5)

    # Señal cuadrada
    senal4_cont = square(2 * np.pi * frecuencia * tiempo_continuo)
    senal4_disc = square(2 * np.pi * frecuencia * tiempo_discreto)

    return (
        (tiempo_continuo, senal1_cont, tiempo_discreto, senal1_disc),
        (tiempo_continuo, senal2_cont, tiempo_discreto, senal2_disc),
        (tiempo_continuo, senal3_cont, tiempo_discreto, senal3_disc),
        (tiempo_continuo, senal4_cont, tiempo_discreto, senal4_disc)
    )
