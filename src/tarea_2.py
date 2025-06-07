import numpy as np
from src.utils.grapher import continuous_plotter

def generar_senoidal_continua(frecuencia):
    """
    Genera una señal senoidal continua para una frecuencia dada.
    Grafica la señal usando continuous_plotter().
    """
    t = np.linspace(0, 2, 1000)  # 2 segundos de duración
    x = np.sin(2 * np.pi * frecuencia * t)
    titulo = f"Señal senoidal continua con f = {frecuencia} Hz"
    continuous_plotter(t, x, titulo)
