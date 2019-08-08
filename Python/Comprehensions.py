
## Create a list
my_list = [0, 1, 2, 3, 4, 5]

## Use comprehensions to add value into the new list
new_list1 = []
for val in my_list:
    new_list1.append(val)

print(new_list1)

 # or
new_list2 = []
new_list2 = [val for val in my_list]

print(new_list2)

## Add a multiplication value
new_list1 = []
for val in my_list:
    new_list1.append(val * val)

print(new_list1)

# or
new_list2 = []
new_list2 = [val*val for val in my_list]

print(new_list2)

# or using map + lambda
new_list3 = []
new_list3 = list(map(lambda val: val * val, my_list))

print (new_list3)
# map() function returns a list of the results after applying the given function to each item of a given iterable
# lambda function is a small anonymous function that can take any number of arguments, but can only have one expression.

## Add only even number as a value of the new list
new_list1 = []
for val in my_list:
    if val % 2 == 0 :
        new_list1.append(val)

print(new_list1)

# or
new_list2 = []
new_list2 = [val for val in my_list if val % 2 == 0]

print(new_list2)

# or using filter + lambda
new_list3 = []
new_list3 = list(filter(lambda val: val % 2 == 0, my_list))

print(new_list3)

## Add value with nested loops
new_list1 = []
for val1 in 'abcd':
    for val2 in range(1, 5):
        new_list1.append((val1, val2))

print(new_list1)

# or
new_list2 = []
new_list2 = [(val1, val2) for val1 in 'abcd' for val2 in range(1, 5)]

print(new_list2)

## Dictionary comprehensions
first_name = ['Bruce', 'Clark', 'Hal', 'Barry', 'Billy']
last_name = ['Wayne', 'Kent', 'Jordan', 'Allen', 'Batson']

# zip() is to map the similar index of multiple containers so that they can be used just using as single entity

new_list1 = {}
for first, last in zip(first_name, last_name):
    new_list1[first] = last

print(new_list1)

# or
new_list2 = {}
new_list2 = {first: last for first, last in zip(first_name, last_name)}

print(new_list2)

# or
print(list(zip(first_name, last_name)))

## Dictionary comprehensions with conditionals
new_list1 = {}
for first, last in zip(first_name, last_name):
    if first != 'Bruce':
        new_list1[first] = last

print(new_list1)

# or
new_list2 = {}
new_list2 = {first: last for first, last in zip(first_name, last_name) if first != "Clark"}

print(new_list2)

## Add only a unique value
numbers = [1, 1, 2, 3, 3, 3, 4, 5, 5, 6, 7, 7, 7, 8]

# set is a collection which is unordered and unindexed

new_list1 = set()
for n in numbers:
    new_list1.add(n)

print(new_list1)

# or
new_list2 = {}
new_list2 = {n for n in numbers}

print(new_list2)

## Generator expressions
def gen_func(list):
    for val in list:
        yield val * val

# yield is a keyword that is used like return, except the function will return a generator

my_gen = gen_func(my_list)

print(list(my_gen))

for gen in my_gen:
    print(gen)
