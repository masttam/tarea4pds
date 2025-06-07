import matplotlib.pyplot as plt

def graficar_senal(tiempo_continuo, senal_continua, tiempo_discreto=None, senal_discreta=None, titulo=""):
    plt.figure(figsize=(10, 4))

    if tiempo_continuo is not None and senal_continua is not None:
        plt.plot(tiempo_continuo, senal_continua, label='Señal continua', color='blue')

    if tiempo_discreto is not None and senal_discreta is not None:
        plt.stem(tiempo_discreto, senal_discreta, linefmt='r-', markerfmt='ro', basefmt='r-', label='Señal discreta')

    plt.title(titulo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()


def continuous_plotter(t, x, titulo=""):
    plt.figure(figsize=(10, 4))
    plt.plot(t, x, label="Señal senoidal continua", color='blue')
    plt.title(titulo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()


def plot_compare_signals(t, signal, ref_signal, A, f, phi, titulo=""):
    """
    Grafica dos señales continuas para comparar:
    signal: señal modificada (parámetros variables)
    ref_signal: señal de referencia fija
    """
    plt.figure(figsize=(10, 4))
    plt.plot(t, ref_signal, label="Señal Referencia (A=1, f=1Hz, ϕ=0)", color='gray', linestyle='--')
    plt.plot(t, signal, label=f"Señal Modificada (A={A}, f={f}Hz, ϕ={phi:.2f} rad)", color='blue')
    plt.title(titulo if titulo else "Comparación de señales continuas")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()


def plot_compare_signals_discrete(n, signal, ref_signal, Ts, A, f, phi, titulo=""):
    """
    Grafica dos señales discretas para comparar:
    n: índice de muestra
    signal: señal modificada
    ref_signal: señal de referencia
    """
    plt.figure(figsize=(10, 4))
    plt.stem(n*Ts, ref_signal, linefmt='gray', markerfmt='o', basefmt='k-', label="Señal Referencia (A=1, f=1Hz, ϕ=0)")
    plt.stem(n*Ts, signal, linefmt='b-', markerfmt='bo', basefmt='k-', label=f"Señal Modificada (A={A}, f={f}Hz, ϕ={phi:.2f} rad)")
    plt.title(titulo if titulo else "Comparación de señales discretas")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()


def discrete_plotter_dac(entrada_digital, salida_analogica, titulo=""):
    """
    Grafica la salida analógica de un DAC frente a su entrada digital.

    Parámetros:
        entrada_digital (array-like): valores digitales de entrada (0 a 2^N-1)
        salida_analogica (array-like): valores analógicos correspondientes (voltaje)
        titulo (str): título opcional para la gráfica
    """
    plt.figure(figsize=(10, 4))
    plt.stem(entrada_digital, salida_analogica, linefmt='b-', markerfmt='bo', basefmt='k-')
    plt.title(titulo if titulo else "Salida analógica del DAC")
    plt.xlabel("Entrada digital (decimal)")
    plt.ylabel("Salida analógica (V)")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()
