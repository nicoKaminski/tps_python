# Trabajo Práctico Nro. 6 - Programación Orientada a Objetos

Este directorio contiene los ejercicios correspondientes al Trabajo Práctico número 6 de la materia Python, enfocados en los conceptos de Programación Orientada a Objetos (POO) como clases, objetos, atributos, métodos, herencia, clases abstractas y polimorfismo.

**Estructura de los Ejercicios:**

- **`ejercicio1.py`**: Implementación de clases `Guerrero` y `Arma` con relaciones de composición. Se simula un ataque entre dos guerreros y la mejora de un arma.
- **`ejercicio2.py`**: Definición de una jerarquía de clases para figuras geométricas utilizando una clase abstracta (`FiguraGeometrica`) y clases derivadas (`Circulo`, `Rectangulo`, `Triangulo`) que implementan métodos abstractos. Se demuestra el polimorfismo al iterar sobre una lista de figuras.
- **`ejercicio3.py`**: Extensión del ejercicio 2 introduciendo clases `FiguraBidimensional` (con método `clonar`) y `FiguraTridimensional` (con método `calcular_volumen`). Se crea una clase `Cubo` que hereda de múltiples clases y se modifica la clase `Circulo` para heredar de `FiguraBidimensional`.

## Ejercicio 1: `ejercicio1.py`

Implementa las clases `Guerrero` y `Arma` para simular un combate.

**Clases:**

- **`Arma`**:
  - **Atributos:** `tipo` (string), `ataque` (int), `categoria` (string).
  - **Métodos:** `__str__`, `mejorar_categoria` (aumenta el ataque del arma).
- **`Guerrero`**:
  - **Atributos:** `nombre` (string), `vida` (int), `ataque` (int), `arma` (objeto de la clase `Arma`).
  - **Métodos:** `__str__`, `atacar` (reduce la vida de otro guerrero), `mejorar_arma` (llama al método de mejora del arma del guerrero).

**Simulación:**

Se crean dos guerreros ("John Snow" y un "Caminante Blanco") con sus respectivas armas, y se simula un ataque de "John Snow" al "Caminante Blanco".

## Ejercicio 2: `ejercicio2.py`

Define una jerarquía de clases abstracta para representar figuras geométricas bidimensionales.

**Clases:**

- **`FiguraGeometrica` (Clase Abstracta)**:
  - **Métodos Abstractos:** `area(self)` (devuelve el área), `perimetro(self)` (devuelve el perímetro).
- **Clases Derivadas:**
  - **`Circulo`**: Hereda de `FiguraGeometrica`. Constructor recibe `radio`. Implementa `area` y `perimetro`.
  - **`Rectangulo`**: Hereda de `FiguraGeometrica`. Constructor recibe `base` y `altura`. Implementa `area` y `perimetro`.
  - **`Triangulo`**: Hereda de `FiguraGeometrica`. Constructor recibe `lado1`, `lado2` y `lado3`. Implementa `area` y `perimetro`.

**Polimorfismo:**

Se crea una lista de diferentes figuras geométricas y se itera sobre ella, llamando a los métodos `area` y `perimetro` de cada figura.

## Ejercicio 3: `ejercicio3.py`

Extiende la jerarquía de figuras geométricas introduciendo conceptos de clonación y figuras tridimensionales.

**Nuevas Clases:**

- **`FiguraBidimensional`**:
  - **Método:** `clonar(self)` (devuelve una copia profunda de la instancia).
- **`FiguraTridimensional`**:
  - **Método:** `calcular_volumen(self)` (método a ser implementado por clases derivadas).
- **`Cubo`**:
  - Hereda de `FiguraGeometrica`, `FiguraBidimensional` y `FiguraTridimensional`.
  - Constructor recibe `lado`.
  - Implementa `calcular_volumen`, `area` y `perimetro`.
- **`Circulo` (Modificada)**:
  - Ahora hereda también de `FiguraBidimensional`.

**Uso:**

Se crean instancias de `Cubo` y `Circulo`, se calculan sus propiedades (área, perímetro, volumen) y se demuestra la funcionalidad del método `clonar`.

## Contacto

Para cualquier consulta o comentario, puedes contactarme a través de [LinkedIn](https://www.linkedin.com/in/nkaminski-profile/) o [GitHub](https://github.com/N-Kaminski).

---

¡Gracias por revisar mi proyecto!
