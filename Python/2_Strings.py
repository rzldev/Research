
## Create a variable with string value
message = 'Hello World'

## Print variable message
print(message)

## Using single quotes and double quotes
single = 'He said "Hello World"'
double = "You're coding right now"

print(single)
print(double)

## Using triple quotes
triple = """You are trying to learn
about quotes on python"""

print(triple)

## Count the length of the string value
print(len(message))

## Access some index of thestring value
print(message[0])
print(message[0:5])
print(message[6:11])

# other way
print(message[:5])
print(message[6:])

## Print string value with lowercase and uppercase
print(message.lower())
print(message.upper())

## Count some index in the string value
print(message.count('Hello'))
print(message.count('l'))

## Find some index in the string value
print(message.find('World'))
print(message.find('Universe'))

## Replace string value
message = message.replace('World', 'Universe')
print(message)

## Combine two string value
hello = 'Hello'
name = 'John'
greeting = hello + ', ' + name + '. Welcome to the party!'

print(greeting)

# second way
greeting = '{}, {}. Welcome to the party!'.format(hello, name)

print(greeting)

# third way

greeting = f'{hello}, {name}. Welcome to the party!'

print(greeting)

## Check all of the atributs and method on the string value (Remove the "#" sign)
#print(dir(greeting))

# and to check the information for the string (Remove the "#" sign)
#print(help(str))
#print(help(str.lower))

