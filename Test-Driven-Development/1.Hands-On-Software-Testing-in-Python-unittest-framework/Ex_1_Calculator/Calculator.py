def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    # assertion
    if y == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    return x / y
