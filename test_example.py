import pytest
from example import greet, add_numbers, is_even, divide_numbers, find_max

def test_greet_default():
    """Prueba el saludo por defecto."""
    assert greet() == "Hello, CI Pipeline!"

def test_greet_custom_name():
    """Prueba el saludo con un nombre personalizado."""
    assert greet("Alice") == "Hello, Alice!"

def test_add_numbers():
    """Prueba la suma de dos números."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_is_even():
    """Prueba para verificar si un número es par o impar."""
    assert is_even(4) is True
    assert is_even(5) is False

def test_divide_numbers():
    """Prueba la división de números."""
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(3, 1) == 3

    with pytest.raises(ValueError):
        divide_numbers(10, 0)

def test_find_max():
    """Prueba para encontrar el número máximo en una lista."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3]) == -1

    with pytest.raises(ValueError):
        find_max([])
