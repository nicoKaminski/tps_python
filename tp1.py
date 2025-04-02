#Ejercicio 1 
#Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidad constante (m/s) durante un tiempo t (s), 
# considerar que es un MRU (Movimiento Rectilíneo Uniforme) 𝑫 = 𝑽 𝒙 𝑻 

print("\n", "Ejercicio 1", "\n")
velocidad = int(input("ingrese la velocidad: "))
tiempo = int(input("Ingrese el tiempo: "))
distancia = velocidad * tiempo

print("la velocidad es: ", velocidad, "y el tiempo es: ", tiempo, "\n",  "la distancia recorrida es: ", distancia)

#Ejercicio 2
# Se necesita obtener el promedio simple de un estudiante a partir de sus tres notas parciales N1, N2 y N3.

print("\n", "Ejercicio 2", "\n")
n1=int(input("Ingrese nota 1: "))
n2=int(input("Ingrese nota 2: "))
n3=int(input("Ingrese nota 3: "))

promedio = (n1+n2+n3)/3

print("El promedio es: ", promedio)

#Ejercicio 3
# Se necesita elaborar un algoritmo que solicite el número de respuestas correctas, incorrectas y en blanco, 
# correspondientes a un postulante, y muestre su puntaje final considerando que por cada respuesta correcta tendrá 3 puntos, 
# respuestas incorrectas tendrá -1 y respuestas en blanco tendrá 0.

print("\n", "Ejercicio 3", "\n")
correctas = int(input("Ingrese la cantidad de respuestas correctas: "))
incorrectas = int(input("Ingrese la cantidad de respuestas incorrectas: "))
enblanco = int(input("Ingrese la cantidad de respuestas en blanco: "))

puntaje = correctas * 3 - incorrectas - enblanco * 0

print("El puntaje es: ", puntaje)


#Ejercicio 4
# Calcular el perímetro y área de un rectángulo, ingresar los datos por consola.

print("\n", "Ejercicio 4", "\n")
baseRec = int(input("Ingrese la base del rectangulo: "))
alturaRec = int(input("Ingrese la altura del rectangulo: "))

Area = baseRec * alturaRec
Perimetro = 2 * (baseRec + alturaRec)

print("El area del rectangulo es: ", Area)
print("El perimetro del rectangulo es: ", Perimetro)

#Ejercicio 5
# Calcular el perímetro y área de un triángulo, ingresar los datos por consola.

print("\n", "Ejercicio 5", "\n")
baseTria= int(input("Ingrese la base: "))
alturaTria= int(input("Ingrese la altura: "))

AreaTria = baseTria * alturaTria / 2
PerimetroTria = baseTria + baseTria + baseTria

print("El area del triangulo es: ", AreaTria)
print("El perimetro (tomando que es un triangulo equilatero) es: ", PerimetroTria)

#Ejercicio 6
# Calcular el perímetro y área de un triángulo, ingresar los datos por consola. Antes de realizar los cálculos, verificar que los datos corresponden a un triángulo.

print("\n", "Ejercicio 6", "\n")
lado1 = int(input("Ingrese el lado 1: "))
lado2 = int(input("Ingrese el lado 2: "))
lado3 = int(input("Ingrese el lado 3: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    PerimetroTria = lado1 + lado2 + lado3
    semiPerimetro = PerimetroTria / 2
    AreaTria = (semiPerimetro * (semiPerimetro - lado1) * (semiPerimetro - lado2) * (semiPerimetro - lado3)) ** 0.5
    print("El area del triangulo es: ", AreaTria)
    print("El perimetro del triangulo es: ", PerimetroTria)
else:
    print("Los lados no corresponden a un triangulo")


#Ejercicio 7
# Calcular el perímetro y área de un círculo. Tener en cuenta que PI es una constante.
print("\n", "Ejercicio 7", "\n")
radio = int(input("Ingrese el radi del circulo: "))
PI = 3.1416
AreaCirculo = PI * radio ** 2
PerimetroCirculo = 2 * PI * radio

print("El area del circulo es: ", AreaCirculo)
print("El perimetro del circulo es: ", PerimetroCirculo)

#Ejercicio 8
# Evaluar si dos N° solicitados por consola, son iguales, o en caso contrario identificar si el primero es mayor o menor que el segundo.
print("\n", "Ejercicio 8", "\n")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

if num1 == num2:
    print("Los numeros son iguales")
elif num1 > num2:
    print("El primer numero ", num1, " es mayor que ", num2)
else:
    print("El segundo numero ", num2, " es mayor que ", num1)


#Ejercicio 9
# Determinar si el alumno está Promocionado (nota mayor o igual a 80), Regular (nota mayor o igual a 60 PERO menor que 80) o Desaprobado (nota menor a 60)
print("\n", "Ejercicio 9", "\n")
nota = int(input("Ingrese la nota del alumno: "))

if nota<10:
    nota=nota*10

if nota >= 80:
    print("El alumno esta promocionado")
elif nota >= 60:
    print("El alumno esta regular")
else:
    print("El alumno esta desaprobado")


#Ejercicio 10
# Ingresar por teclado un número entre 1 y 7, mostrar a qué día de la semana corresponde el número ingresado. 
# Por ejemplo, si ingresa 1, muestra DOMINGO. Usar match. 
print("\n", "Ejercicio 10", "\n")
dia = int(input("Ingrese un numero del 1 al 7: "))

match dia:
    case 1:
        print("El numero ", dia, " es Domingo")
    case 2:
        print("El numero ", dia, " es Lunes")
    case 3:
        print("El numero ", dia, " es Martes")
    case 4:
        print("El numero ", dia, " es Miercoles")
    case 5:
        print("El numero ", dia, " es Jueves")
    case 6:
        print("El numero ", dia, " es Viernes")
    case 7:
        print("El numero ", dia, " es Sabado")
    case 8:
        print("El numero ", dia, " es osvaldo! XD")
    case _:
        print("El numero ", dia, " no es un dia")

#Ejercicio 11
# Idem al ejercicio 10, pero simulando match con un diccionario. 
print("\n", "Ejercicio 11", "\n")
dia = int(input("Ingrese un numero del 1 al 7: "))

dias={
    1:"Domingo",
    2:"Lunes",
    3:"martes",
    4:"Miercoles",
    5:"Jueves",
    6:"Viernes",
    7:"Sabado",
    8:"Osvaldo XD"
}

print("El numero ", dia, "corresponde al dia ", dias[dia])

