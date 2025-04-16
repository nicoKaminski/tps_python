import os
# Escribir un programa para gestionar una agenda telefónica con los nombres y los teléfonos
# de los clientes de una empresa. El programa incluir las funciones:
# ● def busca_contacto(archivo, cliente):

'''
Función que devuelve el teléfono de un cliente de un fichero dado. Parámetros:
archivo: Es un fichero con los nombres y teléfonos de clientes.
cliente: Es una cadena con el nombre del cliente.
Devuelve: El teléfono del cliente guardado en el fichero o un mensaje de error si el teléfono o el fichero no existe.
'''
# ● def agrega_contacto(archivo, cliente, telf):
'''
Función que añade el teléfono de un cliente de un fichero dado. Parámetros:
file: Es un fichero con los nombres y teléfonos de clientes.
cliente: Es una cadena con el nombre del cliente.telf: Es una cadena con el teléfono del cliente.
Devuelve: Un mensaje informando sobre si el teléfono se ha añadido o ha habido algún problema.
'''
# ● def elimina_contacto(archivo, cliente):
'''
Función que elimina el teléfono de un fichero dado.
Parámetros:
file: Es un fichero con los nombres y teléfonos de contacto.
cliente: Es una cadena con el nombre del contacto.
Devuelve: Un mensaje informando sobre si el teléfono se ha borrado o ha habido algún problema.
'''
# ● def crea_directorio(archivo):
'''
Función que crea un fichero vacío para guardar una agenda telefónica.
Parámetros:
archivo: Es un fichero.
Devuelve: Un mensaje informando sobre si el fichero se ha creado correctamente o no.
'''
# ● def menu():
'''
Función que presenta un menú con las operaciones disponibles y devuelve la opción seleccionada por el usuario.
Devuelve:
La opción seleccionada por el usuario.
'''
# ● def Principal():
'''
Función que lanza la aplicación
'''
# Crear el fichero con una agenda telefónica si no existe, para consultar el teléfono de un
# cliente, añadir el teléfono de un nuevo cliente y eliminar el teléfono de un cliente. La agenda
# debe estar guardada en el fichero de texto agenda.txt donde el nombre del cliente y su
# teléfono deben aparecer separados por comas y cada cliente en una línea distinta

carpeta = os.path.dirname(os.path.abspath(__file__))
archivo = os.path.join(carpeta, "agenda.txt")

def crea_directorio(archivo):
    if not os.path.exists(archivo):
        with open(archivo, "w") as f:
            f.write("")
        print("Fichero creado con exito")
    else:
        print("El fichero ya existe")

# se usaria asi: crea_directorio("agenda.txt")

def agrega_contacto(archivo, cliente, telf):
    with open(archivo, "r") as f: #abre el archivo
       lineas = f.readlines() #lee las lineas
    
    for linea in lineas:
        nombre_cargado, _ = linea.strip().split(",") #separa el nombre y el telefono
        if nombre_cargado.lower() == cliente.lower(): #compara el nombre cargado con el nombre ingresado
            return f"El contacto {cliente} ya existe en la agenda"  
    
    with open(archivo, "a") as f: #abre el archivo en modo append
        f.write(f"{cliente},{telf}\n") #escribe el nombre y el telefono en la ultima linea
    return f"Contacto {cliente} agregado con exito"

def busca_contacto(archivo, cliente):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    for linea in lineas:
        nombre_cargado, telf_cargado = linea.strip().split(",") #separa el nombre y el telefono
        if nombre_cargado.lower() == cliente.lower(): #compara el nombre cargado con el nombre ingresado
            return f"El teléfono de '{cliente}' es: {telf_cargado}"
    return f"El contacto {cliente} no existe en la agenda"

def elimina_contacto(archivo, cliente):
    with open(archivo, "r") as f:
        lineas = f.readlines()
    
    nueva_lista = []
    eliminado = False
    for linea in lineas:
        nombre_cargado, telf_cargado = linea.strip().split(",") #separa el nombre y el telefono
        if nombre_cargado.lower() == cliente.lower(): # si NO es el cliente buscado
            nueva_lista.append(linea) #agrega la linea a la nueva lista
        else:
            eliminado = True #si es el cliente buscado, cambia el valor de eliminado a True
    
    if eliminado:
        with open(archivo, "w") as f:
            f.writelines(nueva_lista) #escribe la nueva lista en el archivo
        return f"Contacto {cliente} eliminado con exito"
    else:
        return f"El contacto {cliente} no existe en la agenda"
    
def menu():
    print("\n--- AGENDA TELEFÓNICA ---\n")
    print("1. Agregar contacto")
    print("2. Buscar contacto")
    print("3. Eliminar contacto")
    print("4. Salir")
    opcion = int(input("\n Ingrese una opcion: "))
    return opcion

def Principal():
    archivo = "TP4/agenda.txt"
    crea_directorio(archivo)
    while True:
        opcion = menu()
        if opcion == 1:
            cliente = input("Ingrese el nombre del cliente: ").strip()
            telfono = input("Ingrese el telefono del cliente: ").strip()
            resultado = agrega_contacto(archivo, cliente, telfono)
            print(resultado)
        elif opcion == 2:
            cliente = input("Ingrese el nombre del cliente: ").strip()
            resultado = busca_contacto(archivo, cliente)
            print(resultado)
        elif opcion == 3:
            cliente = input("Ingrese el nombre del cliente: ").strip()
            resultado = elimina_contacto(archivo, cliente)
            print(resultado)
        elif opcion == 4:
            print("Gracias por usar la agenda")
            break
        else:
            print("Opcion no valida")

if __name__ == "__main__":
    Principal()
