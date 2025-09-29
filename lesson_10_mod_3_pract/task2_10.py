def count_char(lst, char):
    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("char len must be 1 and str")
    if not isinstance(lst, list):
        raise TypeError("test_list must be str and list")

    result = []
    for item in lst:
        if not isinstance(item, str):
            raise TypeError("All elements in lst must be strings")
        result.append(item.count(char))
    return result

test_list = ["helloo", "world"]
char_to_count = "o"

result = count_char(test_list, char_to_count)
print("Результат:", result)
