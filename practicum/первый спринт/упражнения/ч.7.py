import random


# 1. Создание списка списков:
rows = 3
cols = 3
harvest = [[random.randint(5, 21) for _ in range(cols)] for _ in range(rows)]  # Примените list comprehension.

# 2. Функция для подсчёта общего урожая:
def total_harvest(harvest):
    first_garden = sum(harvest[0])
    second_garden = sum(harvest[1])
    third_garden = sum(harvest[2]) 
    total_each = (first_garden + second_garden + third_garden)
    return total_each

# 3. Функция для подсчёта среднего урожая с каждого участка:
def average_harvest_per_plot(harvest):
    first_average = int(sum(harvest[0]) / len(harvest[0]))
    second_average = int(sum(harvest[1]) / len(harvest[1]))
    third_average = int(sum(harvest[2]) / len(harvest[2]))
    total_average = [first_average, second_average, third_average]
    return total_average


# Вывод результатов
print('Урожай с каждой грядки на каждом участке:', harvest)
print('Общий урожай со всех участков:', total_harvest(harvest))
print('Средний урожай с каждого участка:', average_harvest_per_plot(harvest))

