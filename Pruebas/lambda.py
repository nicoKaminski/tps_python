
# LAMBDA es simplemente una función rápida y sin nombre de crear funciones simples, sin usar def

# EJEMPLO CON DEF:
def cuadrado(x):
    return x**2

# EJEMPLO CON LAMBDA:
cuadrado = lambda x: x**2

# Y SE PUEDE USAR DIRECTAMENTE:
print((lambda x: x + 5)(3))  # Resultado: 8


# Estructura simple: 
lambda argumentos: "lo_que_devuelve"

# Ejemplo 1
f = lambda x: x + 1
print(f(5)) # Resultado= 6

