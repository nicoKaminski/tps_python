#Ejercicio 1
# A partir de una lista de palabras, creá una lista con aquellas que tengan más de 4 letras, usando comprensión de listas. 
# palabras = ["sol", "luna", "mar", "montaña", "río", "estrella"]
# Resultado esperado: ["montaña", "estrella"]
def ejercicio1():
    print("\n", "Ejercicio 1", "\n")
    palabras = ["sol", "luna", "mar", "montaña", "río", "estrella"]
    resultado = [palabra for palabra in palabras if len(palabra) > 4]
    print("Palabras con mas de 4 letras:", resultado)

#Ejercicio 2
# Generar una matriz de 3x3 con los números del 1 al 9 usando comprensión de listas anidadas.
# Resultado esperado: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def ejercicio2():
    print("\n", "Ejercicio 2", "\n")
    matriz = [[i + j for j in range(1, 4)] for i in range(0, 7, 3)]
    print(matriz)

#Ejercicio 3
# Implementar una función que reciba una cadena que indique el día de la semana y devuelva
# si es “Laboral”, “Fin de semana” o “No válido”. Usar match
def ejercicio3():
    print("\n", "Ejercicio 3", "\n")
    dia = input("Ingrese el dia: ")
    if dia == "lunes" or dia == "martes" or dia == "miercoles" or dia == "jueves" or dia == "viernes":
        tipo = 1
    elif dia == "sabado" or dia == "domingo":
        tipo = 2
    match tipo:
        case 1:
            print("El dia es Laboral")
        case 2:
            print("El dia es Fin de semana")
        case _:
            print("No es un dia valido")

#Ejercicio 4
# Dado un diccionario que representa un cliente con posibles claves "nombre", "edad" y "profesion". para identificar si:
# ● Es mayor de edad (edad >= 18)
# ● Es menor
# ● No se indica la edad
# crear la función clasificar_cliente(cliente)
# Ejemplos: {"nombre": "Ana", "edad": 17} → "Menor de edad"
#           {"nombre": "Carlos", "edad": 21, "profesion": "médico"} → "Mayor de edad"
#           {"nombre": "Lucía"} → "Edad no especificada"

def ejercicio4():
    print("\n", "Ejercicio 4", "\n")
    def ingreso_cliente():
        nombre = input("Ingrese el nombre del cliente: ")
        edad = input("Ingrese la edad del cliente: ")
        profesion = input("Ingrese la profesion del cliente: ")

        cliente = {
            "nombre": nombre,
            "edad": edad,
            "profesion": profesion
        }
        return cliente

    def clasificar_cliente(cliente):
        if "edad" in cliente:
            if int(cliente["edad"]) >= 18:
                return "Mayor de edad"
            else:
                return "Menor de edad"
        else:
            return "Edad no especificada"

    cliente = ingreso_cliente()
    print(clasificar_cliente(cliente))

#Ejercicio 5
# Dada una lista de palabras, usá enumerate para obtener una lista con los índices de las
# palabras que tienen más de 5 letras.palabras = ["hola", "murciélago", "sol", "universo"]
# Resultado esperado: [1, 3]
def ejercicio5():
    print("\n", "Ejercicio 5", "\n")
    palabras = ["hola", "murciélago", "sol", "universo"]
    indices = [i for i, palabra in enumerate(palabras) if len(palabra) > 5]
    print("Indices de palabras con mas de 5 letras:", indices)

#Ejercicio 6
# Dadas dos listas del mismo tamaño, usá zip para obtener una lista con la suma de los elementos correspondientes.
# lista1 = [1, 2, 3]  -  lista2 = [4, 5, 6]  -  Resultado esperado: [5, 7, 9]
def ejercicio6():
    print("\n", "Ejercicio 6", "\n")
    lista1 = [1, 2, 3]
    lista2 = [4, 5, 6]
    suma = [x+y for y, x in zip(lista1, lista2)]
    print(suma)


#Ejercicio 7
# Dadas dos listas, una con nombres y otra con apellidos, usá zip para generar una lista con
# los nombres completos.
# nombres = ["Ana", "Luis", "Carla"]
# apellidos = ["Pérez", "Gómez", "Ruiz"]
# Resultado esperado: ["Ana Pérez", "Luis Gómez", "Carla Ruiz"]
def ejercicio7():
    print("\n", "Ejercicio 6", "\n")
    nombres = ["Ana", "Luis", "Carla"]
    apellidos = ["Pérez", "Gómez", "Ruiz"]
    dic = [i + ", " + j for i, j in zip (nombres, apellidos)]
    print(dic)


#INICIO
while True:
    print("\nSeleccione el ejercicio a ejecutar:")
    print("N° - selecciona el ejercicio deseado")
    print("0 - Salir")

    opcion = input("Ingrese el número del ejercicio: ")

    if opcion == "1":
        ejercicio1()
    elif opcion == "2":
        ejercicio2()
    elif opcion == "3":
        ejercicio3()
    elif opcion =="4":
        ejercicio4()
    elif opcion =="5":
        ejercicio5()
    elif opcion =="6":
        ejercicio6()
    elif opcion =="7":
        ejercicio7()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")