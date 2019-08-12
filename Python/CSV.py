
## CSV (Comma Separated Values) format is the most common import and export format for spreadsheets and databases
## Import CSV module
import csv

## Read csv file
with open('additionals/names.csv', 'r') as csv_file :
    csv_reader = csv.reader(csv_file)

## Print the content of the csv file
with open('additionals/names.csv', 'r') as csv_file :
    csv_reader = csv.reader(csv_file)
    for line in csv_reader :
        print(line)

print()

## Print the content of the csv file based by it's column/index
with open('additionals/names.csv', 'r') as csv_file :
    csv_reader = csv.reader(csv_file)
    # doesn't show the column name
    next(csv_reader)
    for line in csv_reader :
        print(line[2])

print()

# or using DictReader

with open('additionals/names.csv', 'r') as csv_file :
    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader :
        print(line['first_name'], line['last_name'])

print()

## Write the csv file
with open('additionals/names.csv', 'r') as csv_file :
    csv_reader = csv.reader(csv_file)

    with open('additionals/new-names.csv', 'w') as new_csv :
        csv_writer = csv.writer(new_csv, delimiter='\t')

        for line in csv_reader :
            csv_writer.writerow(line)

# or using DictWriter
with open('additionals/names.csv', 'r') as csv_file :
    csv_reader = csv.DictReader(csv_file)

    with open('additionals/new-names.csv', 'w') as new_csv :
        fieldnames = ['first_name', 'last_name', 'email']
        csv_writer = csv.DictWriter(new_csv, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader :
            csv_writer.writerow(line)

## Write new csv file without one of the column
with open('additionals/names.csv', 'r') as csv_file :
    csv_reader = csv.DictReader(csv_file)

    with open('additionals/new-names.csv', 'w') as new_csv :
        fieldnames = ['first_name', 'last_name']
        csv_writer = csv.DictWriter(new_csv, fieldnames=fieldnames, delimiter='\t')
        csv_writer.writeheader()

        for line in csv_reader :
            del line['email']
            csv_writer.writerow(line)

## Read the new file
with open('additionals/new-names.csv', 'r') as csv_file :
    csv_reader = csv.reader(csv_file, delimiter='\t')
    for line in csv_reader :
        print(line)
