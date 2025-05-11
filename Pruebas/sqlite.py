import sqlite3

class UsuarioDB:
    def __init__(self, nombre_db:str = "usuarios.db"):
        self.conn = sqlite3.connect(nombre_db) #crea (o abre) la base de datos
        self.conn.row_factory = sqlite3.Row #para poder acceder a los nombres de las columnas
        self.crear_tabla()

    def crear_tabla(self):
        with self.conn: #abre y cierra la conexion
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS usuarios(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    email TEXT UNIQUE NOT NULL
                )
            """)

    def agregar_usuario(self, nombre, email):
        try:
            with self.conn: #abre y cierra la conexion
                self.conn.execute("INSERT INTO usuarios (nombre, email) VALUES (?, ?)", (nombre, email))
                print("Usuario agregado con exito")
        except sqlite3.IntegrityError:
            print("ERROR X: El usuario ya existe")

    def listar_usuarios(self):
        cur = self.conn.cursor() #crea un cursor (el cursor es para recorrer la base de datos y ejecutar consultas)
        cur.execute("SELECT * FROM usuarios")
        usuarios = cur.fetchall() #devuelve una lista con todos los usuarios
        for usuario in usuarios:
            print(f"ID: {usuario['id']}, Nombre: {usuario['nombre']}, Email: {usuario['email']}")
    
    def actualizar_email(self, id_usuario: int, nuevo_email: str):
        with self.conn:
            self.conn.execute("UPDATE usuarios SET email = ? WHERE id = ?", (nuevo_email, id_usuario))
            print("Email actualizado con exito")

    def eliminar_usuario(self, id_usuario: int):
        with self.conn:
            self.conn.execute("DELETE FROM usuarios WHERE id = ?", (id_usuario,))
            print("Usuario eliminado con exito")
    
    def cerrar_conexion(self):
        self.conn.close()

if __name__ == "__main__":
    usuario_db = UsuarioDB()
    
    # Agregar usuarios
    usuario_db.agregar_usuario("Juan Pérez", "juan@gmail.com")
    usuario_db.agregar_usuario("Ana López", "ana@gmail.com")
    usuario_db.agregar_usuario("Carlos Rodríguez", "carlos@gmail.com")

    # Listar usuarios
    print("\n --- USUARIOS ---")
    usuario_db.listar_usuarios()

    # Actualizar email
    print("\n se actualiza el mail de Juan")
    usuario_db.actualizar_email(1, "juanperez@gmail")

    # Eliminar usuario
    print("\n se elimina el usuario con id 2")
    usuario_db.eliminar_usuario(2)

    # Listar usuarios
    print("\n --- USUARIOS ---")
    usuario_db.listar_usuarios()

    # Cerrar conexion
    usuario_db.cerrar_conexion()