def rgb2hex(r=9, g=152, b=255):
    """
    Конвертирует значения RGB в шестнадцатеричную строку.

    Параметры:
    r, g, b (int): Значения цветовых компонент (0-255)

    Возвращает:
    str: Цвет в формате #rrggbb

    Выбрасывает:
    TypeError: Если компоненты не целые числа
    ValueError: Если значения вне диапазона 0-255
    """
    for name, value in (("r", r), ("g", g), ("b", b)):
        if type(value) is not int:  # исключаем bool и нецелые типы
            raise TypeError(f"{name} должен быть целым числом")
        if not (0 <= value <= 255):
            raise ValueError(f"{name} должен быть в диапазоне 0-255")
    return f"#{r:02x}{g:02x}{b:02x}"

hex = rgb2hex(r=9, g=152, b=255)
print(hex)

def hex2rgb(hex_str):
    """
    Конвертирует шестнадцатеричную строку в словарь RGB.

    Поддерживаемые форматы:
    - #rrggbb
    - rrggbb
    - #rgb → расширяется в #rrggbb

    Параметры:
    hex_str (str): Шестнадцатеричное представление цвета

    Возвращает:
    dict: Словарь с ключами 'r', 'g', 'b' и значениями 0-255

    Выбрасывает:
    TypeError: Если вход не строка
    ValueError: При неверном формате или недопустимых символах
    """
    if not isinstance(hex_str,str):
        raise TypeError("hex value must be a string")

    s = hex_str.strip().lstrip('#').lower()

    if len(s) not in (3, 6):
        raise ValueError("hex string must be in format rrggbb or rgb (with or without leading #)")
    if len(s) == 3:
        s = ''.join(ch * 2 for ch in s)

    allowed = set('0123456789abcdef')
    if not all(ch in allowed for ch in s):
        raise ValueError("invalid hex digits")

    rr, gg, bb = s[0:2], s[2:4], s[4:6]

    r = int(rr, 16)
    g = int(gg, 16)
    b = int(bb, 16)
    return {'r': r, 'g': g, 'b': b}

hex_str = input('введите цвет: ')
print(f'Ваш цвет в RGB: {hex2rgb(hex_str)}')
