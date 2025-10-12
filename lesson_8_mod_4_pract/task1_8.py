def is_palindrome(string):
    """Обычная проверка палиндрома."""
    if not isinstance(string,str):
        raise TypeError("not str")
    return string == string[::-1]

def is_palindrome_recursive(string):
    """Рекурсивная проверка палиндрома."""
    if len(string) <= 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome_recursive(string[1:-1])
    else:
        return False

# Получение ввода от пользователя
string_input = input("Введите строку ")

print("Обычный метод:", is_palindrome(string_input))
print("Рекурсивный метод:", is_palindrome_recursive(string_input))
