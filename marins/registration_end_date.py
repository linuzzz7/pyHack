#!/usr/bin/env python
import csv
import os
import time
from datetime import datetime, timedelta
import calendar
from datetime import datetime

current_datetime = str(datetime.now())[:16]
date = datetime.now()
days_in_month = calendar.monthrange(date.year, date.month)[1]
date += timedelta(days=days_in_month)
expiration = []


def start_check():
    with open('Data_base.csv', 'r') as csvfile_reader:
        site_reader = csv.reader(csvfile_reader)
        for line in site_reader:
            if line[1] != '':
                url = line[1].replace('https://', '')
                if 'www' in url:
                    continue
                date_ex = os.popen(f'whois {url} | grep paid-till').read()[15:-11]
                if date_ex == '':
                    continue
                domain_date = datetime.strptime(date_ex.replace('-', '.'), '%Y.%m.%d')
                if date > domain_date:
                    print(line[1], '-', date_ex, 'WARNING!!!')
                    expiration.append(line[1] + ' - ' + date_ex + ' WARNING!!!')
                else:
                    print(line[1], '-', date_ex)
                time.sleep(1)
            else:
                break


def print_results():
    print('-'*15, 'Данные на', current_datetime, '-'*15)
    for line in expiration:
        print(line)
    print('-'*58)


if __name__ == '__main__':
    start_check()
    print_results()
