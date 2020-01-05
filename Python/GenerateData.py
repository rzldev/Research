import csv, random, time, requests
from bs4 import BeautifulSoup as bs


class GenerateData:

    total_row = 1
    target_row = 63
    list_name = []
    list_random_name = []
    list_date = []
    list_address = []

    ## Name
    with open('additionals/Names.csv', 'r') as csv_names :
        csv_reader = csv.reader(csv_names)
        for name in csv_reader :
            list_name.append(''.join(name))

    while total_row <= target_row :
        random_name = random.choice(list_name)
        if random_name not in list_random_name and random_name is not None :
            list_random_name.append(random_name)
            total_row += 1

    ## Date
    total_row = 1
    while total_row <= target_row :
        start = "1/1/1980"
        end = "1/1/1998"
        format = '%m/%d/%Y'
        prop = random.random()
        stime = time.mktime(time.strptime(start, format))
        etime = time.mktime(time.strptime(end, format))

        ptime = stime + prop * (etime - stime)
        list_date.append('Surabaya, ' + time.strftime(format, time.localtime(ptime)))

        total_row += 1

    ## Address
    target_pages = 15
    no = 1

    for page in range(target_pages) :
        url = 'https://www.99.co/id/jual/rumah/surabaya?radius=-1&hlmn=' + str(page)
        source = requests.get(url).text
        soup = bs(source, 'lxml')
        # print(soup.find('html'))
        for items in soup.find_all('div', class_='search-card__info__title col-xs-7') :
            address = items.ul.text
            address = address.split('Surabaya')

            if address[0] == '' :
                address = []

            else :
                first_address = address[0]
                first_address = first_address.split()[-1]
                if '...' in first_address :
                    address = []

                else :
                    address.insert(1, 'Surabaya')
                    address = ', '.join(address)

                    print(str(no) + ' ' + address)
                    no += 1

    with open('additionals/calon_karyawan.csv', 'w') as new_csv :
        fieldnames = ['id', 'nm_kar', 'ttl_kar', 'almt_kar', 'jkel', 'agama', 'pendidikan', 'telp', 'email']
        csv_writer = csv.writer(new_csv, delimiter='\t')
        csv_writer.writerow(fieldnames)
