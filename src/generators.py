import random
from typing import List, Optional


def rand_int_array(size: int, low: int, high: int, distinct: bool = False, seed: Optional[int] = None) -> List[int]:
    """Генерация массива случайных целых чисел"""
    if size < 0:
        raise ValueError(f"size не может быть отрицательным: {size}")
    if low > high:
        raise ValueError(f"low не может быть больше high: low={low}, high={high}")

    if seed is not None:
        random.seed(seed)

    if distinct and (high - low + 1) < size:
        raise ValueError(f"Невозможно сгенерировать {size} уникальных чисел в диапазоне [{low}, {high}]")

    if distinct:
        return random.sample(range(low, high + 1), size)
    else:
        return [random.randint(low, high) for _ in range(size)]


def nearly_sorted(size: int, swaps: int, seed: Optional[int] = None) -> List[int]:
    """Генерация почти отсортированного массива"""

    if size < 0:
        raise ValueError(f"size не может быть отрицательным: {size}")
    if swaps < 0:
        raise ValueError(f"swaps не может быть отрицательным: {swaps}")
    if swaps > size * (size - 1) // 2:
        raise ValueError(f"swaps слишком большой: {swaps} (максимум {size * (size - 1) // 2})")

    if seed is not None:
        random.seed(seed)

    arr = list(range(size))

    for _ in range(swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    return arr


def reverse_sorted(size: int) -> List[int]:
    """Генерация обратно отсортированного массива"""
    if size < 0:
        raise ValueError(f"size не может быть отрицательным: {size}")
    return list(range(size - 1, -1, -1))


def rand_float_array(size: int, low: float = 0.0, high: float = 1.0, seed: Optional[int] = None) -> List[float]:
    """Генерация массива случайных чисел с плавающей точкой"""
    if size < 0:
        raise ValueError(f"size не может быть отрицательным: {size}")
    if low > high:
        raise ValueError(f"low не может быть больше high: low={low}, high={high}")

    if seed is not None:
        random.seed(seed)
    return [random.uniform(low, high) for _ in range(size)]


def many_duplicates(n: int, k_unique: int = 5, seed: Optional[int] = None) -> List[int]:
    """
    Генерация массива с большим количеством дубликатов
    """
    if n > 0 and k_unique > n:
        raise ValueError(f"k_unique ({k_unique}) не может быть больше n ({n})")

    if seed is not None:
        random.seed(seed)

    if n == 0:
        return []
    unique_values = random.sample(range(-n * 2, n * 2), k_unique)
    result = [random.choice(unique_values) for _ in range(n)]

    return result
