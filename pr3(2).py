# Ситников
import random
import time
import matplotlib.pyplot as plt

# Размеры для тестирования
sizes = [100, 1000, 10000, 100000, 1000000]
results = []

print("=== ТЕСТИРОВАНИЕ ГЕНЕРАТОРОВ СПИСКОВ ===")

for size in sizes:
    print(f"\n=== ТЕСТ НА РАЗМЕРЕ: {size} ===")

    total_start = time.perf_counter()

    # Генерация чисел
    start = time.perf_counter()
    numbers = [random.randint(-125, 125) for _ in range(size)]
    gen_time = time.perf_counter() - start

    # Фильтрация чисел > 75
    start = time.perf_counter()
    filtered = [x for x in numbers if x > 75]
    filter_time = time.perf_counter() - start

    # Замена на up/down
    start = time.perf_counter()
    if filtered:
        replaced = filtered.copy()
        replaced[0] = 'up'
        for i in range(1, len(filtered)):
            if filtered[i] > filtered[i - 1]:
                replaced[i] = 'up'
            else:
                replaced[i] = 'down'
    else:
        replaced = []
    replace_time = time.perf_counter() - start

    total_time = time.perf_counter() - total_start

    print(f"Генерация: {gen_time:.6f} сек")
    print(f"Фильтрация: {filter_time:.6f} сек")
    print(f"Замена: {replace_time:.6f} сек")
    print(f"Всего: {total_time:.6f} сек")

    results.append({
        'size': size,
        'gen_time': gen_time,
        'filter_time': filter_time,
        'replace_time': replace_time,
        'total_time': total_time
    })

# Таблица результатов
print(f"\n{'=' * 60}")
print("ТАБЛИЦА РЕЗУЛЬТАТОВ")
print(f"{'=' * 60}")
print(f"{'Размер':<10} | {'Генерация':<12} | {'Фильтрация':<12} | {'Замена':<12} | {'Всего':<12}")
print("-" * 60)

for res in results:
    print(
        f"{res['size']:<10} | {res['gen_time']:<12.6f} | {res['filter_time']:<12.6f} | {res['replace_time']:<12.6f} | {res['total_time']:<12.6f}")

# График
sizes_list = [r['size'] for r in results]
gen_times = [r['gen_time'] for r in results]
filter_times = [r['filter_time'] for r in results]
replace_times = [r['replace_time'] for r in results]

plt.figure(figsize=(10, 6))
plt.plot(sizes_list, gen_times, 'o-', label='Генерация')
plt.plot(sizes_list, filter_times, 's-', label='Фильтрация')
plt.plot(sizes_list, replace_times, '^-', label='Замена')
plt.xlabel('Размер списка')
plt.ylabel('Время (сек)')
plt.title('Зависимость времени выполнения от размера списка')
plt.legend()
plt.grid(True)
plt.xscale('log')
plt.yscale('log')
plt.show()

print(f"\n{'=' * 40}")
print("АНАЛИЗ СЛОЖНОСТИ")
print(f"{'=' * 40}")
print("Генерация: O(n)")
print("Фильтрация: O(n)")
print("Замена: O(m) где m ≤ n")