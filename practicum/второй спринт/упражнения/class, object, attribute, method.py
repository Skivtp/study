class Employee:
    vacation_days = 28

    def __init__(self, first_name, second_name, gender):
        # Атрибут объекта.
        self.first_name = first_name
        self.second_name = second_name
        self.gender = gender
        self.remaining_vacation_days = Employee.vacation_days

    def consume_vacation(self, vacation_days_spent):
        self.vacation_days_spent = vacation_days_spent

        self.remaining_vacation_days = (
            self.remaining_vacation_days - self.vacation_days_spent
        )
        return self.remaining_vacation_days

    def get_vacation_details(
        self,
    ):
        return f"Остаток отпускных дней: {self.remaining_vacation_days}."


# Создайте экземпляры класса Employee с различными значениями атрибутов.
employee1 = Employee("Роберт", "Крузо", "м")
employee2 = Employee("Том", "ДеНиро", "ж")
# Допишите код для вывода информации о сотрудниках.
print(
    f" Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {Employee.vacation_days}."
)
print(
    f" Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {Employee.vacation_days}."
)

employee1.consume_vacation(5)
employee1.consume_vacation(5)
print(employee1.get_vacation_details())
