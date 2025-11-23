class Stack:
    """Стек, реализованный на основе списка"""

    def __init__(self):
        self.items = []
        self.data_type = None
        self.min_stack = []

    def _validate_type(self, x):
        """Проверка соответствия типа элемента типу стека"""
        if isinstance(x, (int, float)):
            current_type = 'number'
        elif isinstance(x, str):
            current_type = 'string'
        else:
            raise TypeError("Стек поддерживает только числа и строки")

        if self.data_type is None:
            self.data_type = current_type
        elif self.data_type != current_type:
            if self.data_type == 'number':
                raise TypeError("Стек содержит числа, нельзя добавить строку")
            else:
                raise TypeError("Стек содержит строки, нельзя добавить число")

    def push(self, x):
        """Добавление элемента в стек с проверкой типа"""
        self._validate_type(x)
        self.items.append(x)
        if len(self.min_stack)==0 or x<self.min_stack[-1]:
            self.min_stack.append(x)

    def pop(self):
        """Удаление элемента из стека"""
        if self.is_empty():
            raise IndexError("pop из пустого стека")
        value = self.items.pop()
        if self.is_empty():
            self.data_type = None
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def peek(self):
        """Просмотр верхнего элемента"""
        if self.is_empty():
            raise IndexError("peek из пустого стека")
        return self.items[-1]

    def is_empty(self) -> bool:
        """Проверка на пустоту"""
        return len(self.items) == 0

    def __len__(self):
        """Длина стека"""
        return len(self.items)
    def min(self):
        if len(self.min_stack)!=0:
            return self.min_stack[-1]
        else:
            raise Exception("Пустой стек")



class Queue:
    """Очередь, реализованная на основе списка"""

    def __init__(self):
        self.items = []

    def enqueue(self, x):
        """Добавление элемента в очередь"""
        self.items.append(x)

    def dequeue(self):
        """Удаление элемента из очереди"""
        if self.is_empty():
            raise IndexError("dequeue из пустой очереди")
        return self.items.pop(0)

    def front(self):
        """Просмотр первого элемента"""
        if self.is_empty():
            raise IndexError("front из пустой очереди")
        return self.items[0]

    def is_empty(self) -> bool:
        """Проверка на пустоту"""
        return len(self.items) == 0

    def __len__(self):
        """Длина очереди"""
        return len(self.items)
