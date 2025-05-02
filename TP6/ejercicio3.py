# Ejercicio 3
# Extiende el programa anterior que implementa figuras geométricas con los siguientes requisitos:
# Clase FiguraBidimensional: Crea una nueva clase llamada FiguraBidimensional que debe contener
#        un método clonar(self) que devuelve una copia de la instancia (puedes usar copy para realizar la clonación).
# Clase FiguraTridimensional: Crea una clase diferente llamada FiguraTridimensional, que debe incluir 
#       un método calcular_volumen(self) que deberá ser implementado por las clases derivadas que representen figuras tridimensionales.
# Crear la clase Derivada Cubo: Crea una nueva clase llamada Cubo que derive de
#       FiguraGeometrica FiguraBidimensional, FiguraTridimensional. Esta clase debe tener un constructor que acepte el lado del cubo.
# Modificar la clase Circulo para que herede ahora también de FiguraBidimensional.

import copy, math
from ejercicio2 import FiguraGeometrica, Circulo, Rectangulo, Triangulo

class FiguraBidimensional():
    def clonar(self):
        return copy.deepcopy(self) # hace copia del objeto

class FiguraTridimensional():
    def calcular_volumen(self):
        pass

class Cubo(FiguraGeometrica, FiguraBidimensional, FiguraTridimensional):
    def __init__(self, lado):
        self.lado = lado

    def calcular_volumen(self):
        return self.lado ** 3
    
    def perimetro(self):
        return 12 * self.lado
    
    def area(self):
        return 6 * self.lado ** 2

class Circulo(FiguraGeometrica, FiguraBidimensional):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        return 2 * math.pi * self.radio
    
# Crear un cubo
cubo1 = Cubo(3)
print(f"Área del cubo: {cubo1.area()}")
print(f"Perímetro del cubo: {cubo1.perimetro()}")
print(f"Volumen del cubo: {cubo1.calcular_volumen()}", "\n")

# Clonar el cubo
cubo2 = cubo1.clonar()
print(f"Área del cubo clonado: {cubo2.area()}")
print(f"Perímetro del cubo clonado: {cubo2.perimetro()}")
print(f"Volumen del cubo clonado: {cubo2.calcular_volumen()}", "\n")

# Crear y clonar un círculo
circulo1 = Circulo(5)
circulo2 = circulo1.clonar()
print(f"Área del círculo 1: {circulo1.area()}")
print(f"Área del círculo clonado: {circulo2.area()}")