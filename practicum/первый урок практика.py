from math import factorial as fact
from random import randint as rnd
from datetime import datetime 


# 1.
# Чтобы оценить затраты на обслуживание огорода, необходимо уточнить его размеры.
# Предполагается, что огороды всегда прямоугольные.
# Напишите две функции:
# функция get_rectangle_area() должна получить на вход длину и ширину огорода и вернуть его площадь;
# функция get_rectangle_perimeter() должна получить на вход длину и ширину огорода и вернуть его периметр.
# Функции должны не печатать результат, а возвращать его.
# В коде заготовлены значения длины и ширины. Вызовите функции get_rectangle_area() и get_rectangle_perimeter() с аргументами length и width и напечатайте результаты вызовов в таком формате (только числа будут другие):

# Площадь: 32
# Периметр: 24 

def get_rectangle_area(length,width):
    rectangle_area = length * width
    return rectangle_area

def get_rectangle_perimeter(length,width):
    rectangle_perimeter = 2 * (length + width)
    return rectangle_perimeter
# Длина прямоугольника.
length = 5
# Ширина прямоугольника.
width = 10

print('Площадь:', str(get_rectangle_area(length,width)))
print('Периметр:', str(get_rectangle_perimeter(length,width)))

# 2.
# Правильный полив — ключ к здоровью растений!
# Разные виды овощей требуют разного количества воды, и поливать огород надо по науке. 
# Известно, сколько воды требуется для одного растения каждого вида, — и теперь нужна программа, которая рассчитает общее количество воды, необходимое для полива нескольких растений.
# Например, на один куст огурцов нужно 3 литра воды. На огороде — 20 таких кустов. Программа должна провести вычисления: 3 * 20 — и напечатать понятно оформленный ответ.
# Напишите функцию calculate_watering(), которая принимает три параметра:
# plant_type: название растения (например, «Помидоры» или «Ананасы»).
# number_of_plants: общее количество растений.
# volume_per_plant: количество воды в литрах, необходимое для одного растения. Это необязательный параметр. Значение этого параметра по умолчанию должно быть 2.5 (такого объёма воды в среднем должно хватить любому растению).
# Функция calculate_watering() должна вычислить общее количество воды, необходимое для полива, и напечатать строку:
# <название_растения> <количество_растений> шт.: для полива требуется <количество_воды> л воды. 
# Например:

# # При таком вызове:
# calculate_watering('Огурцы', 20, 3)

# # ...функция calculate_watering() должна напечатать строку
# # Огурцы 20 шт.: для полива требуется 60 л воды. 
# Функция calculate_watering() не должна возвращать никаких значений.

# Опишите параметры функции calculate_watering().
def calculate_watering(plant_type,number_of_plants,volume_per_plant=2.5):
    # Здесь вместо ellipsis напишите код функции.
    print(plant_type, number_of_plants, 'шт.:', 'для полива требуется', number_of_plants*volume_per_plant, 'л воды.')
# но лучше вот так 
    print(f'{plant_type} {number_of_plants} шт.: для полива требуется {number_of_plants * volume_per_plant} л воды.')
# Не изменяйте код ниже этого комментария: 
# если ваша функция написана правильно - эти вызовы должны успешно сработать.

# Вызов функции с позиционными аргументами:
calculate_watering('Артишоки', 20, 4)

# Вызов функции с позиционными аргументами, без опционального:
calculate_watering('Кивано', 15)

# Вызов функции с именованными аргументами, без опционального:
calculate_watering(number_of_plants=15, plant_type='Тыквы')

print(fact(7))

# Напишите программу для вычисления факториала случайного целого числа в диапазоне от 1 до 10 включительно. 
# Из модуля math импортируйте функцию, вычисляющую факториал числа; задайте ей псевдоним fact.
# Из модуля random импортируйте функцию, возвращающую случайное целое число; задайте ей псевдоним rnd.
# Ваша программа должна выводить результат на печать в таком виде:
# Факториал 5 равен 120 
# Соблюдайте правила оформления кода: после строк с импортом — две пустые строки.
char = rnd(1,11)
print(f'Факториал {char} равен {fact(char)} ')

# Напишите функцию analyze_skills(), которая 
# найдёт минимальное значение среди перечисленных переменных,
# найдёт максимальное значение среди перечисленных переменных,
# напечатает две строки:

# Доля питонистов, у которых есть наименее популярный навык (в %): <мин.число>
# Доля питонистов, у которых есть наиболее популярный навык (в %): <макс.число> 
# Название навыка печатать не нужно. 
# Функция не должна возвращать никакого значения.
# Многоточия из прекода нужно удалить.

bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34
minimum = min(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)
maximum = max(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)
def analyze_skills():
    print(f'Доля питонистов, у которых есть наименее популярный навык (в %): {minimum}')
    print(f'Доля питонистов, у которых есть наиболее популярный навык (в %): {maximum}')
    
#     # Среди всех переменных найдите минимальное и максимальное значение.
#     # Напечатайте фразы, описанные в задании (две строки).
analyze_skills() 
bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34


def analyze_skills():
    print(f'Доля питонистов, у которых есть наименее популярный навык (в %): {min(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)}')
    print(f'Доля питонистов, у которых есть наиболее популярный навык (в %): {max(bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql)}')
    
# Не удаляйте вызов функции.
analyze_skills()


# а лучше всего вот так 
bash = 31
c_and_c_plus_plus = 29
c_sharp = 11
html_css = 36
java = 19
javascript = 37
sql = 34
skills = [bash, c_and_c_plus_plus, c_sharp, html_css, java, javascript, sql]

def analyze_skills():
    print(f"Наименее популярный навык (в %): {min(skills)}")
    print(f"Наиболее популярный навык (в %): {max(skills)}")

# Не удаляйте вызов функции.
analyze_skills()

# 2.
# Начинающий, но в будущем успешный разработчик никак не угомонится. «А правильно ли было выбрать Python? Может, надо было заняться изучением Java или даже C#? Посмотрю статистику по вакансиям».
# В Интернете нашлось исследование: всемирный рейтинг языков программирования по числу вакансий. Вакансий много, их количество указано в тысячах:

# c_sharp = 375
# java = 546
# javascript = 915
# ... 
# Допишите функцию analyze_jobs(), в ней обработайте переменные, в которых хранится количество вакансий:
# подсчитайте суммарное количество вакансий для перечисленных языков программирования,
# подсчитайте процент вакансий для Python от числа всех исследованных вакансий,
# с помощью встроенной функции round() округлите вычисленный процент до двух знаков после запятой (до сотых долей),
# дважды вызовите print(), чтобы напечатать фразы:
# Общее число исследованных вакансий, в тысячах: <сумма_всех_вакансий>
# Вакансии для Python-разработчиков, в %: <процент_вакансий_для_Python> 

# Количество вакансий для различных языков программирования:
c_sharp = 375
java = 546
java_script = 915
php = 288
python = 603
jobs = [c_sharp, java, java_script, php, python]
def analyze_jobs():
    # Вычислите общее количество исследованных вакансий.
    total_jobs = sum(jobs)
    # Вычислите процент вакансий для Python от общего числа вакансий
    # и округлите результат до двух знаков (до сотых долей):
    python_percent = round((python / total_jobs) * 100, 2)
    # Напечатайте фразы, описанные в задании (две строки).
    print(f'Общее число исследованных вакансий, в тысячах: {total_jobs}')
    print(f'Вакансии для Python-разработчиков, в %: {python_percent}')

analyze_jobs()


def get_dumplings_recommendation():
    return rnd(10,20)
# Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
# dumplings = get_dumplings_recommendation()
print(f'Оптимальным количеством пельменей на сегодня будет {get_dumplings_recommendation()}')

def get_dumplings_recommendation(min,max):
    return rnd(min,max)
# Вызвать функцию get_dumplings_recommendation() и напечатать заданную фразу.
# dumplings = get_dumplings_recommendation(25,30)
print(f'Оптимальным количеством пельменей на сегодня будет {get_dumplings_recommendation(25,30)}')

# Эта функция должна возвращать cтроку "Hello"
def say_hello():
    return 'Hello'


# Эта функция должна возвращать строку "World!" (с восклицательным знаком).
def say_world():
    return 'World!'

    # В переменной result должна быть фраза Hello, World!
    # А функция print() должна вывести эту фразу на экран.


hello_text = say_hello()
result = say_hello() + ', ' + say_world()
print(result)

import operator
from functools import lru_cache

# Доступные операции
ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

def generate_expressions(nums):
    """Рекурсивно генерирует все выражения из списка чисел с операциями и скобками."""
    if len(nums) == 1:
        yield str(nums[0]), nums[0]
        return

    for i in range(1, len(nums)):
        left, right = nums[:i], nums[i:]
        for l_expr, l_val in generate_expressions(left):
            for r_expr, r_val in generate_expressions(right):
                for sym, func in ops.items():
                    try:
                        val = func(l_val, r_val)
                        expr = f"({l_expr}{sym}{r_expr})"
                        yield expr, val
                    except ZeroDivisionError:
                        continue

def find_target(nums, target):
    """Ищет все выражения, которые дают target."""
    results = []
    for expr, val in generate_expressions(nums):
        if abs(val - target) < 1e-9:  # допускаем погрешность для деления
            results.append(expr)
    return results
nums = [1, 2, 4, 8, 16]
target = 64

solutions = find_target(nums, target)
for s in solutions:
    print(s)

print(f"Найдено решений: {len(solutions)}")


# Исходное количество секунд:
total_seconds = 424562

# Переведите количество секунд total_seconds в нужный формат.
days = total_seconds // 86_400
hours = total_seconds // (60 ** 2) % 24
minutes = total_seconds // 60 % 60
seconds = total_seconds % 60

print(total_seconds, 'секунд - это')
print('Суток:', days)
print('Часов:', hours)
print('Минут:', minutes)
print('Секунд:', seconds)

# Функция get_season() принимает на вход название месяца;
# функция должна вернуть название сезона, к которому принадлежит месяц
# или строку "Ошибка в написании месяца!".
winter = ['декабрь', 'январь', 'февраль']
spring = ['март', 'апрель', 'май']
summer = ['июнь', 'июль', 'август']
autumn = ['сентябрь', 'октябрь', 'ноябрь']

# Допишите функцию:
def get_season(month_name):
    if month_name in winter:
        return ('зима')
    elif month_name in spring:
        return('весна')
    elif month_name in summer:
        return('лето')
    elif month_name in autumn:
        return('осень')
    else:
        return('Ошибка в написании месяца!')

# Вызовем функцию и напечатаем результат.
print(get_season('июнь'))
print(get_season('мартобрь'))
print(get_season('сентябрь'))
# На экран должно быть выведено:
# лето
# Ошибка в написании месяца!

def rectangle_area(length, width):
    return length * width

area_1 = rectangle_area(5, 0)
area_2 = rectangle_area(7, 0)

if area_1 < area_2:
    print('Площадь первой грядки меньше второй!')
elif area_1 > area_2:
    print('Площадь первой грядки больше второй!')
# Проверяем, что два условия выполняются одновременно...
elif area_1 == 0:
    # ...и только в этом случае выполняем код.
    print('Площадь первой грядки равна второй!')
    print('Сравниваются две грядки площадью 0 кв. м! Зачем вам это?')
# Остаётся последний вариант: area_1 == area_2. Обрабатываем его:
else:
    print('Площадь первой грядки равна второй!')

print('Сравнение грядок завершено!') 

x = -2
y = 5

if x == 0 and y == 0:
    print('Точка лежит на оси координат и не принадлежит ни одной четверти')
elif x > 0 and y > 0:
    print('Первая четверть')
elif x > 0 and y < 0:
    print('Четвертая четверть')
elif x < 0 and y > 0:
    print('Вторая четверть')
else: 
    print('Третья четверть')


# Вместо многоточия укажите необходимые параметры.
def count_tiles(dep, leng, wid=None):
    # Опишите условие для случая, когда ширина бассейна не указана.
    if wid is None:
        result = (leng ** 2 + 2 * leng * dep + 2 * leng * dep)
    else:
    # Посчитайте, сколько понадобится плиток для стенок и дна бассейна.
        result = (leng * wid + 2 * leng * dep + 2 * wid * dep) 

    # Верните результат работы функции.
    return result


total_tiles_1 = count_tiles(1, 3)
print('Потребуется плиток:', total_tiles_1)
# Должно быть напечатано: Потребуется плиток: 20

total_tiles_2 = count_tiles(1, 39, 3)
print('Потребуется плиток:', total_tiles_2)
# Должно быть напечатано: Потребуется плиток: 16

total_tiles_3 = count_tiles(2, 5, 3)
print('Потребуется плиток:', total_tiles_3)
# Должно быть напечатано: Потребуется плиток: 47


# Код этой функции не меняйте.
def count_tiles(dep, leng, wid=None):
    if wid is None:
        wid = leng

    short_sides = 2 * wid * dep
    long_sides = 2 * leng * dep
    bottom = leng * wid
    total = short_sides + long_sides + bottom

    return total

# Если полученное число заканчивается на 1, но это не 11 — возвращаем слово плитка (1 плитка, 21 плитка, 71 плитка).
# Если полученное число — от 12 до 14 включительно, то возвращаем слово плиток (12 плиток, 13 плиток, 14 плиток).
# Если полученное число заканчивается на 2, 3 или 4 — возвращаем слово плитки (2 плитки, 63 плитки, 94 плитки)
# Допишите код функции.

def make_word(count):
    last = count % 10
    last_two = count % 100
    if last == 1 and last_two != 11:
        return 'плитка'
    elif last in (2, 3, 4) and last_two not in (12, 13, 14):
        return 'плитки'
    else:
        return 'плиток'


# Вычисляем количество плиток:
total_tiles = count_tiles(1, 4, 22)

# Полученное число передаём в make_word(),
# чтобы подобрать нужное склонение для слова "плитка":
correct_word = make_word(total_tiles)

# Печатаем итоговую фразу, в которой применяем число плиток total_tiles
# и слово "плитка" в правильном склонении (correct_word):
print('Потребуется', total_tiles, correct_word)



# Вместо многоточия укажите параметры num, leng и wid.
# Параметру wid присвойте значение по умолчанию.
def check_pool_capacity(num, leng, wid = None):
    if wid is None:
        wid = leng
    if num < 0:
        num = -num
    if leng < 0:
        leng = -leng
    # if wid < 0:
    #     wid = -wid
        

    pool_square_is = leng * wid
    return num <= pool_square_is * 2


# Вычислите площадь бассейна и проверьте,
# помещаются ли в бассейне все люди из очереди.
# Верните True или False в зависимости от результата проверки.


# Код ниже полностью рабочий, он вам пригодится для проверки вашей работы.

# Функция, которая принимает на вход True или False
# и печатает текстовое сообщение.
def show_result(is_ok):
    if is_ok:  # Если передано True:
        print('Все люди из очереди поместятся в бассейн.')
    else:  # Если передано False:
        print('Люди из очереди не поместятся в бассейн.')


# Вызываем check_pool_capacity() с двумя аргументами.
# Этот вызов должен вернуть True (4 чел. в бассейн 2х2).
is_capacity_ok = check_pool_capacity(4, 2)
# Передаём результат вызова на вход show_result()
show_result(is_capacity_ok)
is_capacity_ok = check_pool_capacity(-3, -2, 1)
# Передаём результат вызова на вход show_result()
show_result(is_capacity_ok)
# Вызываем check_pool_capacity() с тремя аргументами.
# Этот вызов должен вернуть False (25 чел. в бассейн 5х2).
is_capacity_ok = check_pool_capacity(25, 5, 2)
# Передаём результат вызова на вход show_result()
show_result(is_capacity_ok)

# При необходимости добавьте свои вызовы аналогичным образом.

# Из модуля decimal импортируйте тип данных Decimal и параметр getcontext.
from decimal import Decimal, getcontext
# Из модуля math импортируйте константу "пи".
from math import pi


# Установите необходимую точность для вычислений.
getcontext().prec = 10
# Приведите константу "пи" к типу Decimal.
# Помните, что Decimal() принимает строку, а константа "пи" - это число.
pi = Decimal(str(pi))

# Функция get_ellipse_area() должна принимать два параметра:
# размер длинной и короткой полуоси.
def get_ellipse_area(x, y):
    ellipse_area = pi * x * y
    return ellipse_area
    # Вычислите площадь эллипса на основе переданных в функцию
    # значений полуосей.
    # Верните получившееся значение (площадь эллипса).

# Объявите три переменные типа Decimal.
long_axis = 12 # Длинная полуось эллипса.
short_axis = 4 # Короткая полуось эллипса.
depth =  5 # Глубина пруда.
ellipse_square = get_ellipse_area(long_axis, short_axis) * depth


# Вызовите функцию get_ellipse_area(), в аргументах передайте длины полуосей эллипса.
# Результат работы функции присвойте переменной area:
area = get_ellipse_area(long_axis, short_axis)

# Вычислите объём пруда: умножьте площадь на глубину.
volume = ellipse_square

# Напечатайте фразы с результатами вычислений.
print(f'Площадь пруда: {area} кв.м.')  # Должно быть напечатано: Площадь пруда: <значение> кв.м.
print(f'Количество воды для наполнения пруда: {volume} куб.м.')  # Должно быть напечатано: Количество воды для наполнения пруда: <значение> куб.м.




birthday = datetime(1955, 6, 8, 23, 20, 00)
# Вместо ... напишите шаблон.
birthday_day_and_month = datetime.strftime(birthday, '%d.%m')
print('День рождения:', birthday_day_and_month)



def get_difference_in_days(datetime_str_1, datetime_str_2):
    datetime_1 = datetime.strptime(datetime_str_1, '%Y/%m/%d %H:%M:%S')
    datetime_2 = datetime.strptime(datetime_str_2, '%Y/%m/%d %H:%M:%S')
    delta = datetime_2 - datetime_1
    return delta.days



# Преобразуйте полученные в качестве аргументов функции строки
# в тип datetime по нужному шаблону.
# Вычислите разницу между двумя датами (получится тип timedelta)
# и верните количество целых дней.


difference = get_difference_in_days('2019/05/10 11:26:31', '2019/10/04 10:01:19')

print('От начала посевной до начала сбора урожая прошло', difference, 'дней.')