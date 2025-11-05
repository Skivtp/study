# 1. Проверь, больше ли `a = 5` чем `b = 3`.
# устаревшее решение
# def check_if(a,b):
#     if a > b:
#         return('a > b') 
#     else:
#         return('b > a')
def check_if(a, b):
    return 'a > b' if a > b else ('b > a' if b > a else 'a = b')
# a = int(input('enter a: '))
# b = int(input('enter b:'))
print(check_if(int(input('enter a: ')), int(input('enter b:'))))

# 2. Запроси число и выведи `"Чётное"` или `"Нечётное"`.
def posneg(num):
    # устаревшее решение
    # num = int(input('enter the number: '))
    # if num % 2 == 0:
    #     num =  'Четное'
    # else:
    #     num = 'Нечетное'
    # print(num)
    # еще одна переделка
    # num = int(input('Enter the number: '))
    # print('Четное' if num % 2 == 0 else 'Нечетное')
    return 'Четное' if num % 2 == 0 else 'Нечетное'
print(posneg(int(input('Enter the number: '))))


# 3. Напиши функцию, которая возвращает `"Положительное"`, `"Отрицательное"` или `"Ноль"`.

def ifnum(num):
    if num > 0:
        result = 'положительное'
    elif num == 0:
        result = 'ноль'
    else:
        result = 'отрицательное'
    return result('enter the number: '))))


     
# 4. Определи, входит ли число в диапазон от 10 до 20.
def if_range(num):
    return 'is in range' if 10<=num<=20 else 'is not in range'
num = int(input('enter the number: '))
print(if_range(num))



# 5. Напиши функцию, которая принимает оценку и возвращает `"Отлично"`, `"Хорошо"`, `"Удовлетворительно"` или `"Неудовлетворительно"
def grades(grade):
    if grade == 5:
        return 'отлично'
    elif grade == 4:
        return 'хорошо'
    elif grade == 3:@a89998538850a
        return 'удовлетворительно'
    elif grade == 2:a2
        return 'неудвлетворительно'
    else:
        return 'no such grade'
print(grades(int(input('enter the grade: '))))