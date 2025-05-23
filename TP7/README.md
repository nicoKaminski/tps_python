# Trabajo Práctico Nro. 7 - Gestión de Datos con SQLite

Este directorio contiene el ejercicio correspondiente al Trabajo Práctico número 7 de la materia Python, enfocado en la **gestión de datos utilizando la base de datos SQLite**. Este módulo actúa como el **backend de una aplicación de nutricionista**, implementando un sistema para gestionar información de pacientes, alimentos y planes de comida.

---

### Objetivos del TP

- **Creación y conexión** a una base de datos SQLite.
- **Definición de clases Python** para representar entidades de la base de datos (Paciente, Alimento, PlanComida).
- Implementación de un **repositorio (`NutricionistaRepo`)** para interactuar con la base de datos.
- **Creación de tablas** en la base de datos utilizando SQL.
- Realización de **operaciones CRUD** (Crear, Leer, Actualizar, Eliminar) sobre los datos de las tablas.
- Uso de **claves primarias y claves foráneas** para establecer relaciones entre tablas.
- Ejecución de **consultas SQL** para obtener y manipular datos.
- Trabajo con **fechas** utilizando el módulo `datetime`.

---

### Archivos Incluidos

- **`ejercicios.py`**: Contiene la implementación de las clases `Paciente`, `Alimento`, `PlanComida` y el repositorio `NutricionistaRepo`. Este archivo está diseñado para funcionar como el **módulo de acceso a datos para el TP8**, permitiendo la interacción con la base de datos desde otras partes de la aplicación.

---

### Clases Implementadas

- **`Paciente`**: Representa a un paciente con atributos como `nombre`, `edad` y `peso_actual`.
- **`Alimento`**: Representa un alimento con atributos como `nombre` y `calorias`.
- **`PlanComida`**: Representa la relación entre un paciente, un alimento, la fecha de consumo y la cantidad.
- **`NutricionistaRepo`**:
  - Establece la conexión con la base de datos SQLite (`nutricionista.db`).
  - Crea las tablas `pacientes`, `alimentos` y `plan_comidas` si no existen.
  - Implementa métodos CRUD para:
    - **`cargar_datos_iniciales()`**: Inserta algunos datos de ejemplo en las tablas.
    - **`agregar_plan_comida(plan: PlanComida)`**: Agrega un nuevo plan de comida.
    - **`listar_planes()`**: Muestra por consola los planes de comida con información detallada.
    - **`obtener_planes()`**: Retorna todos los planes de comida (pensado para ser usado por el frontend).
    - **`eliminar_plan_comida(plan_id)`**: Elimina un plan de comida por su ID.
    - **`agregar_paciente(paciente: Paciente)`**: Agrega un nuevo paciente.
    - **`actualizar_peso(paciente_id, nuevo_peso)`**: Actualiza el peso de un paciente.
    - **`eliminar_paciente(paciente_id)`**: Elimina un paciente por su ID.
    - **`listar_pacientes()`**: Retorna todos los pacientes.
    - **`agregar_alimento(alimento: Alimento)`**: Agrega un nuevo alimento.
    - **`listar_alimentos()`**: Retorna todos los alimentos.
    - **`eliminar_alimento(alimento_id)`**: Elimina un alimento por su ID.

---

### Base de Datos

- **`nutricionista.db`**: Archivo de la base de datos SQLite que se crea (si no existe) en el mismo directorio donde se ejecuta el script. Contiene las tablas `pacientes`, `alimentos` y `plan_comidas`.

---

### Cómo Ejecutar el Programa

1.  Guarda el archivo `ejercicios.py` en una carpeta.
2.  Ejecuta el archivo desde la terminal utilizando el comando: `python ejercicios.py`
3.  El script, al ser ejecutado directamente, realizará las siguientes acciones de demostración:
    - Cargará datos iniciales en la base de datos.
    - Agregará algunos planes de comida de ejemplo.
    - Listará los planes de comida.
    - Actualizará el peso de un paciente.
    - Eliminará un plan de comida y un paciente.
    - Listará los planes de comida nuevamente para mostrar los cambios.

---

### Notas Adicionales

- Se utiliza el módulo `sqlite3` para interactuar con la base de datos SQLite.
- Se emplea `FOREIGN KEY` para asegurar la integridad referencial entre las tablas `plan_comidas`, `pacientes` y `alimentos`.
- La clase `NutricionistaRepo` **encapsula toda la lógica de acceso a los datos**, lo que la hace ideal para ser reutilizada como **capa de persistencia en futuros módulos (como el TP8)**.
- Se utiliza la función `date.today()` del módulo `datetime` para obtener la fecha actual al agregar planes de comida.

---

### Contacto

Para cualquier consulta o comentario, puedes contactarme a través de [LinkedIn](https://www.linkedin.com/in/nkaminski-profile/) o [GitHub](https://github.com/N-Kaminski).

---

¡Gracias por revisar mi proyecto!
