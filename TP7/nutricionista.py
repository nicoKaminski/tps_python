import sqlite3
from datetime import date #para trabajar con fechas

class Paciente:
    def __init__(self, nombre, edad, peso_actual):
        self.nombre = nombre
        self.edad = edad
        self.peso_actual = peso_actual

class Alimento:
    def __init__(self, nombre, calorias):
        self.nombre = nombre
        self.calorias = calorias

class PlanComida:
    def __init__(self, paciente_id, alimento_id, fecha, cantidad):
        self.paciente_id = paciente_id
        self.alimento_id = alimento_id
        self.fecha = fecha
        self.cantidad = cantidad


class NutricionistaRepo:
    def __init__(self, nombre_db = "nutricionista.db"):
        self.conn = sqlite3.connect(nombre_db) #crea (o abre) la base de datos
        self.conn.row_factory = sqlite3.Row #para poder acceder a los nombres de las columnas
        self.conn.execute("PRAGMA foreign_keys = ON") #para que las claves foraneas funcionen
        self.crear_tabla()

    def crear_tabla(self):
        with self.conn: #abre y cierra la conexion
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS pacientes(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    edad INTEGER,
                    peso_actual REAL
                )
            """)
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS alimentos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    calorias REAL
                )
            ''')
            self.conn.execute('''
                CREATE TABLE IF NOT EXISTS plan_comidas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    paciente_id INTEGER,
                    alimento_id INTEGER,
                    fecha TEXT,
                    cantidad REAL,
                    FOREIGN KEY(paciente_id) REFERENCES pacientes(id),
                    FOREIGN KEY(alimento_id) REFERENCES alimentos(id)
                )
            ''')
    
    def cargar_datos_iniciales(self):
        with self.conn:
            self.conn.execute("INSERT INTO pacientes (nombre, edad, peso_actual) VALUES ('Nico', 35, 80.5)")
            self.conn.execute("INSERT INTO pacientes (nombre, edad, peso_actual) VALUES ('Nahue', 38, 75.0)")
            self.conn.execute("INSERT INTO pacientes (nombre, edad, peso_actual) VALUES ('Ari', 30, 68.0)")
            self.conn.execute("INSERT INTO pacientes (nombre, edad, peso_actual) VALUES ('Barb', 31, 60.0)")
            self.conn.execute("INSERT INTO pacientes (nombre, edad, peso_actual) VALUES ('Calip', 36, 85.0)")
            self.conn.execute("INSERT INTO alimentos (nombre, calorias) VALUES ('Arroz', 130)")
            self.conn.execute("INSERT INTO alimentos (nombre, calorias) VALUES ('Leche', 42)")
            self.conn.execute("INSERT INTO alimentos (nombre, calorias) VALUES ('Manzana', 52)")
            self.conn.execute("INSERT INTO alimentos (nombre, calorias) VALUES ('Pan', 265)")
            self.conn.execute("INSERT INTO alimentos (nombre, calorias) VALUES ('Queso', 100)")
            self.conn.execute("INSERT INTO alimentos (nombre, calorias) VALUES ('Cereal', 150)")
            self.conn.execute("INSERT INTO alimentos (nombre, calorias) VALUES ('Cafe', 0)")

    def agregar_plan_comida(self, plan: PlanComida):
        with self.conn: #abre y cierra la conexion
            self.conn.execute('''
                INSERT INTO plan_comidas (paciente_id, alimento_id, fecha, cantidad)
                VALUES (?, ?, ?, ?)
            ''', (plan.paciente_id, plan.alimento_id, plan.fecha, plan.cantidad))

    def listar_planes(self):
        cur = self.conn.cursor() #crea un cursor (el cursor es para recorrer la base de datos y ejecutar consultas)
        cur.execute('''
            SELECT pc.fecha, pc.cantidad,
                   pa.nombre AS paciente,
                   al.nombre AS alimento,
                   al.calorias * pc.cantidad AS calorias_totales
            FROM plan_comidas pc
            JOIN pacientes pa ON pc.paciente_id = pa.id
            JOIN alimentos al ON pc.alimento_id = al.id
        ''')
        for fila in cur.fetchall():
            print(f"{fila['fecha']}: {fila['paciente']} comió {fila['cantidad']} porciones de {fila['alimento']} ({fila['calorias_totales']} kcal)")

    def actualizar_peso(self, paciente_id, nuevo_peso):
        with self.conn:
            self.conn.execute('''
                UPDATE pacientes SET peso_actual = ? WHERE id = ?
            ''', (nuevo_peso, paciente_id))

    def eliminar_plan_comida(self, plan_id):
        with self.conn:
            self.conn.execute('DELETE FROM plan_comidas WHERE id = ?', (plan_id,))

    def eliminar_paciente(self, paciente_id):
        with self.conn:
            self.conn.execute('DELETE FROM pacientes WHERE id = ?', (paciente_id,))


if __name__ == "__main__":
    repo = NutricionistaRepo()

    print("\n Cargando datos iniciales...")
    repo.cargar_datos_iniciales()

    print("\n Agregando plan de comida...")  
    planes = [
    PlanComida(paciente_id=1, alimento_id=2, fecha=str(date.today()), cantidad=1),
    PlanComida(paciente_id=1, alimento_id=7, fecha=str(date.today()), cantidad=2),
    PlanComida(paciente_id=2, alimento_id=3, fecha=str(date.today()), cantidad=2),
    PlanComida(paciente_id=3, alimento_id=4, fecha=str(date.today()), cantidad=1.5),
    PlanComida(paciente_id=4, alimento_id=5, fecha=str(date.today()), cantidad=2),
    PlanComida(paciente_id=5, alimento_id=6, fecha=str(date.today()), cantidad=1)
    ]    
    for plan in planes:
        repo.agregar_plan_comida(plan)

    print("\n Listado de planes:")
    repo.listar_planes()

    print("\n Actualizando peso de paciente...")
    repo.actualizar_peso(paciente_id=1, nuevo_peso=79.8)

    print("\n Eliminando plan y luego paciente...")
    repo.eliminar_plan_comida(plan_id=6)
    repo.eliminar_paciente(paciente_id=5)

    print("\n Listado final:")
    repo.listar_planes()

    repo.conn.close()