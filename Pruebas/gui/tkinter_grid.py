import tkinter as tk

def registrar():
    nombre = entry_nombre.get()
    email = entry_email.get()
    edad = entry_edad.get()

    if nombre and email and edad:
        resultado.config(text=f"✅ Registrado: {nombre}, {email}, {edad} años")
    else:
        resultado.config(text="⚠️ Completá todos los campos")

# Crear ventana
ventana = tk.Tk()
ventana.title("Registro de Usuario grid")
ventana.geometry("350x200")

# Etiqueta y campo: Nombre
tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=0, column=1, padx=10)

# Etiqueta y campo: Email
tk.Label(ventana, text="Email:").grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_email = tk.Entry(ventana)
entry_email.grid(row=1, column=1, padx=10)

# Etiqueta y campo: Edad
tk.Label(ventana, text="Edad:").grid(row=2, column=0, padx=10, pady=10, sticky="e")
entry_edad = tk.Entry(ventana)
entry_edad.grid(row=2, column=1, padx=10)

# Botón
boton_registrar = tk.Button(ventana, text="Registrar", command=registrar)
boton_registrar.grid(row=3, column=0, columnspan=2, pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.grid(row=4, column=0, columnspan=2)

ventana.mainloop()
