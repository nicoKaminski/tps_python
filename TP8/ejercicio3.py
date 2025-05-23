"""
Diseñar una interfaz que incluya un Checkbutton con el siguiente mensaje:
"¿Está de acuerdo con los términos y condiciones?"
También debe incluirse un botón que, inicialmente, esté deshabilitado.
Cuando el usuario marque (tilde) el Checkbutton, el botón debe activarse automáticamente.
Si se desmarca, el botón debe volver a desactivarse.
"""

import tkinter as tk

def verificar():
    if acuerdo_var.get():
        boton.config(state="normal")
    else:
        boton.config(state="disabled")

ventana = tk.Tk()
ventana.title("Ejercicio 3")
ventana.geometry("300x200")

acuerdo_var = tk.BooleanVar()

tk.Checkbutton(ventana, text="Estoy de acuerdo con los términos y condiciones", variable=acuerdo_var, command=verificar).pack(pady=10)
boton = tk.Button(ventana, text="Aceptar", state="disabled")
boton.pack(pady=10)

ventana.mainloop()