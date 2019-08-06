
# Create a dictionaries >> key value pair
student = {'name': 'Bryant', 'age': 25, 'hobby': ['Swimming', 'Programming']}

print(student)
print(student['name'])
print(student['hobby'])

# Alternative way
print(student.get('name'))
print(student.get('phone', 'Not Found'))

# Change the value of the dictionaries
student['name'] = "Bob"

print(student.get('name'))

# Add new value to the dictionaries
student['phone'] = '777-7777'

print(student)

# Update the dictionaries
student.update({'name': 'Tom', 'age': 15, 'city': 'New York'})

print(student)

# Remove value from dictionaries
del student['phone']

print(student)

student_pop = student.pop('city')

print(student_pop)
print(student)

# Check the length of the dictionaries keys
print(len(student))
print(student.keys())
print(student.items())

# Print key and value with looping
for key, value in student.items():
    print(key, value)
