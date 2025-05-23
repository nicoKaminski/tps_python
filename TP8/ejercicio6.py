
import tkinter as tk
from tkinter import ttk, messagebox
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "TP7")))
from nutricionista import NutricionistaRepo, PlanComida, Alimento, Paciente
from datetime import date


# Crear la ventana
root = tk.Tk()
root.title("App Nutricionista")
root.geometry("800x500")

notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Instancia de la clase NutricionistaRepo
db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "TP7", "nutricionista.db"))
repo = NutricionistaRepo(db_path)
# repo = NutricionistaRepo("../TP7/nutricionista.db") 

# Variables
paciente_nombre = tk.StringVar()
paciente_edad = tk.StringVar()
paciente_peso = tk.StringVar()
alimento_nombre = tk.StringVar()
alimento_calorias = tk.StringVar()
cantidad_var = tk.StringVar()
paciente_plan = tk.StringVar()
alimento_plan = tk.StringVar()
cantidad_plan = tk.StringVar()

def limpiar():
    paciente_nombre.set("")
    paciente_edad.set("")
    paciente_peso.set("")

# Pestaña 1: Pacientes
def agregar_paciente():
    nombre = paciente_nombre.get().strip()
    edad = paciente_edad.get().strip()
    peso = paciente_peso.get().strip()

    if not nombre or not edad.isdigit() or not peso.replace(".", "", 1).isdigit():
        messagebox.showerror("Error", "Por favor, completá correctamente todos los campos.")
        return

    paciente = Paciente(nombre, int(edad), float(peso))
    repo.agregar_paciente(paciente)

    pacientes_tw.insert("", tk.END, values=(paciente.nombre, paciente.edad, paciente.peso_actual))

    limpiar()

def eliminar_paciente():
    seleccionado = pacientes_tw.selection()
    if not seleccionado:
        messagebox.showinfo("Info", "Seleccione un paciente para eliminar.")
        return

    # Obtener valores desde el Treeview
    valores = pacientes_tw.item(seleccionado[0], 'values')
    nombre = valores[0]

    # Buscar el ID en la base de datos
    paciente_cur = repo.conn.cursor() #objeto cursos
    paciente_cur.execute("SELECT id FROM pacientes WHERE nombre = ?", (nombre,))
    fila = paciente_cur.fetchone()

    if fila:
        repo.eliminar_paciente(fila["id"])  # Elimina en la BD
        pacientes_tw.delete(seleccionado[0])  # Elimina del Treeview
    else:
        messagebox.showerror("Error", "No se pudo encontrar al paciente en la base.")

def listar_pacientes():
    pacientes = repo.conn.execute("SELECT nombre, edad, peso_actual FROM pacientes").fetchall()
    for p in pacientes:
        pacientes_tw.insert("", tk.END, values=(p["nombre"], p["edad"], p["peso_actual"]))



paciente_frame = ttk.Frame(notebook)
notebook.add(paciente_frame, text="Pacientes")

paciente_datos = ttk.LabelFrame(paciente_frame, text="Datos del Paciente")
paciente_datos.pack(padx=10, pady=10, fill="x")

tk.Label(paciente_datos, text="Nombre:").grid(row=0, column=0, sticky="w")
tk.Entry(paciente_datos, textvariable=paciente_nombre).grid(row=0, column=1, sticky="ew")

tk.Label(paciente_datos, text="Edad:").grid(row=1, column=0, sticky="w")
tk.Entry(paciente_datos, textvariable=paciente_edad).grid(row=1, column=1, sticky="ew")

tk.Label(paciente_datos, text="Peso Actual:").grid(row=2, column=0, sticky="w")
tk.Entry(paciente_datos, textvariable=paciente_peso).grid(row=2, column=1, sticky="ew")

pacientes_tw = ttk.Treeview(paciente_frame, columns=("Nombre", "Edad", "Peso Actual"), show="headings")
for col in ("Nombre", "Edad", "Peso Actual"):
    pacientes_tw.heading(col, text=col)
    pacientes_tw.column(col, width=150)
pacientes_tw.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(paciente_frame, orient="vertical", command=pacientes_tw.yview)
pacientes_tw.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

botones_frame = tk.Frame(paciente_frame)
botones_frame.pack(pady=10)

tk.Button(botones_frame, text="Agregar", command=agregar_paciente).pack(side="left", padx=10)
tk.Button(botones_frame, text="Eliminar", command=eliminar_paciente).pack(side="left", padx=10)

# Pestaña 2: Alimentos
def agregar_alimento():
    nombre = alimento_nombre.get().strip()
    calorias = alimento_calorias.get().strip()

    if not nombre or not calorias.isdigit():
        messagebox.showerror("Error", "Por favor, completá correctamente todos los campos.")
        return

    alimento = Alimento(nombre, int(calorias))
    repo.agregar_alimento(alimento)

    alimento_tw.insert("", tk.END, values=(alimento.nombre, alimento.calorias))
    limpiar()

def eliminar_alimento():
    seleccionado = alimento_tw.selection()
    if not seleccionado:
        messagebox.showinfo("Info", "Seleccione un alimento para eliminar")
        return

    valores = alimento_tw.item(seleccionado[0], 'values')
    nombre = valores[0]

    alimento_cur = repo.conn.cursor()
    alimento_cur.execute("SELECT id FROM alimentos WHERE nombre = ?", (nombre,))
    fila = alimento_cur.fetchone()

    if fila:
        repo.eliminar_alimento(fila["id"])
        alimento_tw.delete(seleccionado[0])
    else:
        messagebox.showerror("Error", "No se encontro el alimento")

def listar_alimentos():
    alimentos = repo.conn.execute("SELECT nombre, calorias FROM alimentos").fetchall()
    for a in alimentos:
        alimento_tw.insert("", tk.END, values=(a["nombre"], a["calorias"]))

alimento_frame = ttk.Frame(notebook)
notebook.add(alimento_frame, text="Alimentos")

alimento_datos = ttk.LabelFrame(alimento_frame, text="Datos del Alimento")
alimento_datos.pack(padx=10, pady=10, fill="x")

tk.Label(alimento_datos, text="Nombre:").grid(row=0, column=0, sticky="w")
tk.Entry(alimento_datos, textvariable=alimento_nombre).grid(row=0, column=1, sticky="ew")

tk.Label(alimento_datos, text="Calorias:").grid(row=1, column=0, sticky="w")
tk.Entry(alimento_datos, textvariable=alimento_calorias).grid(row=1, column=1, sticky="ew")

alimento_tw = ttk.Treeview(alimento_frame, columns=("Nombre", "Calorias"), show="headings")
for col in ("Nombre", "Calorias"):
    alimento_tw.heading(col, text=col)
    alimento_tw.column(col, width=150)
alimento_tw.pack(side="left", fill="both", expand=True)

scroll = ttk.Scrollbar(alimento_frame, orient="vertical", command=alimento_tw.yview)
alimento_tw.configure(yscrollcommand=scroll.set)
scroll.pack(side="right", fill="y")

botones_frame = tk.Frame(alimento_frame)
botones_frame.pack(pady=10)

tk.Button(botones_frame, text="Agregar", command=agregar_alimento).pack(side="left", padx=10)
tk.Button(botones_frame, text="Eliminar", command=eliminar_alimento).pack(side="left", padx=10)


# Pestaña 3: Planes de Comidas

def agregar_plan():
    if not paciente_plan.get() or not alimento_plan.get() or not cantidad_plan.get().replace(".", "", 1).isdigit():
        messagebox.showerror("Error", "Complete todos los campos correctamente.")
        return

    paciente_id = int(paciente_plan.get().split(" - ")[0])
    alimento_id = int(alimento_plan.get().split(" - ")[0])
    cantidad = float(cantidad_plan.get())
    fecha = str(date.today())

    plan = PlanComida(paciente_id, alimento_id, fecha, cantidad)
    repo.agregar_plan_comida(plan)
    mostrar_planes()
    cantidad_var.set("")
    messagebox.showinfo("Éxito", "Plan de comida agregado con éxito.")

def eliminar_plan():
    seleccionado = plan_tw.selection()
    if not seleccionado:
        messagebox.showinfo("Info", "Seleccione un plan para eliminar")
        return
    item = seleccionado[0]
    valores = plan_tw.item(item, "values")
    plan_id = int(valores[0]) 
    repo.eliminar_plan_comida(plan_id)
    mostrar_planes()
    messagebox.showinfo("Eliminado", "Plan eliminado correctamente")

def mostrar_planes():
    plan_tw.delete(*plan_tw.get_children())
    planes = repo.obtener_planes()
    for plan in planes:
        plan_tw.insert("", tk.END, values=(plan["id"], plan["fecha"], plan["paciente"], plan["alimento"], plan["cantidad"], round(plan["calorias_totales"], 2)))


plan_frame = ttk.Frame(notebook)
notebook.add(plan_frame, text="Planes de Comidas")

plan_datos = ttk.LabelFrame(plan_frame, text="Datos del Plan")
plan_datos.pack(padx=10, pady=10, fill="x")

tk.Label(plan_datos, text="Paciente:").grid(row=0, column=0, sticky="w")
paciente_data = repo.conn.execute("SELECT id, nombre FROM pacientes").fetchall()
pacientes_opciones = [f"{p['id']} - {p['nombre']}" for p in paciente_data]
paciente_cb = ttk.Combobox(plan_datos, textvariable=paciente_plan, values=pacientes_opciones, state="readonly")
paciente_cb.grid(row=0, column=1, sticky="ew")

tk.Label(plan_datos, text="Alimento:").grid(row=1, column=0, sticky="w")
alimentos_data = repo.conn.execute("SELECT id, nombre FROM alimentos").fetchall()
alimentos_opciones = [f"{a['id']} - {a['nombre']}" for a in alimentos_data]
alimentos_cb = ttk.Combobox(plan_datos, textvariable=alimento_plan, values=alimentos_opciones, state="readonly")
alimentos_cb.grid(row=1, column=1, sticky="ew")

tk.Label(plan_datos, text="Cantidad(porciones):").grid(row=2, column=0, sticky="w")
tk.Entry(plan_datos, textvariable=cantidad_plan).grid(row=2, column=1, sticky="ew")

plan_tw = ttk.Treeview(plan_frame, columns=("id","Fecha", "Paciente", "Alimento", "Cantidad", "Calorias"), show="headings")
for col in ("id","Fecha", "Paciente", "Alimento", "Cantidad", "Calorias"):
    plan_tw.heading(col, text=col)
    plan_tw.column(col, width=90)
plan_tw.pack(side="left", fill="both", expand=True)

plan_scroll = ttk.Scrollbar(plan_frame, orient="vertical", command=plan_tw.yview)
plan_tw.configure(yscrollcommand=plan_scroll.set)
plan_scroll.pack(side="right", fill="y")

plan_botones = tk.Frame(plan_frame)
plan_botones.pack(pady=10)
tk.Button(plan_botones, text="Agregar Plan", command=agregar_plan).pack(side="left", padx=10)
tk.Button(plan_botones, text="Eliminar Plan", command=eliminar_plan).pack(side="left", padx=10)


listar_pacientes()
listar_alimentos()
mostrar_planes()
root.mainloop()
