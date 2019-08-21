
## Web Scrping using BeautifulSoup and requests
## BeautifulSoup is a Python library for pulling data out of HTML and XML files
## requests library is the de facto standard for making HTTP requests in Python

## Install beautifulsoup and requests using pip
# pip install beautifulsoup4
# pip install lxml
# pip install html5lib
# pip install requests

## import beautifulsoup and request library
from bs4 import BeautifulSoup as bs
import requests
import csv

## read html file contents with beautifulsoup
with open('additionals/indoxxi-script.html') as xxi :
    soup = bs(xxi, 'lxml')

## Print the file content using prettify function
# prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document
# print(soup.prettify())

## Print html file contents with some specific arguments
match = soup.title
print(match)
print()
print(match.prettify())

match = match.text
print(match)

print()

## Print html file contents with some specific class arguments
match = soup.find('div', class_ = 'mli-info')
print(match.prettify())

match_title = match.h2.text
print(match_title)

## Using find_all() statements
# for matches in soup.find_all('div', class_ = 'mli-info') :
#     match_title = matches.h2.text
#
#     print(match_title)

## Grab data from website with requests library
source = requests.get('https://indoxx1.center/').text
soup = bs(source, 'lxml')

## Open CSV File
csv_open = open('additionals/Movie-list.csv', 'w')
csv_writer = csv.writer(csv_open)
csv_writer.writerow(['Film', 'Rating', 'Link'])

## Grab data with specific class and arguments
for film in soup.find_all('div', class_ = 'ml-item') :

    film_title = film.a.h2.text

    film_rating = film.find('span', class_ = 'mli-rating')
    film_rating = film_rating.text
    if film_rating == '-' :
        film_rating = None

    film_link = film.find('a', class_ = 'ml-mask')['href']
    film_link = 'https://indoxx1.center/' + film_link

    print([film_title, film_rating, film_link])

    ## Export the content into csv file
    csv_writer.writerow([film_title, film_rating, film_link])

## Close the CSV file
csv_open.close()
