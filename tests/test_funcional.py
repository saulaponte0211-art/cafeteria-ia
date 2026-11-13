"""Pruebas funcionales de CafeterIA.

Estas pruebas NO buscan vulnerabilidades: verifican que la app siga FUNCIONANDO.
Córrelas después de cada corrección:

    pytest

Si una prueba falla después de tu cambio, tu corrección rompió algo. 🔧
Una corrección de seguridad que rompe la app no cuenta como corrección.
"""
import sqlite3
from contextlib import closing

import pytest

from app import create_app


@pytest.fixture
def app(tmp_path):
    return create_app(
        {
            "TESTING": True,
            "DATABASE": str(tmp_path / "prueba.db"),
            "LOG_FILE": str(tmp_path / "prueba.log"),
        }
    )


@pytest.fixture
def cliente(app):
    return app.test_client()


def entrar(cliente, email="ana@cafeteria.edu", password="ana12345", siguiente=None):
    url = "/login" + (f"?next={siguiente}" if siguiente else "")
    return cliente.post(url, data={"email": email, "password": password})


def consultar(app, sql, parametros=()):
    with closing(sqlite3.connect(app.config["DATABASE"])) as conexion:
        conexion.row_factory = sqlite3.Row
        return conexion.execute(sql, parametros).fetchone()


def texto(respuesta):
    return respuesta.get_data(as_text=True)


def test_menu_principal(cliente):
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200
    assert "Empanada" in texto(respuesta)


def test_buscar_platos(cliente):
    assert "Arepa con queso" in texto(cliente.get("/?q=arepa"))
    assert "No encontramos nada" in texto(cliente.get("/?q=pizza-hawaiana"))


def test_login_correcto(cliente):
    respuesta = entrar(cliente)
    assert respuesta.status_code == 302
    perfil = cliente.get("/perfil")
    assert perfil.status_code == 200
    assert "ana@cafeteria.edu" in texto(perfil)


def test_login_incorrecto(cliente):
    entrar(cliente, password="no-es-mi-clave")
    assert cliente.get("/perfil").status_code == 302


def test_redirige_a_next_despues_del_login(cliente):
    respuesta = entrar(cliente, siguiente="/mis-pedidos")
    assert respuesta.headers["Location"].endswith("/mis-pedidos")


def test_registro_y_login(cliente):
    cliente.post(
        "/registro",
        data={
            "nombre": "Nueva Estudiante",
            "email": "nueva@cafeteria.edu",
            "carrera": "Ingeniería de Sistemas",
            "password": "Una-Clave-Larga-2024",
        },
    )
    entrar(cliente, "nueva@cafeteria.edu", "Una-Clave-Larga-2024")
    assert "nueva@cafeteria.edu" in texto(cliente.get("/perfil"))


def test_publicar_resena(cliente):
    entrar(cliente)
    cliente.post("/plato/2/resena", data={"comentario": "Crocante y deliciosa", "estrellas": "5"})
    assert "Crocante y deliciosa" in texto(cliente.get("/plato/2"))


def test_pedido_descuenta_el_saldo(app, cliente):
    entrar(cliente)
    saldo_antes = consultar(app, "SELECT saldo FROM usuarios WHERE email = 'ana@cafeteria.edu'")["saldo"]
    respuesta = cliente.post(
        "/pedir", data={"plato_id": "2", "cantidad": "2", "precio": "2500", "notas": "Sin ají"}
    )
    assert respuesta.status_code == 302
    saldo_despues = consultar(app, "SELECT saldo FROM usuarios WHERE email = 'ana@cafeteria.edu'")["saldo"]
    assert saldo_antes - saldo_despues == 5000


def test_ver_mi_pedido(cliente):
    entrar(cliente)
    respuesta = cliente.get("/pedido/2")
    assert respuesta.status_code == 200
    assert "Con harto ají" in texto(respuesta)


def test_mis_pedidos(cliente):
    entrar(cliente)
    assert "Empanada" in texto(cliente.get("/mis-pedidos"))


def test_actualizar_perfil(cliente):
    entrar(cliente)
    cliente.post("/perfil", data={"nombre": "Ana María", "carrera": "Ingeniería de Sistemas"})
    assert "Ana María" in texto(cliente.get("/perfil"))


def test_descargar_menu(cliente):
    respuesta = cliente.get("/descargar?archivo=menu-semana.txt")
    assert respuesta.status_code == 200
    assert "MENÚ DE LA SEMANA" in texto(respuesta)


def test_calculadora_de_propinas(cliente):
    assert "123.4" in texto(cliente.get("/propina?expresion=1234*10/100"))


def test_panel_de_administracion(cliente):
    with cliente.session_transaction() as sesion:
        sesion["usuario_id"] = 1
        sesion["es_admin"] = True
    assert cliente.get("/admin").status_code == 200
    exportacion = cliente.get("/admin/exportar-usuarios")
    assert exportacion.status_code == 200
    assert "ana@cafeteria.edu" in texto(exportacion)


def test_estudiante_no_entra_al_admin(cliente):
    entrar(cliente)
    assert cliente.get("/admin").status_code in (302, 403)


def test_pagina_inexistente(cliente):
    assert cliente.get("/esta-pagina-no-existe").status_code == 404
