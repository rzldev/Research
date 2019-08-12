
## Random. This module implements pseudo-random number generators for various distributions
## Import random module
import random

## Using random function
my_number = random.random()
print(my_number)

## Uniform can return a random value with specific range
my_number = random.uniform(1, 3)
print(my_number)

## Randint can return a random integer with specific range
my_number = random.randint(1, 3)
print(my_number)

## Choice can return a random element from the non-empty sequence seq
greetings = ['Hello', 'Hi', 'Hei', 'Ola', 'Bonjour', 'Ciao', 'Marhabaan']
my_greetings = random.choice(greetings)
print(my_greetings)

## Choices can return a sized list of elements chosen from the population with replacement
colors = ['Red', 'Black', 'Blue', 'Yellow']
my_result = random.choices(colors, k=10)
print(my_result)

my_new_result = random.choices(colors, weights=[10, 10, 5, 2], k=10)
print(my_new_result)
# weight can incrase the probability for the value to show up

## Shuffle the sequence value in place
deck = list(range(1, 53))
random.shuffle(deck)
print(deck)

## Sample can return the length of a list of unique elements chosen from the population sequence or set. Used for random sampling without replacement.
deck = list(range(1, 53))
hand = random.sample(deck, k=6)
print(hand)

## Create a automate person's info generator
first_name = ['Bruce', 'Clark', 'Hal', 'Barry', 'Billy']
last_name = ['Wayne', 'Kent', 'Jordan', 'Allen', 'Batson']
fake_cities = ['Gotham City', 'Metropolis', "Coast City", 'Central City', 'Fawcett City']

for num in range(10):
    first = random.choice(first_name)
    last = random.choice(last_name)
    phone = f'{random.randint(100, 999)}-555-{random.randint(1000,9999)}'
    city = random.choice(fake_cities)
    email = first.lower() + last.lower() + '@bogusemail.com'

    print(f'{first} {last}\n{phone}\n{city}\n{email}\n')
