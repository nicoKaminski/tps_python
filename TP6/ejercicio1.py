# Ejercicio 1
# Crear una clase Guerrero que sea reciba como atributos:
# ● Nombre del guerrero.
# ● Vida del guerrero.
# ● Ataque del guerrero.
# ● Arma.
# Como métodos deberá tener:
# ● __str__.
# ● Atacar.
# ● Mejorar arma. (Deberá mejorar la categoría del arma)
# El atributo Arma será otra clase que tendrá los siguientes atributos:
# ● Tipo de arma.
# ● Ataque del arma.
# ● Categoria del arma.
# y la clase Arma tendrá los siguientes métodos:
# ● __str__.
# ● Mejorar categoria. (Deberá aumentar el daño del arma)
# Una vez creadas ambas clases, deberá crear dos guerreros, uno será “John Snow” y el
# otro será un “caminante blanco” y deberá hacer que “John Snow” ataqué al caminante blanco.

class Guerrero:
    def __init__(self, nombre, vida, ataque, arma):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.arma = arma
    
    def __str__(self):
        return f"Guerrero: {self.nombre} \nVida: {self.vida} \nAtaque: {self.ataque} \n {self.arma}"
    
    def atacar(self, enemigo):
        danio_total = self.ataque + self.arma.ataque
        enemigo.vida -= danio_total
        print(f"{self.nombre} ataca a {enemigo.nombre} con {self.arma.tipo} causando {danio_total} de daño!")
    
    def mejorar_arma(self):
        self.arma.mejorar_categoria()

class Arma:
    def __init__(self, tipo, ataque, categoria):
        self.tipo = tipo
        self.ataque = ataque
        self.categoria = categoria
    
    def __str__(self):
        return f"Arma: {self.tipo} \nAtaque: {self.ataque} \nCategoria: {self.categoria}"
    
    def mejorar_categoria(self):
        self.ataque += 5
        print(f"El arma ha mejorado su categoria y ahora tiene {self.ataque} de ataque")

# Crear las armas
espada_acero = Arma("Espada de acero", 30, "cuerpo a cuerpo")
lanza_hielo = Arma("Lanza de hielo", 25, "Cuerpo a cuerpo")
Pistola_corta = Arma("Pistola corta", 40, "A distancia")

# Crear los guerreros
Guerrero1 = Guerrero("John Snow", 100, 20, espada_acero)
Guerrero2 = Guerrero("Caminante Blanco", 120, 15, lanza_hielo)

# Mostrar info y atacar
print(Guerrero1, "\n")
print(Guerrero2, "\n")

Guerrero1.atacar(Guerrero2)

print(Guerrero2, "\n")