def bubble_sort(a: list) -> list:
    """Пузырьковая сортировка"""
    if not all(isinstance(x, (int, float)) for x in a):
        if not all(isinstance(x, str) for x in a):
            raise TypeError("Элементы должны быть одинакового типа")
    arr = a.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(a: list) -> list:
    """Быстрая сортировка"""
    if not all(isinstance(x, (int, float)) for x in a):
        raise TypeError("Элементы должны быть числами")

    if len(a) <= 1:
        return a.copy()

    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


def counting_sort(a: list) -> list:
    """Сортировка подсчетом"""
    if not all(isinstance(x, int) for x in a):
        raise TypeError("Counting sort работает только с целыми числами")

    if not a:
        return []

    min_val = min(a)
    max_val = max(a)
    count = [0] * (max_val - min_val + 1)

    for num in a:
        count[num - min_val] += 1

    sorted_arr = []
    for i in range(len(count)):
        cnt = count[i]
        sorted_arr.extend([i + min_val] * cnt)

    return sorted_arr


def radix_sort(a: list, base: int = 10) -> list:
    """Поразрядная сортировка"""
    if not all(isinstance(x, int) for x in a):
        raise TypeError("Radix sort работает только с целыми числами")

    if not a:
        return []

    arr = a.copy()
    max_num = max(arr)
    exp = 1

    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp, base)
        exp *= base

    return arr


def counting_sort_for_radix(arr, exp, base):
    """Вспомогательная функция для поразрядной сортировки"""
    n = len(arr)
    output = [0] * n
    count = [0] * base

    for i in range(n):
        index = (arr[i] // exp) % base
        count[index] += 1

    for i in range(1, base):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] // exp) % base
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]


def bucket_sort(a: list, buckets: int | None = None) -> list:
    """Сортировка ведрами"""
    if not all(isinstance(x, (int, float)) for x in a):
        raise TypeError("Элементы должны быть числами")

    if not a:
        return []

    if buckets is None:
        buckets = len(a)

    min_val = min(a)
    max_val = max(a)

    if min_val == max_val:
        return a.copy()

    normalized = [(x - min_val) / (max_val - min_val) for x in a]
    bucket_list = [[] for i in range(buckets)]

    for num in normalized:
        index = int(num * buckets)
        if index == buckets:
            index -= 1
        bucket_list[index].append(num)

    for bucket in bucket_list:
        insertion_sort(bucket)

    sorted_normalized = []
    for bucket in bucket_list:
        sorted_normalized.extend(bucket)

    return [x * (max_val - min_val) + min_val for x in sorted_normalized]


def insertion_sort(bucket):
    """Сортировка вставками для небольших списков"""
    for i in range(1, len(bucket)):
        key = bucket[i]
        j = i - 1
        while j >= 0 and bucket[j] > key:
            bucket[j + 1] = bucket[j]
            j -= 1
        bucket[j + 1] = key


def heapify(arr, n, i):
    """Вспомогательная функция для построения кучи"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr: list) -> list:
    """Сортировка кучей"""
    if not all(isinstance(x, (int, float)) for x in arr):
        raise TypeError("Элементы должны быть числами")

    n = len(arr)
    result = arr.copy()

    for i in range(n // 2 - 1, -1, -1):
        heapify(result, n, i)

    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        heapify(result, i, 0)

    return result
