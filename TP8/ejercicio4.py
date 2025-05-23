"""
Disponer un Listbox con una serie de nombres de frutas. Permitir la selección de varias
frutas. Cuando se presione un botón recuperar todas las frutas seleccionadas y mostrarlas
en una Label.
"""
import tkinter as tk
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Ejercicio 4")
root.geometry("200x250")

tk.Label(root, text="Elija las frutas que le gusten").grid(row=0, column=0)
frutas_lb = tk.Listbox(root, selectmode="multiple")
frutas = ["Manzana", "Pera", "Uva", "Sandia", "Banana", "Frutilla", "Arandano"]
for fruta in frutas:
    frutas_lb.insert(tk.END, fruta)
frutas_lb.grid(row=1, column=0, pady=10)

def mostrar_frutas():
    frutas_seleccionadas = frutas_lb.curselection()
    frutas_seleccionadas = [frutas_lb.get(i) for i in frutas_seleccionadas]
    messagebox.showinfo("Frutas seleccionadas", ", ".join(frutas_seleccionadas))

boton_mostrar = tk.Button(root, text="Mostrar frutas", command=mostrar_frutas)
boton_mostrar.grid(row=2, column=0, pady=10)

root.mainloop()