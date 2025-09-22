a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

def sum(a, b):
    return a + b

def difference(a, b):
    return a - b

def composition(a, b):
    return a * b

def division(a, b):
    return a / b

print("Сумма введеных чисел равна -> ", sum(a, b))
print("Разность ввееденых чисел равна -> ", difference(a, b))
print("Умножение введеных чисел равно -> ", composition(a, b))
print("Деление введеных чисел равно -> ", division(a, b))
