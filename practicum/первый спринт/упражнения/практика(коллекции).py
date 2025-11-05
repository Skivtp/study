# Объявите функцию check_winners с параметрами scores и student_score.
# Функция должна напечатать результат в заданном формате.
def check_winners(scores, student_score):
    list.sort(scores)
    winning_scores_index = [-1, -2, -3]
    winning_scores = [scores[i] for i in winning_scores_index]
    if student_score in winning_scores:
        print('Вы в тройке победителей!')
    else:
        print('Вы не попали в тройку победителей.')


# Вызовы для проверки работы функции check_winners().
# Три набора данных - для проверки разных ситуаций.
first_olympiad_scores = [20, 48, 52, 38, 36, 13, 7, 41, 34, 24, 5, 51, 9, 14, 28, 42, 40, 39, 1, 45, 37, 10, 31, 27, 17, 46, 2, 22, 35, 55]
check_winners(first_olympiad_scores, 52)

second_olympiad_scores = [22, 4, 42, 5, 54, 28, 19, 33, 8, 16, 23, 40, 39, 58, 9, 13, 48, 2, 51, 41, 21, 36, 55, 25, 31, 45, 44, 30, 1, 10]
check_winners(second_olympiad_scores, 4)

third_olympiad_scores = [36, 1, 49, 27, 8, 23, 13, 56, 46, 33, 45, 30, 16, 11, 41, 19, 43, 54, 39, 38, 40, 48, 34, 26, 5, 28, 21, 3, 51, 44]
check_winners(third_olympiad_scores, 21)

'''''
задача 2 
'''''

# Допишите функцию get_stickers_comparison().
# Эта функция должна возвращать кортеж из трёх коллекций:
# - уникальные_стикеры из collection_1,
# - уникальные_стикеры из collection_2,
# - стикеры, которые есть в collection_1 и в collection_2.
# Все три коллекции должны быть отсортированы по возрастанию.
def get_stickers_comparison(collection_1, collection_2):

    col_1_set = set(collection_1)
    col_2_set = set(collection_2)

    common_stickers_set = set.intersection(col_1_set, col_2_set)
    anton_stickers_set = set.difference(col_2_set, col_1_set)
    stas_stickers_set = set.difference(col_1_set, col_2_set)

    stas_stickers = tuple(stas_stickers_set)
    anton_stickers = tuple(anton_stickers_set)
    common_stickers = tuple(common_stickers_set)

    return sorted(stas_stickers), sorted(anton_stickers), sorted(common_stickers)


# Списки стикеров:
stas_collection = ['Тим Бернерс-Ли', 'Линус Торвальдс', 'Ада Лавлейс', 'Линус Торвальдс', 'Маргарет Гамильтон', 'Бьярн Страуструп']
anton_collection = ['Тим Бернерс-Ли', 'Гвидо ван Россум', 'Линус Торвальдс', 'Бьярн Страуструп', 'Бьярн Страуструп', 'Кен Томпсон', 'Деннис Ричи']

get_stickers_comparison(stas_collection, anton_collection)
# # Вызываем функцию и распаковываем полученный кортеж в три переменные:
stas_stickers, anton_stickers, common_stickers = get_stickers_comparison(stas_collection, anton_collection)
# Печатаем результаты:
print('Стикеры, которые есть только у Стаса:', stas_stickers)
print('Стикеры, которые есть только у Антона:', anton_stickers)
print('Стикеры, которые есть и у Стаса, и у Антона:', common_stickers)


'''''''''''
задача 3
'''''''''''

def is_palindrome(text):
    # Ваш код здесь
    orig_list = text.replace(" ", "").upper()
    reverse_list = orig_list[::-1]
    return reverse_list == orig_list

# Должно быть напечатано True:
print(is_palindrome('А роза упала на лапу Азора'))
# Должно быть напечатано False:
print(is_palindrome('Не палиндром'))


'''''''''''
задача 4
'''''''''''

def get_selection(collection):
    # Напишите код функции.
    col_len = len(collection)
    col_10 = col_len // 10
    start = int(col_10)
    end = int(-col_10-1)
    slice_col = collection[start:end]
    return slice_col


heights = [140.1, 150.3, 155, 160.4, 162.7, 163, 168.9, 170, 179.1, 180]
heights1 = [163, 165, 167, 169, 171, 173, 175, 177, 179, 181, 183, 185, 187, 189]
selection = get_selection(heights)

print('Выборка:', selection)
selection = get_selection(heights1)
print('Выборка:', selection)
