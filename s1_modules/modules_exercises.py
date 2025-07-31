# *********************************************************
# COURSE 10 EXERCISES 01
# *********************************************************

# HW 01 - CALENTAMIENTO

"""
01 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib

pip install matplotlib==3.7.1
"""
from matplotlib import __version__ as ver
print(ver)


"""
02 - Escribe un código para importar la biblioteca numpy con el alias
    np
"""
import numpy as np


"""
03 - Crea un programa que lea la siguiente lista de números y elija uno
    al azar

        lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]
"""
from random import randint, choice
lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

print(f"\n\tYour number is: {lista[randint(0, len(lista) - 1)]}")
print(f"\n\tYour number is: {choice(lista)}")


"""
04 - Crea un programa que genere aleatoriamente un número entero menor
    que 100
"""
from random import randrange

print(f"\n\tYour number lower than 100 is: {randint(0, 100)}")
print(f"\n\tYour number lower than 100 is: {randrange(100)}")


"""
05 - Crea un programa que solicite a la persona usuaria ingresar dos
    números enteros y calcule la potencia del primer número elevado al
    segundo
"""
number = float(input("\nInput a number: "))
power = int(input("Input a power: "))

print(f"\t{number} to the {power} is: {number ** power}")


# HW2 - APLICANDO A PROYECTOS
"""
06 - Se debe escribir un programa para sortear a un seguidor de una red
    social para ganar un premio. La lista de participantes está
    numerada y debemos elegir aleatoriamente un número según la
    cantidad de participantes. Pide a la persona usuaria que
    proporcione el número de participantes del sorteo y devuelve el
    número sorteado
"""
tamano = int(input("\nInput the number of raffle participants: "))
# raffle = []
# for i in range(1, tamano+1):
#     raffle.append(i)
# print(f"\n\tThe winner is: {choice(raffle)}")
print(f"\n\tThe winner is: {randint(1, tamano)}")


"""
07 - Has recibido una solicitud para generar números de token para
    acceder a la aplicación de una empresa. El token debe ser par y
    variar de 1000 a 9998. Escribe un código que solicite el nombre de
    la persona usuaria y muestre un mensaje junto a este token generado
    aleatoriamente

    print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")
"""
nombre_usuario = input("\nInput you name: ")
token_generado = None
# while token_generado is None or (token_generado % 2) != 0: 
#     token_generado = randint(1000, 9999)
token_generado = randrange(1000, 9999, 2)

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")


"""
08 - Para diversificar y atraer nuevos clientes, una lanchonete creó un
    ítem misterioso en su menú llamado "ensalada de frutas sorpresa".
    En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12
    para componer la ensalada de frutas del cliente. Crea el código que
    realice esta selección aleatoria según la lista dada

    frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]
"""
from random import sample

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

# print(f"\n\tYour random fruit salad have: {choice(frutas)}, {choice(frutas)} and {choice(frutas)}")
print(f"\n\tYour random fruit salad have: {sample(frutas, 3)}")


"""
09 - Has recibido un desafío para calcular la raíz cuadrada de una lista
    de números, identificando cuáles resultan en un número entero. La
    lista es la siguiente:

    numeros = [2, 8, 15, 23, 91, 112, 256]
"""
from math import sqrt

numeros = [2, 8, 15, 23, 91, 112, 256]

print("\n\tYour numbers are: ")
print(numeros)
# sq_roots = []
# enteros = {}
# for value in numeros:
#     raiz = sqrt(value)
#     sq_roots.append(raiz)
#     if (raiz % 1) == 0:
#         enteros[raiz]="entero"
#     else:
#         enteros[raiz]="decimal"
# print("\tLos resultados son los siguientes: ")
# print(enteros)
raices_enteras = [num for num in numeros if sqrt(num) % 1 == 0]
print("\tNumbers with integer squared roots: ", raices_enteras)

"""
10 - Haz un programa para una tienda que vende césped para jardines.
    Esta tienda trabaja con jardines circulares y el precio del metro
    cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el
    radio del área circular y devuelve el valor en reales de cuánto
    tendrá que pagar
"""
from math import pi
meter_price = 25.00
radio = float(input("\nEnter the radius of your circular area: "))
area = pi * radio * radio
total = area * meter_price
print(f"\tThe price for your grass is: ${total:.2f} BRL")
print(f"\tThe price for your grass is: ${round(total)} BRL")
