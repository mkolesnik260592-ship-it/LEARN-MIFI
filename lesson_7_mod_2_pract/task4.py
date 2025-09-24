def decimal_to_binary(num):
    if num < 0:
        raise ValueError("Only non-negative integers are allowed")
    if type(num) is not int:
        raise TypeError("Input must be an integer")

    if num == 0:
        return "0"

    char = ""
    while num > 0:
        char = str(num % 2) + char
        num = num // 2
    return char

num = int(input("Введите десятичное число: "))
binary = decimal_to_binary(num)
print(f"Двоичное представление: {binary}")
