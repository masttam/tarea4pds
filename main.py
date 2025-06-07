import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from tarea_1 import crear_senales
from tarea_2 import generar_senoidal_continua
from src.utils.grapher import graficar_senal

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py [tarea_1 | tarea_2] [frecuencia (si aplica)]")
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
    else:
        print("Tarea no reconocida. Usa 'tarea_1' o 'tarea_2'.")
