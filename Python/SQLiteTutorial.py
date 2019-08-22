
## SQLite is a C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine
## Import SQLite library
import sqlite3

## Create a connection to database
conn = sqlite3.connect('additionals/employee.db')
if conn :
    print('success')
else :
    print('failed')

print()

## cursor() allows Python code to execute PostgreSQL command in a database session
c = conn.cursor()

## Execute create table query
c.execute("CREATE TABLE employees(first_name text, last_name text, salary integer)")

## Execute insert query
c.execute("INSERT INTO employees VALUES('Bruce', 'Wayne', 1000000)")
c.execute("INSERT INTO employees VALUES('Clark', 'Kent', 7000)")

## Execute select query with fetchone() method
# fetchone() method returns a single record or None if no more rows are available
c.execute("SELECT * FROM employees")
print(c.fetchone())

## Execute select query with fetchmany(size) method
# fetchmany(size) returns the number of rows specified by size argument
c.execute("SELECT * FROM employees")
print(c.fetchmany(1))

## Execute select query with fetchall() method
# fetchall() fetches all the rows of a query result
c.execute("SELECT * FROM employees")
print(c.fetchall())

## commit() method sends a COMMIT statement to the MySQL server, committing the current transaction.
conn.commit()

print()

## Import employee class that had been created
from Employee import Employee as e

employee1 = e('Barry', 'Allen', 6500)
employee2 = e('Hal', 'Jordan', 10000)

print(employee1.first)
print(employee1.last)
print(employee1.salary)

print()

## Insert employee1 and employee2 into database
c.execute("INSERT INTO employees VALUES(?, ?, ?)", (employee1.first, employee1.last, employee1.salary))

# or
c.execute("INSERT INTO employees VALUES(:first_name, :last_name, :salary)", {'first_name' : employee2.first, 'last_name' : employee2.last, 'salary' : employee2.salary})

conn.commit()

## Execute select query with some specific parameters
c.execute("SELECT * FROM employees WHERE first_name = 'Hal' AND last_name = 'Jordan'")
print(c.fetchmany(2))

c.execute("SELECT * FROM employees WHERE salary > 8000")
print(c.fetchall())

print()

## Create a select, insert, update and delete function
def select_employee() :
    c.execute("SELECT * FROM employees")
    print(c.fetchall())

def select_employee_by_name(first) :
    c.execute("SELECT * FROM employees where first_name = :first", {'first' : first})
    print(c.fetchall())

def insert_employee(employee) :
    c.execute("INSERT INTO employees values(:first, :last, :salary)", {'first' : employee.first, 'last' : employee.last, 'salary' : employee.salary})
    conn.commit()

def update_employee_salary(employee, salary) :
    c.execute("UPDATE employees SET salary = :salary WHERE first_name = :first AND last_name = :last", {'first' : employee.first, 'last' : employee.last, 'salary' : salary})
    conn.commit()

def delete_employee(employee) :
    c.execute("DELETE FROM employees WHERE first_name = :first AND last_name = :last", {'first' : employee.first, 'last' : employee.last})
    conn.commit()

employee3 = e('Billy', 'Batson', 200)

insert_employee(employee3)
update_employee_salary(employee1, 7500)
delete_employee(employee2)
select_employee()
select_employee_by_name('Bruce')

## Close connection
conn.close()
