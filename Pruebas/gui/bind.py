import tkinter as tk

def bind_clic():
    def al_hacer_clic(evento):
        etiqueta.config(text="¡Hiciste clic!", fg="green")

    def al_pasar_mouse(evento):
        etiqueta.config(text="Estás sobre mí", fg="blue")

    def al_salir_mouse(evento):
        etiqueta.config(text="Ya no estás sobre mí", fg="black")

    def al_hacer_doble_clic(evento):
        etiqueta.config(text="¡Hiciste doble clic!", fg="red")
    
    def al_hacer_click_derecho(evento):
        etiqueta.config(text="¡Hiciste clic derecho!", fg="grey")
    
    def al_hacer_click_centro(evento):
        etiqueta.config(text="¡Hiciste clic con la ruedita!", fg="yellow")

    ventana = tk.Tk()
    ventana.title("Eventos con bind()")
    ventana.geometry("300x200")

    etiqueta = tk.Label(ventana, text="Esperando tu acción...", font=("Arial", 14))
    etiqueta.pack(pady=30) # Agrega un espacio vertical

    # Asociar eventos (esto se hace con .bind)
    etiqueta.bind("<Button-1>", al_hacer_clic)     # Clic izquierdo
    etiqueta.bind("<Enter>", al_pasar_mouse)       # Mouse entra
    etiqueta.bind("<Leave>", al_salir_mouse)       # Mouse sale
    etiqueta.bind("<Double-1>", al_hacer_doble_clic) # Doble clic
    etiqueta.bind("<Button-3>", al_hacer_click_derecho) # Clic derecho
    etiqueta.bind("<Button-2>", al_hacer_click_centro) # Clic con la ruedita

    ventana.mainloop()

def bind_tecla():
    def tecla_presionada(evento):
        etiqueta.config(text=f"Presionaste: {evento.char}")

    ventana = tk.Tk()
    ventana.title("Captura de teclas")
    ventana.geometry("300x150")

    etiqueta = tk.Label(ventana, text="Presioná una tecla...", font=("Arial", 14))
    etiqueta.pack(pady=30)

    ventana.bind("<Key>", tecla_presionada)  # Captura todas las teclas

    ventana.mainloop()


# Ejecutar si es el principal
if __name__ == "__main__":
    bind_clic()
    bind_tecla()
