
## Decorators with arguments
def argument_decorator(argument) :
    def my_decorator(function) :
        def wrapper(*args, **kwargs) :
            print(f'{argument} wrapper executed this before {function.__name__}')
            return function(*args, **kwargs)
        return wrapper
    return my_decorator

@argument_decorator('log:')
def my_display() :
    print('my_display function ran')

@argument_decorator('log:')
def my_name(name, age) :
    print(f"My name is {name}, and i'm {age} years old")
    print()

my_name('Bob', 25)
my_name('Tom', 28)
