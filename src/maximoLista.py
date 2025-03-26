def maximo(lista):
    if not lista:
        raise ValueError("La lista no puede estar vacía")
    return max(lista)
