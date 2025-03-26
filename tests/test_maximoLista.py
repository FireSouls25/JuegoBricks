import pytest
from src.maximoLista import maximo

def test_maximo():
    assert maximo([1, 2, 3, 4, 5]) == 5
    assert maximo([-10, -5, 0, 5, 10]) == 10

def test_maximo_lista_vacia():
    with pytest.raises(ValueError):
        maximo([])