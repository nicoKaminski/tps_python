# Ejercicio 1
# Crear una función que calcule y retorne el área de un triángulo, recibe la base y altura
def ejercicio1():
    print("\n", "Ejercicio 1", "\n")
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingrese la altura: "))
    area = base * altura / 2
    print("El area del triangulo es: ", area)


# Ejercicio 2
# Crear una función crear_usuario que reciba nombre, email, y edad (parámetro por defecto 18), y retorne un diccionario con esos datos.
# Luego invocar de la siguiente manera:
# print(crear_usuario("Ana", "ana@gmail.com"))
# print(crear_usuario(email="leo@example.com", nombre="Leo", edad=25))
def ejercicio2():
    print("\n", "Ejercicio 2", "\n")
    def crear_usuario(nombre, email, edad=18):
        return {"nombre": nombre, "email": email, "edad": edad}

    def ingresar_datos():
        nombre = input("Ingrese el nombree: ")
        email = input("Ingrese el email: ")
        edad = input("Ingrese la edad: ")
        return nombre, email, edad
    
    usuario = ingresar_datos()
    print("\n", crear_usuario(*usuario))
    print("\n", "con los datos ingresados", "\n")
    print(crear_usuario("Ana", "ana@gmail.com"))
    print(crear_usuario(email="leo@example.com", nombre="Leo", edad=25))

# Ejercicio 3
# Crear una función sumar_todo que acepte cualquier cantidad de números y retorne la suma.
def ejercicio3():
    print("\n", "Ejercicio 3", "\n")
    def sumar_todo(*args):
        return sum(args)
    print(sumar_todo(1, 2, 3, 4, 5))

# Ejercicio 4
# Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.
def ejercicio4():
    print("\n", "Ejercicio 4", "\n")
    def max_de_tres(num1, num2, num3):
        return max(num1, num2, num3)
    
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))
    num3 = int(input("Ingrese el tercer numero: "))
    print("\n", "el mas alto es: ", max_de_tres(num1, num2, num3))

# Ejercicio 5
# Crear una función mostrar_info_usuario que imprima todos los datos que recibe. Utiliza *kwargs.
def ejercicio5():
    print("\n", "Ejercicio 5", "\n")
    def mostrar_info_usuario(**kwargs):
        for clave, valor in kwargs.items():
            print(f"{clave}: {valor}")

    nombre = input("Nombre: ")
    edad = input("Edad: ")
    email = input("Email: ")

    mostrar_info_usuario(nombre=nombre, edad=edad, email=email)


# Ejercicio 6
# Crear una función operar_lista(lista, operacion) que reciba una lista de números
# y una función que defina qué operación aplicar sobre la lista (suma o multipliacr sus elementos). 
# La idea es practicar pasar funciones por parámetro
def ejercicio6():
    print("\n", "Ejercicio 6", "\n")
    def operar_lista(lista, operacion):
        return operacion(*lista)

    def sumar(*args):
        return sum(args)

    def multiplicar(*args):
        resultado = 1
        for num in args:
            resultado *= num
        return resultado

    entrada = input("Ingresá números separados por espacios: ")
    numeros = [int(x) for x in entrada.split()]

    opcion = input("¿Qué querés hacer? (sumar / multiplicar): ")
    if opcion.lower() == "sumar":
        print("Resultado= ", operar_lista(numeros, sumar))
    elif opcion.lower() == "multiplicar":
        print("Resultado= ", operar_lista(numeros, multiplicar))
    else:
        print("Operación no reconocida")

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
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")