import ast
from src.data_structures import Stack, Queue
from src.constants import func
from src.generators import rand_int_array, nearly_sorted, reverse_sorted, rand_float_array,many_duplicates
stack = Stack()
queue = Queue()

def commands(command: str, args: list):
    if command in ["factorial", "factorial_recursive", "fibo", "fibo_recursive"]:
        n = int(args[0])
        print(func[command](n))
    elif command in ["bubble_sort", "quick_sort", "counting_sort", "heap_sort"]:
        arr = ast.literal_eval(args[0])
        print(func[command](arr))
    elif command == "radix_sort":
        arr = ast.literal_eval(args[0])
        base = 10
        if len(args) > 1:
            base = int(args[1])
        print(func[command](arr, base))
    elif command == "bucket_sort":
        arr = ast.literal_eval(args[0])
        bucket = None
        if len(args) > 1:
            bucket = int(args[1])
        print(func[command](arr, bucket))
    elif (command == "stack" or command == "queue") and args:
        subcommand = args[0].lower()
        subargs = args[1:]
        if subcommand == "push":
            if not subargs:
                print("Ошибка: требуется значение для push")
            try:
                value_str = subargs[0]
                if value_str.startswith('"') and value_str.endswith('"'):
                    value = value_str[1:-1]
                else:
                    value = float(value_str) if '.' in value_str else int(value_str)
                stack.push(value)
                print(f"Элемент {value} добавлен в стек")
            except ValueError:
                print(f"Ошибка: '{value_str}' не является числом")
            except Exception as e:
                print(f"Ошибка: {e}")

        elif subcommand == "pop":
            try:
                value = stack.pop()
                print(f"Извлечено: {value}")
            except IndexError as e:
                print(f"Ошибка: {e}")

        elif subcommand == "peek":
            try:
                value = stack.peek()
                print(f"Верхний элемент: {value}")
            except IndexError as e:
                print(f"Ошибка: {e}")

        elif subcommand == "min":
            try:
                value = stack.min()
                print(value)
            except Exception as e:
                print(f"Ошибка: {e}")
        elif subcommand == "is_empty" and command == "stack":
            print("Стек пуст" if stack.is_empty() else "Стек не пуст")
        elif subcommand == "is_empty" and command == "queue":
            print("Очередь пустая" if queue.is_empty() else "Очередь не пустая")

        elif subcommand == "len" and command == "stack":
            print(f"Размер: {len(stack)}")
        elif subcommand == "len" and command == "queue":
            print(f"Размер: {len(queue)}")
        elif subcommand == "enqueue":
            if not subargs:
                print("Ошибка: требуется значение для push")
            try:
                value = subargs[0]
                queue.enqueue(value)
                print(f"Добавлен элемент в очередь: {value}")
            except Exception as e:
                print(f"Ошибка: {e}")
        elif subcommand == "dequeue":
            try:
                value = queue.dequeue()
                print(f"Удалено: {value}")
            except Exception as e:
                print(f"Ошибка: {e}")
        elif subcommand == "front":
            try:
                print(queue.front())
            except Exception as e:
                print(f"Ошибка: {e}")
        else:
            print(f"Неизвестная подкоманда: {subcommand}")

    elif command == "rand_int_array":
        try:
            size, low, high = map(int, args[0:3])
            distinct = False
            seed = None
            if len(args) > 3:
                if args[3] in ["True", "False"]:
                    distinct = args[3]
                    if args[4]:
                        seed = int(args[4])
                else:
                    seed = int(args[3])
            print(rand_int_array(size, low, high, distinct, seed))
        except Exception as e:
            print(f"Ошибка: {e}")

    elif command == "nearly_sorted":
        try:
            size, swaps = map(int, args[0:2])
            seed = None
            if len(args) > 2:
                seed = int(args[2])
            print(nearly_sorted(size, swaps, seed))
        except Exception as e:
            print(f"Ошибка: {e}")

    elif command == "reverse_sorted":
        try:
            size = int(args[0])
            print(reverse_sorted(size))
        except Exception as e:
            print(f"Ошибка: {e}")


    elif command == "rand_float_array":
        try:
            size = int(args[0])
            low, high = map(float, args[1:3])
            seed = None
            if len(args) > 3:
                seed = int(args[3])
            print(rand_float_array(size, low, high, seed))

        except Exception as e:
            print(f"Ошибка: {e}")

    elif command == "many_duplicates":
        try:
            n, k = map(int, args[0:2])
            seed = None
            if len(args) > 2:
                seed = int(args[2])
            print(many_duplicates(n, k, seed))
        except Exception as e:
            print(f"Ошибка: {e}")
    else:
        print(f"Неизвестная команда: {command}")
