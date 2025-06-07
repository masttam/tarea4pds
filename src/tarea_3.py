import numpy as np
import matplotlib.pyplot as plt

def generar_senal_continua(A, f, phi, t):
    return A * np.sin(2 * np.pi * f * t + phi)

def generar_senal_discreta(A, f, phi, Ts, n):
    return A * np.sin(2 * np.pi * f * n * Ts + phi)

def tarea_3(amplitud, frecuencia, fase, Ts=0.01, duracion=2):
    # Tiempo continuo (muestra densa)
    t = np.linspace(0, duracion, 1000)
    senal_cont = generar_senal_continua(amplitud, frecuencia, fase, t)
    senal_ref_cont = generar_senal_continua(1, 1, 0, t)  # Señal referencia

    # Tiempo discreto
    n = np.arange(0, int(duracion / Ts))
    senal_disc = generar_senal_discreta(amplitud, frecuencia, fase, Ts, n)
    senal_ref_disc = generar_senal_discreta(1, 1, 0, Ts, n)  # Señal referencia

    return t, senal_cont, senal_ref_cont, n, senal_disc, senal_ref_disc
