from src.commands import commands
def main():
    """Основная функция обработки пользовательского ввода"""
    print("Доступные команды:")
    print("Математика: factorial <n>, factorial_recursive <n>, fibo <n>, fibo_recursive <n>")
    print("Сортировки: bubble_sort <array>, quick_sort, counting_sort, heap_sort, radix_sort, bucket_sort")
    print("Генераторы: rand_int_array <size> <low> <high> <optional seed>, nearly_sorted, reverse_sorted, rand_float_array, many_duplicates")
    print("Структуры: stack <command> <arg>, queue <command> <arg>")
    print("    stack: peek, pop, push <arg>, min, is_empty,__len__")
    print("    queue: front, dequeue, enqueue <arg>, is_empty,__len__")
    print("Выход: q, quit")
    while True:
        try:
            line = input("\nВведите команду ").strip()
            if line=='q' or line=='quit':
                break

            parts = line.split()
            if parts and parts[0].isdigit():
                parts = parts[1:]

            if not parts:
                continue

            command = parts[0]
            args = parts[1:]
            commands(command,args)

        except Exception as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    main()
