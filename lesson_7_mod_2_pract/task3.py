def how_many_times(message):
    if type(message) is not str:
        raise TypeError("Input must be a string")

    total = 0
    for char in message:
        if char != ' ':
            if not ('a' <= char <= 'z'):
                raise ValueError("String must contain only lowercase a-z letters or spaces")
            total += ord(char) - ord('a') + 1
    return total

message = input("Введите сообщение (строчные буквы): ")
clicks = how_many_times(message)
print(f"Количество нажатий: {clicks}")
