
## Import all the libraries we need
import logging
import Employee

## Create a logger so we can create more than one logging format
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Setup the logger format
formatter = logging.Formatter('%(asctime)s:%(levelname)s:%(message)s')

# Setup the file handler for the logger
file_handler = logging.FileHandler('additionals/Math.log')

# Set file handler error
file_handler.setLevel(logging.ERROR)

# Set the formatter and file handler into logger
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Setup the stream handler for the logger
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

## Create function to test it
def add(x, y) :
    return f"Add: {x} + {y} = {x + y}"

def subtract(x, y) :
    return f"Sub: {x} - {y} = {x - y}"

def multiply(x, y) :
    return f"Mul: {x} x {y} = {x * y}"

def divide(x, y) :
    try :
        result = x / y
    except ZeroDivisionError :
        logger.exception('Tried to divided by zero')
    else :
        return f"Div: {x} : {y} = {x / y}"

a = 24
b = 0


print(logger.debug(add(a, b)))
print(logger.debug(subtract(a, b)))
print(logger.debug(multiply(a, b)))
print(logger.debug(divide(a, b)))
