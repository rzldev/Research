## Conditional check using if, else, elif statements
if True:
    print('Conditional was true')

## Conditional check using comparison
# Equal                     ==
# Not Equal              !=
# Greater Than          >
# Less Than               <
# Greater or Equal    >=
# Less or Equal         <=
# Object Identity       is

## Conditional check with some sort of value
language = 'Java'

if language == 'Python':
    print('The language is Python')
elif language == 'Java':
    print('The language is Java')
elif language == 'Ruby':
    print('The language is Ruby')
else:
    print('No Match')

## Using AND, OR, or NOT
# AND
user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# OR
logged_in = False

if user == 'admin' or logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

if user == 'admin' and not logged_in:
    print('Admin Page')
else:
    print('Bad Creds')

# Using IS
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)

print('id X = ' + str(id(x)))
print('id Y = ' + str(id(y)))
print(x is y)

## False values
# False
# None
# Zero of any numeric type. 0
# An empty sequance. '', (), []
# An empty mapping. {}

condition = None

if condition:
    print('True')
else:
    print('False')
