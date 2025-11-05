'''''''''''''''''''''
задача 1
'''''''''''''''''''''
#  Преобразуйте строки в списки, разбив их по пробелам.

# Преобразуйте полученные списки в множества
# (элементами множества будут только уникальные значения из списка).

# Получите пересечение двух множеств - это будет новая коллекция.

# Верните длину получившейся коллекции.


phrase_1 = 'кот зол как лев дай мне сыр дай мне суп'
phrase_2 = 'кто ест сыр тот кот кто ест суп тот нет'


def find_common_words_count(first_string, second_string):
    first_string_list = first_string.split()
    second_string_list = second_string.split()
    first_set = set(first_string_list)
    second_set = set(second_string_list)

    print(first_string_list) # проверка для себя - получился список
    print(first_set) # проверка для себя, получилось множество
    return len(set.intersection(first_set, second_set))


common_words_count = find_common_words_count(phrase_1, phrase_2)
print('Общих уникальных слов в предложениях:', common_words_count)

'''''''''''''''''''''
задача 2
'''''''''''''''''''''


# Овощи, которые растут в каждом из огородов
first_garden = {'помидоры', 'огурцы', 'морковь'}
second_garden = {'перец', 'помидоры', 'лук'}

# 1. Овощи, которые растут и в первом, и во втором огороде
common_vegetables = set.intersection(first_garden, second_garden)
print('Овощи, растущие и в первом, и во втором огороде:', common_vegetables)

# 2. Овощи, которые растут только в первом огороде
only_first_garden = set.difference(first_garden, second_garden)
print('Овощи, растущие только в первом огороде:', only_first_garden)

# 3. Овощи, которые растут только во втором огороде
only_second_garden = set.difference(second_garden, first_garden)
print('Овощи, растущие только во втором огороде:', only_second_garden)

# Для частых операций добавления/удаления используйте list.
# Для данных, которые не должны меняться, — tuple.
# Для быстрого поиска по ключу — dict.
# Для уникальных значений — set.

