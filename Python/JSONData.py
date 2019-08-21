
## JSON (JavaScript Object Notation) is a lightweight data-interchange format. It is easy for humans to read and write
## Import JSON
import json

## Create a json variable with it's values
employee = '''
    {
        "employee": [
            {
                "name":      "Bob",
                "salary":      56000,
                "married":    true
            },
            {
                "name":       "Marry",
                "salary":      60000,
                "married":    true
            }
        ]
    }
'''

data = json.loads(employee)

## Print the data
print(data)

# or
for emp in data['employee'] :
    print(emp['name'], emp['salary'])

## Delete specific data
for emp in data['employee'] :
    del emp['married']

print(data)

## dumps() function >> convert Python object into a JSON string
new_data = json.dumps(data)
print(new_data)

## Using indent
new_data = json.dumps(data, indent=2)
print(new_data)

## sort_keys
new_data = json.dumps(data, indent=2, sort_keys=True)
print(new_data)

## Open JSON files
with open('additionals/states.json') as jsonf :
    data = json.loads(jsonf.read())

## Modify the data
for state in data['states'] :
    del state['area_codes']

## Create a JSON file
with open('additionals/new-states.json', 'w') as file :
    file_writer = json.dump(data, file, indent=2)

## Grab json data from internet
## Import urlopenlibrary
from urllib.request import urlopen

## Grab the data
with urlopen("http://dev.farizdotid.com/api/daerahindonesia/provinsi") as response:
    source = response.read()

print(source)

data = json.loads(source)
print(json.dumps(data, indent=2))

## Count the total item inside the data
print(len(data['semuaprovinsi']))

## Print specific data we want
for item in data['semuaprovinsi'] :
    id = item['id']
    name = item['nama']
    print(id, name)
