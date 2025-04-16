import os
import json

carpeta = os.path.dirname(__file__)  # Carpeta actual donde está el script
archivo = os.path.join(carpeta, "contactos.json")


#si el archivo no existe lo creamos vacio:
if not os.path.exists(archivo): #os.path.exists(archivo)  revisa si el archivo existe.
    with open(archivo, "w") as f:
        json.dump([], f, indent=4) #json.dump([], f): guarda una lista vacía en el archivo, como []
        print("Archivo creado vacio")
else:
    print("El archivo ya existe")

#Funcion para pedir datos a usuario
def agregar_contacto():
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el telefono: ")
    email = input("Ingrese el email: ")
    nuevo_contacto = {"nombre": nombre, "telefono": telefono, "email": email}
    
    #cargar contactos actuales
    with open(archivo, "r") as f:
        contactos = json.load(f)    #Abre el archivo y lee la lista actual de contactos.
    
    #agregar nuevo contacto
    contactos.append(nuevo_contacto)
    
    #guardar contactos actualizados
    with open(archivo, "w") as f:
        json.dump(contactos, f, indent=4)
    
    print("\n Contacto agregado con exito!")

#Funcion para mostrar contactos
def mostrar_contactos():
    with open(archivo, "r") as f:
        contactos = json.load(f)
    
    if not contactos:
        print("\n No hay contactos en la agenda")
    else:
        for contacto in contactos:
            print("Nombre:", contacto["nombre"])
            print("Telefono:", contacto["telefono"])
            print("Email:", contacto["email"])
            print()

#Funcion para hacer menu
def menu():
    while True:
        print("\n --- CONTACTOS --- \n")
        print("1. Agregar contacto")
        print("2. Mostrar contactos")
        print("3. Salir")
        opcion = input("Ingrese una opcion: ")
        
        if opcion == "1":
            agregar_contacto()
        elif opcion == "2":
            print("\n Agenda \n")
            mostrar_contactos()
        elif opcion == "3":
            print("Gracias por usar la agenda")
            break
        else:
            print("Opcion no valida")

#Llamamos a la funcion
menu()