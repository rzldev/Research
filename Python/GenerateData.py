import csv, random, time, requests, re
from bs4 import BeautifulSoup as bs


class GenerateData:

    total_row = 1
    target_row = 63
    list_name = []
    list_random_name = []
    list_date = []
    list_address = []
    list_gender = []
    list_religion = []
    list_education = []
    list_phone_number = []
    list_email = []

    ## Name
    with open('additionals/Names.csv', 'r') as csv_names :
        csv_reader = csv.reader(csv_names)
        for name in csv_reader :
            list_name.append(''.join(name))

    wrong_word = ['PT', 'PT.', 'P.T.', 'Group', 'Ltd.']
    while total_row <= target_row :
        random_name = random.choice(list_name)
        if random_name not in list_random_name and random_name is not None and random_name is not '' and len(random_name.split(' ')) < 5 and len(random_name.split(' ')) > 1 :
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

                    # print(str(no) + ' ' + address)
                    list_address.append(address)
                    no += 1
                    if no == target_row + 1 :
                        break

        if no == target_row + 1 :
            break

    ## Gender
    jkel = ['L', 'P']
    for row in range(target_row):
        random_gender = random.choice(jkel)
        list_gender.append(random_gender)


    ## Religion
    religion = ['Islam', 'Kristen', 'Khatolik', 'Hindu', 'Budha']
    for row in range(target_row):
        random_religion = random.choices(religion, weights=[10, 2, 2, 1, 1])
        list_religion.append(''.join(random_religion))

    ## Education
    education = ['S1 Sistem Informasi', 'S1 Teknik Informatika', 'S1 Sistem Komputer']
    for row in range(target_row) :
        random_education = random.choices(education, weights=[10, 5, 2])
        list_education.append(''.join(random_education))

    ## Phone Number
    provider_format = [
    '0817', '0818', '0819', '0859', '0877', '0878',
    '0896', '0897', '0898', '0899',
    '0811', '0812', '0813', '0821', '0822', '0823', '0851', '0852',
    '0855', '0856', '0857', '0858', '0814', '0815', '0816'
    ]
    for row in range(target_row) :
        random_provider = random.choice(provider_format)
        random_phone_number = random_provider + str(random.randint(111111111, 999999999))
        list_phone_number.append(random_phone_number)

    ## Email
    for name in list_random_name :
        type = ['name', 'number']
        mail = ['@gmail.com', '@gmail.co.id']
        get_type = random.choice(type)
        first_name = re.compile(r'(\w+)\s')
        first_name = first_name.findall(name)
        second = re.compile(r'\s[a-zA-Z]')
        second = second.findall(name)
        second = ''.join(second)
        if get_type is 'name' and first_name is not '' :
            gen_email = ''.join(first_name) + second + random.choice(mail)
            gen_email = gen_email.replace(' ', '')
            list_email.append(gen_email)
        else :
            gen_email = ''.join(first_name) + str(random.randint(11, 99)) + random.choice(mail)
            list_email.append(gen_email)

    with open('additionals/calon_karyawan.csv', 'w') as new_csv :
        fieldnames = ['id', 'nm_kar', 'ttl_kar', 'almt_kar', 'jkel', 'agama', 'pendidikan', 'telp', 'email']
        csv_writer = csv.writer(new_csv, delimiter='\t')
        csv_writer.writerow(fieldnames)
        for now in range(target_row) :
            x = now + 1
            row = [x, list_random_name[now], list_date[now], list_address[now], list_gender[now], list_religion[now], list_education[now], list_phone_number[now], list_email[now]]
            # print(row)
            csv_writer.writerow(row)

    with open('additionals/tes_psikologi.csv', 'w') as new_csv :
        csv_writer = csv.writer(new_csv, delimiter='\t')
        random_score1 = []
        random_score2 = []
        random_score3 = []
        random_score4 = []
        random_score5 = []
        fieldnames = ['id', 'nama', 'kejujuran', 'keberanian', 'tanggung_jawab', 'percaya_diri', 'tangguh']
        csv_writer.writerow(fieldnames)
        score = list(range(10, 40)) + list(range(50, 70)) * 30 + list(range(80, 100)) * 3
        x = 0
        num = 1
        while x < target_row:
            score1 = random.choice(score)
            score2 = random.choice(score)
            score3 = random.choice(score)
            score4 = random.choice(score)
            score5 = random.choice(score)
            if score1 % 2 == 0 and score2 % 2 == 0 and score3 % 2 == 0 and score4 % 2 == 0 and score5 % 2 == 0 :
                row = [num, list_random_name[x], score1, score2, score3, score4, score5]
                # print(row)
                csv_writer.writerow(row)
                x += 1
                num += 1
