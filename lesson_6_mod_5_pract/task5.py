import functools

def enforce_types(*types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_type) in enumerate(zip(args, types)):
                if not isinstance(arg, expected_type):
                    raise TypeError(f"argument {i + 1} must be {expected_type.__name__}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

# Пример
@enforce_types(int, str)
def example(a, b, c=0):
    return f"{a}-{b}-{c}"

print(example(1, "hello"))
print(example(1, "x", True))
