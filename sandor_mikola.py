from functions import *
import matplotlib.pyplot as plt


def initialize_sandor():

    """Inicializa valores utilizados para el experimento del tubo de Sandor Mikola.

    Returns:
        m float: Pendiente de la grafica.
        b float: Error en valores.
    """

    m: float = 1.9274
    b: float = -1.7911

    return m, b


def sandor_mikola():
    
    """Halla valores para el experimento del tubo de Sandor Mikola.

    Returns:
        result float: Resultado de la simulación.
        int: determina que tipo de dato utilizar para mostrar al usuario lo obtenido.
        x float: Distancia utilizada en la simulación.
        t float: Tiempo utilizado en la simulación.
    """
    m, b = initialize_sandor()

    simulation_type: bool = choose_simulation()
    if simulation_type:
        x: float = choose_distance()
        result: float = (x - b) / m
        return result, 0, x, 1
    else:
        t: float = choose_time()
        result: float = m*t + b
        return result, 1, t, 0


def create_graphic_sandor(x: list, have_line: str):

    """Crea la grafica del experimento del tubo de Sandor Mikola.

    Parameters:
        x list: Valores del eje x.
        have_line: Existencia de linea de tendencia.
    """

    m, b = initialize_sandor()

    y = [round(m * x[i]  + b, 2) for i in range(len(x))]
    x_table = ["{:.1f}".format(x[i]) for i in range(len(x))]

    # Crea graficos
    make_graphics(x, y, x_table, have_line) 

    plt.show()