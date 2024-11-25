"""
Pruebas unitarias para las funciones del módulo example.py.
"""
from example import greet, add_numbers, is_even

def test_greet_default():
    """
    Verifica que la función greet devuelva el saludo predeterminado.
    """
    assert greet() == "Hello, CI Pipeline!"

def test_greet_custom_name():
    """
    Verifica que la función greet devuelva un saludo personalizado.
    """
    assert greet("John") == "Hello, John!"

def test_add_numbers():
    """
    Verifica que la función add_numbers realice sumas correctamente.
    """
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_is_even():
    """
    Verifica que la función is_even identifique correctamente números pares e impares.
    """
    assert is_even(4) is True
    assert is_even(3) is False
