- **Tarea 3**: Comparaci�n entre se�ales continuas y discretas con par�metros variables.
- **Tarea 4**: An�lisis del efecto del n�mero de bits en un DAC � c�lculo de niveles, tama�o de paso, resoluci�n porcentual y visualizaci�n de la salida anal�gica para entradas digitales crecientes.

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
�   +-- tarea_1.py
�   +-- tarea_2.py 
�   +-- tarea_3.py 
�   +-- tarea_4.py
�   +-- utils/
�       +-- grapher.py


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
	