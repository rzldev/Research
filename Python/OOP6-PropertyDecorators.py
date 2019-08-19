
## Create a class with variable
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

employee1 = Employee('Clark', 'Kent', 2000)
employee2 = Employee('Bruce', 'Wayne', 100000)

print(employee2.first)
print(employee2.full_name())
print(employee2.email())

print()

employee2.first = employee1.first

print(employee2.first)
print(employee2.full_name())
print(employee2.email())

print()

class New_Employee :

    def __init__(self, first, last, salary) :
        self.first = first
        self.last = last
        self.salary = salary

    @property
    def full_name(self) :
        full = self.first + ' ' + self.last
        return full

    @property
    def email(self) :
        email = self.first + '.' + self.last + '@gmail.com'
        return email

    @full_name.setter
    def full_name(self, name) :
        first, last = name.split(' ')
        self.first = first
        self.last = last

employee2 = New_Employee('Bruce', 'Wayne', 100000)

print(employee2.first)
print(employee2.full_name)
print(employee2.email)

print()

employee2.full_name = "Clark Kent"

print(employee2.first)
print(employee2.full_name)
print(employee2.email)
