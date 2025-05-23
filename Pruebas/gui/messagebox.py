import tkinter as tk
from tkinter import messagebox

def mbox():
    ventana = tk.Tk()
    ventana.title("Messagebox")
    ventana.geometry("300x200")

    def mostrar_info():
        messagebox.showinfo("Información", "Este es un mensaje informativo.")

    def mostrar_error():
        messagebox.showerror("Error", "Algo salió mal.")

    def confirmar():
        respuesta = messagebox.askyesno("Confirmación", "¿Deseás continuar?")
        if respuesta:
            messagebox.showinfo("Gracias", "Continuamos!")
        else:
            messagebox.showwarning("Cancelado", "Operación cancelada.")

    btn_info = tk.Button(ventana, text="Mostrar Info", command=mostrar_info)
    btn_info.pack(pady=5)

    btn_error = tk.Button(ventana, text="Mostrar Error", command=mostrar_error)
    btn_error.pack(pady=5)

    btn_confirmar = tk.Button(ventana, text="Confirmar Acción", command=confirmar)
    btn_confirmar.pack(pady=5)

    ventana.mainloop()

if __name__ == "__main__":
    mbox()
