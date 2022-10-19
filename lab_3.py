import os
from simulator import simulator
from graphic_maker import graphic_maker


def lab_3():

    """Bucle principal de laboratorio 3 (movimiento en una dimensión)
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
            return lab_3()

        graphic_mode =  mode == 'g'    

        os.system("cls")

        if graphic_mode:
            graphic_maker()

        else:
            simulator()
