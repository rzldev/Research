
## Context Manager In any programming language, the usage of resources like file operations or database connections is very common.
# But these resources are limited in supply.

## Open a file
file = open('additionals/text.txt')
content = file.read()
print(content)
file.close()
print(file.closed)

print()

# or
with open('additionals/text.txt') as f:
    content = f.read()

print(content)
print(f.closed)

print()

## Create a class to open a file
class Open_File() :
    def __init__(self, destination, mode) :
        self.destination = destination
        self.mode = mode

    def __enter__(self) :
        self.file = open(self.destination, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, traceback) :
        self.file.close()

## Try to open file with class that have been created
with Open_File('additionals/test_file.txt', 'r') as f :
    context = f.read()

print(context)

print(f.closed)

print()

## Create a class to open a file using context manager
# Import context manager
from contextlib import contextmanager

# Create a class
@contextmanager
def open_file(file, mode) :
    f = open(file, mode)
    yield f
    f.close()

with open_file('additionals/test_file.txt', 'r') as f :
    context = f.read()

print(context)

print(f.closed)

print()

## Try to change directory
# Import library
import os

# change directory
cwd = os.getcwd()
os.chdir('additionals')
print(os.getcwd())
os.chdir(cwd)
print(os.getcwd())

cwd = os.getcwd()
os.chdir('environment')
print(os.getcwd())
os.chdir(cwd)
print(os.getcwd())

print()

## Create class to change directory using context manager
@contextmanager
def changedir(destination) :
    cwd = os.getcwd()
    os.chdir(destination)
    yield
    os.chdir(cwd)

## Execute

with changedir('additionals') :
    print(os.getcwd())

print(os.getcwd())

with changedir('environment') :
    print(os.getcwd())

print(os.getcwd())
