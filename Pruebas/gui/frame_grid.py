import tkinter as tk

def frame_grid():
    ventana = tk.Tk()
    ventana.title("Frame con Grid")
    ventana.geometry("300x150")

    frame = tk.Frame(ventana)
    frame.pack(pady=20)

    tk.Label(frame, text="Usuario:").grid(row=0, column=0, sticky="e")
    tk.Entry(frame).grid(row=0, column=1)

    tk.Label(frame, text="Contraseña:").grid(row=1, column=0, sticky="e")
    tk.Entry(frame, show="*").grid(row=1, column=1)

    tk.Button(frame, text="Ingresar").grid(row=2, columnspan=2, pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    frame_grid()