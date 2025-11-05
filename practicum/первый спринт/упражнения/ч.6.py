from random import randint

# Начальная температура чая
current_temperature = 85
while current_temperature > 60:
    print('Прошла минута.')
    temp_down = int(randint(1, 3))
    current_temperature = current_temperature - temp_down
    print(f'Чай остыл ещё на {temp_down} °C. Текущая температура: {current_temperature}°C ')
print(f'Время пить чай!')

fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.
# Объявляем новый список, в него будем складывать изменённые значения.
corrected_fruit_yields = []
for fruit in fruit_yields:
    new_value = fruit + 1.2
    list.append(corrected_fruit_yields, new_value)
# Объявите цикл, в нём переберите список fruit_yields.
# В теле цикла к каждому значению списка добавьте 1.2,
# затем получившееся значение сохраните в список corrected_fruit_yields.

# Чтобы увидеть, что получилось, 
# напечатаем список с откорректированными значениями.
print(corrected_fruit_yields)

fruit_yields = [164.8, 105.0, 124.3, 113.8]  # Урожайность, кг на дерево.

# Вместо всего этого кода нужно написать единственную строчку,
# которая выполнит те же действия.
# corrected_fruit_yields = []

# for yield_value in fruit_yields:
#     yield_value += 1.2
#     list.append(corrected_fruit_yields, yield_value)

corrected_fruit_yields = [yiel+1.2 for yiel in fruit_yields]  # Ваш код - здесь.


print(corrected_fruit_yields)

numbers = [value ** 2 for value in range(1,11)] # Место для вашего кода
print(numbers)