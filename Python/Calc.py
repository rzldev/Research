## Mathematic functions
def add(x, y) :
    return x + y

def subtract(x, y) :
    return x - y

def multiply(x, y) :
    return x * y

def divide(x, y) :
    if y == 0 :
        # Raise an error and stop the program if x is lower than 0:
        raise ValueError('Can not divided by zero!')
    return x / y
