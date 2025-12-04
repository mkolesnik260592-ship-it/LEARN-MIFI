def filter_dict_by_value(d, threshold):
    if len(d) == 0:
        return {}
    if not isinstance(d, dict):
        raise TypeError("d must be a dict")
    result = {}
    for key, value in d.items():
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise TypeError("All values in dictionary must be int or float")
        if value > threshold:
            result[key] = value
    return result

data = {'a': 1, 'b': 2, 'c': 3}
limit = 2
result = filter_dict_by_value(data, limit)
print("Результат:", result)
