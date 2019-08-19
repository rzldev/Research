
## Classmethod receives the class as implicit first argument, just like an instance method receives the instance
## Staticmethod does not receive an implicit first argument.

## Python OOP
class Employee :
    raise_amount = 0.3      #percentage
    count_employee = 0

    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary
        Employee.count_employee += 1

    def info(self) :
        self.apply_raise_amount()
        self.full = self.first + ' ' + self.last
        self.email = self.first + '.' + self.last + '@company.com'
        self.emp_sal = '$' + str(self.emp_sal)
        return f"Name\t: {self.full}\nEmail\t: {self.email}\nSalary\t: {self.emp_sal}\n"

    def apply_raise_amount(self) :
        self.emp_sal = (1 + self.raise_amount) * int(self.salary)
        return self.emp_sal

    # Set the classmethod
    @classmethod
    def set_raise_amount(cls, amount_now) :
        cls.raise_amount = amount_now

    # Set another classmethod
    @classmethod
    def add_from_string(cls, string) :
        first, last, salary = string.split('-')
        return cls(first, last, salary)

    # Set the staticmethod
    @staticmethod
    def is_work_day(day) :
        if day.weekday() == 5 or day.weekday() == 6 :
            return f'{day} is not a work day'
        return f'{day} is a work day'

employee1 = Employee('Clark', 'Kent', 2000)
employee2 = Employee('Bruce', 'Wayne', 100000)

Employee.set_raise_amount(0.5)
print('Set raise amount: ', Employee.raise_amount)

employee3 = 'Billy-Batson-100'
employee4 = 'Hal-Jordan-2500'

employee3 = Employee.add_from_string(employee3)
employee4 = Employee.add_from_string(employee4)

print('Total employees : ' + str(employee1.count_employee))
print(employee1.info())
print(employee2.info())
print(employee3.info())
print(employee4.info())

import datetime
today = datetime.date.today()
my_day1 = datetime.date(2019, 8, 18)
my_day2 = datetime.date(2019, 8, 15)

print(Employee.is_work_day(today))
print(Employee.is_work_day(my_day1))
print(Employee.is_work_day(my_day2))
