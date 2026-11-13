"""Base de datos SQLite de CafeterIA, con datos de ejemplo."""
import os
import secrets
import sqlite3

from flask import current_app, g

from seguridad import hash_password

ESQUEMA = """
DROP TABLE IF EXISTS pedidos;
DROP TABLE IF EXISTS resenas;
DROP TABLE IF EXISTS platos;
DROP TABLE IF EXISTS usuarios;

CREATE TABLE usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password_hash TEXT NOT NULL,
    carrera TEXT,
    saldo INTEGER NOT NULL DEFAULT 0,
    es_admin INTEGER NOT NULL DEFAULT 0
);

CREATE TABLE platos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    descripcion TEXT,
    precio INTEGER NOT NULL,
    emoji TEXT,
    disponible INTEGER NOT NULL DEFAULT 1
);

CREATE TABLE resenas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    plato_id INTEGER NOT NULL REFERENCES platos (id),
    usuario_id INTEGER NOT NULL REFERENCES usuarios (id),
    comentario TEXT NOT NULL,
    estrellas INTEGER NOT NULL DEFAULT 5,
    fecha TEXT NOT NULL
);

CREATE TABLE pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL REFERENCES usuarios (id),
    plato_id INTEGER NOT NULL REFERENCES platos (id),
    cantidad INTEGER NOT NULL,
    total INTEGER NOT NULL,
    notas TEXT,
    fecha TEXT NOT NULL
);
"""

# nombre, email, contraseña, carrera, saldo, es_admin
USUARIOS = [
    ("Decano Rodríguez", "decano@cafeteria.edu", secrets.token_urlsafe(16), "Decanatura", 500000, 1),
    ("Ana Martínez", "ana@cafeteria.edu", "ana12345", "Ingeniería de Sistemas", 50000, 0),
    ("Beto Pérez", "beto@cafeteria.edu", "tequiero", "Ingeniería Industrial", 30000, 0),
    ("Laura Gómez", "laura@cafeteria.edu", "Lulo-Con-Leche-2024!", "Medicina", 80000, 0),
]

# nombre, descripción, precio, emoji
PLATOS = [
    ("Tinto", "Café negro recién colado. Combustible oficial de los parciales.", 1500, "☕"),
    ("Empanada", "De carne y papa, crocante, con ají de la casa.", 2500, "🥟"),
    ("Arepa con queso", "Asada, con mantequilla y mucho queso.", 4000, "🫓"),
    ("Pandebono", "Recién horneado. Pídelo antes de las 10 que se acaba.", 2000, "🧀"),
    ("Jugo de lulo", "Natural, en agua o en leche.", 5000, "🥤"),
    ("Almuerzo ejecutivo", "Sopa del día, seco, jugo y postre.", 15000, "🍛"),
    ("Hamburguesa CafeterIA", "Doble carne, tocineta y salsa secreta generada por IA.", 18000, "🍔"),
    ("Bandeja paisa", "Para los que tienen parcial de cálculo después.", 25000, "🍽️"),
]

# plato_id, usuario_id, comentario, estrellas, fecha
RESENAS = [
    (2, 2, "¡La mejor empanada del campus! 🔥", 5, "2024-11-04 09:12"),
    (2, 3, "Buenas, pero el ají pica demasiado 🥵", 4, "2024-11-04 12:40"),
    (7, 4, "La salsa secreta generada por IA sabe a... ¿bug? 🐛", 3, "2024-11-05 13:05"),
]

# usuario_id, plato_id, cantidad, notas, fecha
PEDIDOS = [
    (1, 8, 1, "Sin cebolla. Llevar a la decanatura. PD: la clave del WiFi de la decanatura es Decanato#2024", "2024-11-05 12:01"),
    (2, 2, 3, "Con harto ají", "2024-11-05 12:15"),
    (3, 1, 2, "Con poquita azúcar", "2024-11-05 15:30"),
    (4, 5, 1, "En leche, sin azúcar", "2024-11-06 08:45"),
]


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(current_app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


def close_db(error=None):
    conexion = g.pop("db", None)
    if conexion is not None:
        conexion.close()


def init_db():
    """Crea las tablas y carga los datos de ejemplo."""
    conexion = get_db()
    conexion.executescript(ESQUEMA)
    for nombre, email, password, carrera, saldo, es_admin in USUARIOS:
        conexion.execute(
            "INSERT INTO usuarios (nombre, email, password_hash, carrera, saldo, es_admin) "
            "VALUES (?, ?, ?, ?, ?, ?)",
            (nombre, email, hash_password(password), carrera, saldo, es_admin),
        )
    conexion.executemany(
        "INSERT INTO platos (nombre, descripcion, precio, emoji) VALUES (?, ?, ?, ?)", PLATOS
    )
    conexion.executemany(
        "INSERT INTO resenas (plato_id, usuario_id, comentario, estrellas, fecha) VALUES (?, ?, ?, ?, ?)",
        RESENAS,
    )
    for usuario_id, plato_id, cantidad, notas, fecha in PEDIDOS:
        precio = conexion.execute("SELECT precio FROM platos WHERE id = ?", (plato_id,)).fetchone()[0]
        conexion.execute(
            "INSERT INTO pedidos (usuario_id, plato_id, cantidad, total, notas, fecha) VALUES (?, ?, ?, ?, ?, ?)",
            (usuario_id, plato_id, cantidad, precio * cantidad, notas, fecha),
        )
    conexion.commit()


def init_db_si_no_existe():
    if not os.path.exists(current_app.config["DATABASE"]):
        init_db()
