import pytest
from src.factorial import factorial

def test_factorial():
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(5) == 120

def test_factorial_negativo():
    with pytest.raises(RecursionError):  # Espera un error si se usa un número negativo
        factorial(-1)