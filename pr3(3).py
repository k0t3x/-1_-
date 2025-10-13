#Ситников
import time
import random

def zamena(mt, k ):
    result = []
    for row in mt:
        new_row = []
        for elem in row:
            if elem > k:
                new_row.append(elem - k)  # разность с k
            else:
                new_row.append("diff")  # слово "diff"
        result.append(new_row)
    return result

def gen_list(mt):
    combined = []
    for row in mt:
        for elem in row:
            combined.append(elem)
    return combined

def count_diff(combined_list):
    count = 0
    for elem in combined_list:
        if elem == "diff":
            count += 1
    return count

# === ОСНОВНАЯ ПРОГРАММА ===
print("=== ТЕСТ ПРОГРАММЫ ===")
total_start = time.perf_counter()

n = int(input("Введите длину матрицы по горизонтали: "))
m = int(input("Введите длину матрицы по вертикали: "))
k = int(input("Введите число, элементы больше которого нужно заменить: "))

# --- Генерация матрицы ---
start_time = time.perf_counter()
matr = [[random.randint(-75, 75) for i in range(n)] for i in range(m)]
gen_time = time.perf_counter() - start_time

print(f"\nГенерация завершена за {gen_time:.6f} сек")
print("Матрица (первые 3 строки):")
for i in range(min(3, len(matr))):
    print(f"Строка {i}: {matr[i][:8]}..." if len(matr[i]) > 8 else f"Строка {i}: {matr[i]}")

# --- Замена элементов ---
start_time = time.perf_counter()
modified_matrix = zamena(matr, k)
replace_time = time.perf_counter() - start_time

print(f"\nЗамена элементов завершена за {replace_time:.6f} сек (k={k})")
print("Матрица после замены (первые 3 строки):")
for i in range(min(3, len(modified_matrix))):
    print(f"Строка {i}: {modified_matrix[i][:8]}..." if len(modified_matrix[i]) > 8 else f"Строка {i}: {modified_matrix[i]}")

# --- Генерация объединенного списка ---
start_time = time.perf_counter()
combined_list = gen_list(modified_matrix)
gen_list_time = time.perf_counter() - start_time

print(f"\nГенерация объединенного списка завершена за {gen_list_time:.6f} сек")
print(f"Объединенный список (первые 20 элементов): {combined_list[:20]}")

# --- Подсчет слов "diff" ---
start_time = time.perf_counter()
diff_count = count_diff(combined_list)
count_time = time.perf_counter() - start_time

print(f"\nПодсчет слов 'diff' завершен за {count_time:.6f} сек")
print(f"Количество слов 'diff': {diff_count}")

# === ИТОГИ ===
total_time = time.perf_counter() - total_start

print(f"\n{'='*60}")
print("ИТОГИ ВЫПОЛНЕНИЯ")
print(f"{'='*60}")
print(f"{'Операция':<40} | {'Время (сек)':<12} | {'Результат':<15}")
print(f"{'-'*40}-|{'-'*14}-|{'-'*17}")
print(f"{'Генерация матрицы':<40} | {gen_time:<12.6f} | {f'{n}x{m}':<15}")
print(f"{'Замена элементов':<40} | {replace_time:<12.6f} | {f'k={k}':<15}")
print(f"{'Генерация объединенного списка':<40} | {gen_list_time:<12.6f} | {len(combined_list):<15}")
print(f"{'Подсчет слов diff':<40} | {count_time:<12.6f} | {diff_count:<15}")
print(f"{'-'*40}-|{'-'*14}-|{'-'*17}")
print(f"{'ОБЩЕЕ ВРЕМЯ':<40} | {total_time:<12.6f} | {'-':<15}")

# === АНАЛИЗ СЛОЖНОСТИ ===
print(f"\n{'='*50}")
print("АНАЛИЗ СЛОЖНОСТИ АЛГОРИТМОВ (Big O)")
print(f"{'='*50}")
print("1. Генерация матрицы: O(n×m) - зависит от размеров матрицы")
print("2. Замена элементов: O(n×m) - линейная сложность по количеству элементов")
print("3. Генерация объединенного списка: O(n×m) - линейная сложность")
print("4. Подсчет слов 'diff': O(n×m) - линейная сложность")

print(f"\nРазмер матрицы: {n}×{m} = {n*m} элементов")
print(f"Процент замененных на 'diff': {diff_count/(n*m)*100:.1f}%")
