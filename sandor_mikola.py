from functions import *
import matplotlib.pyplot as plt
import numpy


def initialize_sandor():
    m: float = 1.9274
    b: float = -1.7911

    return m, b


def sandor_mikola():
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
    m, b = initialize_sandor()

    y = [round(m * x[i]  + b, 2) for i in range(len(x))]
    x_table = ["{:.1f}".format(x[i]) for i in range(len(x))]

    # Crea graficos
    make_graphics(x, y, x_table, have_line) 

    plt.show()