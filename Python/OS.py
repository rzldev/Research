
## OS module, this module provides a portable way of using operating system dependent functionality
## Import OS module
import os

## Print list directory of the module
print(dir(os))

## Print current directory
print(os.getcwd())

## Save the current directory
cwd = os.getcwd()

## Change directory
os.chdir('/home/rzl/')
print(os.getcwd())

## Change back directory
os.chdir(cwd)
print(os.getcwd())

print('')

## Print all the file and directory
print(os.listdir())

## Making directory
os.mkdir('Bob')

## Making directory with sub-directory
os.makedirs('Tom/Jane/TextFile.txt')

## Remove directory
os.rmdir('Bob/')

## Remove directory with it's sub-directory
os.removedirs('Tom/Jane/TextFile.txt')

## Rename directory
os.rename('test.txt', 'MyFile.txt')
os.rename('MyFile.txt', 'test.txt')

print('')

## Print information about a file
print(os.stat('OS.py'))
print(os.stat('OS.py').st_mtime)

## Print modified time of a file using our modified format
from datetime import datetime
my_datetime =os.stat('OS.py').st_mtime
# print(datetime.fromtimestamp(my_datetime))

print('')

## Print directory tree
for dirpath, dirnames, filenames in os.walk(os.getcwd()) :
    print('Current path\t: ', dirpath)
    print('Directories\t: ', dirnames)
    print('Files\t\t:', filenames)

print('')

## Print environment variables
print(os.environ)
print(os.environ.get('HOME'))

## Print a file path
# Create a path
file_path = os.path.join(os.environ.get('HOME'), '/home/user/text.txt')
print(file_path)

# Print the file or directory
file_path = os.path.basename('/home/user/text.txt')
print(file_path)

# Print the file or directory path
file_path = os.path.dirname('/home/user/text.txt')
print(file_path)

# Split between the file and the file's path
file_path = os.path.split('/home/user/text.txt')
print(file_path)

# Check if the path exist
file_path = os.path.exists('/home/user/text.txt')
print(file_path)

# Check if the directory exist
file_path = os.path.isdir('/home/user/text.txt')
print(file_path)

# Check if the file exist
file_path = os.path.isfile('/home/user/text.txt')
print(file_path)

# Split between the file and it's extension
file_path = os.path.splitext('/home/user/text.txt')
print(file_path)
