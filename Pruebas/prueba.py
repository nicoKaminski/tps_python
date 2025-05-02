# pais = "Argentina"
# print(pais)
# #asi se puede comentar tambien
# dia = input ("ingrese un dia: ")
# numero = int(input("ingrese un numero: "))
# suma = 2+ numero
# print(suma)
# print("hola, ha ingresado el dia: ", dia, "y el numero: ", numero,"y todo suma: ", suma)

# saludo = "Hola_Mundo"
# print(saludo[3::3])

# print(pais.index("e", 0))

# print(pais*3)
# print(len(pais))
# print(min(pais))
# print(max(pais))
# print(pais.upper())
# print(pais.lower())
# print(pais.strip())
# print(pais.replace("a", "A"))

# frase= "esto es una prueba de strings en esto que es python"

# print(frase.find("prueba"))
# print(frase.count("esto"))

# lista = [1,2,3,4,5]
# print(lista)
# lista.append(6)
# print(lista)
# lista.remove(2)
# print(lista)
# print(lista.pop())
# lista.sort()
# print(lista)

# diccionario={
#     "numero": 1,
#     "pais": "Argentina",
#     "ciudad": "Buenos Aires"
# }

# print(diccionario)
# print(diccionario["pais"])
# print("aca imprimo keys ", diccionario.keys())
# print("aca imprimo values ", diccionario.values())

# diccionario["pais"] = "Uruguay"
# print(diccionario)
# print(diccionario["pais"])

"""
def procesar_archivo (nombre):
    f=open (nombre, "r")
    resultado = {i: linea.count("error") for i, linea in enumerate(f) if "error" in linea}
    return resultado

print(procesar_archivo("error.txt"))
"""

"""
def procesar_archivo (nombre):
    with open(nombre, "r") as f:
        lineas = f.readlines()
    resultado = {}
    for i, linea in enumerate(lineas):
        if "error" in linea:
            resultado[i] = linea.count("error")
    return resultado

print(procesar_archivo("error.txt"))
"""

"""
def generador():
    print("Empieza")
    yield 1            # 1ª pausa: devuelve 1
    print("Continúa")
    yield 2            # 2ª pausa: devuelve 2
    print("Termina")
    yield 3            # 3ª pausa: devuelve 3
    print("Sin más yields")

gen = generador()
print(next(gen))      # Imprime "Empieza", luego devuelve 1
print(next(gen))      # Retoma, imprime "Continúa", devuelve 2
print(next(gen))      # Retoma, imprime "Termina", devuelve 3
next(gen)             # Retoma, imprime "Sin más yields", luego StopIteration

print("\n")
for i in generador():
    print(i)
"""
"""
from functools import wraps

def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Antes
        print(f"Iniciando {func.__name__} con args={args}, kwargs={kwargs}")
        resultado = func(*args, **kwargs)  # Llamada original
        # Después
        print(f"{func.__name__} finalizada, resultado={resultado}")
        return resultado
    return wrapper
@log_decorator #Ponemos @log_decorator encima de la definición de la función a decorar:

def saludar(nombre):
    return f"¡Hola, {nombre}!"
print(saludar("Ana"))
# Verás registro de inicio, fin y resultado.
"""

"""
class Casa:
    direccion = None
    ambientes = 0
    color = ""

    def __init__(self, direc, ambien, col):
        self.direccion = direc
        self.ambientes = ambien
        self.color = col

    def mostrar_info(self):
        print(f"Dirección: {self.direccion}")
        print(f"Ambientes: {self.ambientes}")
        print(f"Color: {self.color}")

mi_casa = Casa("Belgrano 123", 4, "amarillo")
mi_casa.mostrar_info()
"""

"""
class ejemplo:
    def __init__(self, valor):
        self.valor = valor

    def mostrar_info(self):
        print(f"El valor es: {self.valor}")

obj = ejemplo(5)
obj.mostrar_info()
"""
"""
objeto = map(lambda x: x*2, [1, 2, 3])
print(list(objeto))
"""
"""
def f(a, b=[]):
    b.append(a)
    return b

print(f(1))
print(f(2))
print(f(3))
"""
def incremento (x, step=1): # PARAMETRO
    count = 0
    count += x * step
    return count

print(incremento(5)) # ARGUMENTO