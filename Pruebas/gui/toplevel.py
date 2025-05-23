import tkinter as tk
from tkinter import messagebox

def toplevel():
    ventana_principal = tk.Tk()
    ventana_principal.title("Ventana Principal")
    ventana_principal.geometry("300x200")

    def abrir_ventana_secundaria():
        nueva_ventana = tk.Toplevel()
        nueva_ventana.title("Ventana Secundaria")
        nueva_ventana.geometry("250x150")

        tk.Label(nueva_ventana, text="¡Hola desde otra ventana!").pack(pady=10)

        tk.Button(nueva_ventana, text="Cerrar", command=nueva_ventana.destroy).pack(pady=5)

    tk.Button(ventana_principal, text="Abrir Ventana Secundaria", command=abrir_ventana_secundaria).pack(pady=50)

    ventana_principal.mainloop()

if __name__ == "__main__":
    toplevel()
