import functools
import inspect

def asks(arg_name, prompt):
    def decorator(func):
        if not hasattr(func, '_asks_metadata'):
            func._asks_metadata = []
        func._asks_metadata.append((arg_name, prompt))
        return func
    return decorator

def interactive(title=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if title:
                print(title)
            metadata = getattr(func, '_asks_metadata', [])[::-1]
            collected_args = {}
            for arg_name, prompt in metadata:
                value = input(prompt)
                collected_args[arg_name] = value
            result = func(**collected_args)
            if result is not None:
                print(result)
        return wrapper
    return decorator

@interactive('Calculator Program')
@asks('x', 'Enter first number: ')
@asks('y', 'Enter second number: ')
def calculate(x, y):
    return int(x) + int(y)

calculate()

@interactive()
@asks('name', 'Name: ')
def greet(name):
    print(f"Hello, {name}!")

greet()

@interactive()
@asks('a', 'A: ')
@asks('b', 'B: ')
@asks('c', 'C: ')
def concat(a, b, c):
    return f"{a}-{b}-{c}"

concat()
