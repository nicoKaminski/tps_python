import tkinter as tk
from tkinter import messagebox

def radiobutton_y_listbox():
    ventana = tk.Tk()
    ventana.title("00")

    # Nombre
    tk.Label(ventana, text="Nombre:").pack()
    entry_nombre = tk.Entry(ventana)
    entry_nombre.pack()

    # Radiobutton: Género
    tk.Label(ventana, text="Género:").pack()
    genero = tk.StringVar() #Crea una variable asociada al grupo de Radiobutton para saber cuál se seleccionó
    genero.set("Masculino")  # valor por defecto

    tk.Radiobutton(ventana, text="Masculino", variable=genero, value="Masculino").pack()
    tk.Radiobutton(ventana, text="Femenino", variable=genero, value="Femenino").pack()

    # Listbox: Lenguajes favoritos
    tk.Label(ventana, text="Lenguaje favorito:").pack()
    listbox = tk.Listbox(ventana, height=5) # tk.Listbox Crea una lista desplegable
    lenguajes = ["Python", "Java", "C++", "JavaScript", "Otro"]
    for leng in lenguajes:
        listbox.insert(tk.END, leng)
    listbox.pack()

    # Botón para mostrar selección
    def mostrar_datos():
        nombre = entry_nombre.get()
        genero_seleccionado = genero.get()
        try:
            lenguaje = listbox.get(listbox.curselection()) # Obtiene el lenguaje seleccionado
        except:
            lenguaje = "(ninguno)"

        mensaje = f"Nombre: {nombre}\nGénero: {genero_seleccionado}\nLenguaje: {lenguaje}"
        messagebox.showinfo("Resumen", mensaje) # Muestra una ventana emergente con un mensaje

    tk.Button(ventana, text="Mostrar resumen", command=mostrar_datos).pack(pady=10)

    ventana.mainloop()

# Ejecutar si es el principal
if __name__ == "__main__":
    radiobutton_y_listbox()
