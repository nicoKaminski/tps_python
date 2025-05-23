import tkinter as tk

# Función que se ejecuta al presionar el botón
def registrar():
    nombre = entry_nombre.get()
    email = entry_email.get()
    edad = entry_edad.get()

    if nombre and email and edad:
        resultado.config(text=f"Te registraste bien {nombre}! tu mail es: {email} y tenes {edad} años")
    else:
        resultado.config(text="⚠️ Completá todos los campos")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Registro de Usuario pack")
ventana.geometry("300x250")

# Etiquetas y entradas
tk.Label(ventana, text="Nombre:").pack(pady=(10, 0)) # pack ubica el widget y pady es para agregar margen arriba 10px, abajo 0px
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Email:").pack(pady=(10, 0))
entry_email = tk.Entry(ventana)
entry_email.pack()

tk.Label(ventana, text="Edad:").pack(pady=(10, 0))
entry_edad = tk.Entry(ventana)
entry_edad.pack()

# Botón
boton_registrar = tk.Button(ventana, text="Registrar", command=registrar)
boton_registrar.pack(pady=15)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack()

# Ejecutar la interfaz
ventana.mainloop()
