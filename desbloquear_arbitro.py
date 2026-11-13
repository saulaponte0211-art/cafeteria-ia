#!/usr/bin/env python3
"""🔒 Desbloquea al Árbitro cuando el instructor diga la clave en voz alta.

Uso, desde la carpeta raíz del proyecto:

    python desbloquear_arbitro.py
    python desbloquear_arbitro.py --equipo "Los Parches"

Nota: el cifrado de este archivo es solo un juego para la clase. En un sistema
real usa librerías criptográficas probadas (por ejemplo «cryptography») en vez
de inventar tu propio cifrado.
"""
import argparse
import base64
import hashlib
import hmac
import os
import subprocess
import sys
import unicodedata
import zlib

RAIZ = os.path.dirname(os.path.abspath(__file__))
CABECERA = "CAFETERIA-ARBITRO-1"
ITERACIONES = 400_000


def normalizar(clave):
    """No importan mayúsculas, tildes, espacios ni signos."""
    sin_tildes = unicodedata.normalize("NFKD", clave).encode("ascii", "ignore").decode()
    return "".join(c for c in sin_tildes.lower() if c.isalnum())


def derivar(clave, sal):
    llave = hashlib.pbkdf2_hmac("sha256", normalizar(clave).encode(), sal, ITERACIONES, dklen=64)
    return llave[:32], llave[32:]


def flujo(llave, longitud):
    partes, total, contador = [], 0, 0
    while total < longitud:
        bloque = hashlib.sha256(llave + contador.to_bytes(8, "big")).digest()
        partes.append(bloque)
        total += len(bloque)
        contador += 1
    return b"".join(partes)[:longitud]


def descifrar(contenido, clave):
    lineas = contenido.strip().splitlines()
    if not lineas or lineas[0].strip() != CABECERA:
        raise ValueError("arbitro.cifrado no tiene el formato esperado")
    datos = base64.b64decode("".join(lineas[1:]))
    sal, etiqueta, cifrado = datos[:16], datos[16:48], datos[48:]
    llave_cifrado, llave_mac = derivar(clave, sal)
    if not hmac.compare_digest(etiqueta, hmac.new(llave_mac, sal + cifrado, hashlib.sha256).digest()):
        return None
    return zlib.decompress(bytes(a ^ b for a, b in zip(cifrado, flujo(llave_cifrado, len(cifrado)))))


def main():
    parser = argparse.ArgumentParser(description="Desbloquea al Árbitro de CafeterIA")
    parser.add_argument("--equipo", default="", help="nombre de tu equipo")
    parser.add_argument("--clave", default="", help="la clave que dijo el instructor")
    argumentos = parser.parse_args()
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

    ruta = os.path.join(RAIZ, "arbitro.cifrado")
    if not os.path.exists(ruta):
        print("❌ No encuentro arbitro.cifrado. ¿Estás en la carpeta raíz del proyecto?")
        return 1
    with open(ruta, encoding="utf-8") as archivo:
        contenido = archivo.read()

    clave = argumentos.clave or input("🔑 Escribe la clave que dijo el instructor: ")
    print("⏳ Verificando la clave...", flush=True)
    codigo = descifrar(contenido, clave)
    if codigo is None:
        print("❌ Clave incorrecta. No importan mayúsculas, tildes ni espacios: escúchala bien e intenta otra vez.")
        return 1

    destino = os.path.join(RAIZ, "arbitro.py")
    with open(destino, "wb") as archivo:
        archivo.write(codigo)
    print("✅ ¡Árbitro desbloqueado! Que comience el juicio...\n", flush=True)
    comando = [sys.executable, destino] + (["--equipo", argumentos.equipo] if argumentos.equipo else [])
    return subprocess.call(comando, cwd=RAIZ)


if __name__ == "__main__":
    sys.exit(main())
