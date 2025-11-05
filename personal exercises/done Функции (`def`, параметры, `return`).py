#  Напиши функцию `hello()` — выводит `"Привет!"`.
# 2. Функция `square(n)` — возвращает квадрат числа.
# 3. Функция `is_even(n)` — возвращает `True`, если число чётное.
# 4. Функция `greet(name, age)` — возвращает `"Привет, name! Тебе age лет."`
# 5. Функция `sum_list(lst)` — возвращает сумму всех чисел в списке.

def greetings():
    print('hello')
greetings()

def square(n):
    return (n ** 2)
number = int(input('please enter the number:'))
print(square(number))

# вот это нужно написать не так. это можно сделать короче, через тернарный оператор, но я постоянно забываю как 
def is_even(n):
    if n % 2 == 0:
        return 'True'
    else:
        return 'False'
number = int(input('please enter the number:'))
print(is_even(number))
# вот как правильно
def is_even(n):
    return True if n % 2 == 0 else False
# или короче 
def is_even(n):
    return n % 2 == 0


def greet(name, age):
    return f"Привет, {name}! Тебе {age} лет."
name = input('enter name:')
age = input('enter age:')
print(greet(name,age))

def sum_list(lst):
    total = sum(lst)
    return total
kist = range(1,12)
print(sum_list(kist))
# вот так короче
def sum_list(lst):
    return sum(lst)