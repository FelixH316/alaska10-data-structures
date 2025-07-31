# *********************************************************
# COURSE 10 SESSION 01
# *********************************************************
"""
INSTALACIÓN DE BIBLIOTECAS/MODULOS

LTS Newest (it will install other dependency modules, so you might
    unistall each of them after if needed)
        pip install matplotlib

Specific released version
        pip install matplotlib==3.5.1

Uninstall
        pip uninstall matplotlib
"""
import matplotlib

print(matplotlib.__version__)


"""
Python Package Index (PYPI)

pip funciona conectándose al PYPI que ess el repositorio centralizado
    más grande para paquetes de Python con miles de bibliotecas
    disponibles para la instalación. Podemos buscar en PyPI para
    encontrar paquetes que satisfagan nuestras necesidades y luego usar
    pip para instalarlos en nuestros proyectos

        https://pypi.org/

En Google colab puedes usar el siguiente comando para imprimir todos
    los paquetes instalados en tu entorno
    
    !pip list
"""

# Importando una biblioteca/modulo
import matplotlib.pyplot as plt
plt.show()

"""
1.2 Utilizando módulos/bibliotecas
Documentación de Python (https://docs.python.org/es/3/)

Ejemplo 1: Vamos a probar la biblioteca Matplotlib para un ejemplo
    sobre el cálculo de los promedios de notas de los estudiantes de
    una clase.
    
        (https://matplotlib.org/stable/tutorials/introductory/pyplot.html)
"""
from matplotlib import pyplot as plt

estudiantes = ["Juan", "María", "José"]
notas = [9, 8.5, 6.5]

plt.bar(x=estudiantes, height=notas)
plt.show()

"""
Ejemplo 2: Vamos a seleccionar aleatoriamente a un alumno para
    presentar su trabajo de ciencia de datos usando la biblioteca
    random
    
        (https://docs.python.org/es/3/library/random.html)
"""
from random import choice

estudiantes2 = ["Juan", "María", "José", "Erika"]
estudiante = choice(estudiantes2)
print(estudiante)

"""
Tip: Podrás notar a medida que avanzas en los ejercicios la importancia
    de acudir a la documentación para aprender cómo utilizar un método
    de algún módulo en el lenguaje Python

El método help(), por ejemplo, retorna una descripción sobre una variable,
    método o clase.

        https://docs.python.org/es/3/library/functions.html?#help
"""
print(help(choice))


""" OTRAS FORMAS DE IMPORTAR 
Ya hemos trabajado con dos formas de importar paquetes: 
    import nombre_biblioteca             # para todo el paquete y 
    from nombre_biblioteca import metodo # para solo un método de una biblioteca dada

La importación de métodos específicos de una biblioteca puede tener
    algunas ventajas para nuestro proyecto, como:

    1. Economía de memoria: cuando importamos una biblioteca completa,
        todo su código se carga en la memoria, incluso si no utilizamos
        todos sus métodos. Importar solo los métodos que necesitamos
        puede ahorrar memoria, especialmente en programas con grandes
        bibliotecas

    2. Mayor claridad en el código: importar solo los métodos que vamos
        a usar hace que el código sea más claro y fácil de entender

    3. Reducción de conflictos de nombres: al importar una biblioteca
        completa, podríamos tener conflictos de nombres con otras
        variables o funciones en nuestro código

    4. Reducción en el tiempo de ejecución: como no se importa toda la
        biblioteca, el tiempo de ejecución del programa puede ser más
        rápido, ya que se carga y se interpreta menos código en la
        memoria por el intérprete de Python
"""

"""
Métodos especificos
    from nombre_biblioteca import met_1, met_2
"""
from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

sample(lista, 5)

"""
Importar todo

from nombre_biblioteca import *
"""
# Comparación 1
import math 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")


# Comparación 2
from math import * 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {sqrt(n)}")


"""
Observa que, en el segundo ejemplo, hemos omitido el nombre math
    utilizando el método deseado y escribiendo el código con menos
    caracteres

Nota: La importación en este sentido requiere ciertos cuidados:
    1. Podríamos tener conflictos de nombres entre las variables. Por
       ejemplo, si tenemos una función llamada sqrt antes de importar
       la de la biblioteca math

    2. Podríamos reducir la eficiencia de la ejecución si el número de
       funciones importadas es grande

    3. No queda explícito de dónde proviene esa variable, método o
       clase
"""
