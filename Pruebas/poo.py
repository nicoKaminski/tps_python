# 1. Ejemplo simple: creación de clases y objetos

def ejemplo_simple():
    class Perro:
        def __init__(self, nombre, raza):
            self.nombre = nombre
            self.raza = raza

        def ladrar(self):
            print(f"{self.nombre} dice: ¡Guau!")

    mi_perro = Perro("Rex", "Labrador")
    mi_perro.ladrar()  # Muestra: Rex dice: ¡Guau! (se llama al método ladrar)


# 2. Encapsulamiento: atributos privados y métodos de acceso

def encapsulamiento():
    class Animal:
        def __init__(self, nombre, edad):
            self.__nombre = nombre  #Los atributos tienen doble guión bajo __: eso los vuelve privados.
            self.__edad = edad      # atributo privado

        def get_nombre(self):
            return self.__nombre

        def set_nombre(self, nuevo):
            self.__nombre = nuevo

    a = Animal("Toby", 5)
    print(a.get_nombre())  # Muestra: Toby
    a.set_nombre("Max")
    print(a.get_nombre())  # Muestra: Max


# 3. Abstracción: uso de clases abstractas
from abc import ABC, abstractmethod

def abstraccion():
    class Animal(ABC):  # ABC convierte esta clase en abstracta (es decir: no se puede usar directamente.)
        def __init__(self, nombre):
            self.nombre = nombre

        @abstractmethod  # obliga a las subclases a implementar este método
        def hacer_sonido(self):
            pass
        
        def dormir(self):  # método NO obligatorio
            print(f"{self.nombre} está durmiendo")    

    class Perro(Animal):
        def hacer_sonido(self):
            print(f"{self.nombre} dice: ¡Guau!")

    p = Perro("Rex")
    p.hacer_sonido()  # Muestra: Rex dice: ¡Guau!
    p.dormir()        # Muestra: Rex está durmiendo


# 4. Herencia: Permite crear una nueva clase basada en otra.

def herencia():
    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre

    class Perro(Animal):  # Perro hereda de Animal. así que no necesita volver a escribir el __init__
        def hablar(self):
            print(f"{self.nombre} dice: ¡Guau!")

        def dormir(self): # Nuevo metodo, solo para Perro
            print(f"{self.nombre} esta durmiendo") 

    class Gato(Animal):
        def hablar(self):
            print(f"{self.nombre} dice: ¡Miau!")

    p = Perro("Rex")
    g = Gato("Mishi")
    p.hablar()
    p.dormir()
    g.hablar()


# 5. Polimorfismo: diferentes clases con métodos del mismo nombre

def polimorfismo():
    class Animal:
        def hablar(self):
            pass

    class Perro(Animal):
        def hablar(self):
            print("Guau")

    class Gato(Animal):
        def hablar(self):
            print("Miau")

    def hacer_hablar(animal):
        animal.hablar()  # El método se adapta según la clase del objeto

    # Aunque hablar se llama igual en Perro y Gato, cada uno hace algo distinto
    hacer_hablar(Perro())  # Muestra: Guau
    hacer_hablar(Gato())   # Muestra: Miau



# 6. Métodos especiales y decoradores

def metodos_especiales():
    class Animal:
        especie = "Mamífero"

        def __init__(self, nombre):
            self._nombre = nombre

        @property  # permite acceder como si fuera un atributo
        def nombre(self):
            return self._nombre

        @nombre.setter  # Permite asignar con validación
        def nombre(self, nuevo):
            self._nombre = nuevo

        def __str__(self):  # cambia lo que se muestra cuando hacés print(objeto).
            return f"Animal llamado {self._nombre}"

        @staticmethod
        def saludar():  # No recibe ni self (instancia) ni cls (clase), funciona como una función normal dentro de la clase
            print("Hola desde Animal")

        @classmethod
        def crear_anonimo(cls):  # cls es la clase misma (Animal). Acá se usa para crear una instancia.
            return cls("SinNombre")

    a = Animal("Toby")
    print(a)  # Animal: Toby
    a.nombre = "Max"  # Se llama al setter
    print(a.nombre)   # Max (se llama al getter)
    Animal.saludar()  # Hola desde Animal (no usa self ni cls)
    b = Animal.crear_anonimo()  # se crea un Animal con nombre "SinNombre"
    print(b)

# 7. Relación de dependencia (usa): una clase usa otra sin contenerla

def dependencia():
    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre

    class Veterinario:
        def vacunar(self, animal): # Usa la clase Animal sin ser parte de ella
            print(f"Vacunando a {animal.nombre}")  # usa al objeto, pero no lo contiene

    vet = Veterinario()
    gato = Animal("Mishi")
    vet.vacunar(gato)  # Muestra: Vacunando a Mishi


# 8. Agregación y composición

def agregacion_composicion():
    class Corazon:
        def __init__(self):
            print("Corazón creado")

    class Ropa:
        def __init__(self):
            self.estado = "sin ropa"

    class Dueño:
        def __init__(self, nombre):
            self.nombre = nombre
            self.animales = []  # Agregación: se pasa desde fuera

    class Animal:
        def __init__(self):
            self.corazon = Corazon()  # composición: el corazón es parte del animal (Si muere el animal, muere el corazón.)

    class Zoologico:
        def __init__(self):
            self.animales = [] # Agregación: El zoológico agrega animales, pero no los crea

        def agregar_animal(self, animal):
            self.animales.append(animal)  # agregación: animales independientes

    a = Animal()
    zoo = Zoologico()
    zoo.agregar_animal(a)


# 9. Inspección de objetos: Son formas de mirar por dentro de un objeto en tiempo de ejecución.

def inspeccion_objetos():
    class Animal:
        def __init__(self, nombre):
            self.nombre = nombre
            self.edad = 3

        def hablar(self):
            print("Hola")

    a = Animal("Toby")
    print(hasattr(a, "nombre"))  # True, porque el objeto tiene el atributo nombre
    print(getattr(a, "edad", 0))  # Devuelve el valor de edad si existe, sino 0
    print(isinstance(a, Animal))  # True, porque 'a' es una instancia de Animal


#INICIO
while True:
    print("\nSeleccione el ejercicio a ejecutar:")
    print("N° - selecciona el ejercicio deseado")
    print("0 - Salir")

    opcion = input("Ingrese el número del ejercicio: ")

    if opcion == "1":
        ejemplo_simple()
    elif opcion == "2":
        encapsulamiento()
    elif opcion == "3":
        abstraccion()
    elif opcion =="4":
        herencia()
    elif opcion =="5":
        polimorfismo()
    elif opcion =="6":
        metodos_especiales()
    elif opcion =="7":
        dependencia()    
    elif opcion =="8":
        agregacion_composicion()  
    elif opcion =="9":
        inspeccion_objetos()
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")