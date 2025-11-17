from functools import wraps

def uppercase_output(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, str):
            return result.upper()
        return result
    return wrapper

@uppercase_output
def greeting():
    return "hello"

print(greeting())
print(type(greeting()))
