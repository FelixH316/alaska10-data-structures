"""
# *********************************************************
# COURSE 10 EXERCISES 02
# *********************************************************
"""

# HW 01 - CALENTAMIENTO
"""
01 - Escribe un código que lee la lista siguiente y realiza:

    lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

A. Leer el tamaño de la lista
B. Leer el valor máximo y mínimo
C. Calcular la suma de los valores de la lista
D. Mostrar un mensaje al final:
    La lista tiene `tamano` números, donde
    el mayor es `mayor` y el menor es `menor`. La suma de los valores
    es `suma`
"""
lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]

lenght = len(lista)
lista.sort()
small = lista[0]    # small = min(lista)
big = lista[-1]     # big = max(lista)
total = sum(lista)
print(f"The list has [{lenght}] numbers, where the greatest is [{big}] \n\
        and the smallest is [{small}]. The sum of all its values is \
        [{total}]")


"""
02 - Escribe una función que genere la tabla de multiplicar de un
    número entero del 1 al 10, según la elección del usuario. Como
    ejemplo, para el número 7, la tabla de multiplicar se debe mostrar
    en el siguiente formato:

Tabla del  7:
    7 x 0 = 0
    7 x 1 = 7
    [...]
    7 x 10 = 70
"""
def multiplication_table(number: int):
    """
        Prints the multiplication table of the received number

        Params:
            @int number
    """
    print(f"Tabla del {number}:")
    for i in range(11):
        print(f"\t{number} x {i} = {number * i}")
    print("\n")

multiplication_table(2)
multiplication_table(8)


"""
03 - Crea una función que lea la siguiente lista y devuelva una nueva
    lista con los múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]
"""
lista = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99, 3]
def list_multiplier(lista: list, multiplier: float) -> list:
    """
        Multiplies all elements in the list by a specified number

        Params:
            @list lista
            @float multiplier

        Return:
            @list new_list
    """
    new_list = []
    for value in lista:
        new_list.append(value * multiplier)
    return new_list


listax3 = list_multiplier(lista, 3)
print(lista)
print(listax3)

# Corrected
def mcm_filter(lista: list, mcm: int) -> list:
    """
        Filter just the numbers that are a multiplier of the given number

        Params:
            @list lista
            @int mcm (minimum common multiplier)

        Return:
            @list new_list
    """
    return [num for num in lista if num % mcm == 0]

filter_3 = mcm_filter(lista, 3)
print(f"Multipliers of 3: {filter_3}")


"""
04 - Crea una lista de los cuadrados de los números de la siguiente
    lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Recuerda utilizar las funciones lambda y map() para calcular el
    cuadrado de cada elemento de la lista
"""
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lambda_cuadrados = lambda x: x * x
cuadrados = map(lambda_cuadrados, lista)
cuadrados = list(cuadrados)
print(f"Squared numbers: {cuadrados}")


# HW 02 - APLICANDO A PROYECTOS
"""
05 - Has sido contratado como científico(a) de datos de una asociación
    de skate. Para analizar las notas recibidas por los skaters en
    algunas competiciones a lo largo del año, necesitas crear un código
    que calcule la puntuación de los atletas. Para ello, tu código debe
    recibir 5 notas ingresadas por los jueces
"""
# TODO
notas = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(5)]
notas.sort()
media = sum(notas[1:4]) / 3
print(f"Nota de la maniobra: {media:.2f}")

"""
06 - Para cumplir con una demanda de una institución educativa para el
    análisis del rendimiento de sus estudiantes, necesitas crear una
    función que reciba una lista de 4 notas y devuelva:

    mayor nota
    menor nota
    media
    situación (Aprobado(a) o Reprobado(a))

Uso de la función
    Mostrar: El estudiante obtuvo una media de `media`, con la mayor
        nota de `mayor` puntos y la menor nota de `menor` puntos y fue
        `situacion`
"""
# TODO
def analisis_notas(notas):
    mayor = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    situacion = "Aprobado" if media >= 6 else "Reprobado"
    return mayor, menor, media, situacion

# Uso de la función
notas_estudiante = [float(input(f"Ingrese la nota {i + 1}: ")) for i in range(4)]
resultado = analisis_notas(notas_estudiante)
print(f"El estudiante obtuvo una media de {resultado[2]:.2f}, con la mayor nota de {resultado[0]:.2f} puntos y la menor nota de {resultado[1]:.2f} puntos y fue {resultado[3]}")


"""
07 - Has recibido una demanda para tratar 2 listas con los nombres y
    apellidos de cada estudiante concatenándolos para presentar sus
    nombres completos en la forma Nombre Apellido. Las listas son:

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

Normalizar nombres y apellidos y crear una nueva lista con los nombres
    completos
    
*Puedes apoyarte en la función map()
"""
nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

lambda_cap = lambda name : name.capitalize()
lambda_merge = lambda name, last_n : name + ' ' + last_n

nombres = list(map(lambda_cap, nombres))
apellidos = list(map(lambda_cap, apellidos))
print(nombres)
print(apellidos)

full_name = list(map(lambda_merge, nombres, apellidos))
print(full_name)

# FROM INSTRUCTOR
nombres = ["juan", "MaRia", "JOSÉ"]
sobrenombres = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
nombres_normalizados = map(lambda x: x.capitalize(), nombres)
sobrenombres_normalizados = map(lambda x: x.capitalize(), sobrenombres)
nombres_completos = list(map(lambda x, y: f"Nome completo: {x} {y}", nombres_normalizados, sobrenombres_normalizados))
print(nombres_completos)


"""
08 - Como científico de datos en un equipo de fútbol, necesitas
    implementar nuevas formas de recopilación de datos sobre el
    rendimiento de los jugadores y del equipo en su conjunto. Tu
    primera acción es crear una forma de calcular la puntuación del
    equipo en el campeonato nacional a partir de los datos de goles
    marcados y recibidos en cada juego

Escribe una función llamada calcula_puntos() que recibe como parámetros
    dos listas de números enteros, representando los goles marcados y
    recibidos por el equipo en cada partido del campeonato. La función
    debe devolver la puntuación del equipo y el rendimiento en
    porcentaje, teniendo en cuenta que la victoria vale 3 puntos, el
    empate 1 punto y la derrota 0 puntos

Nota: si la cantidad de goles marcados en un partido es mayor que los
    recibidos, el equipo ganó. En caso de ser igual, el equipo empató,
    y si es menor, el equipo perdió. Para calcular el rendimiento,
    debemos hacer la razón entre la puntuación del equipo y la
    puntuación máxima que podría recibir

Para la prueba, utiliza las siguientes listas de goles marcados y
    recibidos:

    goles_marcados = [2, 1, 3, 1, 0]
    goles_recibidos = [1, 2, 2, 1, 3]

    Texto probablemente mostrado:
        La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"
"""
def calcula_puntos (goals_scored: list, goals_received: list):
    """
        Calculates the total points of the season and the performance
        in percentage

        Params:
            @list goals_scored
            @list goals_received

        Return:
            @int points
            @float performance
    """
    points = 0
    for i, match_scrd in enumerate(goals_scored):
        if match_scrd > goals_received[i]:
            points += 3
        elif match_scrd == goals_received[i]:
            points += 1
    max_points = len(goals_scored) * 3
    performance = points * 100 / max_points
    return points, performance


goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
team_points, team_perf = calcula_puntos(goles_marcados, goles_recibidos)
print(f"\nThis season the team had [{team_points}] points \n\
        \rwith a performance of [{team_perf:.2f}%]")


"""
09 - Te han desafiado a crear un código que calcule los gastos de un
    viaje a una de las cuatro ciudades desde Recife, siendo ellas:
    Salvador, Fortaleza, Natal y Aracaju.

El costo diario del hotel es de 150 reales en todas ellas y el consumo
    de gasolina en el viaje en coche es de 14 km/l, siendo que el
    precio de la gasolina es de 5 reales por litro. Los gastos con
    paseos y alimentación a realizar en cada una de ellas por día
    serían [200, 400, 250, 300], respectivamente

Sabiendo que las distancias entre Recife y cada una de las ciudades
    son aproximadamente [850, 800, 300, 550] km, crea tres funciones:
    la primera función calcula los gastos de hotel (gasto_hotel), la
    segunda calcula los gastos de gasolina (gasto_gasolina) y la
    tercera los gastos de paseo y alimentación (gasto_paseo)

Para probar, simula un viaje de 3 días a Salvador desde Recife
    Considera el viaje de ida y vuelta en coche

Texto probablemente mostrado:
    Con base en los gastos definidos, un viaje de [dias] días a
    [ciudad] desde Recife costaría [gastos] reales
"""
# TODO
dias = int(input("¿Cuántas diarias? "))
ciudad = input("¿Cuál es la ciudad? [Salvador, Fortaleza, Natal o Aracaju]: ")
distancias = [850, 800, 300, 550]
paseo = [200, 400, 250, 300]
km_l = 14
gasolina = 5

def gasto_hotel(dias):
    return 150 * dias

def gasto_gasolina(ciudad):
    if ciudad == "Salvador":
        return (2 * distancias[0] * gasolina) / km_l 
    elif ciudad == "Fortaleza":
        return (2 * distancias[1] * gasolina) / km_l 
    elif ciudad == "Natal":
        return (2 * distancias[2] * gasolina) / km_l 
    elif ciudad == "Aracaju":
        return (2 * distancias[3] * gasolina) / km_l 

def gasto_paseo(ciudad, dias):
    if ciudad=="Salvador":
        return paseo[0] * dias
    elif ciudad=="Fortaleza":
        return paseo[1] * dias
    elif ciudad=="Natal":
        return paseo[2] * dias 
    elif ciudad=="Aracaju":
        return paseo[3] * dias 

gastos = gasto_hotel(dias) + gasto_gasolina(ciudad) + gasto_paseo(ciudad, dias)
print(f"Con base en los gastos definidos, un viaje de {dias} días a {ciudad} desde Recife costaría {round(gastos, 2)} reales")


"""
10 - Has comenzado una pasantía en una empresa que trabaja con
    procesamiento de lenguaje natural (NLP)
    
    Tu líder te solicitó que crees un fragmento de código que reciba
    una frase escrita por el usuario y filtre solo las palabras con un
    tamaño mayor o igual a 5, mostrándolas en una lista. Esta demanda
    se centra en el análisis del patrón de comportamiento de las
    personas al escribir palabras de esta cantidad de caracteres o más

Consejo: utiliza las funciones lambda y filter() para filtrar estas
    palabras. Recordando que la función integrada filter() recibe una
    función (en nuestro caso, una función lambda) y filtra un iterable
    según la función. Para tratar la frase, utiliza replace() para
    cambiar ',' '.', '!' y '?' por espacio

Utiliza la frase "Aprender Python aquí en Alura es muy bueno" para
    probar el código
"""
frase = "¡Aprender Python aquí en Alura, es muy bueno!, vrd?"
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').replace('¡',' ').split()
print(frase)
lambada_size = lambda palabra : len(palabra) >= 5
filter_words = list(filter(lambada_size, frase))
print(filter_words)
