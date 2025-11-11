numbers = [1, 3, 4, 6, 9, 11]

result = sum(num ** 3 for num in numbers if num % 3 == 0)
print(result)

def calc(func, first, second):
    return func(first, second)


# Первый аргумент при вызове calc() - это лямбда-функция с нужным выражением:
print(calc(lambda a, b: a + b, 5, 10))   # Складываем.
print(calc(lambda a, b: a * b, 30, 10))  # Умножаем.
print(30 ** 2) 

people = ['Антон', 'Соня', 'Коля', 'Женя', 'Тоня', 'Стёпа']

def say_to_all(func, sequence):
    for item in sequence:
        func(item)


# Этот вызов для каждого имени из списка должен напечатать
# строчку Привет, <имя>!
say_to_all(lambda name: print(f'Здравствуй,  {name}!' if name.startswith("С") else f'Привет, {name}!'), people)
# Этот вызов для каждого имени из списка должен напечатать
# строчку До завтра, <имя>!
say_to_all(lambda name: print(f'До завтра, {name}!'), people)