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
