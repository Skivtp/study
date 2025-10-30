from datetime import datetime, timedelta, time
from decimal import Decimal, getcontext


def get_weekday_name(weekday_number):
    days = [
        'понедельник',
        'вторник',
        'среда',
        'четверг',
        'пятница',
        'суббота',
        'воскресенье'
    ]
    return days[weekday_number]

def get_day_after_tomorrow(date_string):
    # С помощью шаблона преобразуйте date_string в значение типа datetime
    string_from_date = datetime.strptime(date_string, '%Y-%m-%d')
    now = datetime.date(string_from_date)
    # Получите день недели для now:
    now_weekday = get_weekday_name(now.weekday())
    # Вычислите послезавтрашнюю дату:
    day_after_tomorrow = now + timedelta(days=2)
    # Получите день недели для day_after_tomorrow:
    day_after_tomorrow_weekday = get_weekday_name(day_after_tomorrow.weekday())
    return (f'Сегодня {now}, {now_weekday}, а послезавтра - {day_after_tomorrow_weekday}')

# Проверьте работу программы, можете подставить свои значения.
print(get_day_after_tomorrow('2024-01-01'))
print(get_day_after_tomorrow('2024-01-02'))
print(get_day_after_tomorrow('2024-01-03'))
print(get_day_after_tomorrow('2024-01-04'))
print(get_day_after_tomorrow('2024-01-05'))
print(get_day_after_tomorrow('2024-01-06'))

"""""""""""""""""""""""""""""""""""""""""
задание 2
"""""""""""""""""""""""""""""""""""""""""

# Допишите код функции.
def get_results(leader_time, your_time):
    # Сохраните формат времени как строку в переменную time_format
    time_format = '%H:%M:%S'
    # Преобразуйте полученные в аргументах строки в объекты datetime:
    leader_time_object = datetime.strptime(leader_time, time_format)
    your_time_object = datetime.strptime(your_time, time_format)
    leader = datetime.time(leader_time_object)
    your = datetime.time(your_time_object)
    # Если два объекта datetime равны, то получатель сообщения – лидер.
    # Составьте и верните строку c сообщением для лидера.
    if your == leader:
        return (f'Вы пробежали за {datetime.time(your_time_object)} и победили!')
    else:
        # В противном случае вычислите разницу
        # между временем лидера и временем участника.
        # Результатом будет значение типа timedelta.
        difference = your_time_object - leader_time_object

        # Верните сообщение с указанием времени участника
        # и его отставания от лидера:
        return (f'Вы пробежали за {your} с отставанием от лидера на {difference}. ')


# Проверьте работу программы. Здесь вы можете подставить свои значения.
print(get_results('02:02:02', '02:02:02'))
print(get_results('02:02:02', '03:04:05'))

"""""""""""""""""""""""""""""""""""""""""
задание 3
"""""""""""""""""""""""""""""""""""""""""

# Установите требуемую точность вычислений:
getcontext().prec = 3


# Допишите код функции.
def get_monthly_payment(total_sum, months_count, percents):
    # Подсчитайте основную сумму ежемесячного платежа, без учёта процентов:
    monthly_raw = Decimal(total_sum) / Decimal(months_count)

    # Подсчитайте ежемесячный платёж по процентам банка,
    # исходя из ежемесячной части основной суммы и процентной ставки:
    monthly_addition = Decimal(monthly_raw) * Decimal(percents) / Decimal('100')

    # Подсчитайте общую сумму ежемесячного платежа:
    total_per_month = Decimal(monthly_raw)+(monthly_addition)
    # Верните общую сумму ежемесячного платежа:
    return total_per_month


payment_value = get_monthly_payment(54, 24, 9)
print('Ежемесячный платёж:', payment_value, 'ВтК.')
