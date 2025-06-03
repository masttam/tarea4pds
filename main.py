from src.tarea1 import crear_senales
from src.utils.grapher import graficar_senal
import matplotlib.pyplot as plt

def main():
    señales = crear_senales()

    nombres = [
        "Señal Sinusoidal: x₁(t) = sin(2πft)",
        "Señal Exponencial: x₂(t) = e^(-2t) · u(t)",
        "Señal Triangular: x₃(t) = tri(t, f)",
        "Señal Cuadrada: x₄(t) = sq(t, f)"
    ]

    for i, señal in enumerate(señales):
        t, x_cont, tn, x_disc = señal
        graficar_senal(t, x_cont, tn, x_disc, nombres[i])

    plt.show()

if __name__ == "__main__":
    main()
