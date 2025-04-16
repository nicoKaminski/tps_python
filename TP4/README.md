# Trabajo Práctico Nro. 4 - Gestión de Archivos

Este directorio contiene los ejercicios correspondientes al Trabajo Práctico número 4 de la materia Python, enfocados en la gestión de archivos.

**Estructura de los Ejercicios:**

- **`ejercicio1.py`**: Programa que pide un número entero entre 1 y 10 y muestra la tabla de multiplicar correspondiente desde el archivo `tabla-n.txt`.
- **`ejercicio2.py`**: Programa que pide dos números enteros entre 1 y 10 (n y m) y muestra la línea m de la tabla de multiplicar n desde el archivo `tabla-n.txt`.
- **`ejercicio3.py`**: Programa para gestionar una agenda telefónica con funcionalidades para agregar, buscar y eliminar contactos, almacenados en el archivo `agenda.txt`.

## Ejercicio 1: `ejercicio1.py`

Programa que interactúa con archivos de tablas de multiplicar (del 1 al 10) almacenados en una subcarpeta llamada `tablas`.

**Funcionalidades:**

- **`crear_tablas()`**: Crea la carpeta `tablas` (si no existe) y genera los archivos `tabla-1.txt` hasta `tabla-10.txt`, cada uno conteniendo la tabla de multiplicar correspondiente.
- **`pedir_numero()`**: Pide al usuario un número (n) entre 1 y 10 para seleccionar la tabla.
- **`mostrar_tabla(carpeta_tablas)`**: Pide el número n al usuario, lee el archivo `tabla-n.txt` y muestra su contenido completo. Si el archivo no existe, muestra un mensaje.

## Ejercicio 2: `ejercicio2.py`

Programa que interactúa con archivos de tablas de multiplicar (del 1 al 10) almacenados en una subcarpeta llamada `tablas`.

**Funcionalidades:**

- **`crear_tablas()`**: Crea la carpeta `tablas` (si no existe) y genera los archivos `tabla-1.txt` hasta `tabla-10.txt`, cada uno conteniendo la tabla de multiplicar correspondiente.
- **`pedir_numero()`**: Pide al usuario un número (n) entre 1 y 10 para seleccionar la tabla.
- **`pedir_linea()`**: Pide al usuario un número (m) entre 1 y 10 para seleccionar la línea de la tabla.
- **`mostrar_tabla(carpeta_tablas)`**: Pide los números n y m al usuario, lee el archivo `tabla-n.txt` y muestra la línea m. Si el archivo no existe, muestra un mensaje.

## Ejercicio 3: `ejercicio3.py` (Gestión de Agenda Telefónica)

Programa para gestionar una agenda telefónica con nombres y teléfonos de clientes de una empresa. La agenda se guarda en el archivo `agenda.txt`.

**Funcionalidades:**

- **`crea_directorio(archivo)`**: Crea un archivo vacío para la agenda si no existe.
- **`agrega_contacto(archivo, cliente, telf)`**: Añade un nuevo contacto (nombre y teléfono) a la agenda.
- **`busca_contacto(archivo, cliente)`**: Busca y muestra el teléfono de un cliente.
- **`elimina_contacto(archivo, cliente)`**: Elimina un contacto de la agenda.
- **`menu()`**: Presenta un menú con las opciones disponibles.
- **`Principal()`**: Lanza la aplicación de la agenda.

## Estructura de Carpetas:

- **`tp4/`**: Contiene los tres archivos de ejercicios:
  - `ejercicio1.py`
  - `ejercicio2.py`
  - `ejercicio3.py`
  - `tablas/` (se crea al ejecutar `ejercicio1.py` o `ejercicio2.py`)
    - `tabla-1.txt`
    - `tabla-2.txt`
    - ...
    - `tabla-10.txt`
  - `agenda.txt` (se crea al ejecutar `ejercicio3.py`)

## Contacto

Para cualquier consulta o comentario, puedes contactarme a través de [LinkedIn](https://www.linkedin.com/in/nkaminski-profile/) o [GitHub](https://github.com/N-Kaminski).

---

¡Gracias por revisar mi proyecto!
