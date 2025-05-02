# Ejercicio 2
# Crear la siguiente jerarquía de clases para representar diferentes figuras geométricas utilizando herencia, clases abstractas y polimorfismo.
# 1. Clase Abstracta: Define una clase abstracta llamada FiguraGeometrica que contenga los siguientes métodos abstractos:
# ○ area(self): devuelve el área de la figura.
# ○ perimetro(self): devuelve el perímetro de la figura.
# 2. Clases Derivadas:
# ○ Clase Circulo: Deriva de FiguraGeometrica e implementa los métodos area y perimetro. 
#                  El constructor debe recibir el radio del círculo.
# ○ Clase Rectangulo: Deriva de FiguraGeometrica e implementa los métodos area y perimetro. 
#                  El constructor debe recibir la base y la altura del rectángulo.
# ○ Clase Triangulo: Deriva de FiguraGeometrica e implementa los métodos area y perimetro. 
#                  El constructor debe recibir los tres lados del triángulo.
# 3. Polimorfismo: Crea una lista de diversas figuras geométricas 
#                 (por ejemplo, uno de cada tipo: Circulo, Rectangulo, Triangulo) y escribe un bucle que recorra la lista
# llamando a los métodos area y perimetro de cada figura, mostrando los resultados

from abc import ABC, abstractmethod
import math

class FiguraGeometrica(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return 2 * math.pi * self.radio

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

class Triangulo(FiguraGeometrica):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def area(self):
        semiPerimetro = (self.lado1 + self.lado2 + self.lado3) / 2
        return math.sqrt(semiPerimetro * (semiPerimetro - self.lado1) * (semiPerimetro - self.lado2) * (semiPerimetro - self.lado3))

    def perimetro(self):
        return self.lado1 + self.lado2 + self.lado3

# Usando 
figuras = [Circulo(5), Rectangulo(4, 6), Triangulo(3, 4, 5)]

for figura in figuras:
    print(type(figura).__name__, "Area:", figura.area())
    print(type(figura).__name__, "Perimetro:", figura.perimetro(), "\n")