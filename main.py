import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from tarea_1 import crear_senales
from tarea_2 import generar_senoidal_continua
from src.utils.grapher import graficar_senal, plot_compare_signals, plot_compare_signals_discrete
import numpy as np

def generar_senales_tarea_3(A, f, phi):
    """
    Genera señal modificada y señal referencia para tarea 3.
    """
    t = np.linspace(0, 2, 1000)  # Tiempo continuo
    n = np.arange(0, 2, 0.01)    # Índices discretos, Ts=0.01
    Ts = 0.01

    # Señal referencia (A=1, f=1Hz, phi=0)
    senal_ref_cont = np.sin(2 * np.pi * 1 * t)
    senal_ref_disc = np.sin(2 * np.pi * 1 * n)

    # Señal modificada
    senal_cont = A * np.sin(2 * np.pi * f * t + phi)
    senal_disc = A * np.sin(2 * np.pi * f * n + phi)

    return t, senal_cont, senal_ref_cont, n, senal_disc, senal_ref_disc, Ts

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py [tarea_1 | tarea_2 | tarea_3] [parámetros]")
        sys.exit(1)

    tarea = sys.argv[1]

    if tarea == "tarea_1":
        senales = crear_senales()
        nombres = ["Senoidal", "Exponencial con escalón", "Triangular", "Cuadrada"]
        for (tiempo_c, senal_c, tiempo_d, senal_d), nombre in zip(senales, nombres):
            graficar_senal(tiempo_c, senal_c, tiempo_d, senal_d, nombre)

    elif tarea == "tarea_2":
        if len(sys.argv) < 3:
            print("Uso correcto: python main.py tarea_2 [frecuencia]")
            sys.exit(1)
        try:
            frecuencia = float(sys.argv[2])
        except ValueError:
            print("La frecuencia debe ser un número (float o entero).")
            sys.exit(1)

        tiempo, senal = generar_senoidal_continua(frecuencia)
        graficar_senal(tiempo, senal, tiempo, senal, f"Senoidal continua - {frecuencia} Hz")

    elif tarea == "tarea_3":
        if len(sys.argv) < 5:
            print("Uso correcto: python main.py tarea_3 [A] [f] [phi]")
            sys.exit(1)
        try:
            A = float(sys.argv[2])
            f = float(sys.argv[3])
            phi = float(sys.argv[4])
        except ValueError:
            print("A, f y phi deben ser números (float o enteros).")
            sys.exit(1)

        t, senal_cont, senal_ref_cont, n, senal_disc, senal_ref_disc, Ts = generar_senales_tarea_3(A, f, phi)

        # Graficar señales continuas comparativas
        plot_compare_signals(t, senal_cont, senal_ref_cont, A, f, phi)

        # Graficar señales discretas comparativas
        plot_compare_signals_discrete(n, senal_disc, senal_ref_disc, Ts, A, f, phi)

    else:
        print("Tarea no reconocida. Usa 'tarea_1', 'tarea_2' o 'tarea_3'.")
