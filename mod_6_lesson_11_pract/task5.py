# Создайте пользовательское исключение здесь
class VectorOperationError(Exception):
    pass

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Вектор({self.x}, {self.y})'

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise VectorOperationError("Операция сложения возможна только с другим вектором")
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        if not isinstance(scalar,(int, float)):
            return NotImplemented
        return Vector(self.x * scalar, self.y * scalar)

    def __eq__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y


# Пример использования
v1 = Vector(2, 3)
v2 = Vector(3, 4)
print(f"v1 = {v1}")
print(f"v2 = {v2}")

v3 = v1 + v2
print(f"v1 + v2 = {v3}")

v4 = v1 * 5
print(f"v1 * 5 = {v4}")

print(f"v1 == Vector(2, 3) -> {v1 == Vector(2, 3)}")
print(f"v1 == v2 -> {v1 == v2}")

try:
    result = v1 + 10  # Попытка сложить вектор и число
except VectorOperationError as e:
    print(f"Ошибка: {e}")
