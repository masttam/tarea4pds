def dac_output(n_bits, VFS=5.0):
    """
    Calcula la salida analógica de un DAC para una entrada digital creciente.

    Parámetros:
        n_bits (int): Número de bits del DAC.
        VFS (float): Voltaje de escala completa (default 5V).

    Retorna:
        entrada_digital (list): Lista de valores digitales desde 0 hasta 2^n_bits - 1.
        salida_analogica (list): Lista de voltajes correspondientes a cada valor digital.
        niveles (int): Número total de niveles del DAC.
        tam_paso (float): Tamaño del paso (voltaje entre niveles).
        resolucion_pct (float): Resolución porcentual del DAC.
    """
    niveles = 2 ** n_bits
    tam_paso = VFS / (niveles - 1)
    resolucion_pct = (tam_paso / VFS) * 100

    entrada_digital = list(range(niveles))
    salida_analogica = [v * tam_paso for v in entrada_digital]

    return entrada_digital, salida_analogica, niveles, tam_paso, resolucion_pct
