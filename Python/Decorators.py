from functools import wraps
## The functools module is for higher-order functions: functions that act on or return other functions
## This is a convenience function for invoking update_wrapper() as a function decorator when defining a wrapper function

## Decorator is a design pattern in Python that allows a user to add new functionality to an existing object without modifying its structure
## Nested Function
def outer_function() :
    message = 'Hey'

    def inner_function() :
        print(message)

    return inner_function()

outer_function()

#or
my_func = outer_function
my_func()

print()

# or
def outer_function(message) :

    def inner_function() :
        print(message)

    return inner_function()

hi_func = outer_function('Hi')
hi_func
bye_func = outer_function('Bye')
bye_func

print()

## Decorator
def decorator_function(function) :
    def wrapper() :
        print(f'wrapper executed this before {function.__name__}')
        return function()
    return wrapper

def display() :
    print('display function ran')

my_decorator = decorator_function(display)
my_decorator()

print()

# or
def decorator_function(function) :
    def wrapper() :
        print(f'wrapper executed this before {function.__name__}')
        return function()
    return wrapper()

@decorator_function
def display() :
    print('display function ran')

display

print()

## Using more than one decorator
def my_decorator(function) :
    def wrapper(*args, **kwargs) :
        print(f'wrapper executed this before {function.__name__}')
        return function(*args, **kwargs)
    return wrapper

@my_decorator
def my_display() :
    print('my_display function ran')

@my_decorator
def my_name(name, age) :
    print(f"My name is {name}, and i'm {age} years old")

my_display()
my_name('Bob', 25)

print()

## Class decorator
class decorator_class(object) :
    def __init__(self, function) :
        self.function = function

    def __call__(self, *args, **kwargs) :
        print(f'call method executed this before {self.function.__name__}')
        return self.function(*args, **kwargs)

@decorator_class
def new_display() :
    print('my_display function ran')

@decorator_class
def new_name(name, age) :
    print(f"My name is {name}, and i'm {age} years old")

new_display()
new_name('Bob', 25)

print()

## Two decorators inside one function
## Logging and timming decorators
def my_logger(func) :
    import logging
    # logging defines functions and classes which implement a flexible event logging system for applications and libraries
    logging.basicConfig(filename=f"{func.__name__}.log", level=logging.INFO)

    @wraps(func)
    def wrapper(*args, **kwargs) :
        logging.info(f'Ran with args: {args}, and kwargs: {kwargs}')
        return func(*args, ** kwargs)

    return wrapper

def my_timer(func) :
    import time
    # time module is handling about time-related tasks

    @wraps(func)
    def wrapper(*args, **kwargs) :
        t1 = time.process_time()
        results = func(*args, *kwargs)
        t2 = time.process_time() - t1
        print(f"{func.__name__} ran in: {t2} sec")
        return results

    return wrapper

@my_logger
@my_timer
def display_info(name, age) :
    import time
    time.sleep(1)
    print(f"display_info ran with arguments ({name}, {age})")

display_info('Bob', 251)
