-- Base de Datos NetDare Bot
CREATE DATABASE IF NOT EXISTS netdare_db;
USE netdare_db;

-- Tabla de Usuarios del Juego
CREATE TABLE IF NOT EXISTS usuarios_juego (
    id INT PRIMARY KEY AUTO_INCREMENT,
    dni VARCHAR(15) UNIQUE NOT NULL,
    nombre_completo VARCHAR(100) NOT NULL,
    telefoneo VARCHAR(15),
    foto_url VARCHAR(255),
    edad INT,
    profesion VARCHAR(50),
    dinero_juego INT DEFAULT 0,
    nivel INT DEFAULT 1,
    estado_civil VARCHAR(20),
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE
);

-- Tabla de Usuarios Telegram
CREATE TABLE IF NOT EXISTS usuarios_telegram (
    id INT PRIMARY KEY AUTO_INCREMENT,
    telegram_id BIGINT UNIQUE NOT NULL,
    nombre_usuario VARCHAR(100),
    usuario_juego_id INT,
    creditos INT DEFAULT 0,
    plan VARCHAR(20) DEFAULT 'basico',
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    activo BOOLEAN DEFAULT TRUE,
    FOREIGN KEY (usuario_juego_id) REFERENCES usuarios_juego(id)
);

-- Tabla de Transacciones de Créditos
CREATE TABLE IF NOT EXISTS transacciones_creditos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_telegram_id BIGINT NOT NULL,
    tipo VARCHAR(20),
    cantidad INT NOT NULL,
    razon VARCHAR(255),
    admin_id BIGINT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_telegram_id) REFERENCES usuarios_telegram(telegram_id)
);

-- Tabla de Búsquedas
CREATE TABLE IF NOT EXISTS busquedas (
    id INT PRIMARY KEY AUTO_INCREMENT,
    usuario_telegram_id BIGINT NOT NULL,
    tipo_busqueda VARCHAR(20),
    criterio VARCHAR(100),
    usuario_encontrado_id INT,
    creditos_gastados INT,
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_telegram_id) REFERENCES usuarios_telegram(telegram_id),
    FOREIGN KEY (usuario_encontrado_id) REFERENCES usuarios_juego(id)
);

-- Tabla de Planes
CREATE TABLE IF NOT EXISTS planes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50) UNIQUE NOT NULL,
    limites_busquedas_semana INT,
    precio INT,
    descripcion VARCHAR(255),
    activo BOOLEAN DEFAULT TRUE
);

-- Insertar planes por defecto
INSERT INTO planes (nombre, limites_busquedas_semana, precio, descripcion) VALUES
('gratis', 5, 0, 'Plan gratuito - 5 búsquedas por semana'),
('basico', 50, 10000, 'Plan básico - 50 búsquedas por semana'),
('premium', 200, 50000, 'Plan premium - 200 búsquedas por semana'),
('elite', 500, 150000, 'Plan elite - Búsquedas ilimitadas');
