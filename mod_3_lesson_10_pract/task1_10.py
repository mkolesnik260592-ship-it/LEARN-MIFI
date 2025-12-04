def replace_characters(lst, old, new):
    if not isinstance(lst, list):
        raise TypeError("lst must be a list of strings")
    if not isinstance(old, str) or not isinstance(new, str) or len(old) != 1 or len(new) != 1:
        raise TypeError("old and new must be single characters and str")

    result = []
    for item in lst:
        if not isinstance(item, str):
            raise TypeError("All elements in lst must be strings")
        result.append(item.replace(old, new))
    return result


test_list = ["hello", "world"]
old_char = "o"
new_char = "1"

result = replace_characters(test_list, old_char, new_char)
print("Результат:", result)
