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
