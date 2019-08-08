
## Import module
from additional import my_module

city = ['New York', 'Chicago', 'Detroit', 'Gotham']

index = my_module.find_index(city, 'Detroit')
print(index)

## Check a module's path
import sys
print(sys.path)

## Using alias to call module
from additional import my_module as mm

new_index = mm.find_index(city, 'Gotham')
print(new_index)

## Import function inside module from specific path
# Change python path to get the module
sys.path.append('/additionals')

# import function
from my_module import find_index

index_function = find_index(city, 'New York')
print(index_function)

## Import variable inside module
from my_module import find_index as fi, test as t

new_fi = fi(city, 'Chicago')
print(new_fi)
print(t)

# Import everything inside path or module
from additional import *

index2 = my_module.find_index(city, 'Gotham')
test2 = my_module.test

print(index2)
print(test2)

# Use random library
import random

random_city = random.choice(city)

print(random_city)

# Import math library
import math

rads = math.radians(90)

print(rads)
print(math.sin(rads))

# Import datetime and calendar library
import calendar
import datetime

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# Import OS library
import os

print(os.getcwd())
print(os.__file__)

# Import antigravity library
import antigravity
