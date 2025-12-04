def calculate_month_to_threshold(start, rate, threshold):

    if rate <= 0:
        raise ValueError("Growth rate must be greater than 0.")
    if start <= 0 or threshold <= 0:
        raise ValueError("Start and threshold must be positive numbers.")
    if start >= threshold:
        return 0

    months = 0
    while start < threshold:
        start = start + start * rate / 100
        months += 1

        if months > 1000:
            break
    return months

start = int(input("Введите начальное количество пользователей: "))
rate = float(input("Введите темп роста в процентах: "))
threshold = int(input("Введите пороговое значение: "))

months = calculate_month_to_threshold(start, rate, threshold)
print(f"Количество месяцев для достижения порога: {months}")
