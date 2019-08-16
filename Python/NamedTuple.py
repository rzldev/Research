
## Namedtuple >> factory function for creating tuple subclasses with named fields
## Import namedtuple
from collections import namedtuple

# List
color_list = [55, 155, 155]
print('list: ' + str(color_list[1]))

## Dictionary
color_tuple = {'red' : 55, 'green' : 155, 'blue' : 155}
print('dictionary: ' + str(color_tuple['green']))

## Namedtuple
named_color = namedtuple('color', ['red', 'green', 'blue'])
my_color = named_color(000, 111, 222)
black = named_color(0, 0, 0)
white = named_color(255, 255, 255)

print('my_color, red: ' + str(my_color.red))
print('my_color, green: ' + str(my_color[1]))
print('black, red: ' + str(black.red))
print('black, green: ' + str(black[1]))
print('white, red: ' + str(white.red))
print('white, green: ' + str(white[1]))
