# *********************************************************
# COURSE 10 SESSION 02
# *********************************************************
"""
FUNCIONES
En Python, las funciones son secuencias de instrucciones que ejecutan
    tareas específicas, permitiendo su reutilización en diferentes
    partes del código. Estas pueden recibir parámetros de entrada (que
    también los conocemos como inputs) y también retornar resultados

2.1 Built-in function (Función Incorporada)
    El interpretador de Python contiene una serie de funciones
    incorporadas que pueden ser invocadas es cualquier momento. Algunas
    que vamos a utilizar a lo largo de este curso son: type(), print(),
    list(), zip(), sum(), map(), etc

Documentación: https://docs.python.org/es/3/library/functions.html

SITUATION 1
    La institución educativa para la cual nos encontramos trabajando
    compartió los datos de las notas de un estudiante para que
    pudiesemos calcular su promedio con una casilla decimal

Los datos recibidos corresponden a un diccionario cuyas llaves indican
    el trimestre en cuestión y sus valores corresponden a las notas de
    cada trimestre del estudiante en una respectiva materia
"""
notas = {"1° trimestre" : 9.5,
         "2° trimestre": 8,
         "3° trimestre": 7}
suma = 0
for s in notas.values():
    suma += s
print(suma)

promedio = sum(notas.values()) / len(notas)
print(promedio)

# Redondear el promedio usando round():
# https://docs.python.org/es/3/library/functions.html#round

print(help(round))
print(round(promedio, 1))


"""
2.2 CREATING FUNCTIONS
Tras explorar las funciones incorporadas y aprender cómo utilizar
    algunas de ellas, es posible que tengas la necesidad de resolver un
    problema específico y estas no sean suficientes

Por este motivo, necesitaremos crear nuestras propias funciones, y aún
    más, si necesitamos aplicarlas en varias partes de nuestros códigos

Funciones sin parámetros
Formato estándar:

    def <nombre>():
        <instrucciones>
"""
def promedio():
    calculo = (10 + 9 + 7) / 3
    print(calculo)

promedio()

# Funciones con parámetros
# Formato estándar:
# def <nombre>(<param_1>, <param_2>, ..., <param_n>):
#   <instrucciones>

def promedio(nota1, nota2, nota3):
    calculo = (nota1 + nota2 + nota3) / 3
    print(calculo)

promedio(10, 9, 7)
promedio(nota3=7, nota2=9, nota1=10)

"""
SITUATION 2
Recibimos una solicitud para crear una función que calcule el promedio
    de notas de un estudiante a partir de una lista; que permita
    alterar la cantidad de notas, y que no implique tener que modificar
    la función

Los datos recibidos, en esta ocasión, corresponden a una lista que
    contiene las notas de un mismo estudiante en una determinada
    materia

notas = 8.5, 9.0, 6.0, 10.0

Para facilitar nuestra comprensión del proceso, vamos a aplicar las
    notas de un único estudiante; sin embargo, puedes probar otros
    casos para practicar
"""
notas = [8.5, 9.0, 6.0, 10.0]

def promedio(lista):
    calculo = sum(lista) / len(lista)
    print(calculo)

media = promedio(notas)
print(type(media))

"""
WARNING
Cuando utilizamos funciones, necesitamos prestar atención a una
    propiedad llamada Alcance de una función. Esta propiedad determina
    dónde una variable puede ser utilizada dentro del código. Por
    ejemplo, una variable creada dentro de una función existirá
    únicamente dentro de esta función. O sea, cuando finaliza la
    ejecución de una función, la variable no estará disponible para el
    usuario en el resto del código
"""
print(calculo) # Error


"""
2.3 FUNCTIONS THAT RETURN VALUES

Formato estándar:

def <nombre>(<param_1>, <param_2>, ..., <param_n>):
    <instrucciones>
    return resultado

Retomando la actividad anterior, podemos retornar y guardar el valor del promedio de la siguiente forma:
"""
# Notas del estudiante
notas = [8.5, 9.0, 6.0, 10.0]

def promedio(lista):
    return sum(lista) / len(lista)

resultado = promedio(notas)
print(resultado)
print(type(resultado))


"""
SITUATION 3
Recibimos una nueva solicitud. Debemos calcular el promedio de un
    estudiante a partir de una lista y retornar tanto el promedio como
    la situación del estudiante ("Aprobado(a)" si la nota es mayor o
    igual a 7.0, en caso contrario, será "Reprobado(a)")

Además de ello, necesitamos exhibir un pequeño texto para indicar el
    promedio del estudiante y cuál es su situación. Los datos recibidos
    corresponden a una lista que contiene apenas las notas de un
    estudiante en una materia determinada

Para facilitar nuestra comprensión del proceso, vamos a aplicar las
    notas de un único estudiante; sin embargo, puedes probar otros
    casos para practicar
"""
# Notas del estudiante
notas = [8.5, 9.0, 6.0, 10.0]

def boletin(lista):
    resultado = sum(lista) / len(lista)
    if resultado >= 7:
        situacion = "Aprobado(a)"
    else:
        situacion = "Reprobado(a)"
    return (resultado, situacion)

print(boletin(notas))
resultado, situacion = boletin(notas)
print(f"El(La) estudiante obtuvo un puntaje de {resultado} y su situación es: {situacion}")

def calificaciones(lista):
    resultado = sum(lista) / len(lista)
    if resultado >= 7:
        situacion = "Aprobado(a)"
    else:
        situacion = "Reprobado(a)"
    return f"El(La) estudiante obtuvo un puntaje de {resultado} y su situación es: {situacion}"

notas2 = [7.5, 4.0, 3.0, 10.0]
calificaciones(notas2)


"""
FUNCIONES LAMBDA
También se conocen como funciones anónimas, son funciones que no
    necesitan ser definidas, o sea, no poseen un nombre, y describen en
    una única fila los comandos que deseamos aplicar

https://docs.python.org/es/3/reference/expressions.html?#lambda

Formato estándar:

lambda <variable>: <expresion>
"""
dato_float = float(input("Digite una nota: "))

def cualitativa(nota):
    return nota + 0.5

print(cualitativa(dato_float))

from_lambda = lambda x: x + 0.5

print(from_lambda(dato_float))


"""
SITUATION 4
En esta nueva solicitud, necesitamos crear una calculadora simple para
    obtener el promedio ponderado de notas de una materia determinada
    Vamos a pedir que el usuario introduzca 3 notas (N1, N2, N3) del
    estudiante y devuelva el promedio ponderado de este estudiante. Los
    pesos de las notas son de, respectivamente 3, 2 y 5

Necesitamos exhibir un pequeño texto para poder indicar el promedio del
    estudiante
"""
n1 = float(input("Digite la primera nota: "))
n2 = float(input("Digite la primera nota: "))
n3 = float(input("Digite la primera nota: "))
ponderado = lambda x, y, z : (x * 3 + y * 2 + z * 5) / 10

nota_final = ponderado(n1, n2, n3)
print(nota_final)

print(f"El promedio ponderado del estudiante es: {nota_final}")


"""
SITUATION 5

Ahora, debemos crear una pequeña función que permita dar una nota
    cualitativa (puntaje extra) a las notas del trimestre de los
    estudiantes del grupo que ganó el concurso de programación
    realizado en la institución. Cada estudiante recibirá el
    cualitativo de 0.5 añadido al promedio

Los datos recibidos corresponden a una lista que contiene las notas de
    algunos estudiantes y una variable con el cualitativo recibido

Para facilitar nuestra comprensión del proceso, vamos a aplicar las
    notas de 5 estudiantes; sin embargo, puedes probar otros casos
    para practicar
"""
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
cualitativo = 0.5

notas_actualizadas = lambda x: x + 0.5

# Error, para un iterable tenemos que mapear los valores
notas_actualizadas(notas)


"""
MAPEANDO VALORES

Formato estándar:

map(<lambda function>, <iterador>)
"""
notas_actualizadas = map(lambda x: x + 0.5, notas)
print(notas_actualizadas)
notas_actualizadas = list(notas_actualizadas)
print(notas_actualizadas)
print(notas)

"""
ADDING DOCUMENTATION TO FUNCTIONS
Es importante hacer que nuestro código o análisis de datos sea lo más
    accesible posible para el público. Una de las formas de lograr este
    propósito es documentar las funciones. Podemos ayudar a quienes
    leen nuestro proyecto o utilizan las funciones que hemos
    desarrollado a entender qué tipos de variables podemos usar, si hay
    o no valores predeterminados o incluso describir de manera sucinta
    lo que hace ese fragmento de código

Aquí, te pedimos que sigas este paso a paso en la documentación de la
    función de media que construimos durante la clase. Será requerida
    nuevamente más adelante en nuestros estudios

Type Hint

Type Hint es una sintaxis utilizada en Python para indicar el tipo de
    dato esperado de un parámetro o el retorno de una función, ayudando
    en la legibilidad y mantenimiento del código. Podemos decir, en
    pocas palabras, que es una sugerencia de tipado de datos

Formato:
def <nombre>(<param>: <tipo_param>) -> <tipo_retorno>:
    <instrucciones>
    return resultado

Aplicando esto a nuestro ejemplo de la función media(), podemos usar
    Type Hint de la siguiente manera:
"""
# nuestra función recibe una lista del tipo list y retorna una variable del tipo float
def media(lista: list) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

"""
Si escribimos la función media() en otra celda y pasamos el ratón por
    encima, podemos observar la sugerencia de tipo de los parámetros de
    entrada y salida de la función

Default Value

En Python, Default Value es un valor predeterminado asignado a un
    argumento de función que se utiliza si el usuario no proporciona
    ningún valor

Formato:
<nombre_variable>: <tipo_variable> = <valor_variable>

Extendiendo nuestra función media(), podemos usar el valor
    predeterminado de la siguiente manera:
"""
# nuestra función recibe una lista del tipo list y retorna una variable
# del tipo float si no recibe ningún valor de parámetro, se pasará una
# lista con un único elemento, siendo este cero
def media(lista: list=[0]) -> float:
    calculo = sum(lista) / len(lista)
    return calculo

"""
De la misma manera que hicimos con Type Hint, si escribimos la función
    media() en otra celda y pasamos el ratón por encima, podemos
    observar la sugerencia de tipo de los parámetros de entrada y
    salida de la función, así como el valor predeterminado para nuestra
    lista si el usuario no proporciona ningún valor durante la ejecución

Si ejecutamos la función media, esta será la salida:
0.0
"""


"""
DOCSTRING
Finalmente, tenemos el Docstring, que es una cadena literal utilizada
    para documentar módulos, funciones, clases o métodos en Python. Se
    coloca como el primer elemento de la definición y se puede acceder
    utilizando la función help()

El Docstring debe describir el propósito, los parámetros, el tipo de
    retorno y las excepciones que puede generar la función. Es una
    buena práctica de programación utilizar Docstrings en tu código
    para facilitar la lectura, el mantenimiento y el intercambio de
    código con otros desarrolladores

Formato:
"""
def <nombre>(<param_1>, <param_2>, ..., <param_n>):
    '''Texto documentando su función...
    '''
    <instrucciones>
    return resultado

# Concluyendo la implementación de nuestra función media(), podemos
#   usar el Docstring de la siguiente manera:
def media(lista: list=[0]) -> float:
    '''Función para calcular la media de notas pasadas por una lista

    lista: list, default [0]
        Lista con las notas para calcular la media
    return = calculo: float
        Media calculada
    '''
    calculo = sum(lista) / len(lista)
    return calculo

# Si ejecutamos el código help(media) en otra celda, obtenemos la
#   siguiente salida:
"""
Help on function media in module __main__:

media(lista: list = [0]) -> float
    Función para calcular la media de notas pasadas por una lista

    lista: list, default [0]
        Lista con las notas para calcular la media
    return = calculo: float
        Media calculada
"""
