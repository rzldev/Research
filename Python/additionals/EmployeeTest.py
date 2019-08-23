import requests

## Standard employee class
class Employee :
    raise_amount = 1.07

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

    def apply_amount(self) :
        self.salary = int(self.salary * self.raise_amount)

    def monthly_schedule(self, month) :
        response = requests.get(f"http://company.com/{self.last}/{month}")
        if response.ok :
            return response.text
        else :
            return 'Bad Response!'
