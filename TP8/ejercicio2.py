"""
Crear una interfaz con tres controles de tipo Radiobutton etiquetados "Rojo", "Verde" y
"Azul". Cuando el usuario seleccione uno de los botones, el color de fondo de la ventana
debe cambiar al color correspondiente.
"""
import tkinter as tk

def cambiar_color():
    ventana.configure(bg=color_var.get())
    tk.Radiobutton.config(bg=color_var.get())

ventana = tk.Tk()
ventana.title("Color de Fondo")
ventana.geometry("150x100")

color_var = tk.StringVar(value="white")

tk.Radiobutton(ventana, text="Rojo", variable=color_var, value="red", command=cambiar_color).pack()
tk.Radiobutton(ventana, text="Verde", variable=color_var, value="green", command=cambiar_color).pack()
tk.Radiobutton(ventana, text="Azul", variable=color_var, value="blue", command=cambiar_color).pack()
tk.Radiobutton(ventana, text="Original", variable=color_var, value="white", command=cambiar_color).pack()

ventana.mainloop()