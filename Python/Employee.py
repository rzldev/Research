import logging

## Standard employee class
class Employee :

    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary

    def full_name(self) :
        full = self.first + ' ' + self.last
        return full

    def email(self) :
        email = self.first + '.' + self.last + '@gmail.com'
        return email

## Format Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Setup the logger format
formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')

# Setup the file handler for the logger
file_handler = logging.FileHandler('additionals/Employee.log')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Setup the stream handler for the logger
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)

## Employee class with logging function
class Employee_log :
    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary

        logger.info(f"Created Employee: {self.full_name}")

    @property
    def email(self) :
        return f"{self.first}.{self.last}@employee.com"

    @property
    def full_name(self) :
        return f"{self.first} {self.last}"

employee1 = Employee_log('Bruce', 'Wayne', 1000000)
employee2 = Employee_log('Clark', 'Kent', 10000)

print()
