# Proyecto de Se�ales en Python

Este proyecto contiene scripts para generar, graficar y comparar diferentes tipos de se�ales (continuas y discretas) usando Python y Matplotlib.

---

## Contenido

- `tarea_1.py`: Genera y grafica cuatro tipos de se�ales en forma continua y discreta.
  - Se�al senoidal
  - Se�al exponencial con escal�n
  - Se�al triangular
  - Se�al cuadrada

- `tarea_2.py`: Genera y grafica una se�al senoidal continua para una frecuencia dada.

- `tarea_3.py`: Compara se�ales continuas y discretas modificadas con se�ales de referencia, permitiendo variar amplitud, frecuencia y fase.

- `src/utils/grapher.py`: Funciones para graficar se�ales continuas, discretas y para comparar se�ales.

- `main.py`: Script principal para ejecutar cualquiera de las tareas desde l�nea de comandos.

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
