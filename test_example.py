"""
Pruebas unitarias para las funciones del módulo example.py.
"""
# test_example.py
import pytest
from example import add_numbers, subtract_numbers, multiply_numbers, divide_numbers, is_prime

def test_add_numbers():
    """Verifica la suma de dos números."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_subtract_numbers():
    """Verifica la resta de dos números."""
    assert subtract_numbers(5, 3) == 2
    assert subtract_numbers(0, 5) == -5
    assert subtract_numbers(-1, -1) == 0

def test_multiply_numbers():
    """Verifica la multiplicación de dos números."""
    assert multiply_numbers(3, 4) == 12
    assert multiply_numbers(-1, 5) == -5
    assert multiply_numbers(0, 10) == 0

def test_divide_numbers():
    """Verifica la división de dos números."""
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(-10, 2) == -5
    with pytest.raises(ValueError):
        divide_numbers(10, 0)  # Probar división por cero

def test_is_prime():
    """Verifica si un número es primo."""
    assert is_prime(2) is True
    assert is_prime(3) is True
    assert is_prime(4) is False
    assert is_prime(0) is False
    assert is_prime(-5) is False
