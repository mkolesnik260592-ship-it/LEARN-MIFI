class Temperature:
    def __init__(self, celsius):
        self.celsius = float(celsius)

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Температура не может быть ниже абсолютного нуля")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5/9


# Пример использования
t = Temperature(25)
print(f"{t.celsius}°C равно {t.fahrenheit}°F")

t.fahrenheit = 32
print(f"Новая температура: {t.celsius}°C")

try:
    t.celsius = -300
except ValueError as e:
    print(f"Ошибка: {e}")
