def sets_intersection(*sets):

    if len(sets) == 0:
        return set()
    if len(sets) == 1:
        if not isinstance(sets[0], set):
            raise TypeError("All arguments must be sets")
        return sets[0].copy()

    result = sets[0].copy()
    for current_set in sets[1:]:
        result = result.intersection(current_set)
    return result
print(sets_intersection({1, 2, 3}, {2, 3, 4}, {3, 4, 5}))
