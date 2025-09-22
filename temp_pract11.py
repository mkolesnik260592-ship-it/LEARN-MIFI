c = float(input("Введите температуру в градусах цельсия "))
def to_farenheit(c):
    return round(c * 9/5 + 32, 2)

def to_kelvin(c):
    return round(c + 273.15, 2)

print("Ваша температура в градусах Фаренгейта:", to_farenheit(c))
print("Ваша температура в градусах Кельвина:", to_kelvin(c))
