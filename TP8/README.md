# Trabajo Práctico Nro. 8 - Interfaces Gráficas con Tkinter

Este directorio contiene los ejercicios correspondientes al Trabajo Práctico número 8 de la materia Python, enfocado en la creación de interfaces gráficas de usuario (GUI) utilizando la biblioteca Tkinter. Este TP explora varios widgets de Tkinter y culmina con la integración de una interfaz gráfica para la aplicación de nutricionista desarrollada en el TP7.

---

### Objetivos del TP

- **Introducción a Tkinter**: Comprender los conceptos básicos de la creación de interfaces gráficas.
- **Manejo de Widgets**: Aprender a utilizar y configurar diversos controles de Tkinter como `Entry`, `Radiobutton`, `Checkbutton`, `Listbox`, `Notebook`, `Treeview` y `Combobox`.
- **Interacción con la Interfaz**: Implementar la lógica para responder a eventos del usuario (clics en botones, selección de opciones).
- **Validación de Entrada**: Realizar validaciones básicas de datos ingresados por el usuario.
- **Organización de la Interfaz**: Utilizar `ttk.Notebook` para estructurar la interfaz en pestañas.
- **Integración de Backend**: Conectar la interfaz gráfica con la lógica de negocio y persistencia de datos desarrollada en el **TP7**.

---

### Archivos Incluidos

- **`ejercicio1.py`**: Calculadora simple con `Entry` y `Radiobutton`.
- **`ejercicio2.py`**: Cambio de color de fondo de la ventana con `Radiobutton`.
- **`ejercicio3.py`**: Activación/desactivación de un botón con `Checkbutton`.
- **`ejercicio4.py`**: Selección de elementos de una lista (`Listbox`) y visualización en un `Label`.
- **`ejercicio5.py`**: Sistema de inventario con `Notebook` (pestañas), `Entry`, `Combobox` y `Treeview`.
- **`ejercicio6.py`**: Aplicación completa de nutricionista, integrando el backend del TP7.

---

### Descripción Detallada de los Ejercicios

#### `ejercicio1.py` - Suma o Resta de Enteros

Este ejercicio crea una interfaz sencilla para realizar sumas o restas de dos números enteros.

- **Widgets utilizados**: `Entry` (para la entrada de números), `Radiobutton` (para seleccionar la operación), `Button` (para ejecutar el cálculo).
- **Funcionalidad**: Permite al usuario ingresar dos números, elegir entre suma o resta, y mostrar el resultado en una `messagebox`. Incluye validación básica de entrada numérica.

#### `ejercicio2.py` - Selector de Color de Fondo

Una interfaz para cambiar el color de fondo de la ventana.

- **Widgets utilizados**: `Radiobutton`.
- **Funcionalidad**: Al seleccionar un `Radiobutton` (Rojo, Verde, Azul, Original), el color de fondo de la ventana cambia dinámicamente.

#### `ejercicio3.py` - Términos y Condiciones

Demuestra cómo controlar el estado de un botón con un `Checkbutton`.

- **Widgets utilizados**: `Checkbutton`, `Button`.
- **Funcionalidad**: Un botón permanece deshabilitado hasta que el usuario marca un `Checkbutton` indicando acuerdo con los términos y condiciones. Si se desmarca, el botón vuelve a deshabilitarse.

#### `ejercicio4.py` - Selección Múltiple de Frutas

Permite al usuario seleccionar múltiples elementos de una lista y mostrarlos.

- **Widgets utilizados**: `Listbox` (con selección múltiple), `Button`, `messagebox`.
- **Funcionalidad**: Los usuarios pueden elegir varias frutas de una lista y, al presionar un botón, verán las frutas seleccionadas en un cuadro de mensaje.

#### `ejercicio5.py` - Sistema de Inventario con Pestañas

Una aplicación más compleja que simula un sistema de gestión de inventario.

- **Widgets utilizados**: `ttk.Notebook` (para las pestañas "Registro de Producto" e "Inventario"), `Entry`, `ttk.Combobox`, `ttk.Treeview` (para mostrar la lista de productos), `ttk.Scrollbar`.
- **Funcionalidad**:
  - **Registro**: Permite ingresar nombre, precio y categoría de un producto.
  - **Inventario**: Muestra los productos agregados en una tabla interactiva (`Treeview`).
  - Incluye botones para **agregar**, **limpiar** campos, **eliminar** productos seleccionados y **ver detalles** de un producto en una ventana emergente.

#### `ejercicio6.py` - Aplicación de Nutricionista (Frontend)

La aplicación principal del TP, que integra la lógica de la base de datos del **TP7** con una interfaz gráfica completa. Este ejercicio actúa como el **frontend** para el **backend** de gestión de nutricionista.

- **Integración**: Importa las clases y el repositorio (`NutricionistaRepo`) desde el archivo `nutricionista.py` del directorio `TP7`.
- **Widgets utilizados**: `ttk.Notebook` (pestañas para Pacientes, Alimentos, Planes de Comidas), `Entry`, `ttk.Treeview`, `ttk.Combobox`, `Button`, `messagebox`.
- **Funcionalidad**:
  - **Pestaña Pacientes**: Permite agregar nuevos pacientes, listar pacientes y eliminar pacientes existentes.
  - **Pestaña Alimentos**: Permite agregar nuevos alimentos, listar alimentos y eliminar alimentos existentes.
  - **Pestaña Planes de Comidas**: Permite registrar planes de comida asociando un paciente, un alimento, una cantidad y la fecha actual. También permite listar y eliminar planes de comida.
  - Todos los datos se persisten en la base de datos `nutricionista.db` gestionada por el módulo del TP7.

---

### Contacto

Para cualquier consulta o comentario, puedes contactarme a través de [LinkedIn](https://www.linkedin.com/in/nkaminski-profile/) o [GitHub](https://github.com/N-Kaminski).

---

¡Gracias por revisar mi proyecto!
