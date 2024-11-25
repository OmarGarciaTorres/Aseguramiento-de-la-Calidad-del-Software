"""
Pruebas unitarias para las funciones del módulo example.py.
"""
import pytest
from example import greet, add_numbers, is_even

def test_greet_default():
    assert greet() == "Hello, CI Pipeline!"

def test_greet_custom_name():
    assert greet("John") == "Hello, John!"

def test_add_numbers():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0

def test_is_even():
    assert is_even(4) is True
    assert is_even(3) is False
