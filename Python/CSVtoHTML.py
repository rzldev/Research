
## Import csv module
import csv

html_output = ' '
contributors = []

## Read csv file
with open('additionals/contributors.csv', 'r') as csv_file :
    csv_reader = csv.DictReader(csv_file)

    next(csv_reader)
    next(csv_reader)

    # write the csv file into the list
    for line in csv_reader :
        if line['FirstName'] == 'No Reward' :
            continue
        contributors.append(f'{line["FirstName"]} {line["LastName"]}')

## Print the list into HTML format
html_output += f'<P>There are currently {len(contributors)} public contributors. Thank you!</p>'
html_output += '\n<ul>'
for contributor in contributors :
    html_output += f'\n\t<li>{contributor}</li>'
html_output += '\n<ul>'

## Print the HTML
print(html_output)
