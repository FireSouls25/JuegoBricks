def fibonacci(n):
    if n < 0:
        raise ValueError("El número no puede ser negativo")
    if n == 0:
        return []
    if n == 1:
        return [0]
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    return fib