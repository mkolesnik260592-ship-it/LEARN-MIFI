class Employee:
    total_employees = 0

    def __init__(self, name, position):
        self.name = name
        self.position = position
        Employee.total_employees += 1

    @classmethod
    def get_total_employees(cls):
        return cls.total_employees

    @classmethod
    def from_string(cls, employee_string):
        if not isinstance(employee_string, str) or '-' not in employee_string:
            raise ValueError("Должно содержать имя и должность, разделенные дефисом")
        name, position = employee_string.split('-', 1)
        return cls(name, position)

    @staticmethod
    def is_valid_email(email):
        if not '@' in email:
            return False
        if not '.' in email.split("@", 1)[1]:
            return False
        return True

# Пример использования
emp1 = Employee("Иван", "Разработчик")
emp2 = Employee("Мария", "Тестировщик")
print(f"Всего сотрудников: {Employee.get_total_employees()}")

emp3_str = "Анна-Менеджер"
emp3 = Employee.from_string(emp3_str)
print(f"Создан сотрудник: {emp3.name}, должность: {emp3.position}")
print(f"Всего сотрудников: {emp3.get_total_employees()}")

print(f"Является ли 'test@example.com' валидным email: {Employee.is_valid_email('test@example.com')}")
print(f"Является ли 'test-example.com' валидным email: {Employee.is_valid_email('test-example.com')}")
