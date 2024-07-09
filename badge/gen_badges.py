#!/usr/bin/env python3

import csv
from datetime import datetime

START_DATE = "2024-01-01 00:00:00"
#START_DATE = "2024-06-22 23:59:59"
SEP = '~'
MAXLEN = 18

orga_uk=[]
orga_fr=[]
speakers_uk=[]
speakers_fr=[]
attendees_uk=[]
attendees_fr=[]
with open('2024_orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        datetime_str = f"{row['Order date']} {row['Order time']}"
        datetime_format = "%Y-%m-%d %H:%M:%S"
        # ignore older records
        if datetime.strptime(datetime_str, datetime_format) < datetime.strptime(START_DATE, datetime_format):
            continue
        code = row['Order code']
        name = row['Attendee name']
        if SEP in name:
            print(f'Error: SEP "{SEP}" in {name} ({code}). Use another SEP!')
            exit()
        if ' ' not in name:
            print(f'Error: missing data in "{name}" ({code}). Skipping.')
            continue
        firstname, lastname = name.title().split(' ', 1)

        extra = row['Badge supplemental information'].replace("'@", '@')
        if SEP in extra:
            print(f'Error: SEP "{SEP}" in {extra} ({code}). Use another SEP!')
            exit()
        fr = row['Are you at ease to converse in French?']
        product = row['Product']

        if len(firstname) > MAXLEN:
            print(f'Warning: firstname field too long {firstname} ({code})')
        if len(lastname) > MAXLEN:
            print(f'Warning: lastname field too long {lastname} ({code})')
        if len(extra) > MAXLEN:
            print(f'Warning: extra field too long {extra} ({code})')

        record = f'{code}{SEP}{firstname}{SEP}{lastname}{SEP}{extra}'

        if product == 'Organization team tickets' and fr == 'No':
            orga_uk.append(record)
        elif product == 'Organization team tickets' and fr == 'Yes':
            orga_fr.append(record)
        elif product == 'Speakers tickets' and fr == 'No':
            speakers_uk.append(record)
        elif product == 'Speakers tickets' and fr == 'Yes':
            speakers_fr.append(record)
        elif product in ['Regular ticket', 'Sponsors tickets'] and fr == 'No':
            attendees_uk.append(record)
        elif product in ['Regular ticket', 'Sponsors tickets'] and fr == 'Yes':
            attendees_fr.append(record)
        else:
            print('Error Product="%s" French="%s". Skipping.' % (product, fr))
            continue
#    attendees_fr.append(f'ZZZZZ{SEP}Victor{SEP}Teuwen{SEP}')
#    attendees_fr.append(f'ZZZZZ{SEP}Arthur{SEP}Teuwen{SEP}')

date = datetime.strptime(START_DATE, datetime_format).strftime('%Y%m%d-%H%M%S')
with open(f'{date}_orga_uk.txt', 'w') as f:
    for i in sorted(orga_uk):
        f.write(f'{i}\n')
with open(f'{date}_orga_fr.txt', 'w') as f:
    for i in sorted(orga_fr):
        f.write(f'{i}\n')
with open(f'{date}_speakers_uk.txt', 'w') as f:
    for i in sorted(speakers_uk):
        f.write(f'{i}\n')
with open(f'{date}_speakers_fr.txt', 'w') as f:
    for i in sorted(speakers_fr):
        f.write(f'{i}\n')
with open(f'{date}_attendees_uk.txt', 'w') as f:
    for i in sorted(attendees_uk):
        f.write(f'{i}\n')
with open(f'{date}_attendees_fr.txt', 'w') as f:
    for i in sorted(attendees_fr):
        f.write(f'{i}\n')
