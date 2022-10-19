import os
from pista_carros import inclinated_speedway
from sandor_mikola import sandor_mikola
from constants import *
from functions import choose_mode


def simulator():

    """Entra en el modo simulador en el que se puede encontrar valores aislados de los distintos experimentos.
    """

    end = False

    while not end:
            selected = choose_mode()
            os.system("cls")

            if selected:
                result, variable, simulation, unit = sandor_mikola()
                print('\nEl resultado para {} = {}{} con una inclinacion de 5°, es: {} = {:.2f}{}'.format(VARIABLES[variable], simulation, UNITS[unit-1], VARIABLES[variable-1], result, UNITS[unit]))
            
            else:
                result, variable, simulation, unit, degrees = inclinated_speedway()
                print('\nEl resultado para {} = {}{} con inclinacion {}°, es: {} = {:.2f}{}'.format(VARIABLES[variable], simulation, UNITS[unit-1], degrees, VARIABLES[variable-1], result, UNITS[unit]))

            flag: str = input('\nPresione enter para volver a usar el simulador, [Q] salir: ')
            flag.lower()
            os.system("cls")
            end =  flag == 'q'