
## Create a list
my_list = [3, 1, 4, 2, 5, 7, 6, 8, 0, 9]
print(my_list)

## Sorted list
sorted_list = sorted(my_list)
print(sorted_list)

# or
my_list.sort()
print(my_list)

## Reversed the sorted list
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)

#or
my_list.sort(reverse=True)
print(my_list)

## Create a tupple
my_tupple = (5, 1, 6, 2, 7, 3, 8, 4, 9, 0)
print(my_tupple)

## Sorted tupple
sorted_tupple = sorted(my_tupple)
print(sorted_tupple)

## Reversed the sorted tupple
reverse_tupple = sorted(my_tupple, reverse=True)
print(reverse_tupple)

## Create a new list
new_list = [9, 3, 0, -3, 6, -6]
print(new_list)

## Sorted list
sorted_list = sorted(new_list)
print(sorted_list)

## Sorted list base absolute number
sorted_list = sorted(new_list, key=abs)
print(sorted_list)

## Create a dictionary
my_dictionary = {'name' : 'Bob', 'age' : 25, 'job' : 'Progrmmer', 'hobby' : 'Coding'}
print(my_dictionary)

## Sorted dictionary
sorted_dictionary = sorted(my_dictionary)
print(sorted_dictionary)

# or create a sorted function
# Create a class
class init_dict():
    def __init__(self, name, age, job):
        self.name = name
        self.age = age
        self.job = job
    # __init__ is a reseved method in python classes. It is called as a constructor in object oriented terminology

    def __repr__(self):
        return f'({self.name}, {self.age}, {self.job})'
    # __repr__ should return a printable representation of the object

d1 = init_dict('John', 44, 'Designer')
d2 = init_dict('Mary', 23, 'Data Scientist')
d3 = init_dict('Bob', 25, 'Developer')

dictionary = [d1, d2, d3]
print(dictionary)

# Create a sorted function base by the key
def sort_dict(dictionary):
    return dictionary.name

# Use the function
sorted_dictionary = sorted(dictionary, key=sort_dict)
print(sorted_dictionary)

# without the function
sorted_dictionary2 = sorted(dictionary, key=lambda d: d.name)
print(sorted_dictionary2)

## Sorted dictionary using function which already exist
# import the function
from operator import attrgetter

# Sort the dictionary usinf attrgetter as it's key
easy_sorted = sorted(dictionary, key=attrgetter('name'))
print(easy_sorted)
