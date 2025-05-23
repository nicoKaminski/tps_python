import tkinter as tk

def frame():
    ventana = tk.Tk()
    ventana.title("Frame")
    ventana.geometry("300x200")

    # Frame para datos del usuario
    marco_datos = tk.Frame(ventana, bg="lightblue", padx=10, pady=10) # tk.frame Crea un contenedor donde meteremos otros widgets
    marco_datos.pack(fill="x", pady=5) # fill="x" expande el marco en el eje x para que ocupe toda la ventana

    tk.Label(marco_datos, text="Nombre:").grid(row=0, column=0) 
    tk.Entry(marco_datos).grid(row=0, column=1) # grid para posicionar los elementos como tabla

    tk.Label(marco_datos, text="Email:").grid(row=1, column=0)
    tk.Entry(marco_datos).grid(row=1, column=1)

    # Frame para los botones
    marco_botones = tk.Frame(ventana, bg="lightgreen", pady=10)
    marco_botones.pack(fill="x", pady=5)

    tk.Button(marco_botones, text="Guardar").pack(side="left", padx=20)
    tk.Button(marco_botones, text="Cancelar").pack(side="right", padx=20)

    ventana.mainloop() # Muestra la ventana
    # bg, padx, pady	Son parámetros visuales: color de fondo y márgenes

# Ejecutar solo si es el programa principal
if __name__ == "__main__":
    frame()
