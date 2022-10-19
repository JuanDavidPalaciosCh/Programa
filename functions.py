import os
import matplotlib.pyplot as plt
import numpy
from constants import LINE, NOT_LINE, ROWS


def choose_lab() -> bool:
    choose: bool = False
    lab: str = input('Elija el laboratorio a usar: \n[3] Laboratorio 3: Movimiento unidimensional \n[4] Laboratorio 4: Movimiento en dos dimensiones \n \n')
    os.system("cls")

    if lab != '3' and lab != '4':
        print('Elección invalida...')
        return choose_lab()

    choose = lab == '3'

    return choose


def choose_mode() -> bool: 
    choose: bool = False
    simulator: str = input('Elija el experimento a usar... [t] tubo sandor mikola, [p] pista de carros inclinada: ')

    simulator = simulator.lower()
    simulator = simulator[0]

    if simulator == 'a':
        return 'a'

    if simulator != 't' and simulator != 'p':
        print('Elección invalida...')
        return choose_mode()
    
    choose =  simulator == 't'

    return choose


def choose_simulation() -> bool:
    simulation: bool = False
    simulator_type: str = input('Elija la variable a hallar... [t] tiempo con respecto a distancia, [x] distancia con respecto a tiempo: ')

    simulator_type = simulator_type.lower()
    simulator_type = simulator_type[0]

    if simulator_type != 't' and simulator_type != 'x':
        print('Elección invalida...')
        return choose_simulation()

    simulation =  simulator_type == 't'

    return simulation


def choose_degrees() -> float:
    inclination: int = int(input('Elija los grados de inclinación para la pista de carros entre (4, 8 y 12)°: '))
    if inclination != 4 and inclination != 8 and inclination != 12:
        input('Elija una inclinación valida, presione enter para continuar: ')
        os.system("cls")
        return choose_degrees()
    return inclination


def choose_time() -> float:
    time: float = float(input('Elija un tiempo a simular (segundos): '))
    return time


def choose_distance() -> float:
    distance: float = float(input('Elija una distancia a simular (centimetros): '))
    return distance


def tendence_line() -> str:
    tendence_line = False
    with_line: str = input('Elija [l] si desea linea de tendencia, de lo contrario elija [n]: ')

    with_line = with_line.lower()
    with_line = with_line[0]

    tendence_line =  with_line == 'l'

    if tendence_line:
        return LINE
    
    else:
        return NOT_LINE


def mode_x_values():
    choose: bool = False
    flag: str = input('Elegir valores [v], elegir rango de valores [r]: ')

    flag = flag.lower()
    flag = flag[0]

    if flag != 'v' and flag != 'r':
        print('Elección invalida...')
        return mode_x_values()

    choose =  flag == 'v'

    return choose


def set_x_values(choose: bool) -> list:
    os.system("cls")
    x = []
    if choose:

        valor: str = ''
        i: int = 1
        
        while valor != 'q':
            valor = input('Ingrese el {} valor, [Q] para generar la grafica: '.format(i))

            valor = valor.lower()

            try:
                valor = float(valor)
                x.append(valor)
                i += 1

            except ValueError:
                if valor == 'q':
                    break
                print('No es un valor valido por favor intente de nuevo...')
            
    
    else:

        xi = float(input('Elija un valor (x) inicial: '))
        xf = float(input('Elija un valor (x) final: '))
        jump = float(input('Elija el salto de los valores: '))

        x = numpy.arange(xi, xf + jump, jump)
    
    x.sort()
    return x


def make_graphics(x, y, x_table, have_line, degrees=5):
    
    """
    #Tabla de datos
    fig, ax = plt.subplots()
    the_table = ax.table(cellText=[x_table, y],loc='top', rowLabels=ROWS)
    fig.tight_layout()
    """
    plt.subplots_adjust(top=0.95, bottom=0.15, left=0.17)
    
    #Grafica
    plt.plot(x,y, 'or{}'.format(have_line))
    
    if degrees == 5:
        plt.title('Grafica x-t, tubo Sandor Mikola ({}°)'.format(degrees), y=1.15)
    else:
        plt.title('Grafica x-t, Pista de carros inclinada ({}°)'.format(degrees), y=1.15)
        
    plt.ylabel('distancia (cm)')
    plt.xlabel('tiempo (s)')
    plt.grid(True)
    plt.figtext(0.95, 0.02, 'GRP-1: Andrés Acosta, Miguel Botiva, Gabriel Estupiñan, Juan David Palacios', horizontalalignment='right', size=6, weight='light')



            