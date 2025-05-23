import tkinter as tk
from tkinter import ttk

def treeview():
    ventana = tk.Tk()
    ventana.title("}Treeview")
    ventana.geometry("400x250")

    # Crear el widget Treeview
    tabla = ttk.Treeview(ventana)
    tabla["columns"] = ("nombre", "edad", "curso")
    tabla.column("#0", width=0, stretch=tk.NO)  # Oculta la primera columna (por defecto se muestra)
    tabla.column("nombre", anchor="w", width=150) # anchor="w" alinea a la izquierda
    tabla.column("edad", anchor="center", width=100) # anchor="center" alinea al centro
    tabla.column("curso", anchor="e", width=100) # anchor="e" alinea a la derecha

    tabla.heading("nombre", text="Nombre", anchor="w")
    tabla.heading("edad", text="Edad", anchor="center")
    tabla.heading("curso", text="Curso", anchor="e")

    # Insertar datos
    tabla.insert("", "end", values=("Nico", 35, "JS")) #agrega una fila
    tabla.insert("", "end", values=("Ari", 30, "TS"))
    tabla.insert("", "end", values=("Nahue", 28, "python"))

    tabla.pack(pady=20)

    ventana.mainloop()

if __name__ == "__main__":
    treeview()
