weight = float(input("Введите ваш вес (кг): "))
height = float(input("Введите ваш рост (м): "))
if weight < 0:
    print("Вес сне может быть отрицательным")

if height < 0:
    print("Рост не может быть отрицательным")

def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 1)

def get_bmi_category(bmi):
    if bmi < 25:
        return "Норма, жить можно"
    if bmi > 25:
        if bmi > 30:
            return "Ожирение"
        return "Избыточный вес, стоит задуматься"

bmi = calculate_bmi(weight, height)
category = get_bmi_category(bmi)

print("Ваш ИМТ: ", round(bmi, 1))
print("Категория: ", category)
