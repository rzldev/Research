
## Create a function
def square_number(nums) :
    results = []
    for i in nums :
        results.append(i * i)
    return results

my_numbers = square_number([1, 2, 3, 4 , 5])
print(my_numbers)

print()

## Create a generator from that function
def square_number_gen(nums) :
    for i in nums :
        yield(i * i)

my_numbers = square_number_gen([1, 2, 3, 4, 5])
print(my_numbers)
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))
print(next(my_numbers))

# or
my_numbers = square_number_gen([1, 2, 3, 4, 5])
for nums in my_numbers :
    print(nums)

print()

## Create a generator inside variable
my_numbers = (i * i for i in [1, 2, 3, 4, 5])
print(my_numbers)
print(list(my_numbers))

# or
my_numbers = (i * i for i in [1, 2, 3, 4, 5])
for nums in my_numbers :
    print(nums)

print()

## Create a custom generator
import memory_profiler as mem_profile
import random
import time

first_name = ['Bruce', 'Clark', 'Hal', 'Barry', 'Billy']
last_name = ['Wayne', 'Kent', 'Jordan', 'Allen', 'Batson']

mem_before = mem_profile.memory_usage()
print(f'Memory (Before) : {mem_before}Mb')

# Function
def people_list(num_people) :
    results = []
    for i in range(num_people) :
        person = {
        'id' : i,
        'first' : random.choice(first_name),
        'last' : random.choice(last_name)
        }
        results.append(person)
    return results

t1 = time.process_time()
people = people_list(1000000)
t2 = time.process_time()

mem_people_list = mem_profile.memory_usage()
print(f"Memory (After) : {mem_people_list}Mb")
print(f"took {t2 - t1}")

print()

# Generator
def people_generator(people) :
    results = []
    for i in people :
        person = {
        'id' : i,
        'first' : random.choice(first_name),
        'last' : random.choice(last_name)
        }
        yield results

t1 = time.process_time()
people = people_generator(1000000)
t2 = time.process_time()

mem_people_gen = mem_profile.memory_usage()
print(f"Memory (After) : {mem_people_gen}Mb")
print(f"took {t2 - t1}")
