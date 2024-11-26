import pytest
from example import greet, add_numbers, is_even, divide_numbers, find_max

def test_greet_default():
    """Prueba el saludo por defecto."""
    assert greet() == "Hello, CI Pipeline!"

def test_greet_custom_name():
    """Prueba el saludo con un nombre personalizado."""
    assert greet("Alice") == "Hello, Alice!"

def test_greet_edge_cases():
    """Prueba casos límite para greet."""
    assert greet("") == "Hello, !"
    assert greet("A"*1000) == f"Hello, {'A'*1000}!"

def test_add_numbers():
    """Prueba la suma de dos números."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0

def test_add_numbers_edge_cases():
    """Prueba casos límite para add_numbers."""
    assert add_numbers(1.5, 2.5) == 4.0
    assert add_numbers(1e10, 1e10) == 2e10

def test_is_even():
    """Prueba para verificar si un número es par o impar."""
    assert is_even(4) is True
    assert is_even(5) is False

def test_is_even_edge_cases():
    """Prueba casos límite para is_even."""
    assert is_even(-2) is True
    assert is_even(-3) is False
    assert is_even(10**6) is True

def test_divide_numbers():
    """Prueba la división de números."""
    assert divide_numbers(10, 2) == 5
    assert divide_numbers(3, 1) == 3

    with pytest.raises(ValueError):
        divide_numbers(10, 0)

def test_divide_numbers_edge_cases():
    """Prueba casos límite para divide_numbers."""
    assert divide_numbers(-10, 2) == -5
    assert divide_numbers(10, -2) == -5
    assert divide_numbers(1, 3) == pytest.approx(0.333, rel=1e-3)

def test_find_max():
    """Prueba para encontrar el número máximo en una lista."""
    assert find_max([1, 2, 3, 4, 5]) == 5
    assert find_max([-1, -2, -3]) == -1

    with pytest.raises(ValueError):
        find_max([])

def test_find_max_edge_cases():
    """Prueba casos límite para find_max."""
    assert find_max([42]) == 42
    assert find_max([i for i in range(1000)]) == 999
