#Ситников 2.1
import random
import time

# Начало замера общего времени выполнения
start_total = time.perf_counter()

b = int(input('Введите длину списка: '))

# Замер времени генерации списка
start_gen = time.perf_counter()
spisok = [random.randint(0, 10) for i in range(b)]
gen_time = time.perf_counter() - start_gen

def zamena(lst):
    start_func = time.perf_counter()
    result = []
    for i in lst:
        istr = str(i)
        sumcif = 0
        for j in istr:
            sumcif += int(j)
        if sumcif > 5:
            result.append(i)
    func_time = time.perf_counter() - start_func
    print(f"Время выполнения функции zamena: {func_time:.8f} секунд")
    return result

# Замер времени фильтрации
start_filter = time.perf_counter()
new_spisok = zamena(spisok)
filter_time = time.perf_counter() - start_filter

# 2. Функция для получения позиций Фибоначчи
def get_fibonacci_positions(max_index):
    start_func = time.perf_counter()
    positions = []
    a, b_fib = 0, 1
    while a <= max_index:
        positions.append(a)
        a, b_fib = b_fib, a + b_fib
    func_time = time.perf_counter() - start_func
    print(f"Время выполнения функции get_fibonacci_positions: {func_time:.8f} секунд")
    return positions

# 3. Функция для замены элементов на позициях Фибоначчи на -1
def replace_fibonacci_positions(lst):
    start_func = time.perf_counter()
    fib_positions = get_fibonacci_positions(len(lst) - 1)
    for pos in fib_positions:
        if pos < len(lst):
            lst[pos] = -1
    func_time = time.perf_counter() - start_func
    print(f"Время выполнения функции replace_fibonacci_positions: {func_time:.8f} секунд")
    return lst

def sredn(lst):
    start_func = time.perf_counter()
    sr = sum(lst)/len(lst)
    func_time = time.perf_counter() - start_func
    print(f"Время выполнения функции sredn: {func_time:.8f} секунд")
    return sr

# Замер времени замены позиций Фибоначчи
start_replace = time.perf_counter()
itog = replace_fibonacci_positions(new_spisok)
replace_time = time.perf_counter() - start_replace

# Замер времени расчета среднего
start_avg = time.perf_counter()
average_result = sredn(itog)
avg_time = time.perf_counter() - start_avg

# Конец общего замера времени
total_time = time.perf_counter() - start_total

print("Финальный список:", itog)
print("Среднее значение:", average_result)

print("\n" + "="*50)
print("РЕЗУЛЬТАТЫ ЗАМЕРА ВРЕМЕНИ")
print("="*50)
print(f"Генерация списка: {gen_time:.8f} секунд")
print(f"Фильтрация чисел: {filter_time:.8f} секунд")
print(f"Замена позиций Фибоначчи: {replace_time:.8f} секунд")
print(f"Расчет среднего: {avg_time:.8f} секунд")
print("-" * 50)

print(f"ОБЩЕЕ ВРЕМЯ ВЫПОЛНЕНИЯ: {total_time:.8f} секунд")

