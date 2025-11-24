import time
from typing import Callable


def timeit_once(func: Callable, *args, **kwargs) -> float:
    """Измеряет время выполнения функции один раз"""
    start = time.time()
    func(*args, **kwargs)
    end = time.time()
    return end - start