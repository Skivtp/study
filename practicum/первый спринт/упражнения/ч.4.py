# Количество корзин с овощами, шт.
baskets = 462 
# Средний вес овощей в одной корзине, кг.
average_weight = 25
# Стоимость одного килограмма урожая, в монетах.
price_per_kg = 175 


# Допишите функцию, которая рассчитывает вес и стоимость урожая.
def calc(bas, av_weight, price):
    total_weight = (bas * av_weight)
    total_price = (total_weight * price)
    return total_weight, total_price


# Вызовите функцию calc() и обработайте вернувшееся значение.
total_weight, total_price = calc(baskets, average_weight, price_per_kg)

# Составьте f-строку и напечатайте её.
print(f'Общий вес урожая: {total_weight} кг. Оценённая стоимость урожая: {total_price}. ')  



def planting_plan(rows):
    start = 2       # Укажите стартовое значение диапазона.
    step = 2       # Укажите шаг диапазона.
    end =  (rows * 2) + 1     # Вычислите правую границу диапазона.
    # Опишите диапазон:
    row_positions = range(start, end, step)
    # Преобразуйте диапазон в список и верните этот список:
    return list(row_positions)

print(planting_plan(4))


sequence_1 = [69, 59, 57, 60, 63, 44, 46, 69]
sequence_2 = [33, 73, 50, 25, 36, 68, 52, 76]

def compare_sequences(sequence_1, sequence_2):
    if sequence_1 > sequence_2:
        result = (f'Список {sequence_1} больше.')
    elif sequence_1 < sequence_2:
        result = (f'Список {sequence_2} больше.')
    else:
        result = (f'Списки равны.')
    return result

# Вызовите функцию compare_sequences(),
# передайте в неё списки sequence_1 и sequence_2.
# Напечатайте результат, который вернёт функция.
result = compare_sequences(sequence_1,sequence_2)
print(result)

# Функция для создания словаря информации об овощах

def create_vegetable_info(vegetables, varieties, yields):
    # Ваш код здесь
    cort = list(zip(varieties, yields))
    vegetable_info = dict(zip(vegetables, cort))
    return vegetable_info

# Тестовые данные:
vegetables = ['Помидоры', 'Огурцы', 'Баклажаны', 'Перец', 'Капуста']
varieties = ['Красный куб', 'Аллигатор', 'Василёк', 'Тропический закат', 'Арктик']
yields = [6.5, 4.3, 2.8, 2.2, 3.5]

# Вызов функции:
print(create_vegetable_info(vegetables, varieties, yields))

# Объявим set, элементами которого будут списки:
vegetables = ['Томат', 'Огурец', 'Кабачок', 'Баклажан']
vegetable_prices = [100, 50, 70, 120]
vegetables_set = set(zip(vegetables, vegetable_prices))

print(vegetables_set, type(vegetables_set))
# Вывод в терминал: TypeError: unhashable type: 'list'
# Ничего не вышло:
# элементами множества могут быть только неизменяемые объекты. 
import time

# Создаётся множество с миллионом элементов (10 в степени 6)
num_set = set(range(10**6))

# Создаём и наполняем список - тоже миллион элементов:
num_list = list(range(10**6))

# Перед началом поиска в переменную start_time сохраняем 
# текущее время в секундах:
start_time = time.time()

# Начинаем проверку "есть ли значение 954365 в множестве num_set":
if 954365 in num_set:
    print(True)
# После выполнения поиска вновь получаем текущее время
# и находим разницу с временем, сохранённым в start_time.
# Печатаем разницу - это и есть время, затраченное на поиск.
print('Поиск элемента в множестве занял', (time.time() - start_time), 'сек.')

# Вновь засекаем текущее время:
start_time = time.time()

# Начинаем проверку "есть ли значение 954365 в списке num_list":
if 954365 in num_list:
    print(True)

print('Поиск элемента в списке занял', (time.time() - start_time), 'сек.')