# *********************************************************
# COURSE 10 SESSION 03
# *********************************************************
"""
ESTRUCTURAS DE DATOS COMPUESTAS
3.1 Estructuras anidadas
Previamente, aprendimos a manipular las listas, tuplas y diccionarios
    para trabajar con una secuencia o colección de valores sean
    numéricos, categóricos, etc. En esta aula, vamos a profundizar en
    otra situación común para la persona científica de datos que es
    trabajar con estos tipos de estructuras anidadas, o sea, cuando,
    por ejemplo, tenemos listas dentro de una lista

Lista de listas
    [[a1, a2,...,an], [b1, b2,...,bn], ..., [n1, n2,...,nn]]


SITUATION 6
Recibimos la demanda de transformar una lista con el nombre y las notas
de tres trimestres de algunos estudiantes en una lista simple, con los
nombres separados de las notas, y una lista de listas con las tres
notas de cada estudiante separadas entre sí. Los datos recibidos
corresponden a una lista con los nombres y las respectivas notas de
cada estudiante

Para facilitar nuestra comprensión del proceso, vamos a trabajar con un
grupo de 5 estudiantes; sin embargo, puedes probar otros casos para
practicar
"""
notas_grupo = ["Juan", 8.0, 9.0, 10.0,
               "Maria", 9.0, 7.0, 6.0,
               "José", 3.4, 7.0, 7.0,
               "Claudia", 5.5, 6.6, 8.0,
               "Ana", 6.0, 10.0, 9.5]

nombres = []
notas = []

for i in range(len(notas_grupo)):
    if i % 4 == 0:
        nombres.append(notas_grupo[i])
    else:
        notas.append(notas_grupo[i])

print(nombres)
print(notas)

notas_separadas = []
for i in range(0, len(notas), 3):
    notas_separadas.append([notas[i], notas[i+1], notas[i+2]])
print(notas_separadas)


"""
Lista de tuplas
    [(a1, a2,...,an), (b1, b2,...,bn), ..., (n1, n2,...,nn)]

SITUATION 7
Necesitamos generar una lista de tuplas con los nombres de los
estudiantes y el código ID de cada uno de ellos para la plataforma de
análisis de datos. La creación del código consiste en concatenar la
primera letra del nombre del estudiante con un número aleatorio de 0 a
999. Los datos recibidos corresponden a una lista con los nombres de
cada estudiante

Para facilitar nuestra comprensión del proceso, vamos a trabajar con un
grupo de 5 estudiantes; sin embargo, puedes probar otros casos para
practicar
"""
from random import randint

def genera_numero():
    return randint(0, 999)

codigo_estudiantes = []

for i in range(len(nombres)):
    codigo_estudiantes.append(( nombres[i], nombres[i][0] + str(randint(0, 999)) ))

print(codigo_estudiantes)

"""
Tuplas
Las tuplas son estructuras de datos inmutables en el lenguaje Python que se utilizan para almacenar conjuntos de múltiples elementos y a menudo se aplican para agrupar datos que no deben modificarse. Es decir, no es posible agregar, cambiar o eliminar sus elementos después de creadas. Vamos a explorar un poco más este tipo de estructura enfocada en la aplicación en ciencia de datos.

Las tuplas son especialmente útiles en situaciones en las que necesitamos garantizar que los datos no se modifiquen accidental o intencionalmente. Por ejemplo, en un conjunto de datos que representa el registro de estudiantes, podemos utilizar una tupla para representar a ese estudiante en particular y mantenerlo en la base de datos de una institución educativa. De esta manera, aseguramos que la información de cada estudiante no se modifique inadvertidamente.

Para crear una tupla, simplemente separamos sus elementos por comas y los envolvemos entre paréntesis. Por ejemplo, podemos crear una tupla con un registro de una estudiante de la siguiente manera:
"""
registro = ("Julia", 23, "CDMX", "EM", "Python para DS 1")

# Para acceder a los elementos de una tupla, podemos usar el índice entre corchetes. Por ejemplo:
print(registro[0])  # imprime Julia
print(registro[-1])  # imprime Python para DS 1

# Además, al ser un iterable, podemos desempaquetar los datos de una tupla pasando cada valor a una variable. Por ejemplo:
nombre, edad, ciudad, estado, curso = registro

# Y mostrar los datos del registro de la estudiante:
print(f'La estudiante {nombre} tiene {edad} años y vive en {ciudad}-{estado}. Ella está matriculada en el curso de {curso}.')

# Salida
# La estudiante Julia tiene 23 años y vive en CDMX-EM. Ella está matriculada en el curso de Python para DS 1.


"""
3.2 List comprehension
Es una forma simple y concisa de crear una lista. Podemos aplicar
condicionales y lazos para crear diversos tipos de listas a partir de
patrones que deseamos para nuestra estructura de datos

https://docs.python.org/es/3/tutorial/datastructures.html?#list-comprehensions

Formato estándar:
    [expresion for item in lista]

SITUATION 8
Recibimos la demanda de crear una lista con el promedio de los
estudiantes de la lista de listas que creamos en la Situación 6,
redondeando el promedio a una casilla decimal. Recordando que cada
lista de la lista de listas contiene las tres notas de cada estudiante

*Tip: Utiliza el formato:
    [expresion for item in lista]
"""




"""
Situación 9:
Ahora, necesitamos utilizar los promedios calculados en el ejemplo anterior, y agruparlos con el nombre de los respectivos estudiantes. Esto será necesario para generar una lista que seleccione a aquellos estudiantes que posean un promedio final mayor o igual a 8 para concursar por una beca de estudios para el próximo año lectivo. Los datos recibidos corresponden a una lista de tuplas con los nombres y los códigos de los estudiantes junto a la lista de promedios calculados previamente.

Nota: El número de código será diferente cada vez que se ejecute la celda que los genera, por lo tanto, es completamente normal que estos códigos sean diferentes.

¿Vamos a resolver este desafío?

Para facilitar nuestra comprensión del proceso vamos a trabajar con un grupo de 5 estudiantes.

Tip: Utiliza el formato:

[expresion for item in lista if condicion]
"""



"""
Tip: Para lograr parear los promedios y los nombres fácilmente, podemos acudir a otra built-in function: zip()

Esta recibe uno o más iterables (lista, string, dict, etc.) y los retorna como un iterador de tuplas donde cada elemento de los iterables es pareado.
"""



"""
Situación 10:
Recibimos dos demandas sobre este proyecto con las notas de los estudiantes:

Crear una lista de la situación de los estudiantes considerando los siguientes casos: Si su promedio es mayor o igual a 7, recibirá el valor "Aprobado" y en caso contrario recibirá el valor "Reprobado".
Generar una lista de listas con:
Lista de tuplas con el nombre de los estudiantes y sus códigos
Lista de listas con las notas de cada estudiante
Lista con los promedios de cada estudiante
Lista de la situación de los estudiantes de acuerdo con los promedios
Los datos que utilizaremos son los mismos que generamos en las situaciones anteriores (nombres, notas, promedios).

¿Vamos a resolver este desafío?

Para avanzar en el proceso, vamos a dejar escritas las estructuras de datos que ya produjimos.

Tip: Para la lista de las situaciones utiliza el formato:

[resultado_if if condicion else resultado_else for item in lista]
"""



"""
Tip: Para generar la lista de listas del enunciado podemos utilizar el siguiente formato:

[expresion for item in lista de listas]
"""



"""
Tip: Podemos acudir a la forma más simple de generación de lista de listas con el uso directo de los corchetes sin la necesidad de utilizar las expresiones y el lazo for que se emplea en la comprensión de listas.
"""


"""
3.3 Dict comprehension
Es una forma simple y concisa de crear o modificar un diccionario. Podemos aplicar condicionales y lazos para crear diversos tipos de diccionarios a partir de los patrones que buscamos para nuestra estructura de datos y con el soporte de iterables como listas o sets.

https://peps.python.org/pep-0274/

Formato estándar:
{llave: valor for item in lista}
Situación 11:
Ahora, nuestra demanda consiste en generar un diccionario a partir de la lista de listas que creamos en la Situación 10 para entregar a la persona responsable por construir las tablas para el análisis de los datos.

Las llaves de nuestro diccionario serán las columnas identificando el tipo de dato
Los valores serán las listas con los datos correspondientes a aquella llave.
¿Vamos a resolver este desafío?

Para facilitar nuestra comprensión del proceso vamos a trabajar con un grupo de 5 estudiantes.

Tip: Utiliza el formato

{llave: valor for item in lista}
"""

