
## Class Variables
## Create a class with variable
class Employee :
    raise_amount = 0.3      #percentage
    number_of_employee = 0

    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary
        Employee.number_of_employee += 1

    def info(self) :
        self.apply_raise_amount()
        self.full = self.first + ' ' + self.last
        self.email = self.first + '.' + self.last + '@company.com'
        self.emp_sal = '$' + str(self.emp_sal)
        return f"Name\t: {self.full}\nEmail\t: {self.email}\nSalary\t: {self.emp_sal}\n"

    def apply_raise_amount(self) :
        self.emp_sal = (1 + self.raise_amount) * self.salary
        return self.emp_sal

employee1 = Employee('Clark', 'Kent', 2000)
employee2 = Employee('Bruce', 'Wayne', 100000)

print('Total employees : ' + str(employee1.number_of_employee))
print(employee1.info())
print(employee2.info())
