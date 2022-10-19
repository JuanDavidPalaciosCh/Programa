from sandor_mikola import initialize_sandor
from pista_carros import initialize_speedway
import matplotlib.pyplot as plt
from constants import ROWS


def make_all_graphics(x: list, have_line: str):

    """Genera todas las graficas del laboratorio 3 en una sola ventana: Sandor Mikola,
     Pista de carros 4, 8 y 12 grados para un mismo conjunto de valores del eje x.

    Parameters:
        x list: Valores para el eje x.
        have_line str: Determina la existencia de linea de tendencia.
    """
    x_table = ["{:.1f}".format(x[i]) for i in range(len(x))]

    fig = plt.figure(figsize=(30,30))
    fig.tight_layout()
    plt.subplots_adjust(wspace=0.5, hspace=0.4)
    
    colors = ['blue', 'green', 'red', 'cyan']

    m, b = initialize_sandor()
    y1 = [round(m * x[i]  + b, 2) for i in range(len(x))] #Sandor Mikola

    ax1 = plt.subplot(2, 2, 1)
    ax1.plot(x, y1, 'o{}'.format(have_line), color=colors[0])
    ax1.set_xlabel(ROWS[0])
    ax1.set_ylabel(ROWS[1])
    ax1.set_title('Grafica x-t, tubo Sandor Mikola (5°)')
    plt.grid(True)

    a, vi, xi, de, degrees = initialize_speedway(4) 
    xi -= de
    y2 = [round((a*(x[i]**2)) + (vi * x[i]) + xi, 2) for i in range(len(x))] #Pista de carros 4°

    ax2 = plt.subplot(2, 2, 2)
    ax2.plot(x, y2, 'o{}'.format(have_line), color=colors[1])
    ax2.set_xlabel(ROWS[0])
    ax2.set_ylabel(ROWS[1])
    ax2.set_title('Grafica x-t, Pista de carros inclinada ({}°)'.format(degrees))
    plt.grid(True)

    a, vi, xi, de, degrees = initialize_speedway(8) 
    xi -= de
    y3 = [round((a*(x[i]**2)) + (vi * x[i]) + xi, 2) for i in range(len(x))] #Pista de carros 8°

    ax3 = plt.subplot(2, 2, 3)
    ax3.plot(x, y3, 'o{}'.format(have_line), color=colors[2])
    ax3.set_xlabel(ROWS[0])
    ax3.set_ylabel(ROWS[1])
    ax3.set_title('Grafica x-t, Pista de carros inclinada ({}°)'.format(degrees))
    plt.grid(True)

    a, vi, xi, de, degrees = initialize_speedway(12) 
    xi -= de
    y4 = [round((a*(x[i]**2)) + (vi * x[i]) + xi, 2) for i in range(len(x))] #Pista de carros 12°

    ax4 = plt.subplot(2, 2, 4)
    ax4.plot(x, y4, 'o{}'.format(have_line), color=colors[3])
    ax4.set_xlabel(ROWS[0])
    ax4.set_ylabel(ROWS[1])
    ax4.set_title('Grafica x-t, Pista de carros inclinada ({}°)'.format(degrees))
    plt.grid(True)
    
    plt.figtext(0.95, 0.02, 'GRP-1: Andrés Acosta, Miguel Botiva, Gabriel Estupiñan, Juan David Palacios', horizontalalignment='right', size=6, weight='light')


    plt.show()




        
