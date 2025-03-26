import pytest
from fibonacci import fibonacci

def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(5) == [0, 1, 1, 2, 3]

def test_fibonacci_negativo():
    with pytest.raises(ValueError):
        fibonacci(-1)