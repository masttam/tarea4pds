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


def continuous_plotter(t, x, titulo=""):
    plt.figure(figsize=(10, 4))
    plt.plot(t, x, label="Señal senoidal continua", color='blue')
    plt.title(titulo)
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.tight_layout()
    plt.show()
