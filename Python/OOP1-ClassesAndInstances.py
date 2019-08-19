
## Classes and instances
## Create a class
class Employee :
    pass

employee1 = Employee()
employee1.first_name = 'Bruce'
employee1.last_name = 'Wayne'
employee1.full_name = employee1.first_name + ' ' + employee1.last_name
employee1.email = employee1.first_name + '.' + employee1.last_name + '@company.com'
employee1.salary = 600

print(employee1.full_name)
print(employee1.email)
print('$' + str(employee1.salary))

## Create a class with constructors and functions
class New_Employee :
    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary

    def info(self) :
        self.full = self.first + ' ' + self.last
        self.email = self.first + '.' + self.last + '@company.com'
        self.emp_sal = '$' + str(self.salary)
        return f"Name\t: {self.full}\nEmail\t: {self.email}\nSalary\t: {self.emp_sal}"

new_employee = New_Employee('Clark', 'Kent', 1000)
print(new_employee.info())
