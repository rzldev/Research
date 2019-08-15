
## EAFP = Easier to Ask for Forgiveness than Permission
## First case
class Duck :
    def quack(self) :
        print('Quack quack!')
    def fly(self) :
        print('Flap flap!')

class Person :
    def quack(self) :
        print('I\'m quacking like a Duck!')
    def fly(self) :
        print('I\'m flapping my arms!')

def quack_and_fly(thing) :
    # isinstance() function returns True if the specified object is of the specified type, otherwise False
    if isinstance(thing, Duck) :
        thing.quack()
        thing.fly()
    else :
        print('This has to be a Duck!')

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

print()

## Second case
def quack_and_fly(thing) :
    thing.quack()
    thing.fly()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

print()

## Third case
def quack_and_fly(thing) :
    try :
        thing.quack()
        thing.fly()
        thing.jump()
    except AttributeError as ae :
        print(ae)

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

print()

## LBYL = Look Before You Leap
def quack_and_fly(thing) :
    # hasattr() function returns True if the specified object has the specified attribute, otherwise False
    if hasattr(thing, 'quack') :
        # callable() function returns True if the specified object is callable, otherwise it returns False
        if callable(thing.quack) :
            thing.quack()
    if hasattr(thing, 'fly') :
        if callable(thing.fly) :
            thing.fly()

d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)

print()

## EAFP or LBYL
person = {'name' : 'Bob', 'age' : 25, 'job' : 'Programmer'}
person = {'name' : 'Bob', 'age' : 25}

# EAFP
try :
    print(f'My name is {person["name"]}. I\'m {person["age"]} years old, and i\'m a {person["job"]}')
except KeyError as e :
    print(f'Missing {e} key')

# LBYL
if 'name' in person and 'age' in person and 'job' in person :
    print(f'My name is {person["name"]}. I\'m {person["age"]} years old, and i\'m a {person["job"]}')
else :
    print('Missing some keys')

print()

# or
my_list = [1, 2, 3, 4, 5, 6]
my_list = [1, 2, 3, 4, 5]

# EAFP
try :
    print(my_list[5])
except IndexError :
    print('That index does not exist')

# LBYL
if len(my_list) >= 6 :
    print(my_list[5])
else :
    print('That index does not exist')

print()

# or
import os

my_file = 'additionals/test_file.txt'

# EAFP
try :
    f = open(my_file)
except IOError as e :
    print('File can not be accessed!')
else :
    with f :
        print(f.read())

# LBYL
if os.access(my_file, os.R_OK) :
        with open(my_file) as f :
            print(f.read())
else :
    print('File can not be accessed!')
