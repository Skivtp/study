#  imports
from decimal import Decimal
import datetime

# пустой словарь
goods = {}

# функции 

# добавление основное
def add(items, title, amount, expiration_date=None):
    if isinstance(expiration_date, str):
        try:
            year, month, day = map(int, expiration_date.split('-'))
            expiration_date = datetime.date(year, month, day)
        except:
            expiration_date = None

    batch = {
        'amount': Decimal(str(amount)),
        'expiration_date': expiration_date
    }

    if title not in items:
        items[title] = []

    items[title].append(batch)

# добавление через строку - не нашел варианта лучше для названий из двух и более слов.
def add_by_note(items, note):
    parts = note.split()

    for i, part in enumerate(parts):
        if part.replace('.', '', 1).isdigit():
            amount_index = i
            break
    else:
        print('Не найдено количество')
        return

    title = ' '.join(parts[:amount_index])
    amount = Decimal(parts[amount_index])

    if len(parts) > amount_index + 1:
        date_str = parts[amount_index + 1]
        if len(date_str) == 10 and date_str.count('-') == 2:
            year, month, day = map(int, date_str.split('-'))
            expiration_date = datetime.date(year, month, day)
        else:
            expiration_date = None
    else:
        expiration_date = None
    if title not in items:
        items[title] = []

    items[title].append({
        'amount': amount,1333333
        'expiration_date': expiration_date
    })
    # функция поиска по названию продукта
def find(items, needle):
    needle = needle.lower()
    matches = []

    for key in items.keys():
        if needle in key.lower():
            matches.append(key)
    return matches



# функция получения количества
def get_amount(items, needle):
    needle = needle.lower()
    total = Decimal('0')

    for key in items.keys():
        if needle in key.lower():
            total += sum(batch['amount'] for batch in items[key])
    return total  


def get_expired(items, in_advance_days=0):
    today = datetime.date.today()
    deadline = today + datetime.timedelta(days=in_advance_days)
    totals = {}

    for name, batches in items.items():
        for batch in batches:
            date = batch['expiration_date']
            if isinstance(date, datetime.date) and date <= deadline:
                totals[name] = totals.get(name, Decimal('0')) + batch['amount']

    return list(totals.items())


# вызов добавления продукта 
add(goods, 'Яйца', Decimal('10'), '2025-11-30')
add(goods, 'Яйца', Decimal('3'), '2023-10-15')
add(goods, 'Вода', Decimal('2.5'))
add_by_note(goods, 'Яйца гусиные 4 2023-07-15')
add_by_note(goods, 'Яйца гусиные 2 2025-07-15')
add_by_note(goods, 'куриное филе мятеленка 20')

#проверки

print(find(goods, 'кур'))



