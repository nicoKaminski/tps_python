"""
Disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles
Radiobutton permitir seleccionar si queremos sumarlos o restarlos. Al presionar un botón
mostrar el resultado de la operación seleccionada
"""
import tkinter as tk
from tkinter import ttk, messagebox


def calcular():
    try:
        num1 = int(num1_var.get())
        num2 = int(num2_var.get())
        operacion = operacion_var.get()
        if operacion == "suma":
            resultado = num1 + num2
        else:
            resultado = num1 - num2

        messagebox.showinfo("Resultado", f"El resultado es: {resultado}")
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingrese valores numéricos.")

root = tk.Tk()
root.title("Ejercicio 1")
root.geometry("300x200")

#variables
num1_var = tk.StringVar()
num2_var = tk.StringVar()
operacion_var = tk.StringVar(value="suma")

#widgets
tk.Label(root, text="Numero 1: ").pack()
tk.Entry(root, textvariable=num1_var).pack()
tk.Label(root, text="Numero 2: ").pack()
tk.Entry(root, textvariable=num2_var).pack()

tk.Label(root, text="Operacion: ").pack()
tk.Radiobutton(root, text="Suma", variable=operacion_var, value="suma").pack()
tk.Radiobutton(root, text="Resta", variable=operacion_var, value="resta").pack()

tk.Button(root, text="Calcular", command=calcular).pack()

root.mainloop()