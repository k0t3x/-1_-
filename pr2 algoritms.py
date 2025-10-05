#Ситников 2.3
import random
import time
import matplotlib.pyplot as plt


def generate_matrix(rows, min_cols, max_cols):
    #создаём матрицу со строками разной длины
    matrix = []
    for i in range(rows):
        cols = random.randint(min_cols, max_cols)
        row = [random.randint(-50, 50) for _ in range(cols)]
        matrix.append(row)
    return matrix


def find_shortest_row(matrix):
    #находим индекс самой короткой строки
    min_len = len(matrix[0])
    min_index = 0
    for i in range(1, len(matrix)):
        if len(matrix[i]) < min_len:
            min_len = len(matrix[i])
            min_index = i
    return min_index


def extend_row(matrix):
    #увеличиваем самую короткую строку до максимальной длины
    max_len = 0
    for row in matrix:
        if len(row) > max_len:
            max_len = len(row)

    short_index = find_shortest_row(matrix)


    current_len = len(matrix[short_index])
    if current_len < max_len:
        matrix[short_index].extend([0] * (max_len - current_len))

    return matrix, short_index, max_len

print("=" * 50)

sizes = [10, 100, 300]
results = []

for size in sizes:
    print(f"\nТестирование для размера {size}:")

    start_total = time.perf_counter()

    # Генерация матрицы
    start_gen = time.perf_counter()
    matrix = generate_matrix(size, size // 2, size)
    gen_time = time.perf_counter() - start_gen

    print(f"Сгенерировано строк: {len(matrix)}")
    print(f"Длины первых 3 строк: {[len(row) for row in matrix[:3]]}")

    # Поиск самой короткой строки
    start_find = time.perf_counter()
    short_index = find_shortest_row(matrix)
    find_time = time.perf_counter() - start_find

    print(f"Самая короткая строка: индекс {short_index}, длина {len(matrix[short_index])}")

    # Увеличение длины
    start_extend = time.perf_counter()
    new_matrix, extended_index, new_len = extend_row(matrix)
    extend_time = time.perf_counter() - start_extend

    print(f"Увеличена строка {extended_index} до длины {new_len}")

    # Проверка
    lengths = [len(row) for row in new_matrix]
    print(f"Все строки одной длины: {len(set(lengths)) == 1}")

    total_time = time.perf_counter() - start_total

    # Сохраняем результаты для графика
    results.append({
        'size': size,
        'gen_time': gen_time,
        'find_time': find_time,
        'extend_time': extend_time,
        'total_time': total_time
    })

    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ ЗАМЕРА ВРЕМЕНИ")
    print("=" * 50)
    print(f"Генерация матрицы: {gen_time:.8f} секунд")
    print(f"Поиск короткой строки: {find_time:.8f} секунд")
    print(f"Увеличение длины: {extend_time:.8f} секунд")
    print("-" * 50)
    print(f"ОБЩЕЕ ВРЕМЯ ВЫПОЛНЕНИЯ: {total_time:.8f} секунд")

# Построение графика
print("\n" + "=" * 50)
print("ГРАФИК ЗАВИСИМОСТИ ВРЕМЕНИ ОТ РАЗМЕРА МАТРИЦЫ")
print("=" * 50)

sizes_list = [r['size'] for r in results]
gen_times = [r['gen_time'] for r in results]
find_times = [r['find_time'] for r in results]
extend_times = [r['extend_time'] for r in results]
total_times = [r['total_time'] for r in results]

plt.figure(figsize=(10, 6))
plt.plot(sizes_list, gen_times, marker='o', label='Генерация матрицы')
plt.plot(sizes_list, find_times, marker='s', label='Поиск короткой строки')
plt.plot(sizes_list, extend_times, marker='^', label='Увеличение длины')
plt.plot(sizes_list, total_times, marker='d', label='Общее время')

plt.title('Зависимость времени выполнения от размера матрицы')
plt.xlabel('Размер матрицы (количество строк)')
plt.ylabel('Время (секунды)')
plt.legend()
plt.grid(True)
plt.show()

