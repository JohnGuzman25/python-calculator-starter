"""Core calculator operations with type hints and docstrings."""
from typing import Union

Number = Union[int, float]

def add(a: Number, b: Number) -> Number:
    """Return the sum of a and b."""
    return a + b

def subtract(a: Number, b: Number) -> Number:
    """Return the difference of a and b (a - b)."""
    return a - b

def multiply(a: Number, b: Number) -> Number:
    """Return the product of a and b."""
    return a * b

def divide(a: Number, b: Number) -> float:
    """Return the result of dividing a by b. Raises ValueError if b == 0."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
