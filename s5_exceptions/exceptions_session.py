# *********************************************************
# COURSE 10 SESSION 05
# *********************************************************
"""
4. LIDIANDO CON EXCEPCIONES
Hemos podido evidenciar hasta aquí la existencia de algunos errores y
    excepciones en la ejecución de algún comando. Como científico/a de
    datos o programador, necesitarás estar atento a estas situaciones
    para evitar bugs o problemas en tus códigos y análisis que puedan
    afectar la experiencia tanto del usuario como la eficiencia de su
    análisis.

Existen básicamente dos formas distintas de errores: Los errores de
    sintáxis y las excepciones.

Las excepciones son errores detectados durante la ejecución e
    interrumpen el flujo del programa cerrándolo en caso de que no sean
    tratadas.

Vamos a aprender a identificar y tratar algunas de las excepciones aquí,
    pero es siempre importante consultar la documentación para investigar
    y verificar cuáles se ajustan a sus proyectos.

Documentación sobre errores y excepciones:
    https://docs.python.org/es/3/tutorial/errors.html

4.1 TRATANDO LAS EXCEPCIONES
El tratamiento de las excepciones contribuye a establecer un flujo
    alternativo para la ejecución del código evitando la interrupción 
    de los procesos inesperadamente.

Existe una serie de excepciones, y a partir del comportamiento que
    queremos, y de los errores que queremos tratar, es posible 
    construir un camino para el usuario, o también, proveer más
    detalles sobre aquella excepción.

Jerarquía de las excepciones 
    https://docs.python.org/es/3/library/exceptions.html#exception-hierarchy

Try ... Except

try:
    # código que será ejecutado. En caso de que surja una excepción,
    # para inmediatamente
except <nombre_de_la_excepcion as e>:
    # Si surje una excepción en el try, ejecuta este código, si no,
    # salta esta etapa

SITUATION 12
Creaste un código que lee un diccionario con las notas de los
   estudiantes y querías retornar la lista de notas de un estudiante.

En caso que el/la estudiante no esté matriculado(a) en el grupo debemos
    tratar la excepción para presentar el mensaje "Estudiante no
    matriculado(a) en el grupo".

Vamos a trabajar en este ejemplo con la excepción Key Error que
    interrumpirá el processo de este trecho de código.
"""
notas = {'Juan': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0],
         'José': [3.4, 7.0, 8.0], 'Claudia': [5.5, 6.6, 8.0],
         'Ana': [6.0, 10.0, 9.5], 'Jorge': [5.5, 7.5, 9.0],
         'Julia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    nombre = input ("Digita el nombre del(de la) estudiante: ")
    resultado = notas[nombre]
    print(resultado)
except Exception as e:
    print(type(e), e)

try:
    nombre = input("Digitar el nombre del(de la) estudiante: ")
    resultado = notas[nombre]
except KeyError:
    print("Estudiante no matriculado(a) en el grupo")


"""
AGREGANDO LA CLÁUSULA ELSE

try:
    # código que será ejecutado. En caso de que surja una excepción,
    # para inmediatamente
except:
    # Si surje una excepción en el try, ejecuta este código, si no,
    # salta esta etapa
else:
    # Si no surjen excepciones, ejecuta esta parte del código

SITUATION 13
Creaste un código que lee un diccionario con las notas de los
    estudiantes y querías retornar la lista de notas de un estudiante.

En caso de que el/la estudiante no esté matriculado(a) en la clase,
    debe aparecer el siguiente mensaje: "Estudiante no matriculado(a)
    en el grupo" y, si no surje la excepción, debemos exhibir la lista
    con las notas del(la) estudiante.

Vamos a trabajar en este ejemplo con la excepción Key Error que
    interrumpirá el proceso de este trecho de código.
"""
try:
    nombre = input("Digitar el nombre del(de la) estudiante: ")
    resultado = notas[nombre]
except KeyError:
    print("Estudiante no matriculado(a) en el grupo")
else:
    print(f"Las notas del(de la) estudiante son: {resultado}")


"""
AÑADIENDO LA CLÁUSULA FINALLY

try:
    # código que será ejecutado. En caso de que surja una excepción,
    # para inmediatamente
except:
    # Si surje una excepción en el try, ejecuta este código, si no,
    # salta esta etapa
else:
    # Si no surjen excepciones, ejecuta esta parte del código
finally:
    # Ejecuta este trecho (con o sin excepción)

SITUATION 14
Creaste un código que lee un diccionario con las notas de los
    estudiantes y querías retornar la lista de notas de un estudiante.

En caso de que el/la estudiante no esté matriculado(a) en la clase,
    debe aparecer el siguiente mensaje: "Estudiante no matriculado(a)
    en el grupo" y, si no surje la excepción, debemos exhibir la lista
    con las notas del(la) estudiante. Un texto avisando que "La
    consulta ha concluído." debe ser mostrado independientemente de si
    surgió o no alguna excepción.

Vamos a trabajar en este ejemplo con la excepción Key Error que
    interrumpirá el proceso de este trecho del código.
"""
try:
    nombre = input("Digitar el nombre del/la estudiante: ")
    resultado = notas[nombre]
except KeyError:
    print("Estudiante no matriculado(a) en el grupo")
else:
    print(f"Las notas del(de la) estudiante son: {resultado}")
finally:
    print("La consulta ha concluido")


"""
En Python, básicamente existen dos formas distintas de errores: los de sintaxis y las excepciones. Las excepciones son una manera de manejar errores y situaciones inesperadas en el código, asegurando un flujo de ejecución más controlado.

Como científico de datos, deberás prestar atención a situaciones como estas para evitar errores o problemas en tus códigos y análisis que puedan afectar tanto la experiencia del usuario como la eficiencia de tu análisis.

Tipos de Excepciones

SyntaxError

Ocurre cuando el analizador detecta un error en la descripción del código. Normalmente, una flecha señala la parte del código que generó el error, como una especie de pista sobre dónde puede haber ocurrido el error.
"""
print(10 / 2

# Salida
#   File "<ipython-input-16-2db3afa07d68>", line 1
#     print(10/2
#               ^
# SyntaxError: unexpected EOF while parsing

"""
Observa que olvidamos cerrar el paréntesis y, por lo tanto, se presentó un error de sintaxis, es decir, de escritura de código.

NameError

Excepción lanzada cuando intentamos utilizar un nombre de algún elemento que no está presente en nuestro código.
"""
raiz = sqrt(100)

# Salida
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# <ipython-input-17-2e14e900fb9f> in <module>
# ----> 1 raiz = sqrt(100)

# NameError: name 'sqrt' is not defined

"""
En este caso, el intérprete no puede aplicar el método de la raíz cuadrada porque no se ha importado junto con la biblioteca math.

IndexError

Excepción lanzada cuando intentamos indexar alguna estructura de datos como lista, tupla o incluso una cadena más allá de sus límites.
"""
lista = [1, 2, 3]
lista[4]

# Salida
# ---------------------------------------------------------------------------
# IndexError                                Traceback (most recent call last)
# <ipython-input-18-f5fe6d922eea> in <module>
#       1 lista = [1, 2, 3]
# ----> 2 lista[4]

# IndexError: list index out of range

"""
Para esta situación, solo tenemos 3 elementos en la lista y tratamos de leer el elemento en la posición 4, que no existe. Recibimos el mensaje de que el índice está fuera de rango.

TypeError

Excepción lanzada cuando un operador o función se aplican a un objeto cuyo tipo es inapropiado.
"""
"1" + 1

# Salida
# ---------------------------------------------------------------------------
# TypeError                                 Traceback (most recent call last)
# <ipython-input-20-ec358fc6499a> in <module>
# ----> 1 "1" + 1

# TypeError: can only concatenate str (not "int") to str

"""
Observa que intentamos "sumar" una cadena con un número entero y esto generó una excepción en nuestro código. Esto ocurrió por 2 razones: el operador de suma se consideró como concatenación porque comenzamos usando una cadena (en este caso, el signo de suma se utiliza para concatenar cadenas), y un valor de tipo entero no se puede concatenar en este tipo de operación.

KeyError

Excepción lanzada cuando intentamos acceder a una clave que no está en el diccionario presente en nuestro código.
"""
estados = {'EM': 1, 'JC': 2, 'OA': 3}
estados["MI"]

# Salida
# ---------------------------------------------------------------------------
# KeyError                                  Traceback (most recent call last)
# <ipython-input-22-45729db26889> in <module>
#       1 estados =  {'EM': 1, 'JC': 2, 'OA': 3}
# ----> 2 estados["MI"]

# KeyError: 'MI'

"""
Intentamos acceder a los datos del Estado MI (Michoacán), que no está presente en el diccionario, lanzando así la excepción.

Warning

Excepción lanzada en situaciones en las que necesitamos alertar al usuario sobre algunas condiciones del código. Estas condiciones no necesariamente interrumpen la ejecución del programa, pero pueden lanzar advertencias sobre el uso de módulos obsoletos, o que pueden ser obsoletos en futuras actualizaciones, o también para cambios que pueden repercutir en alguna parte del código.

Es importante recordar que, en el caso de los Warnings, pueden ser ignorados o tratados como excepciones.
"""
import numpy as np

a = np.arange(5)
a / a  # presenta una advertencia

# Salida
# <ipython-input-23-93a37b275923>:4: RuntimeWarning: invalid value encountered in true_divide
#   a / a  # presenta una advertencia
# array([nan,  1.,  1.,  1.,  1.])

# Intentamos dividir cero por cero. En un array Numpy, que es esta
#   estructura en la salida de la consola, este resultado genera un
#   valor nan (Not a Number). Es decir, puedes seguir con la ejecución
#   del programa, pero es probable que necesites procesar los datos
#   para poder utilizar este array en alguna operación más adelante.


"""
4.2 RAISE
Otra forma de trabajar con las excepciones en tu código, es generando
    tus propias excepciones para determinados comportamientos que
    deseas en tu código.

Para ello, utilizamos la palabra clave raise junto al tipo de excepción
    que se desea mostrar y el mensaje que será exhibido.

raise NombreDelError("Mensaje deseado.")

SITUATION 15
Creaste una función para calcular el promedio de un estudiante en una
    determinada materia pasando en una lista las notas de este
    estudiante.

Pretendes tratar 2 situaciones:
    + Si la lista posee un valor no numérico el cálculo de promedio no será
        ejecutado y un mensaje de "No fue posible calcular el promedio
        del(la) estudiante. Solo se admiten valores numéricos!" será
        exhibido.

    + En caso que la lista tenga más de 4 notas, surgirá una excepción del
        tipo ValueError informando que "La lista no puede poseer más de 4
        notas."

Un texto avisando que "La consulta ha concluído." debe ser mostrado
    independientemente de si surgió o no alguna excepción.
"""
raise NombreDelError("Mensaje deseado")
def promedio(lista: list=[0]) -> float:
    """
    Función para calcular el promedio de notas en una lista

    Params:
        @list lista=default[0] "Lista con las notas para calcular el promedio"
    Return
        @float                 "Promedio calculado"
    """
    calculo = sum(lista) / len(lista)
    if len(lista) > 4:
        raise ValueError("La lista no pued poseer más de 4 notas")
    return calculo


notas = [6, 7, 8, 9, 10]
resultado = promedio(notas)
resultado

notas = [6, 7, 8, 9, "10"]
resultado = promedio(notas)
resultado

# Va a fallar tanto por tamaño como por el tipo de dato
try:
    notas = [6, 7, 8, 9, "10"]
    resultado = promedio(notas)
    print(resultado)
# El orden que se evaluan los excepts va a depender de la hierarchy de los excepts
except ValueError as e:
    print(e)
except TypeError:
    print("No fue posible calcular el promedio del(de la) estudiante. Solo se admiten valores númericos")
else:
    print(f"Las notas del(de la) estudiante son: {resultado}")
finally:
    print("La consulta ha concluido")

# Correcto con solo 4 valores int
try:
    notas = [6, 7, 8, 9]
    resultado = promedio(notas)
    print(resultado)
# El orden que se evaluan los excepts va a depender de la hierarchy de los excepts
except ValueError as e:
    print(e)
except TypeError:
    print("No fue posible calcular el promedio del(de la) estudiante. Solo se admiten valores númericos")
else:
    print(f"Las notas del(de la) estudiante son: {resultado}")
finally:
    print("La consulta ha concluido")
