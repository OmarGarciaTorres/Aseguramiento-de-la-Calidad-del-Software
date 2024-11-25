"""
Este módulo contiene pruebas unitarias para el módulo example.
"""

from example import greet

def test_greet():
    """
    Prueba que la función greet devuelva el saludo esperado.
    """
    assert greet("CI Pipeline") == "Hello, CI Pipeline!"
