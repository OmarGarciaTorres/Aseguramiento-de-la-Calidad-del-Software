"""
Este módulo contiene funciones de ejemplo.
"""

def greet(name="CI Pipeline"):
    """
    Devuelve un saludo personalizado.
    
    Args:
        name (str): Nombre de la persona a saludar.
    Returns:
        str: Saludo personalizado.
    """
    return f"Hello, {name}!"

def add_numbers(a, b):
    """
    Suma dos números.
    
    Args:
        a (int): Primer número.
        b (int): Segundo número.
    Returns:
        int: Resultado de la suma.
    """
    return a + b

def is_even(number):
    """
    Verifica si un número es par.
    
    Args:
        number (int): Número a verificar.
    Returns:
        bool: True si es par, False si es impar.
    """
    return number % 2 == 0
