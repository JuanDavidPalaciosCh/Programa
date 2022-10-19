from functions import *
import math


def initialize_speedway(degrees: int=None):

    """Initializa valores para el experimento de pista de carros inclinada.

    Parameters:
        degrees int: Grados utilizados para los valores.

    Returns:
        a float: 1/2 de la aceleración.
        vi float: Velocidad inicial.
        xi float: Distancia inicial.
        de float: Promedio desviación estándar.
        degrees int: Grados utilizados para selección de datos.
    """
        
    if degrees == None:
        degrees:int = choose_degrees()

    if degrees == 4: #Valores para 4° de inclinación.
        a: float = 1.91
        vi: float = 67.61
        xi: float = -31.72
        de: float = 0.05

    elif degrees == 8: #Valores para 8° de inclinación.
        a: float = 47.02
        vi: float = 35.55
        xi: float = -8.5
        de: float = 0.0357

    elif degrees == 12: #Valores para 12° de inclinación.
        a: float = 40.52
        vi: float = 70.21
        xi: float = -13.03
        de: float = 0.02

    else:
        print('Grados seleccionados no validos...')
        return initialize_speedway()

    return a, vi, xi, de, degrees


def inclinated_speedway():

    """Halla valores para el experimento de la pista de carros inclinada.

    Returns:
        result float: Resultado de la simulación.
        int: determina que tipo de dato utilizar para mostrar al usuario lo obtenido.
        x float: Distancia utilizada en la simulación.
        t float: Tiempo utilizado en la simulación.
        degrees int: Grados de inclinación utilizados en la simulación.
    """

    a, vi, xi, de, degrees = initialize_speedway()

    simulation_type: bool = choose_simulation()

    if simulation_type:
        x: float = choose_distance()
        xi -= x + de
        result: float = ((-vi + math.sqrt(vi**2-(4*a*xi)))/(2*a))
        return result, 0, x, 1, degrees
    else:
        xi -= de
        t: float = choose_time()
        result: float = (a*(t**2)) + (vi * t) + xi
        return result, 1, t, 0, degrees


def create_graphic_car(x: list, a: float, vi: float, xi: float, de: float, degrees: int, have_line: str):

    """Crea la grafica del experimento de pista de carros inclinada.

    Parameters:
        x list: Valores del eje x.
        a float: 1/2 de la aceleración.
        vi float: Velocidad inicial.
        xi float: Distancia inicial.
        de float: Promedio desviación estándar.
        have_line: Existencia de linea de tendencia.
    """

    xi -= de
    y = [round((a*(x[i]**2)) + (vi * x[i]) + xi, 2) for i in range(len(x))]
    x_table = ["{:.1f}".format(x[i]) for i in range(len(x))]

    # Crea graficos
    make_graphics(x, y, x_table, have_line, degrees) 
    
    plt.show() 