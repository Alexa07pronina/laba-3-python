from src.commands import commands
def main():
    """Основная функция обработки пользовательского ввода"""

    print("Доступные команды:")
    print("Математика: factorial <n>, factorial_recursive <n>, fibo <n>, fibo_recursive <n>")
    print("Сортировки: bubble_sort <array>, quick_sort <array>, counting_sort <array>, heap_sort <array>, "
          "radix_sort <array> <optional base>, bucket_sort <array> <optional buckets>")
    print("Генераторы: rand_int_array <size> <low> <high> <optional seed>, nearly_sorted <size> <swaps> <optional seed>,"
          " reverse_sorted <size>, rand_float_array <size> <low> <high> <optional seed>, many_duplicates <size> <k_uniq> <optional seed>")
    print("Структуры: stack <command> <arg>, queue <command> <arg>")
    print("    stack: peek, pop, push <arg>, min, is_empty,len")
    print("    queue: front, dequeue, enqueue <arg>, is_empty,len")
    print("Тайминг: timeit_once <sorting> <arr>")
    print("Выход: q, quit\n")
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
