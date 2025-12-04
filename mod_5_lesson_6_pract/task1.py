from functools import wraps

def call_counter(func):
    """декоратор"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        result = func(*args, **kwargs)
        return result
    wrapper.calls = 0
    return wrapper


@call_counter
def greet(name):
    return f"Hello, {name}"

greet("Alice")
greet("Bob")
greet("Matt")
print(greet.calls)
