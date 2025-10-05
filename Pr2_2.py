#Ситников 2.2
import random
import time
import math

start_total = time.perf_counter()

b = int(input('Введите длину списка: '))


start_gen = time.perf_counter()
spisok = [5**i for i in range(260)]
gen_time = time.perf_counter() - start_gen
lst = [random.randint(1,10) for i in range(b)]
spisok = spisok + lst
print(f"Время выполнения генерации списка: {gen_time:.8f} секунд")

start_addlogs = time.perf_counter()
for i in range(123, 196):
    spisok[i] = math.log(int(spisok[i]), 5)
addlogs_time = time.perf_counter() - start_addlogs
print(f"Время выполнения замены логарифмов: {addlogs_time:.8f} секунд")

def is_perfect_square(n):
    start_square = time.perf_counter()
    if n < 0:
        return False
    sqrt_n = math.sqrt(n)
    trt = (sqrt_n == int(sqrt_n))
    square_time = time.perf_counter() - start_square
    return trt

a = []
start_addthree = time.perf_counter()
for i in range(0,len(spisok)):
    if (is_perfect_square(spisok[i])):
        a.append(3)
    a.append(spisok[i])
addthree_time = time.perf_counter() - start_addthree
print(f"Время выполнения вставки троек: {addthree_time:.8f} секунд")

start_len = time.perf_counter()
a.append(len(a))
len_time = time.perf_counter() - start_len
print(f"Время выполнения добавления длины: {len_time:.8f} секунд")

#Первые 10 элементов
print(a[:10])

total_time = time.perf_counter() - start_total

print("\n" + "="*50)
print("РЕЗУЛЬТАТЫ ЗАМЕРА ВРЕМЕНИ")
print("="*50)
print(f"Генерация списка: {gen_time:.8f} секунд")
print(f"Замена логарифмов: {addlogs_time:.8f} секунд")
print(f"Вставка троек: {addthree_time:.8f} секунд")
print(f"Добавление длины: {len_time:.8f} секунд")
print("-" * 50)
print(f"ОБЩЕЕ ВРЕМЯ ВЫПОЛНЕНИЯ: {total_time:.8f} секунд")