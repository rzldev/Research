
# Import module
import antigravity
import os
import calendar
import datetime
import math
import random
from additional import *
from my_module import find_index as fi, test as t
from my_module import find_index
from additional import my_module as mm
import sys
from additional import my_module

city = ['New York', 'Chicago', 'Detroit', 'Gotham']

index = my_module.find_index(city, 'Detroit')
print(index)

# Check a module's path
print(sys.path)

# Using alias to call module

new_index = mm.find_index(city, 'Gotham')
print(new_index)

# Import function inside module from specific path
# Change python path to get the module
sys.path.append('/additionals')

# import function

index_function = find_index(city, 'New York')
print(index_function)

# Import variable inside module

new_fi = fi(city, 'Chicago')
print(new_fi)
print(t)

# Import everything inside path or module

index2 = my_module.find_index(city, 'Gotham')
test2 = my_module.test

print(index2)
print(test2)

# Use random library

random_city = random.choice(city)

print(random_city)

# Import math library

rads = math.radians(90)

print(rads)
print(math.sin(rads))

# Import datetime and calendar library

today = datetime.date.today()
print(today)
print(calendar.isleap(2020))

# Import OS library

print(os.getcwd())
print(os.__file__)

# Import antigravity library
