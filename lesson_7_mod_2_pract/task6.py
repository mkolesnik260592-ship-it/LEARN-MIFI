def armstr(num):
    if type(num) is not int:
        raise TypeError("input must be an integer")
    if num < 0:
        raise ValueError("Input must be non-negstive")
    if num == 0:
        None
    first = True
    for i in range(1, num):
        y = i
        x = i
        k = 0
        while x > 0:
            k += 1
            x = x // 10
        x = y
        sp = 0
        while x > 0:
            digit = x % 10
            sp += digit ** k
            x //= 10
        if i == sp:
            if first:
                print(i, end="")
                first = False
            else:
                print(f", {i}", end="")


num = int(input("Введите верхнюю границу диапазона: "))
armstr(num)
