
## Logging module defines functions and classes which implement a flexible event logging system for applications and libraries.

## Logging levels
# DEBUG: Detailed information, typically of interest only when diagnosing problems.
# INFO: Confirmation that things are working as expected.
# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
# ERROR: Due to a more serious problem, the software has not been able to perform some function.
# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

## Import logging library
import logging

## Change log format
file_log = 'additionals/test.log'
logging.basicConfig(filename=file_log, level=logging.DEBUG,
    format='%(asctime)s:%(levelname)s:%(message)s')

## Create function to test it
def add(x, y) :
    return f"Add: {x} + {y} = {x + y}"

def subtract(x, y) :
    return f"Sub: {x} - {y} = {x - y}"

def multiply(x, y) :
    return f"Mul: {x} x {y} = {x * y}"

def divide(x, y) :
    return f"Div: {x} : {y} = {x / y}"

a = 24
b = 15

print(add(a, b))
print(subtract(a, b))
print(multiply(a, b))
print(divide(a, b))

print()

## Use th logging levels
print(logging.debug(add(a, b)))
print(logging.info(add(a, b)))
print(logging.warning(add(a, b)))
print(logging.error(add(a, b)))
print(logging.critical(add(a, b)))

print()

## Create class employee
class Employee :
    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary

        logging.info(f"Created Employee: {self.full_name}")

    @property
    def email(self) :
        return f"{self.first}.{self.last}@employee.com"

    @property
    def full_name(self) :
        return f"{self.first} {self.last}"

employee1 = Employee('Bruce', 'Wayne', 1000000)
employee2 = Employee('Clark', 'Kent', 10000)
