-- PASO 1: Crea la tabla para los tipos de membresía.
CREATE TABLE tipos_membresia (
    id_membresia SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL,
    descripcion TEXT
);

-- PASO 2: Crea la tabla de clientes, referenciando a la tabla de membresías.
CREATE TABLE cliente (
    id_cliente SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL,
    id_membresia INTEGER NOT NULL,   
    fecha_registro DATE NOT NULL DEFAULT CURRENT_DATE,
    email VARCHAR(100) UNIQUE,
    -- Definimos la restricción de la clave foránea.
    CONSTRAINT fk_membresia
        FOREIGN KEY(id_membresia) 
        REFERENCES tipos_membresia(id_membresia)
);

-- PASO 3 (Ejemplo): Insertar algunos tipos de membresía.
INSERT INTO tipos_membresia (nombre, precio) VALUES 
('Plan Básico', 50000.00),
('Plan Premium', 85000.00),
('Plan VIP', 120000.00);

-- PASO 4 (Ejemplo): Inserta un cliente de prueba.
INSERT INTO cliente (nombre, apellido, id_membresia, email) VALUES
('Carlos', 'Pérez', 2, 'carlos.perez@email.com'); -- Carlos tiene el Plan Premium (ID 2)

--SELECT * from cliente;