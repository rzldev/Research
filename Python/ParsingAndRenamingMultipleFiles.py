
## The point of this python file is to create script to automate parsing and renaming multiple files
## Import os module
import os

## Make directory to work
os.makedirs('additionals/multiple-file/')

## Create all the files that will be need
write_file = open('additionals/multiple-file/Mercury - Solar System - #1.txt', 'w')
write_file = open('additionals/multiple-file/Venus - Solar System - #2.txt', 'w')
write_file = open('additionals/multiple-file/Earth - Solar System - #3.txt', 'w')
write_file = open('additionals/multiple-file/Mars - Solar System - #4.txt', 'w')
write_file = open('additionals/multiple-file/Jupiter - Solar System - #5.txt', 'w')
write_file = open('additionals/multiple-file/Saturn - Solar System - #6.txt', 'w')
write_file = open('additionals/multiple-file/Uranus - Solar System - #7.txt', 'w')
write_file = open('additionals/multiple-file/Neptune - Solar System - #8.txt', 'w')

## Change directory into working directory
os.chdir('additionals/multiple-file')
print(os.getcwd())

## Renaming the file
# Get all the file we need
for f in os.listdir() :
    # Split between the file name and the file extension
    f_name, f_ext = os.path.splitext(f)

    # Split every words inside the file name
    f_planet, f_system, f_number= f_name.split(' - ')

    # Custome all the words that already splitted
    f_planet = f_planet.strip()
    f_system = f_system.strip()
    f_number = f_number.strip()[1:].zfill(2)

    # Create a variable for the new file name
    new_file_name = f'{f_number} - {f_planet} - {f_system}{f_ext}'

    # Rename the file name
    os.rename(f, new_file_name)
