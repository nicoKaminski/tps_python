#Ejercicio 1
# Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, 
# e imprima por pantalla la frase “Tu índice de masa corporal es <imc>” donde <imc> es el índice de masa corporal calculado
# redondeado con dos decimales. (Usar la función x=round(x,decimales))

def ejercicio1():
    print("\n", "Ejercicio 1", "\n")
    peso = float(input("Ingrese su peso en kg: "))
    estatura = float(input("Ingrese su estatura en metros: "))
    imc = round(peso / estatura ** 2, 2)
    print("Tu indice de masa corporal es: ", imc)

# Ejercicio 2
# Usando funciones de cadenas, contar la cantidad de veces que aparece una subcadena “Hola” en la cadena “Hola, ¿cómo estás? Hola, ¿qué tal?”
def ejercicio2():
    print("\n", "Ejercicio 2", "\n")
    cadena = "Hola, ¿cómo estás? Hola, ¿qué tal?"
    subcadena = "Hola"
    cantidad = cadena.count(subcadena)
    print("La cantidad de veces que aparece la subcadena '", subcadena, "'", "\n", "en la cadena: ", cadena, "\n", "es:", cantidad)

# Ejercicio 3
# Hacer un programa que reciba una cadena de texto y devuelva la misma cadena pero invertida.
def ejercicio3():
    print("\n", "Ejercicio 3", "\n")
    cadena = input("Ingrese una cadena de texto: ")
    invertida = cadena[::-1]
    print("La cadena invertida es:", invertida)

#Ejercicio 4
# Pedir una cadena y dos índices (inicio y fin), y mostrar la subcadena que se encuentra entre esos índices.
def ejercicio4():
    print("\n", "Ejercicio 4", "\n")
    cadena = input("Ingrese una palabra: ")
    inicio = int(input("Ingrese un numero: "))
    fin = int(input("Ingrese otro numero: "))
    resultado = cadena[inicio:fin]
    print("El resultado es: ", resultado)

# Ejercicio 5
# Escribir un programa para una empresa que tiene salas de juegos para todas las edades y
# quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar.
# El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si
# el cliente es menor de 4 años puede entrar gratis, si tiene entre 4 y 18 años debe pagar
# $400 y si es mayor de 18 años, $800.
def ejercicio5():
    print("\n", "Ejercicio 5", "\n")
    edad = int(input("Ingrese su edad: "))
    if 1 <= edad <= 4:
        print("Usted entra gratis mi amigo!")
    elif 5 <= edad <= 18:
        print("Usted debe pagar $400 joven")
    elif edad > 18:
        print("Usted debe pagar $800 por viejo XD")
    else:
        print("Usted aun no ha nacido! que pasa aqui?")

# Ejercicio 6
# La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los
# ingredientes para cada tipo de pizza aparecen a continuación.
# ● Ingredientes vegetarianos: Pimiento y tofu.
# ● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.
# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en
# función de su respuesta le muestre un menú con los ingredientes disponibles para que elija.
# Solo se puede elegir un ingrediente además de la mozzarella y el tomate que están en
# todas las pizzas. Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no
# y todos los ingredientes que lleva.
def ejercicio6():
    print("\n", "Ejercicio 6", "\n")
    respuesta = input("Usted es vegetariano? ")
    if respuesta.lower() == "si":
        print("\n", "Perfecto!, elija un ingrediente:")
        print("\n", "Opcion 1= Pimiento", "\n", "Opcion 2= Tofu")
        ingrediente = int(input("Seleccion: "))
        if ingrediente == 1:
            print("\n", "Preparando una pizza de Pimiento, Salsa y Muzarella")
        else:
            print("\n", "Preparando una pizza de Tofu, Salsa y Muzarella")
    elif respuesta.lower() == "no":
        print("\n", "Perfecto!, elija un ingrediente:")
        print("\n", "Opcion 1= Peperoni", "\n", "Opcion 2= Jamón", "\n", "Opcion 3= Salmón")
        ingrediente = int(input("Seleccion: "))
        match ingrediente:
            case 1:
                print("\n", "Preparando una pizza de Peperoni, Salsa y Muzarella")
            case 2:
                print("\n", "Preparando una pizza de Jamón, Salsa y Muzarella")
            case 3:
                print("\n", "Preparando una pizza de Salmón, Salsa y Muzarella")
            case _:
                print("Esa opcion no esta disponible")
    else:
        print("Veo que no respondio bien, hasta pronto!")

# Ejercicio 7 (usando for)
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
# todos los números impares desde 1 hasta ese número separados por comas.
def ejercicio7():
    print("\n", "Ejercicio 7", "\n")
    numero = int(input("Ingrese un numero entero positivo: "))
    impares = []
    for i in range (1, numero + 1):
        if i % 2 != 0:
            impares.append(str(i))
    print(",".join(impares))


# Ejercicio 8 (usando for)
# Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla
# la cuenta atrás desde ese número hasta cero separados por comas.
def ejercicio8():
    print("\n", "Ejercicio 8", "\n")
    numero = int(input("Ingrese un numero entero positivo: "))
    cuentaAtras = []
    for i in range (numero, -1, -1):
        cuentaAtras.append(str(i))
    print(",".join(cuentaAtras))

# Ejercicio 9 (usando for)
# Escribir un programa que pida al usuario un número entero y muestre por pantalla un
# triángulo rectángulo como el de más abajo, de altura el número introducido.
def ejercicio9():
    print("\n", "Ejercicio 9", "\n")
    numero = int(input("Ingrese un numero entero: "))
    for i in range (1, numero + 1):
        print("*" * i)

# Ejercicio 10 (usando for)
# Escribir un programa que pida al usuario una palabra y luego muestre por pantalla una a
# una las letras de la palabra introducida empezando por la última.
def ejercicio10():
    print("\n", "Ejercicio 10", "\n")
    palabra = input("Ingrese una palabra: ")
    for i in range(len(palabra) - 1, -1, -1):
        print(palabra[i])

# Ejercicio 11 (usando for)
# Escribir un programa que muestre por pantalla las tablas de multiplicar del 1 al 10.
def ejercicio11():
    print("\n", "Ejercicio 11", "\n")
    for i in range (1, 11):
        print(f"\nTabla del {i}")
        for j in range (1, 11):
            print(f"{i} x {j} = {i * j}")

# Ejercicio 12 (usando while)
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el
# usuario escriba “salir” que terminará.
def ejercicio12():
    print("\n", "Ejercicio 12", "\n")
    print("Esto ya lo hice para pedir los ejercicios XD")

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
    elif opcion =="8":
        ejercicio8()
    elif opcion =="9":
        ejercicio9()
    elif opcion =="10":
        ejercicio10()
    elif opcion =="11":
        ejercicio11()
    elif opcion =="12":
        ejercicio12()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")