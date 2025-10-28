# Создай список из 3 фруктов и выведи его.
# 2. Добавь элемент `"grape"` в список.
# 3. Удали второй элемент списка.
# 4. Выведи длину списка.
# 5. Пройди по списку и выведи каждый элемент в верхнем регистре.


fruits = ['orange', 'milk', 'salmon']
print(fruits)
fruits.append('grape')
fruits.pop(1)
print(len(fruits))
for item in fruits:
    print(item.upper())