
## String formatting
first_name = 'Bob'
last_name = 'Walker'

sentence = "Hello, my name is {} {}".format(first_name, last_name)
print(sentence)

# or
sentence = f"Hello, my name is {first_name.upper()} {last_name.upper()}"
print(sentence)

print()

## String formatting
person = {'name' : 'Bob', 'age' : 25}

sentence = "My name is {}, and i'm {} years old".format(person['name'], person['age'])
print(sentence)

# or
sentence = f"My name is {person['name']}, and i'm {person['age']} years old"
print(sentence)

print()

## Integer formatting
calculating = "4 times 11 is equal to {}".format(4 * 11)
print(calculating)

calculating = f"4 times 11 is equal to {4 * 11}"
print(calculating)

print()

## Float formatting
pi = 3.14159265359

calculating = "pi is equal to {}".format(pi)
print(calculating)

calculating = f"pi is equal to {pi:.2f}"
print(calculating)

print()

## String formatting with loop
for index in range(1, 4) :
    sentence = "Number {}".format(index)
    print(sentence)

print()

for index in range(1, 4) :
    sentence = f"Number {index:02}"
    print(sentence)

print()

## Datetime formatting
import datetime
my_date = datetime.date(2019, 8, 16)
sentence = "{}". format(my_date)

print(sentence)

sentence = f"Today is {my_date:%B %d, %Y}"
print(sentence)
