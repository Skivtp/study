'''''''''''
задание 1
'''''''''''

def print_pack_report(starting_value):
    # Объявите диапазон от starting_value до 1 включительно
    range_name = list(range(starting_value,0,-1))
    # и переберите его в цикле:
    for number in range_name:
        # Проверьте, делится ли текущий элемент
        if number % 3 == 0:
             if number % 5 == 0:
                print(f'{number} - расфасуем по 3 или по 5')
             else: 
                print(f'{number} - расфасуем по 3')
        elif number % 5  == 0:
            print(f'{number} - расфасуем по 5')
        else:
            print(f'{number} - не заказываем!')



print_pack_report(31)

'''''''''''
задание 2
'''''''''''

def count_canisters(temperatures_per_day):
    hot_days_counter = 0
    # Допишите функцию.
    for temp in temperatures_per_day:
        if temp >= 30:
            hot_days_counter += 1
    return hot_days_counter


forecast_temperatures = [26, 28, 30, 31, 29, 31, 28, 26]
# Вызовите функцию и напечатайте результат в нужном формате.
print(f'Нужно канистр: {count_canisters(forecast_temperatures)}') 

'''''''''''
задание 3
'''''''''''
def print_multiplication_table():
    # Напишите код, который напечатает таблицу умножения.
   chars = list(range(1,10))
   multipliers = list(range(1,10))
  
   for char in chars:
    for multiplier in multipliers:
        print(f'{char} * {multiplier} = {char * multiplier}')
    print('-'* 10)   




print_multiplication_table()


'''''''''''
задание 4 \ 5
'''''''''''
def analyze_results(data):
    race = dict.keys(data[0])
    winner_team = None
    winner_score = 0 
    result = sorted(race)
    scores = {}
    for race in data:
        for team, score in race.items():
            if team in scores:
                scores[team] += score
            else:
                scores[team] = score
    for team, score in scores.items():
        if score > winner_score:
            winner_score = score
            winner_team = team
    

    print("Команды, участвовавшие в чемпионате:")
    for race in result:
        print(f"  * {race}")
    print(f'В чемпионате победила команда {winner_team} с результатом {winner_score} баллов')
   

races_data = [
    {'Ferrari': 20, 'Mercedes': 5, 'Aston Martin': 10, 'Williams': 15},
    {'Mercedes': 15, 'Aston Martin': 20, 'Ferrari': 10, 'Williams': 0},
    {'Ferrari': 20, 'Williams': 15, 'Aston Martin': 10, 'Mercedes': 5}
]

analyze_results(races_data)


