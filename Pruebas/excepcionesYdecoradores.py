def excepciones():
    try: #codigo que puede fallar
        x = int(input("Ingrese un número: "))
        y = 10 / x
    except ValueError as e: #except: captura y maneja el error
        print("Eso no es un número válido.")
    except ZeroDivisionError as e:
        print("¡No podés dividir por cero!")
    else: #se ejecuta si no hubo ningun error
        print("Resultado:", y)
    finally: #se ejecuta siempre
        print("¡Fin del bloque try/except!")


def decoradores(): #El decorador te permite añadir lógica sin tocar el código original.
    from functools import wraps
    def log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):   #*args → recibe todos los parámetros posicionales.
                                        #**kwargs → recibe todos los parámetros nombrados.
            # Antes
            print(f"Iniciando {func.__name__} con args={args}, kwargs={kwargs}")
            resultado = func(*args, **kwargs)  # Llamada original
            # Después
            print(f"{func.__name__} finalizada, resultado={resultado}")
            return resultado
        return wrapper

    @log_decorator #Ponemos @log_decorator encima de la definición de la función a decorar:
    def saludar(nombre):
        """Retorna saludo."""
        return f"¡Hola, {nombre}!"

    print(saludar("Ana"))
    # Verás registro de inicio, fin y resultado.


def generadores():
    def cuenta_regresiva(n):
        print("Empieza")
        yield 1            # 1ª pausa: devuelve 1
        print("Continúa")
        yield 2            # 2ª pausa: devuelve 2
        print("Termina")
        yield 3            # 3ª pausa: devuelve 3
        print("Sin más yields")

    gen = cuenta_regresiva(3)
    gen = generador()
    print(next(gen))      # Imprime "Empieza", luego devuelve 1
    print(next(gen))      # Retoma, imprime "Continúa", devuelve 2
    print(next(gen))      # Retoma, imprime "Termina", devuelve 3
    next(gen)             # Retoma, imprime "Sin más yields", luego StopIteration


def trycatch():
    def calculadora():
        while True:
            try:
                a = float(input("Ingrese primer número: "))
                op = input("Operación (+ - * /): ")
                b = float(input("Ingrese segundo número: "))
                if op == "+":
                    print(a + b)
                elif op == "-":
                    print(a - b)
                elif op == "*":
                    print(a * b)
                elif op == "/":
                    print(a / b)
                else:
                    raise Exception("Operador inválido") 
            except ValueError: #el usuario no ingresa un número
                print("Debe ingresar un número válido.")
            except ZeroDivisionError: #el usuario intenta dividir por cero
                print("No se puede dividir por cero.")
            except Exception as e:
                print("Error:", e)
            rta = input("¿Continuar? (s/n): ")
            if rta.lower() != "s":
                break
    calculadora()


def decorador1():
    from functools import wraps #Importamos wraps, que copia metadatos (nombre, docstring) de la función original al wrapper.

    def log_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[INICIO] {func.__name__}, args={args}, kwargs={kwargs}")
            resultado = func(*args, **kwargs)
            print(f"[FIN] {func.__name__}, resultado={resultado}")
            return resultado
        return wrapper

    @log_decorator
    def saludar(nombre):
        return f"¡Hola, {nombre}!"

    print(saludar("Yo"))


def decorador2(): 
    from functools import wraps

    def exception_handler(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs) #intenta ejecutar la función original.
            except Exception as e:          #Captura cualquier excepción
                print(f"Se ha producido un error en la función {func.__name__}: {e}")
                return None
        return wrapper

    @exception_handler
    def dividir(a, b):
        return a / b

    @exception_handler
    def convertir_a_entero(valor):
        return int(valor)

    print(dividir(10, 2)) # 5
    print(dividir(10, 0)) # Se ha producido un error en la función dividir: division by zero
    print(convertir_a_entero("123")) # 123
    print(convertir_a_entero("abc")) # Se ha producido un error en la función convertir_a_entero: invalid literal for int() with base 10: 'abc'


def generador():
    def es_primo(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
   
    def generador_primos():
        n = 2
        while True:
            if es_primo(n):
                yield n
            n += 1

    # Obtener los primeros 10 primos:
    misPrimos = generador_primos()
    for _ in range(10):
        print(next(misPrimos))



#INICIO
while True:
    print("\nSeleccione el ejercicio a ejecutar:")
    print("N° - selecciona el ejercicio deseado")
    print("0 - Salir")

    opcion = input("Ingrese el número del ejercicio: ")

    if opcion == "1":
        excepciones()
    elif opcion == "2":
        decoradores()
    elif opcion == "3":
        generadores()
    elif opcion =="4":
        trycatch()
    elif opcion =="5":
        decorador1()
    elif opcion =="6":
        decorador2()    
    elif opcion =="7":
        generador()  
    elif opcion == "0":
        print("Saliendo del programa...")
        break
    else:
        print("Opción no válida, intente de nuevo.")