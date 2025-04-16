import os

# Escribir una función que pida dos números n y m entre 1 y 10, lea el fichero tabla-n.txt con
# la tabla de multiplicar de ese número, y muestre por pantalla la línea m del fichero. Si el
# fichero no existe debe mostrar un mensaje por pantalla informando de ello.

def crear_tablas():
         # 1. Carpeta base de tp4
    carpeta_actual = os.path.dirname(__file__)
         # 2. Carpeta donde guardar las tablas
    carpeta_tablas = os.path.join(carpeta_actual, "tablas") 
         # 3. Si no existe la carpeta "tablas"...
    if not os.path.exists(carpeta_tablas):
        os.mkdir(carpeta_tablas)
        print("Carpeta 'tablas' creada.")
    else:
        print("La carpeta 'tablas' ya existe.")
         # 4. Crear los archivos tabla-1.txt hasta tabla-10.txt
    for n in range(1, 11):
        ruta_archivo = os.path.join(carpeta_tablas, f"tabla-{n}.txt")
        with open(ruta_archivo, "w") as f:
            for i in range(1, 11):
                f.write(f"{n} x {i} = {n * i}\n")
        print(f"Archivo 'tabla-{n}.txt' creado.")
    return carpeta_tablas

def pedir_numero():
    while True:
        try:
            numeroN = int(input("\n Ingrese el número de la tabla: "))
            if 1 <= numeroN <= 10:
                return numeroN
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debe ingresar un número válido.")    

def pedir_linea():
    while True:
        try:
            numeroM = int(input("\n Ingrese el numero a multiplicar: "))
            if 1 <= numeroM <= 10:
                return numeroM
            else:
                print("El número debe estar entre 1 y 10.")
        except ValueError:
            print("Debe ingresar un número válido.")


def mostrar_tabla(carpeta_tablas):
    numeroN = pedir_numero()
    numeroM = pedir_linea()
    archivo = os.path.join(carpeta_tablas, f"tabla-{numeroN}.txt")
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            contenido = f.readlines()
            print(f" \n Tabla de multiplicar del número {numeroN}:")
            print(contenido[numeroM - 1].strip()) #strip para eliminar el salto de linea
    else:
        print(f"El archivo tabla-{numeroN}.txt no existe.")


carpeta = crear_tablas()
mostrar_tabla(carpeta)