import tkinter as tk
from tkinter import ttk

def combobox():
    ventana = tk.Tk()
    ventana.title("Combobox")
    ventana.geometry("300x150")

    tk.Label(ventana, text="Elige tu lenguaje favorito:").pack(pady=10)

    opciones = ["Python", "Java", "C++", "JavaScript"]
    combo = ttk.Combobox(ventana, values=opciones, state="readonly") # ttk.Combobox Crea una lista desplegable | values=define opciones | state="readonly" impide escribir (sólo se puede elegir).
    combo.current(0)  # selecciona la primera opción por defecto
    combo.pack()

    def mostrar_eleccion():
        lenguaje = combo.get() # combo.get() devuelve lo que el usuario eligio
        resultado.config(text=f"Elegiste: {lenguaje}")

    tk.Button(ventana, text="Aceptar", command=mostrar_eleccion).pack(pady=10)
    resultado = tk.Label(ventana, text="")
    resultado.pack()

    ventana.mainloop()

if __name__ == "__main__":
    combobox()
