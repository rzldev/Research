
## Create a list
my_list = [1, 2, 3, 4, 5]

## Else clause on for statements
for i in my_list :
    print(i)
else :
    print('Hit the For/Else Statements!')

print()

# Or
for i in my_list :
    print(i)
    if i == 3 :
        break
else :
    print('Hit the For/Else Statements!')

print()

# Or
for i in my_list :
    print(i)
    if i == 6 :
        break
else :
    print('Hit the For/Else Statements!')

print()

## Else clause on while statements
num = 1
while num <= 5 :
    print(num)
    num += 1
else :
    print('Hit the While/Else Statements!')

print()

# Or
num = 1
while num <= 5 :
    print(num)
    if num > 3 :
        break
    num += 1
else :
    print('Hit the While/Else Statements!')

print()

## Using else clauses on loop cases
name_list = ['Bruce', 'Clark', 'Hal']

def find_index(list, target) :
    for i, value in enumerate(list) :
        if value == target :
            break
    else :
        return -1
    return i

find_name = find_index(name_list, 'Hal')

print(f'Location of target is n index : {find_name}')
