def tribonacci (n):
    if type(n) is not int:
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")

    if n == 0:
        return 0
    elif n <= 2:
        return 1

    a, b, c = 0, 1, 1
    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c

n = int(input("Введите номер числа Трибоначчи: "))
result = tribonacci(n)
print(f"T({n}) = {result}")
