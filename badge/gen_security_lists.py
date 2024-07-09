#!/usr/bin/env python3

import csv
from datetime import datetime

START_DATE = "2024-01-01 00:00:00"
#START_DATE = "2024-06-22 23:59:59"

ppl1 = []
ppl2 = []
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
        if ' ' not in name:
            print(f'Error: missing data in "{name}" ({code}). Skipping.')
            continue
        firstname, lastname = name.title().replace('El Hassen', 'El_Hassen').split(' ', 1)

        ppl1.append(f'{code} {firstname} {lastname}')
        ppl2.append(f'{lastname} {firstname}')

date = datetime.strptime(START_DATE, datetime_format).strftime('%Y%m%d-%H%M%S')
with open(f'{date}_ppl1.txt', 'w') as f:
    for i in sorted(ppl1):
        f.write(f'{i}\n')
with open(f'{date}_ppl2.txt', 'w') as f:
    for i in sorted(ppl2):
        f.write(f'{i}\n')
