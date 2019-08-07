
# Create a alphabets list
alphabets = ['A', 'B', 'C', 'D']

print(alphabets)

# Count the length of the list
print(len(alphabets))

# Print list value items by index number
print(alphabets[0])
print(alphabets[-1])
print(alphabets[:2])
print(alphabets[2:])

# Add value to the list
alphabets.append('E')
print(alphabets)

alphabets.insert(0, 'F')
print(alphabets)

alphabets_extend = ['G', 'H', 'I']
alphabets.extend(alphabets_extend)
print(alphabets)

# Remove value from the list
alphabets.remove("F")
print(alphabets)

alphabets_pop = alphabets.pop()
print(alphabets_pop)
print(alphabets)

# Sort the list
alphabets.reverse()
print(alphabets)

alphabets.sort()
print(alphabets)

number = [4, 6, 2, 3, 8]

number.sort()
print(number)

number.sort(reverse=True)
print(number)

# create a new list with sorted values from other variable
sorted_number = sorted(number)
print(sorted_number)

## Min, Max and Sum
print(min(number))
print(max(number))
print(sum(number))

# Find the index of a value in the list
print(alphabets.index('C'))

# Check if there is a value that we try to find
print("A" in alphabets)
print("Z" in alphabets)

# Print item one by one in the list with looping
for index, item in enumerate(alphabets, start=1):  # item is name of a variable
    print(index, item)

# Give seperate sign between the values in the list
alphabets_string = ' - '.join(alphabets)
print(alphabets_string)

# making it back
alphabets_new = alphabets_string.split(' - ')
print(alphabets_new)

# Create a tuples
# Mutable
list1 = ['Chair', 'Table', 'Cupboard']
list2 = list1

print(list1)
print(list2)

list1[0] = 'Door'

print(list1)
print(list2)

# Imutable
tuple1 = ('Chair', 'Table', 'Cupboard')
tuple2 = tuple1

print(tuple1)
print(tuple2)

#tuple1[0] = 'Door'

# print(tuple1)
# print(tuple2)

# Create a sets
# set doesn't care about the order
# if there are index with the same value, it will only showed once
set1 = {'Computer', 'Laptop', 'Android', 'Laptop'}

print(set1)

set2 = {'Speaker', 'Headset', 'Computer', 'Laptop'}

print('Laptop' in set2)
print(set1.intersection(set2))
print(set1.difference(set2))
print(set1.union(set2))

# Create an empty lists
empty_list = []
empty_list = list()

# Create an empty tuples
empty_tuple = ()
empty_tuple = tuple()

# Create an empty sets
empty_set = {}  # this is wrong
empty_set = set()
