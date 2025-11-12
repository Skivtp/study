import time


# Декоратор объявляется до декорируемой функции.
def time_of_function(func):
    # В декораторе есть вложенная функция.
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func()
        execution_time = round(time.time() - start_time, 3)
        print(f'Время выполнения: {execution_time} сек.')
        return result
    # Декоратор возвращает вызываемый объект (callable object),
    # в нашем случае - функцию.
    return wrapper


# Имя функции-декоратора (с символом @)
# ставится перед объявлением декорируемой функции.
@time_of_function
def sleep_one_sec():
    time.sleep(1)
    return 'Функция sleep_one_sec() завершила вычисления.'


# После декорирования любой вызов функции sleep_one_sec()
# будет автоматически сопровождаться измерением времени её выполнения.
sleep_one_sec()

class Robot:
    base_battery_status = 100

    def __init__(self, name):
        self.name = name

    @classmethod
    def update_base_battery_status(cls, new_status):
        cls.base_battery_status = new_status

    def report(self):
        print(
            f'{self.name} reporting: Battery status is '
            f'{self.base_battery_status}%'
        )

    @staticmethod
    def predict_battery_lifetime(current_capacity, charge_cycles):
        """
        Прогнозирует срок службы аккумулятора
        на основе текущей ёмкости и количества циклов зарядки.
        """
        # Пусть максимальная ёмкость нового аккумулятора будет равна 5000 мАч
        max_capacity = 5000
        return (current_capacity / max_capacity) * (1000 - charge_cycles)

# Вызов статического метода через имя класса:
battery_lifetime = Robot.predict_battery_lifetime(4000, 100)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {battery_lifetime:.0f} циклов зарядки.'
)

# Создаём объект класса:
robot = Robot('R2-D2')
# Статический метод доступен и в объекте:
r2d2_battery_lifetime = robot.predict_battery_lifetime(3500, 150)
print(
    'Прогноз срока службы аккумулятора: '
    f'осталось {r2d2_battery_lifetime:.0f} циклов зарядки.'
) 