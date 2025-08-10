# *********************************************************
# COURSE 10 SESSION 04
# *********************************************************
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
def promedio(lista: list[0]) -> float:
    """
        Función para calcular el promedio de notas en una lista

        Params:
            @list lista "Lista con las notas para calcular el promedio"
                default = [0]
        Return:
            @float promedio "Promedio calculado"    
    """
    calculo = sum(lista) / len(lista)
    return calculo


notas = [[8.0, 9.0, 10.0],
         [9.0, 7.0, 6.0],
         [3.4, 7.0, 7.0],
         [5.5, 6.6, 8.0],
         [6.0, 10.0, 9.5]]
promedio = [round(promedio(nota), 1) for nota in notas]
print(promedio)


"""
SITUATION 9
Ahora, necesitamos utilizar los promedios calculados en el ejemplo
    anterior, y agruparlos con el nombre de los respectivos estudiantes
    Esto será necesario para generar una lista que seleccione a
    aquellos estudiantes que posean un promedio final mayor o igual a 8
    para concursar por una beca de estudios para el próximo año lectivo.
    Los datos recibidos corresponden a una lista de tuplas con los
    nombres y los códigos de los estudiantes junto a la lista de
    promedios calculados previamente.

*Nota: El número de código será diferente cada vez que se ejecute la
    celda que los genera, por lo tanto, es completamente normal que
    estos códigos sean diferentes.

Para facilitar nuestra comprensión del proceso vamos a trabajar con un
    grupo de 5 estudiantes.

*Tip: Utiliza el formato:
    [expresion for item in lista if condicion]
"""
nombres = [('Juan', 'J833'),
           ('Maria', 'M535'),
           ('José', 'J561'),
           ('Claudia', 'C833'),
           ('Ana', 'A402')]
promedios = [9.0, 7.3, 5.8, 6.7, 8.5]

nombres = [nombre[0] for nombre in nombres]
print(nombres)

"""
Tip: Para lograr parear los promedios y los nombres fácilmente, podemos
    acudir a otra built-in function: zip()

Esta recibe uno o más iterables (lista, string, dict, etc.) y los
    retorna como un iterador de tuplas donde cada elemento de los
    iterables es pareado.
"""
estudiantes = list(zip(nombres, promedios))
print(estudiantes)

candidatos = [estudiante[0] for estudiante in estudiantes if estudiante[1] >= 8]
print(candidatos)

"""
[START] TO LEARN MORE: Built-in function zip()
La función zip() es una función incorporada de Python que toma uno o
    más iterables (lista, cadena, diccionario, etc.) y los devuelve
    como un iterador de tuplas donde cada elemento de los iterables
    está emparejado. Es útil para realizar iteraciones simultáneas en
    varias listas.

La función zip() se puede utilizar junto con otras funciones de Python,
    como map() y filter(), para crear soluciones elegantes y concisas
    para ciertos problemas. Realicemos una prueba simple para verificar
    este comportamiento:

"""
objeto_zip = zip([1, 2, 3])
objeto_zip

# Salida
# <zip at 0x7f28fc5c0040>

# Notamos que zip() creó un objeto zip en la memoria, que sería nuestro
#   iterable. Coloquemos el resultado en una lista para verificar la
#   salida:
list(objeto_zip)

# Salida
# [(1,), (2,), (3,)]

"""
Observa que, con solo un iterable, se generó una lista de tuplas, donde
    cada tupla tiene, como uno de los pares, los elementos provenientes
    de la lista [1, 2, 3] y la otra parte de los pares está vacía. Como
    solo usamos un iterable, cada tupla está vacía en el segundo
    elemento, ya que zip() actúa para crear pares de iterables.

Pero lo más interesante es trabajar con dos o más iterables en los que
    podemos emparejarlos. Por ejemplo, si queremos crear una lista de
    tuplas con la asignación de las regiones de Brasil con sus
    respectivos identificadores:
"""
id = [1, 2, 3, 4, 5]
region = ["Norte", "Oriente", "Sudeste", "Centro", "Sur"]

mapa = list(zip(id, region))
mapa

# Salida
# [(1, 'Norte'), (2, Oriente), (3, 'Sudeste'), (4, 'Centro'), (5, 'Sur')]

"""
Para un científico de datos, esta función puede ayudar a emparejar dos
    listas diferentes en un único objeto zip, que se puede transformar
    en una lista de tuplas (formato ideal para generar un índice de más
    de un nivel que se explorará en algunos de los cursos de la
    formación) o en un diccionario pasando el objeto zip a la función
    dict().

Ahora, si las listas de entrada tienen longitudes diferentes, la salida
    contendrá el mismo número de tuplas que la lista de menor longitud
    y los elementos restantes de los otros iterables se ignorarán. Por
    ejemplo:
"""
codigos = ["1000", "1001", "1002", "1003", "1004", "1005"]
frutas = ["manzana", "uva", "banana", "naranja"]

mercancia = list(zip(codigos, frutas))
mercancia

# Salida
# [('1000', 'manzana'), ('1001', 'uva'), ('1002', 'banana'), ('1003', 'naranja')]

"""
Para realizar el proceso contrario, de transformar una tupla iterable
    en listas, basta con colocar el operador asterisco (*) al lado
    izquierdo del nombre de la tupla iterable que se desea extraer los
    datos, transmitiendo cada tupla a una variable.
"""
tupla_iterable = [('J392', 'Juan'), ('M890', 'Maria'), ('J681', 'José'), ('C325', 'Claudia'), ('A49', 'Ana')]
ids, nombres = zip(*tupla_iterable)

ids = list(ids)
nombres = list(nombres)

print("IDs = ", ids)
print("Nombres = ", nombres)

# Salida
# IDs = ['J392', 'M890', 'J681', 'C325', 'A49']
# Nombres = ['Juan', 'Maria', 'José', 'Claudia', 'Ana']

"""
La idea de realizar un "desempaquetado inverso" es útil cuando
  queremos extraer claves o valores por separado o generar una lista
  de tuplas separadas, con el conjunto de claves y valores, cada uno
  representado en una tupla.

[END] TO LEARN MORE: Built-in function zip()
"""

"""
SITUATION 10
Recibimos dos demandas sobre este proyecto con las notas de los estudiantes:

+ Crear una lista de la situación de los estudiantes considerando los siguientes casos: Si su promedio es mayor o igual a 7, recibirá el valor "Aprobado" y en caso contrario recibirá el valor "Reprobado".

+ Generar una lista de listas con:
    ¬ Lista de tuplas con el nombre de los estudiantes y sus códigos
    ¬ Lista de listas con las notas de cada estudiante
    ¬ Lista con los promedios de cada estudiante
    ¬ Lista de la situación de los estudiantes de acuerdo con los promedios

Los datos que utilizaremos son los mismos que generamos en las situaciones anteriores (nombres, notas, promedios).

Para avanzar en el proceso, vamos a dejar escritas las estructuras de datos que ya produjimos.

*Tip: Para la lista de las situaciones utiliza el formato:
    [resultado_if if condicion else resultado_else for item in lista]
"""
nombres = [('Juan', 'J833'),
           ('Maria', 'M535'),
           ('José', 'J561'),
           ('Claudia', 'C833'),
           ('Ana', 'A402')]
promedios = [9.0, 7.3, 5.8, 6.7, 8.5]
notas = [[8.0, 9.0, 10.0],
         [9.0, 7.0, 6.0],
         [3.4, 7.0, 7.0],
         [5.5, 6.6, 8.0],
         [6.0, 10.0, 9.5]]

situacion = ["Aprobado(a)" if promedio >= 7 else "Reprobado(a)" for promedio in promedios]
print(situacion)


"""
*Tip: Para generar la lista de listas del enunciado podemos utilizar el siguiente formato:

    [expresion for item in lista de listas]
"""
registros = [x for x in [nombres, notas, promedios, situacion]]
print("REGISTROS: ", registros)


"""
Tip: Podemos acudir a la forma más simple de generación de lista de
    listas con el uso directo de los corchetes sin la necesidad de
    utilizar las expresiones y el lazo for que se emplea en la
    comprensión de listas.
"""
lista_completa = [nombres, notas, promedios, situacion]
print("LISTA COMPLETAS: ", lista_completa)

"""
WHAT IS THIS CODE DOING?
Andrés recibió una solicitud para analizar el conjunto de datos que
    contiene información sobre la altura y el peso de varias personas.
    Para procesar estos datos, André utilizó la estructura de list
    comprehension para calcular y también guardar los datos del Índice
    de Masa Corporal (IMC). Vea el código desarrollado por él a
    continuación:
"""
alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)


"""
3.3 Dict comprehension
Es una forma simple y concisa de crear o modificar un diccionario.
    Podemos aplicar condicionales y lazos para crear diversos tipos de
    diccionarios a partir de los patrones que buscamos para nuestra 
    estructura de datos y con el soporte de iterables como listas o
    sets.

https://peps.python.org/pep-0274/

Formato estándar:
    {llave: valor for item in lista}

SITUATION 11
Ahora, nuestra demanda consiste en generar un diccionario a partir de
    la lista de listas que creamos en la Situación 10 para entregar a
    la persona responsable por construir las tablas para el análisis de
    los datos.

    + Las llaves de nuestro diccionario serán las columnas
        identificando el tipo de dato
    + Los valores serán las listas con los datos correspondientes a
        aquella llave.

How to solve it?
Para facilitar nuestra comprensión del proceso vamos a trabajar con un
    grupo de 5 estudiantes.

Tip: Utiliza el formato
    {llave: valor for item in lista}
"""
lista_completa = [[('Juan', 'J833'),
                   ('Maria', 'M535'),
                   ('José', 'J561'),
                   ('Claudia', 'C833'),
                   ('Ana', 'A402')],
                  [[8.0, 9.0, 10.0],
                   [9.0, 7.0, 6.0],
                   [3.4, 7.0, 7.0], 
                   [5.5, 6.6, 8.0], 
                   [6.0, 10.0, 9.5]],
                  [9.0, 7.3, 5.8, 6.7, 8.5],
                  ['Aprobado(a)', 'Aprobado(a)',
                   'Reprobado(a)', 'Reprobado(a)',
                   'Aprobado(a)']]
columnas = ["Notas", "Promedio Final", "Situación"]
registro = {columnas[i] : lista_completa[i+1] for i in range(len(columnas))}
print(registro)

registro["Estudiante"] = [lista_completa[0][i][0] for i in range(len(lista_completa[0]))]
print("\n\nREGISTRO FINAL: ", registro)

"""
[START] TO LEARN MORE: selecting scholarship recipients
Recibimos una demanda de la institución educativa de nuestro proyecto que nos proporcionó una lista de 20 estudiantes y sus respectivos promedios finales. Aquí, necesitamos seleccionar estudiantes que tengan un promedio final mayor o igual a 9.0. Estos estudiantes serán premiados con una beca de estudios para el próximo año escolar.

Para filtrar los datos, debemos generar un diccionario cuyas claves son los nombres y los valores son los promedios de los estudiantes seleccionados. Estos son los datos recibidos:
"""
nombres_estudiantes = ["Enrique Montero", "Luna Pereira", "Anthony Silva", "Leticia Fernandez", "Juan González", "Maira Caldera", "Diana Carvajo", "Mariana Rosas", "Camila Fernandez", "Levi Alves", "Nicolás Rocha", "Amanda Navas",  "Lara Morales", "Leticia Olivera", "Lucas Navas", "Lara Arteaga", "Beatriz Martinez", "Victor Acevedo", "Stephany Hernández", "Gustavo Lima"]

medias_estudiantes = [5.4, 4.1, 9.1, 5.3, 6.9, 3.1, 9.0, 5.0, 8.2, 5.5,
                    8.1, 7.4, 5.0, 3.7, 8.1, 6.2, 6.1, 5.6, 10.0, 8.2]

"""
¿Cuál de los códigos a continuación representa la forma correcta de generar el diccionario con los estudiantes seleccionados?

Tip ⇒ Utiliza a forma:
    {expresion_llave: expresion_valor for item in iterable if condicion}
"""
becados = {nombre: media for nombre, media in zip(nombres_estudiantes, medias_estudiantes) if media >= 9.0}
print(becados)

# Salida: {'Anthony Silva': 9.1, 'Stephany Hernández': 10.0}

"""
[END] TO LEARN MORE: selecting scholarship recipients
"""