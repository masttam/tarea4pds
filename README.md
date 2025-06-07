- **Tarea 3**: Comparación entre señales continuas y discretas con parámetros variables.
- **Tarea 4**: Análisis del efecto del número de bits en un DAC — cálculo de niveles, tamaño de paso, resolución porcentual y visualización de la salida analógica para entradas digitales crecientes.

---

## Requisitos

- Python 3.x
- Paquete `matplotlib`
- Paquete `numpy`

Instala los requisitos con:

```bash
pip install -r requirements.txt

estructura:

+-- main.py
+-- .gitignore
+-- requirements.txt
+-- README.md
+-- src/
¦   +-- tarea_1.py
¦   +-- tarea_2.py 
¦   +-- tarea_3.py 
¦   +-- tarea_4.py
¦   +-- utils/
¦       +-- grapher.py


uso:

python main.py tarea_1

python main.py tarea_2 [frecuencia]
	Ejemplo:
	python main.py tarea_2 5
python main.py tarea_3 [Amplitud] [Frecuencia] [Fase en radianes]
	Ejemplo:
	python main.py tarea_3 1 2 0.785
Tarea 4 (DAC)
	Ejemplo:
	