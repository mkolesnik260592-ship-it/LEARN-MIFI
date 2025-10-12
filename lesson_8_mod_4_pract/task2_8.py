def reverse_image(image):
    """Обычное преобразование в негатив."""
    return [[1 - pixel for pixel in row] for row in image]

def reverse_image_recursive(image):
    """Рекурсивное преобразование в негатив."""
    if not image:
        return []

    first_row = image[0]  # Берем первую строку
    rest_of_image = image[1:]  # Берем остальную часть изображения
    # Инвертируем первую строку (можно использовать списковое включение)
    inverted_first_row = [1 - pixel for pixel in first_row]
    # Рекурсивно инвертируем остальную часть изображения
    inverted_rest_of_image = reverse_image_recursive(rest_of_image)
    # Объединяем инвертированную первую строку с инвертированной остальной частью
    return [inverted_first_row] + inverted_rest_of_image

# Пример входных данных
input_image = [
    [
    [1, 0, 1],
    [0, 1, 0],
    [1, 0, 1]
    ],
    [
    [1, 1, 1],
    [0, 0, 0]
    ],
    [
    [1, 0, 0],
    [1, 0, 0]
    ]
]
for index, item in enumerate(input_image):
    # Вывод результатов
    print("Пример №", index + 1)
    print("Обычный метод:", reverse_image(item))
    print("Рекурсивный метод:", reverse_image_recursive(item))
