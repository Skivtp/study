apple_tree_yields = (150, 210, 90, 120, 140, 190, 130, 150, 110, 200, 150)

# Функция reversed_sort() должна принять на вход кортеж
# и вернуть кортеж с теми же элементами, отсортированными по убыванию.
def reversed_sort(tpl):
    apple_tree_sorted = sorted(tpl, reverse=True)
    apple_tree_cort = tuple(apple_tree_sorted,)
    return apple_tree_cort
    # 1. К полученному кортежу примените функцию сортировки;
    # затем результат сортировки преобразуйте в кортеж и верните.

result = reversed_sort(apple_tree_yields)
# Присвойте переменной result результат
# вызова функции reversed_sort() с аргументом apple_tree_yields.
# Напечатайте:
print(result[0])  # наибольшее значение из кортежа result,
print(result[1]) # второе по величине значение из кортежа result,
print(result[2]) # третье по величине значение из кортежа result.

def assess_yield(number_of_plants, average_weight):
    total_weight = (number_of_plants * average_weight / 1000)
    if total_weight > 100:
        result = 'Ожидается отличный урожай.'
    elif total_weight > 50:
        result = 'Ожидается хороший урожай.'
    elif total_weight > 0:
        result = 'Урожай будет так себе.'
    else:
        result = 'Урожая не будет.'
    return tuple ([total_weight, result])


    # Вычислите общий вес урожая в килограммах.
    # В зависимости от получившегося веса урожая выберите подходящее сообщение.
    # Верните два значения: общий вес и строку с сообщением.

# Вызываем функцию и распаковываем кортеж:
total_weight, rating = assess_yield(50, 200)

# Печатаем результат:
print(total_weight, 'кг.', rating)