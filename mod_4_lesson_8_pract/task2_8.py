def reverse_image(image):
    """Обычное преобразование в негатив."""
    return [[1 - pixel for pixel in row] for row in image]

def reverse_image_recursive(image):
    """Рекурсивное преобразование в негатив."""
    if not image:
        return []
    first_row = image[0]
    rest_of_image = image[1:]
    inverted_first_row = [1 - pixel for pixel in first_row]
    inverted_rest_of_image = reverse_image_recursive(rest_of_image)
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
