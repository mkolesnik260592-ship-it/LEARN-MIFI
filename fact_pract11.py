def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


n = int(input("Введите число:"))
if n < 0:
    print("Факториал отрицательного числа не существует")
else:
    print("Факториал равен: ", factorial(n))
