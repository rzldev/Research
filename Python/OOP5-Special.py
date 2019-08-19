
## Python OOP
class Employee1 :
    raise_amount = 0.3      #percentage
    number_of_employee = 0

    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary
        Employee1.number_of_employee += 1

    def info(self) :
        self.apply_raise_amount()
        self.full = self.first + ' ' + self.last
        self.email = self.first + '.' + self.last + '@company.com'
        self.emp_sal = '$' + str(self.emp_sal)
        return f"Name\t\t: {self.full}\nEmail\t\t: {self.email}\nSalary\t\t: {self.emp_sal}\n"

    def apply_raise_amount(self) :
        self.emp_sal = (1 + self.raise_amount) * self.salary
        return self.emp_sal

    def __repr__(self) :
        return f"{self.first} {self.last}"

class Employee2 :
    raise_amount = 0.3      #percentage
    number_of_employee = 0

    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary
        Employee2.number_of_employee += 1

    def info(self) :
        self.apply_raise_amount()
        self.full = self.first + ' ' + self.last
        self.email = self.first + '.' + self.last + '@company.com'
        self.emp_sal = '$' + str(self.emp_sal)
        return f"Name\t\t: {self.full}\nEmail\t\t: {self.email}\nSalary\t\t: {self.emp_sal}\n"

    def apply_raise_amount(self) :
        self.emp_sal = (1 + self.raise_amount) * self.salary
        return self.emp_sal

    def __repr__(self) :
        return f"{self.first} {self.last}"

    def __str__(self) :
        return f"{self.first}.{self.last}@company.com"

    def __add__(self, bonus_salary) :
        return (self.salary + bonus_salary)

    def __len__(self) :
        return len(f"{self.first} {self.last}")

## Python __repr__() function returns the object representation. It could be any valid python expression such as tuple, dictionary, string etc.
## Python __str__() function returns the string representation of the object.

employee1 = Employee1('Clark', 'Kent', 2000)
employee2 = Employee2('Bruce', 'Wayne', 100000)

print(employee1)
print(employee2)

print()

print(employee2.__repr__())
print(employee2.__str__())

print()

print(repr(employee2))
print(str(employee2))

print()

print(employee2.salary)
print(employee2 + 100000)

print()

print(len(employee2))
print(len(employee1))
