# 1. Выведи числа от 1 до 5 с помощью `for`.
for i in range(1,6):
    print(i)

# 2. Выведи все символы строки `"Python"` по одному.
text = 'python'
for i in text:
    print(i)
print('готово')

# 3. С помощью `while` выведи числа от 10 до 5.
x = 11
while x > 5:
    x = x - 1
    print(x)
print('готово')
# альтернативное решение 
x = 10
while x >= 5:
    print(x)
    x -= 1
print('готово')
#  альтернативное решение без while
for i in range(10, 4, -1):
    print(i)
print('готово')
# 4. Подсчитай сумму чисел от 1 до 100.

# for i in range(101):
#     total = i + i
#     print(total)
# здесь ошибка, правильно:
print(sum(range(1, 101)))
print('готово')
# 5. Выведи только чётные числа от 1 до 20.
for i in range(1,21):
    if i % 2 == 0:
        print(i)
print('готово')
# можно короче
for i in range(2, 21, 2):
    print(i)
print('готово')