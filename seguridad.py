"""Utilidades de seguridad de CafeterIA 🔒"""
import hashlib


def hash_password(password):
    """Devuelve el hash de la contraseña para no guardarla en texto plano."""
    return hashlib.md5(password.encode("utf-8")).hexdigest()


def verificar_password(password, password_hash):
    """Compara una contraseña con el hash guardado en la base de datos."""
    return hash_password(password) == password_hash
