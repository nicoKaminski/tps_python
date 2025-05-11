# Trabajo Práctico Nro. 7 - Gestión de Datos con SQLite

Este directorio contiene el ejercicio correspondiente al Trabajo Práctico número 7 de la materia Python, enfocado en la gestión de datos utilizando la base de datos SQLite. El ejercicio implementa un sistema simple para gestionar información de pacientes, alimentos y planes de comida.

**Objetivos del TP:**

- Creación y conexión a una base de datos SQLite.
- Definición de clases Python para representar entidades de la base de datos (Paciente, Alimento, PlanComida).
- Implementación de un repositorio (`NutricionistaRepo`) para interactuar con la base de datos.
- Creación de tablas en la base de datos utilizando SQL.
- Realización de operaciones CRUD (Crear, Leer, Actualizar, Eliminar) sobre los datos de las tablas.
- Uso de claves primarias y claves foráneas para establecer relaciones entre tablas.
- Ejecución de consultas SQL para obtener y manipular datos.
- Trabajo con fechas utilizando el módulo `datetime`.

**Archivos Incluidos:**

- **`ejercicios.py`**: Contiene la implementación de las clases `Paciente`, `Alimento`, `PlanComida` y el repositorio `NutricionistaRepo`.

**Clases Implementadas:**

- **`Paciente`**: Representa a un paciente con atributos como `nombre`, `edad` y `peso_actual`.
- **`Alimento`**: Representa un alimento con atributos como `nombre` y `calorias`.
- **`PlanComida`**: Representa la relación entre un paciente, un alimento, la fecha de consumo y la cantidad.
- **`NutricionistaRepo`**:
  - Establece la conexión con la base de datos SQLite (`nutricionista.db`).
  - Crea las tablas `pacientes`, `alimentos` y `plan_comidas` si no existen.
  - Implementa métodos para:
    - `cargar_datos_iniciales()`: Inserta algunos datos de ejemplo en las tablas.
    - `agregar_plan_comida(plan: PlanComida)`: Agrega un nuevo plan de comida.
    - `listar_planes()`: Lista los planes de comida mostrando información relacionada de pacientes y alimentos.
    - `actualizar_peso(paciente_id, nuevo_peso)`: Actualiza el peso de un paciente.
    - `eliminar_plan_comida(plan_id)`: Elimina un plan de comida.
    - `eliminar_paciente(paciente_id)`: Elimina un paciente.

**Base de Datos:**

- **`nutricionista.db`**: Archivo de la base de datos SQLite que se crea (si no existe) en el mismo directorio donde se ejecuta el script. Contiene las tablas `pacientes`, `alimentos` y `plan_comidas`.

**Cómo ejecutar el programa:**

1.  Guarda el archivo `ejercicios.py` en una carpeta.
2.  Ejecuta el archivo desde la terminal utilizando el comando: `python ejercicios.py`
3.  El script realizará las siguientes acciones:
    - Cargará datos iniciales en la base de datos.
    - Agregará algunos planes de comida de ejemplo.
    - Listará los planes de comida.
    - Actualizará el peso de un paciente.
    - Eliminará un plan de comida y un paciente.
    - Listará los planes de comida nuevamente para mostrar los cambios.

**Notas Adicionales:**

- Se utiliza el módulo `sqlite3` para interactuar con la base de datos SQLite.
- Se utiliza `FOREIGN KEY` para asegurar la integridad referencial entre las tablas `plan_comidas`, `pacientes` y `alimentos`.
- La clase `NutricionistaRepo` encapsula la lógica de acceso a los datos.
- Se utiliza la función `date.today()` del módulo `datetime` para obtener la fecha actual al agregar planes de comida.

## Contacto

Para cualquier consulta o comentario, puedes contactarme a través de [LinkedIn](https://www.linkedin.com/in/nkaminski-profile/) o [GitHub](https://github.com/N-Kaminski).

---

¡Gracias por revisar mi proyecto!
