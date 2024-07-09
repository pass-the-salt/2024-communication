#!/usr/bin/env python3

import csv
from datetime import datetime

START_DATE = "2024-01-01 00:00:00"
#START_DATE = "2024-06-22 23:59:59"

ppl = []
with open('2024_orders.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=';')
    for row in reader:
        datetime_str = f"{row['Order date']} {row['Order time']}"
        datetime_format = "%Y-%m-%d %H:%M:%S"
        # ignore older records
        if datetime.strptime(datetime_str, datetime_format) < datetime.strptime(START_DATE, datetime_format):
            continue
        name = row['Attendee name']
        email = row['Email']
        ppl.append(f'{email};{name};')

date = datetime.strptime(START_DATE, datetime_format).strftime('%Y%m%d-%H%M%S')
with open(f'{date}_ppl_wifi.csv', 'w') as f:
    for i in sorted(ppl):
        f.write(f'{i}\n')
