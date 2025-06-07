# Proyecto de Señales en Python

Este proyecto contiene scripts para generar, graficar y comparar diferentes tipos de señales (continuas y discretas) usando Python y Matplotlib.

---

## Contenido

- `tarea_1.py`: Genera y grafica cuatro tipos de señales en forma continua y discreta.
  - Señal senoidal
  - Señal exponencial con escalón
  - Señal triangular
  - Señal cuadrada

- `tarea_2.py`: Genera y grafica una señal senoidal continua para una frecuencia dada.

- `tarea_3.py`: Compara señales continuas y discretas modificadas con señales de referencia, permitiendo variar amplitud, frecuencia y fase.

- `src/utils/grapher.py`: Funciones para graficar señales continuas, discretas y para comparar señales.

- `main.py`: Script principal para ejecutar cualquiera de las tareas desde línea de comandos.

---

## Requisitos

- Python 3.7 o superior
- NumPy
- SciPy
- Matplotlib

Puedes instalar las dependencias con:

```bash
pip install numpy scipy matplotlib

Uso:
python main.py tarea_1

python main.py tarea_2 [frecuencia]
	Ejemplo:
	python main.py tarea_2 5
python main.py tarea_3 [Amplitud] [Frecuencia] [Fase en radianes]
	Ejemplo:
	python main.py tarea_3 1 2 0.785
