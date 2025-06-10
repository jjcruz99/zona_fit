
## Zona Fit - Gestor de Clientes de Gimnasio 

Este proyecto es una aplicación de escritorio desarrollada en Python para la gestión de 
clientes de un gimnasio. Permite realizar operaciones básicas de CRUD (Crear, Leer, Actualizar y Borrar)
sobre los registros de los clientes, todo a través de una interfaz gráfica intuitiva construida con Tkinter.

El objetivo principal es aplicar y demostrar conceptos clave de la programación, como la Programación Orientada 
a Objetos (POO), la gestión de bases de datos con pools de conexiones, el manejo de errores mediante logging y la 
creación de una arquitectura de software organizada (Modelo-Vista-Controlador adaptado).

## Estructura del Proyecto

```text
zona_fit_app/
│
├── main.py                     # Punto de entrada principal de tu aplicación
│
├── config/
│   └── settings.py             # Credenciales de BD)
│
├── src/                        # Directorio principal del código fuente
│   │
│   ├── __init__.py             
│   │
│   ├── models/                 # Clases de objetos de negocio (POO)
│   │   ├── __init__.py
│   │   └── client.py           # Clase Client 
│   │
│   ├── database/               # Para la lógica de acceso a datos y pool de conexiones
│   │   ├── __init__.py
│   │   └── connection.py       # Gestiona el pool de conexiones
│   │   └── client_dao.py       # CRUD operations for clients (Data Access Object)
|   |   └── cursor_from_pool.py #Crear pool de conexiones
│   │
│   ├── gui/                    #Interfaces gráficas con Tkinter
│   │   ├── __init__.py
│   │   └── main_window.py      # Ventana principal de la aplicación
│   │   └── loging.py           # Ventana de login
│   │   
│   │
│   ├── services/               # Lógica de negocio o servicios
│   │   ├── __init__.py
│   │   └── client_service.py   # Lógica de negocio para clientes (usa client_dao)
│   │
│   └── utils/                  # Utilidades, como la configuración del logging
│       ├── __init__.py
│       └── logger_config.py    # Configuración del logging
│
├── tests/                      # Pendiente
│   ├── __init__.py
│   └── (archivos de prueba)
│
├── requirements.txt            # Dependencias del proyecto
└── README.md                   # Descripción del proyecto

##Características Principales
Gestión de Clientes: Añade, actualiza, y elimina clientes de la base de datos.
Visualización de Datos: Muestra un listado completo de todos los clientes registrados en una tabla.
Interfaz Gráfica de Usuario: GUI simple y funcional desarrollada con el framework nativo de Python, 
Tkinter.
Manejo de Errores: Registro detallado de operaciones y errores en un archivo .log para facilitar la 
depuración.
Acceso Seguro: Ventana de login para proteger el acceso a los datos.

##Tecnologías Utilizadas
Lenguaje: Python 3
Base de Datos: PostgreSQL
GUI: Tkinter (Librería estándar de Python)
Conexión a BD: psycopg2 con pool de conexiones.
IDE: PyCharm
Gestor de BD: pgAdmin 4

##Instalación y Puesta en Marcha
Sigue estos pasos para ejecutar el proyecto en tu máquina local.
*Prerrequisitos
Tener instalado Python 3.x.
Tener instalado y corriendo un servidor de PostgreSQL.

##Configurar la Base de Datos:
Abre pgAdmin 4 y crea una nueva base de datos llamada zona_fit.
Ejecuta el script SQL del proyecto para crear las tablas tipos_membresia y cliente.

## Ejecutar la aplicación: python main.py

## Modo de Uso
Inicio de Sesión: Ingresa las credenciales de administrador para acceder a la aplicación.
Añadir un Cliente: Llena los campos del formulario en la parte superior y haz clic en el botón "Guardar".

Actualizar un Cliente:
Selecciona un cliente de la tabla haciendo clic sobre su fila. Sus datos se cargarán en el formulario.
Modifica los datos que desees en los campos del formulario.
Haz clic en el botón "Actualizar".

Eliminar un Cliente:
Selecciona el cliente que deseas eliminar de la tabla.
Haz clic en el botón "Eliminar".

## Estado del Proyecto
Actualmente, el proyecto se encuentra en desarrollo. Las funcionalidades principales de CRUD están 
implementadas y son funcionales. Próximos pasos incluyen la implementación de pruebas unitarias
y la adición de nuevas características.


