import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Formulario de Registro")
root.geometry("400x500")

#contenedor principal para formulario
formulario =  tk.Frame(root, padx=10, pady=10) #padx es para agregar margen horizontal y pady es para agregar margen vertical
formulario.pack(pady=20)

#contenedor para boton
boton_frame = tk.Frame(root)
boton_frame.config(bg="#d0e0f0")
boton_frame.pack(pady=10)

#variables
nombre_var = tk.StringVar() #tk.StringVar() crea una variable asociada a un Entry
edad_var = tk.StringVar()
genero_var = tk.StringVar(value="otro")
comida_var = tk.StringVar()

#uso de entry
tk.Label(formulario, text="Nombre: ").grid(row=0, column=0, sticky="w")
tk.Entry(formulario, textvariable=nombre_var).grid(row=0, column=1)
tk.Label(formulario, text="Edad: ").grid(row=1, column=0, sticky="w")
tk.Entry(formulario, textvariable=edad_var).grid(row=1, column=1)

#uso de radiobutton
tk.Label(formulario, text="Genero: ").grid(row=2, column=0, sticky="w")
tk.Radiobutton(formulario, text="Masculino", variable=genero_var, value="masculino").grid(row=2, column=1)
tk.Radiobutton(formulario, text="Femenino", variable=genero_var, value="femenino").grid(row=3, column=1)
tk.Radiobutton(formulario, text="Otro", variable=genero_var, value="otro").grid(row=4, column=1)

#uso de combobox
tk.Label(formulario, text="Comida favorita: ").grid(row=5, column=0, sticky="w")
comida_cb = ttk.Combobox(formulario, textvariable=comida_var, state="readonly") # state="readonly" impide escribir (sólo se puede elegir).
comida_cb['values'] = ("Pizza", "Buerger", "Asado", "Fajitas", "Pollo", "Ensalada")
comida_cb.current(0) # selecciona la primera opcion por defecto
comida_cb.grid(row=5, column=1)

#uso de listbox
tk.Label(formulario, text="Hobbies: ").grid(row=6, column=0, sticky="w")
hobbies_lb = tk.Listbox(formulario, selectmode="multiple", height=5) #selectmode="multiple" permite seleccionar varias opciones
hobbies = ["lectura", "Viajes", "Musica", "VideoJuegos", "Deporte"]
for hobby in hobbies:
    hobbies_lb.insert(tk.END, hobby) #inserta las opciones en el listbox
hobbies_lb.grid(row=6, column=1, pady=10)

def mostrar_resumen():
    nombre = nombre_var.get()
    edad = edad_var.get()
    genero = genero_var.get()
    comida = comida_var.get()
    seleccion = hobbies_lb.curselection()
    hobbies_seleccionados = [hobbies_lb.get(i) for i in seleccion]

    if not nombre or not edad.isdigit():
        messagebox.showerror("Error", "Por favor, ingrese un nombre válido y una edad numérica.")
        return

    # Crear ventana secundaria
    resumen = tk.Toplevel(root, text="Resumen del Usuario", padx=10, pady=10)
    resumen.title("Resumen del Usuario")

    tk.Label(resumen, text=f"Nombre: {nombre}").pack()
    tk.Label(resumen, text=f"Edad: {edad}").pack()
    tk.Label(resumen, text=f"Género: {genero}").pack()
    tk.Label(resumen, text=f"Comida favorita: {comida}").pack()
    tk.Label(resumen, text="Hobbies: " + ", ".join(hobbies_seleccionados)).pack()

tk.Button(boton_frame, text="Guardar", command=mostrar_resumen).pack()

#uso de place
tk.Label(root, text="Formulario de practica", fg="blue", font=("Arial", 16)).place(x=100, y=470)

root.mainloop()