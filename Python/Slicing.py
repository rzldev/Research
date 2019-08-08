
## Create a list
my_list = [0,   9,   8,   7,   6,   5,   4,   3,   2,   1]
#               0,   1,    2,   3,   4,   5,   6,   7,   8,   9
#             -10, -9,  -8,  -7,  -6, -5,  -4,  -3, -2,  -1

## Print a value inside the list
print(my_list[0])
print(my_list[-10])
print(my_list[9])
print(my_list[-1])

## Print some value inside the list
# print(my_list[start : end : step])
print(my_list[:10])
print(my_list[0:])
print(my_list[-10:])
print(my_list[2:8])
print(my_list[-8:-2])
print(my_list[0:10:2])
print(my_list[-1:-10:-3])
print(my_list[::2])

## Print reserved strings
name = "Alexander Bob"
print(name[:-4:-1])
print(name[-5::-1])

## Print String the selected value of strings
my_str = "https://www.google.com/"
print(my_str[:5])
print(my_str[8:-1])
print(my_str[-5:-1])
