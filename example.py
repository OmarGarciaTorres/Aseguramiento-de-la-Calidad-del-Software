def greet(name="CI Pipeline"):
    """Devuelve un saludo personalizado."""
    return f"Hello, {name}!"

def add_numbers(a, b):
    """Suma dos números."""
    return a + b

def is_even(number):
    """Verifica si un número es par."""
    return number % 2 == 0

def divide_numbers(a, b):
    """Divide dos números. Lanza una excepción si el divisor es cero."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

def find_max(numbers):
    """Encuentra el número máximo en una lista."""
    if not numbers:
        raise ValueError("The list cannot be empty")
    return max(numbers)
