
## The try block lets you test a block of code for errors.And the except block lets you handle the error.
try :
    open_file = open('additionals/testfile.txt')
except Exception :
    print('Error detected!')

## Handle the error for File Not Found Error
try :
    open_file = open('additionals/testfile.txt')
except FileNotFoundError :
    print('File Not Found!')

## Try to combine it
try :
    open_file = open('additionals/test_file.txt')
    var = varA
except FileNotFoundError :
    print('File Not Found!')
except Exception :
    print('Error detected!')

## Using alias
try :
    open_file = open('additionals/testfile.txt')
    var = varA
except FileNotFoundError as e :
    print(e)

# or
try :
    open_file = open('additionals/RE_Data.txt')
    var = varA
except Exception as e :
    print(e)

print()

## Using else statement
try :
    open_file = open('additionals/test_file.txt')
    var = 'varA'
except FileNotFoundError :
    print('File Not Found!')
except Exception :
    print('Error detected!')
else :
    print(open_file.read())
    open_file.close()

## Using finally statements
try :
    open_file = open('additionals/test_file.txt')
    var = 'varA'
except FileNotFoundError :
    print('File Not Found!')
except Exception :
    print('Error detected!')
else :
    print(open_file.read())
    open_file.close()
finally :
    print('The code has been executed...')
