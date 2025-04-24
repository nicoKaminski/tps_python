"""
Dada una lista de palabras, usar filter y lambda para quedarse solo con aquellas cuya
longitud sea mayor o igual a 5 caracteres.
#Ejemplo: palabras = ["sol", "estrella", "luna", "universo", "mar"]
#salida esperada: ["estrella", "universo"]
"""
def ejercicio1():
    print("\n", "Ejercicio 1", "\n")
    palabras = ["sol", "estrella", "luna", "universo", "mar"]
    resultado = list(filter(lambda x: len(x) >= 5, palabras))
    print("Palabras con mas de 5 letras:", resultado)

"""
Cree una función que reciba dos parámetros: (x, y) y retorne la suma de ambos
parámetros. Cree una tupla de números (1, 2,3,4) Utilice la función reduce para que se
sumen todos los elementos.
# Ejemplo tupla= (1, 2,3,4)
# salida esperada: 1
"""
def ejercicio2():
    from functools import reduce
    print("\n", "Ejercicio 2", "\n")
    tupla = (1, 2, 3, 4)
    resultado = reduce(lambda x, y: x + y, tupla)
    print("La suma de los elementos de la tupla es:", resultado)

"""
Usar reduce (de functools) y lambda para calcular la suma de todos los números de una lista.
#Ejemplo: numeros = [3, 7, 1, 9, 4]
#salida esperada: 24
"""
def ejercicio3():
    from functools import reduce
    print("\n", "Ejercicio 3", "\n")
    numeros = [3, 7, 1, 9, 4]
    resultado = reduce(lambda x, y: x + y, numeros)
    print("La suma de los elementos de la lista es:", resultado)

"""
Filtrar solo los números pares.
Multiplicar cada uno por sí mismo (elevar al cuadrado).
Reducir la lista resultante para obtener el producto de todos sus elementos.
#Ejemplo: nums = [2, 3, 4, 5, 6]
Pares → [2, 4, 6]
Cuadrados → [4, 16, 36]
Producto → 4 * 16 * 36 = 2304
#salida esperada: 2304
"""
def ejercicio4():
    from functools import reduce
    print("\n", "Ejercicio 4", "\n")
    nums = [2, 3, 4, 5, 6]
    pares = list(filter(lambda x: x % 2 == 0, nums))
    cuadrados = list(map(lambda x: x**2, pares))
    producto = reduce(lambda x, y: x * y, cuadrados)
    print("El producto de los cuadrados de los pares de la lista es:", producto)

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
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")