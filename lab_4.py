import os
import math
from matplotlib import pyplot as plt
from functions import mode_x_values, set_x_values, tendence_line


VARIABLES: list = ['h', 'x']

#Constante experimental del laboratorio
a: float = 0.0064 


def choose_simulation() -> bool:

    """Pregunta al usuario que variable desea hallar (Alcance maximo o altura).

    Returns:
        simulation bool: define la selección
    """

    simulation: bool = False
    simulator_type: str = input('Elija la variable a hallar... [x] Alcance maximo con respecto a la altura, [h] altura con respecto al alcance maximo: ')

    simulator_type = simulator_type.lower()
    simulator_type = simulator_type[0]

    if simulator_type != 'x' and simulator_type != 'h':
        print('Elección invalida...')
        return choose_simulation()

    simulation =  simulator_type == 'x'

    return simulation


def make_simulation():

    """Halla valores resultantes para la simulación del laboratorio 4.

    Returns:
        result float: Resultado de la simulación.
        int: determina que tipo de dato utilizar para mostrar al usuario lo obtenido.
        h float: Altura utilizada en la simulación.
        x float: Alcance maximo utilizado en la simulación.
    """
    simulation_type: bool = choose_simulation()
    if simulation_type:
        h: float = float(input('Elija una altura a simular (cm): '))
        result: float = math.sqrt(h/a)
        return result, 0, h
    else:
        x: float = float(input('Elija un alcance maximo a simular (cm): '))
        result: float = a * (x**2)
        return result, 1, x


def lab_4():

    """Bucle principal de laboratorio 4 (movimiento en dos dimensiones)
    """
    
    while True:
        os.system("cls")
        graphic_mode: bool = False
        mode: str = input('Elija el modo a usar... [s] simulador de valores, [g] creador de graficas, [Q] selección laboratorio: ')

        mode = mode.lower()
        mode = mode[0]

        if mode == 'q':
            return None

        if mode != 's' and mode != 'g' and mode != 'q':
            print('Elección invalida...')
            return lab_4()

        graphic_mode =  mode == 'g'    

        os.system("cls")

        if graphic_mode:
            choose = mode_x_values()
            x = set_x_values(choose)
            have_line = tendence_line()
            y = [a * (x[i]**2) for i in range(len(x))]

            plt.plot(x, y, 'o{}'.format(have_line), color='green')
            plt.xlabel('Alcance x (cm)')
            plt.ylabel('Altura h (cm)')
            plt.title('Grafica h-x - movimiento semiparabolico - lanzador de proyectiles')
            plt.grid(True)
            
            plt.show()

        else:
            end = False

            while not end:
                    
                    result, variable, simulation = make_simulation()
                    print('\nEl resultado para {} = {}cm es: {} = {:.2f}cm'.format(VARIABLES[variable], simulation, VARIABLES[variable-1], result))
                    
                    
                    flag: str = input('\nPresione enter para volver a usar el simulador, [Q] salir: ')
                    flag.lower()
                    os.system("cls")
                    end =  flag == 'q'
