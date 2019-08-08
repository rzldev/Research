'''
LEGB Rule
Local(L): Defined inside function/class
Enclosed(E): Defined inside enclosing functions(Nested function concept)
Global(G): Defined at the uppermost level
Built-in(B): Reserved names in Python builtin modules
'''

# import builtins module
import builtins

# Create a global variables
x = 'Global Variable'
print(x)

# Create a function


def my_func():
    # Create a local variable
    x = 'Local Variable'
    print(x)


my_func()

# Create a function with global variable


def new_func():
    print(x)


new_func()

# Use global function
y = [3, 5, 9, 7, 1]
print(min(y))

# Check all the attributes inside the module
print(dir(builtins))

# Create a function with a same name with global function


def min(var):
    print(var)


min(y)

# Create a nested function


def outter_func():
    x = "Outter Variable"

    def inner_func():
        x = "Inner Variable"
        print(x)

    inner_func()
    print(x)


outter_func()
print(x)

# Create a function with non-local variables


def nested_func():
    x = 'Nested Variable'

    def new_nested_func():
        nonlocal x
        x = 'Non-Local X'
        print(x)

    new_nested_func()
    print(x)


nested_func()
