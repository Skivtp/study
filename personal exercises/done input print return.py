#
# 1. Запроси имя пользователя и выведи приветствие.
def greeting():
    name = input('enter your name:')  
    return(name)

name = greeting()
print('hello,', name)


# 2. Запроси два числа и выведи их сумму.
def do_some_math(num1, num2):
    return num1 + num2
a = int(input('enter first number:'))
b = int(input('enter second number:'))
print(do_some_math(a, b))


# 3. Напиши функцию `greet(name)`, которая возвращает строку `"Hello, name!"`.
def greet(name):
    print(f'Hello, {name}!')
name = input('enter your name: ')
greet(name)


# 4. Напиши функцию, которая запрашивает число и возвращает его квадрат.
def dc():
    mul = int(input('enter number: '))
    print(mul ** 2)
dc()

# 5. Напиши функцию, которая принимает строку и возвращает её длину.
def stroke_len():
    stroke = input('enter your stroke: ')
    s = len(stroke)
    print(s)
stroke_len()