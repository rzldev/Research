
## Open a file
open_file = open('additionals/text.txt', 'r')

## Print file name and mode
print(open_file.name)
print(open_file.mode)

## Close file
open_file.close()

## Open file using 'with' statement
with open('additionals/text.txt', 'r') as file :
    pass

## Check if the file closed or not
print(file.closed)

print()

## Read the contents inside the file
with open('additionals/text.txt', 'r') as file :
    print(file.read())

## Read a the content from the file with single line
with open('additionals/text.txt', 'r') as file :
    file_content = file.readlines()
    print(file_content)

print()

## Read a single line from the file
with open('additionals/text.txt', 'r') as file :
    file_content = file.readline()
    print(file_content)

## Read a multiple line content from the file using single line statements
with open('additionals/text.txt', 'r') as file :
    file_content = file.readline()
    print(file_content, end='')
    file_content = file.readline()
    print(file_content, end='')

print()

with open('additionals/text.txt', 'r') as file :
    for line in file :
        print(line, end='')

print()

## Print the first 99 character of a file
with open('additionals/text.txt', 'r') as file :
    file_content = file.read(100)
    print(file_content, '')

print()

# or
with open('additionals/text.txt', 'r') as file :
    size_to_read = 10
    file_content = file.read(size_to_read)
    while len(file_content) > 0 :
        print(file_content, end='*')
        file_content = file.read(size_to_read)

## Check the file proposition
with open('additionals/text.txt', 'r') as file :
    size_to_read = 100
    file_content = file.read(size_to_read)
    print(file.tell())

## Back to first line
with open('additionals/text.txt', 'r') as file :
    file_content = file.readline()
    print(file_content, end='')
    file_content = file.readline()
    print(file_content, end='')
    file.seek(0)
    file_content = file.readline()
    print(file_content, end='')

print()

## Write a file
write_file = open('additionals/new-text.txt', 'w')

## Write a file with contents inside
with open('additionals/new-text.txt', 'w') as file :
    file.write('Hello World!')

## The content of the file can be overwritten
with open('additionals/new-text.txt', 'w') as file :
    file.write('World!')

## Maybe you don't understand this
with open('additionals/new-text.txt', 'w') as file :
    file.write('Hello World!')
    file.seek(0)
    file.write('World')

## Copy file content into the new file
with open('additionals/text.txt', 'r') as t :
    with open('additionals/new-text.txt', 'w') as nt :
        for line in t :
            nt.write(line)

## Copy image content into a new image file as binary code
with open('additionals/silent-cats.jpg', 'rb') as sc :
    with open('additionals/new-cats.jpg', 'wb') as nc :
        for line in sc :
            nc.write(line)

with open('additionals/silent-cats.jpg', 'rb') as sc :
    with open('additionals/new-cats2.jpg', 'wb') as nc :
        chunk_size = 480
        sc_chunk = sc.read(chunk_size)
        while len(sc_chunk) > 0 :
            nc.write(line)
            sc_chunk = sc.read(chunk_size)
