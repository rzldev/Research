
## Inheritance allows us to define a class that inherits all the methods and properties from another class

## Python OOP
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
        return f"Name\t\t: {self.full}\nEmail\t\t: {self.email}\nSalary\t\t: {self.emp_sal}\n"

    def apply_raise_amount(self) :
        self.emp_sal = (1 + self.raise_amount) * self.salary
        return self.emp_sal

## Create a subclass that inherit the employee class
class Developer(Employee) :
    work = 'Programmer'

    def __init__(self, first, last, salary, specialist) :
        super().__init__(first, last, salary)
        self.specialist = specialist

    def info(self) :
        super().info()
        if self.specialist == '' :
            self.work = 'Employee'
            self.specialist = 'None'
        return f"Name\t\t: {self.full}\nEmail\t\t: {self.email}\nSalary\t\t: {self.emp_sal}\nWork\t\t: {self.work}\nSpecialist\t: {self.specialist}\n"

    ## Create another subclass that inherit the employee class
class Manager(Employee) :
    work = 'Manager'
    specialist = ''

    def __init__(self, first, last, salary, employees=None) :
        super().__init__(first, last, salary)
        if employees is None :
            self.employees = []
        else :
            self.employees = employees

    def info(self) :
        super().info()
        if self.work == 'Manager' :
            self.work = 'Manager'
            self.specialist = 'None'
        return f"Name\t\t: {self.full}\nEmail\t\t: {self.email}\nSalary\t\t: {self.emp_sal}\nWork\t\t: {self.work}\nSpecialist\t: {self.specialist}\n"

    def add_employee(self, employee) :
        if employee not in self.employees :
            self.employees.append(employee)

    def remove_employee(self, employee) :
        if employee in self.employees :
            self.employees.remove(employee)

    def print_employees(self) :
        print(f'Employee of {self.full}')
        for employee in self.employees :
            print('- ' + employee.full)

employee1 = Developer('Billy', 'Batson', 100, '')
developer1 = Developer('Clark', 'Kent', 2000, 'Java')
developer2 = Developer('Bruce', 'Wayne', 100000, 'Python')
manager1 = Manager('Hal', 'Jordan', 4000, [employee1])

print('Total employees : ' + str(developer1.number_of_employee))
print(manager1.info())
print(employee1.info())
print(developer1.info())
print(developer2.info())

manager1.add_employee(developer1)
manager1.add_employee(developer2)
manager1.print_employees()

print()

manager1.remove_employee(developer1)
manager1.add_employee(developer2)
manager1.print_employees()
