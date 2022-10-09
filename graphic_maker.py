import os
from functions import *
from pista_carros import create_graphic_car, initialize_speedway
from sandor_mikola import create_graphic_sandor
from all_graphics import make_all_graphics


def graphic_maker():
    print('Elija [a] para mostrar todas las graficas en un conjunto de valores x')
    selected = choose_mode()
    os.system("cls")

    if selected == 'a':
        choose = mode_x_values()
        x = set_x_values(choose)
        have_line = tendence_line()
        make_all_graphics(x, have_line)

    elif selected:
        choose = mode_x_values()
        x = set_x_values(choose)
        have_line = tendence_line()

        create_graphic_sandor(x, have_line)
        os.system("cls")

    else:
        a, vi, xi, de, degrees = initialize_speedway()
        choose = mode_x_values()
        x = set_x_values(choose)
        have_line = tendence_line()

        create_graphic_car(x, a, vi, xi, de, degrees, have_line)
        os.system("cls")