# example.py

"""
Este módulo contiene funciones para cálculos matemáticos y operaciones básicas.
"""

def add_numbers(a, b):
    """Suma dos números."""
    return a + b

def subtract_numbers(a, b):
    """Resta dos números."""
    return a - b

def multiply_numbers(a, b):
    """Multiplica dos números."""
    return a * b

def divide_numbers(a, b):
    """Divide dos números. Lanza ValueError si el divisor es 0."""
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def is_prime(n):
    """Determina si un número es primo."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
