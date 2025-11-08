class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь!')

    def call(self, phone_number):
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')


rotary_phone = Phone('дисковый')

print(rotary_phone.line_type)
print(rotary_phone.dial_type)
rotary_phone.ring()


# Выведется:
# проводной
# Дзззззыыыыыыыынь!
class MobilePhone(Phone):
    line_type = 'беспроводной'
    battery_type = 'Li-ion'

    def __init__(self, dial_type_value, network_type):
        # Вызов родительского инициализатора.
        super().__init__(dial_type_value)
        # Новый атрибут объекта.
        self.network_type = network_type

    # Переопределить метод ring() класса Phone.
    def ring(self):
        print('Дзынь-дзынь!')

    def start_game(self):
        print('Игра запущена!')


mobile_phone = MobilePhone('сенсорный', 'LTE')

print(mobile_phone.battery_type)
print(mobile_phone.network_type)
mobile_phone.start_game()
print(mobile_phone.dial_type)
