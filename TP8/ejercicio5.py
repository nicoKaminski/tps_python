import tkinter as tk
from tkinter import ttk, messagebox

# Configuración de la ventana
root = tk.Tk()
root.title("Inventario")
root.geometry("600x400")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True) # Expandir el notebook para ocupar toda la ventana

# Variables
nombre_var = tk.StringVar()
precio_var = tk.StringVar()
categoria_var = tk.StringVar()

# Pestaña 1: Registro
frame1 = ttk.Frame(notebook) #Crea una pestaña
notebook.add(frame1, text="Registro de Producto") #Agrega la pestaña al notebook

# Contenedor de datos
datos_frame = ttk.LabelFrame(frame1, text="Datos del Producto")
datos_frame.pack(padx=10, pady=10, fill="x")

tk.Label(datos_frame, text="Nombre:").grid(row=0, column=0, sticky="w")
tk.Entry(datos_frame, textvariable=nombre_var).grid(row=0, column=1, sticky="ew")

tk.Label(datos_frame, text="Precio:").grid(row=1, column=0, sticky="w")
tk.Entry(datos_frame, textvariable=precio_var).grid(row=1, column=1, sticky="ew")

tk.Label(datos_frame, text="Categoría:").grid(row=2, column=0, sticky="w")
categorias_cb = ttk.Combobox(datos_frame, textvariable=categoria_var, state="readonly")
categorias_cb['values'] = ["Alimentos", "Limpieza", "Tecnología"]
categorias_cb.grid(row=2, column=1, sticky="ew")

productos = []

def agregar_producto():
    nombre = nombre_var.get()
    precio = precio_var.get()
    categoria = categoria_var.get()
    if not nombre or not precio.replace('.', '', 1).isdigit(): # replace('.', '', 1).isdigit() verifica que sea num valido y entero
        messagebox.showerror("Error", "Cargue datos primero")
        return
    else:
        messagebox.showinfo("Info", "Producto cargado")
    productos_tw.insert("", tk.END, values=(nombre, precio, categoria))
    productos.append((nombre, precio, categoria))

def limpiar():
    nombre_var.set("")
    precio_var.set("")
    categoria_var.set("")

botones_frame = tk.Frame(frame1)
botones_frame.pack(pady=10)

tk.Button(botones_frame, text="Agregar", command=agregar_producto).pack(side="left", padx=10)
tk.Button(botones_frame, text="Limpiar", command=limpiar).pack(side="left", padx=10)

# Pestaña 2: Inventario
frame2 = ttk.Frame(notebook) #Crea una pestaña
notebook.add(frame2, text="Inventario") #Agrega la pestaña al notebook

# Contenedor de datos
productos_tw = ttk.Treeview(frame2, columns=("Nombre", "Precio", "Categoría"), show="headings") #Crea una tabla y define los encabezados
for col in ("Nombre", "Precio", "Categoría"):
    productos_tw.heading(col, text=col) # Define los encabezados
    productos_tw.column(col, width=150)
productos_tw.pack(side="left", fill="both", expand=True) # pone el tw en el frame y le agrega diseño

# Crea scroll para la tabla
scroll = ttk.Scrollbar(frame2, orient="vertical", command=productos_tw.yview) # Crea el scroll
productos_tw.configure(yscrollcommand=scroll.set) # Configura el scroll. le dice al tw que se sincronize con el scroll
scroll.pack(side="right", fill="y") # pone el scroll en el frame

def eliminar():
    seleccionado = productos_tw.selection()
    for item in seleccionado:
        productos_tw.delete(item)

def ver_detalles():
    seleccionado = productos_tw.selection()
    if not seleccionado:
        messagebox.showinfo("Info", "Seleccione un producto")
        return
    datos = productos_tw.item(seleccionado[0], 'values')
    top = tk.Toplevel(root)
    top.title("Detalle")
    top.geometry("200x100")
    tk.Label(top, text=f"Nombre: {datos[0]}").pack()
    tk.Label(top, text=f"Precio: ${datos[1]}").pack()
    tk.Label(top, text=f"Categoría: {datos[2]}").pack()

botones_frame2 = tk.Frame(frame2)
botones_frame2.pack(side="right", padx=10, pady=10)

tk.Button(botones_frame2, text="Eliminar", command=eliminar).pack(fill="x", pady=5)
tk.Button(botones_frame2, text="Ver Detalles", command=ver_detalles).pack(fill="x", pady=5)

root.mainloop()