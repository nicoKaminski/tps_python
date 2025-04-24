
numeros = [1, 2, 3, 4]

# MAP: transformar cada elemento de una lista

# sin lambda
def al_cuadrado(x):
    return x * x
cuadradosSin = list(map(al_cuadrado, numeros))
print(cuadradosSin)  # [1, 4, 9, 16]

# con lambda
cuadradosCon = list(map(lambda x: x**2, numeros))
print(cuadradosCon)  # [1, 4, 9, 16]



#FILTER: quedarte solo con los elementos que cumplen una condición

# sin lambda
def es_par(x):
    return x % 2 == 0
pares = list(filter(es_par, numeros))
print(pares)  # [2, 4]

# con lambda
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # [2, 4]



#REDUCE: combinar todos los elementos de una lista en uno solo
from functools import reduce #Primero importás functools y luego reduce.

# sin lambda
def sumar(x, y):
    return x + y
suma = reduce(sumar, numeros)
print(suma)  # 10

# con lambda
suma = reduce(lambda x, y: x + y, numeros)
print(suma)  # Resultado: 10
"""
x + y = 1 + 2 = 3
x + y = 3 + 3 = 6
x + y = 6 + 4 = 10
x siempre es el acumulador - y es el siguiente valor de la lista
"""

# MAP, FILTER Y REDUCE JUNTOS

nombres = ["ana", "juan", "marcos", "eva"]

# 1. Quiero convertirlos a mayúsculas
mayusculas = list(map(lambda x: x.upper(), nombres))

# 2. Quiero filtrar solo los que tienen más de 3 letras
largos = list(filter(lambda x: len(x) > 3, mayusculas))

# 3. Quiero juntar todos en una sola cadena separada por comas
unidos = reduce(lambda x, y: x + ", " + y, largos)

print(unidos)