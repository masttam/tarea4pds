import matplotlib.pyplot as plt

def graficar_senal(t, x_cont, tn, x_disc, titulo, ylabel="Amplitud"):
    plt.figure(figsize=(8, 4))
    plt.plot(t, x_cont, label='Señal continua', linewidth=2)
    plt.stem(tn, x_disc, linefmt='r-', markerfmt='ro', basefmt='k-', label='Señal muestreada')
    plt.title(titulo)
    plt.xlabel('Tiempo [s]')
    plt.ylabel(ylabel)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
