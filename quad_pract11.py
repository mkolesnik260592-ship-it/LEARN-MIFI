def discriminant(a, b, c):
    return  b ** 2 - 4 * a * c

def solve_quadratic(a, b ,c):
    d = discriminant(a, b, c)
    if d > 0:
        x1 = (-b + d**0.5) / (2*a)
        x2 = (-b - d**0.5) / (2*a)
        return round(x1, 2) + round(x2, 2)
    elif d == 0:
        x = -b / (2*a)
        return round(x, 2)
    else:
        real = -b / (2*a)
        imag = abs(d)**0.5 / (2*a)
        return complex(round(real, 2), round(imag, 2)) + complex(round(real, 2), -round(imag, 2))

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

roots = solve_quadratic(a, b, c)
print("Корни уравнения:", roots)
