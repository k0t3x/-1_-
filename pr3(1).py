#Ситников
import random
import time

def delitels(n):
    n = abs(n)
    if n < 2:
        return []  # У 0 и 1 нет простых делителей

    divisors = []
    # Проверяем делимость на 2 отдельно
    if n % 2 == 0:
        divisors.append(2)
        while n % 2 == 0:
            n //= 2
    # Проверяем нечетные делители
    i = 3
    while i * i <= n:
        if n % i == 0:
            divisors.append(i)
            while n % i == 0:
                n //= i
        i += 2

    # Если осталось простое число больше 2
    if n > 1:
        divisors.append(n)

    return divisors

# ОСНОВНАЯ ПРОГРАММА
print("=== ТЕСТ ПРОГРАММЫ ===")
total_start = time.perf_counter()

# Ввод данных
n = int(input("Введите длину списка: "))

# --- Числовые операции ---
print("\n--- ЧИСЛОВЫЕ ОПЕРАЦИИ ---")

# Генерация чисел
start = time.perf_counter()
spisok = [random.randint(-50, 50) for i in range(n)]
gen_num_time = time.perf_counter() - start
print(f"Генерация чисел: первые 10 -> {spisok[:10]}")
print(f"Время генерации: {gen_num_time:.8f} сек")

# Обработка чисел (простые делители)
start = time.perf_counter()
for index, zhislo in enumerate(spisok):
    if (zhislo < 0):
        divisors = delitels(zhislo)
        spisok[index] = divisors if divisors else 0
proc_num_time = time.perf_counter() - start
print(f"После обработки (простые делители): первые 10 -> {spisok[:10]}")
print(f"Время обработки: {proc_num_time:.8f} сек")

# Извлечение первых 5 элементов
start = time.perf_counter()
spis_it = iter(spisok)
pyaterka = []
for i in range(5):
    pyaterka.append(next(spis_it))
iter_num_time = time.perf_counter() - start
print(f"Первые 5 элементов: {pyaterka}")
print(f"Время извлечения: {iter_num_time:.8f} сек")

# --- Строковые операции ---
print("\n--- СТРОКОВЫЕ ОПЕРАЦИИ ---")

# Создание кортежей
start = time.perf_counter()
spisok_2 = ["level", "madam", "hello", "noon"]
result = list(enumerate(spisok_2))
enum_time = time.perf_counter() - start
print(f"Создание кортежей: {result}")
print(f"Время создания кортежей: {enum_time:.8f} сек")

# Фильтрация палиндромов
start = time.perf_counter()
iterator = iter(enumerate(spisok_2))
palindromes = []

for i in range(len(spisok_2)):
    index, word = next(iterator)
    if word == word[::-1]:
        palindromes.append((index, word))
filter_time = time.perf_counter() - start
print(f"Найденные палиндромы: {palindromes}")
print(f"Время фильтрации: {filter_time:.8f} сек")

# === ИТОГИ ===
total_end = time.perf_counter()
total_time = total_end - total_start

print("\n" + "="*50)
print("ИТОГИ ВЫПОЛНЕНИЯ")
print("="*50)

print(f"{'Операция':<40} | {'Время (сек)':<12}")
print("-" * 55)
print(f"{'Генерация чисел':<40} | {gen_num_time:<12.8f}")
print(f"{'Обработка чисел (простые делители)':<40} | {proc_num_time:<12.8f}")
print(f"{'Извлечение первых 5 элементов':<40} | {iter_num_time:<12.8f}")
print(f"{'Создание кортежей через enumerate':<40} | {enum_time:<12.8f}")
print(f"{'Фильтрация палиндромов':<40} | {filter_time:<12.8f}")
print("-" * 55)
print(f"{'ОБЩЕЕ ВРЕМЯ':<40} | {total_time:<12.8f}")

print("\n" + "="*50)
print("АНАЛИЗ СЛОЖНОСТИ АЛГОРИТМОВ (Big O)")
print("="*50)
print("1. Генерация чисел: O(n) - линейная сложность")
print("2. Обработка чисел (простые делители): O(n × √m) - зависит от размера чисел")
print("3. Извлечение первых элементов: O(1) - константная сложность")
print("4. Создание кортежей: O(n) - линейная сложность")
print("5. Фильтрация палиндромов: O(n) - линейная сложность")








