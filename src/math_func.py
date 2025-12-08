def factorial(n: int) -> int:
    """Итеративный подсчет факториала"""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_recursive(n: int) -> int:
    """Рекурсивный подсчет факториала"""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0 or n == 1:
        return 1
    return n * factorial_recursive(n - 1)

def fibo(n: int) -> int:
    """Итеративный подсчет числа Фибоначчи"""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def fibo_recursive(n: int) -> int:
    """Рекурсивный подсчет числа Фибоначчи"""
    if n < 0:
        raise ValueError("n должно быть неотрицательным")
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibo_recursive(n - 1) + fibo_recursive(n - 2)
