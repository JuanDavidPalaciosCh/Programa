<center><h1><strong> Simulaciones de fundamentos de mecanica:</strong></h1>


<h3><em>Creado por: Juan David Palacios, Gabriel Mauricio Estupiñan, Andres Fernando Acosta y Miguel Botiva</em></h3>
<h4 style="color:#999999"> jpalaciosch@unal.edu.co, gestupinanp@unal.edu.co, anacostaz@unal.edu.co, jbotiva@unal.edu.co</h4></center>
<hr size="8px" color ="Red"/>
<h3 style="color:#FF0000">Funcionamiento del programa: </h3>
<p>Este programa recopila los laboratorios de Fundamentos de mecanica, permitiendonos, a partir de los datos experimentales poder predecir datos de ciertos tiempos o posiciones especificas de los experimentos.</p>

<p>El programa cuenta con los siguientes laboratorios:</p>

<ol>
    <li>Sandor Mikola.</li>
    <li>Pista inclinada de carros.</li>
    <li>movimiento en dos dimensiones.</li>
</ol>

En cada uno de estos laboratorios el programa permite graficar en un intervalo dado por el usuario con la posibilidad de elegir si se añade una linea de tendencia; o si el usuario lo quiere dar cada valor del eje x para que el programa encuentre las imagenes.

<hr size="8px" color ="Red"/>
<h3 style="color:#FF0000">Especificaciones del programa: </h3>
<p>El programa esta realizado en python, usando las librerias: Matplotlib, math, os y Numpy. <p>

<hr size="8px" color ="Red"/>
<h3 style="color:#FF0000">Especificaciones de uso: </h3>
Estas son las variables que se pueden cambiar segun el resultado que se busque, o segun los datos experimentales hayan indicado.

<ol>
    <li> En la funcion initialize_speedway que se encuentra en pista_carros.py se puede cambiar los valores experimentales de:</li>
    <ul>
        <li>'a' es la aceleracion divido 2.</li>
        <li>'vi' es la velocidad inicial.</li>
        <li>'xi' es la distancia inicial.</li>
        <li>'de' es el promedio de la desviacion estandar.</li>
    </ul>
        <li> En la funcion initialize_sandor que se encuentra en sandor_mikola.py se pueden cambiar los valores experimentales:</li>
    <ul>
        <li>'m' es la pendiente.</li>
        <li>'b' es el origen.</li>
    </ul>
        <li> En el archivo lab_4 se puede modificar:</li>
    <ul>
        <li>'a' que es la constante experimental del laboratorio.</li>
    </ul>
</ol>
