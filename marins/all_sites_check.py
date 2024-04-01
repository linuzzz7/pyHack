import csv
import time
import requests
import re
from datetime import datetime
current_datetime = str(datetime.now())[:16]
count_sites = 0


def check_site(url, title, code):
    global count_sites
    try:
        reqs = requests.get(url)
        title_check = re.findall('<title>(.*?)</title>', reqs.text)[0]
    except (requests.exceptions.ConnectionError, IndexError):
        count_sites += 1
        return url, "Сайт не доступен!!!", reqs.status_code
    if title == title_check and reqs.status_code == int(code):
        print(url, "SITE Available")
        result = url, "Сайт доступен", reqs.status_code
        return result
    else:
        print(url, "SITE - Unavailable!!!")
        result = url, "Сайт не доступен!!!", reqs.status_code
        count_sites += 1
        return result


def start_check():
    with open('Output_Data_base.csv', 'r') as csvfile_reader, \
            open('Result_Scan.csv', 'a') as csvfile_writer:
        site_reader = csv.reader(csvfile_reader)
        site_writer = csv.writer(csvfile_writer)
        site_writer.writerow(['Начало сканирования:', current_datetime])
        site_writer.writerow(['Адрес сайта', 'Доступность', 'Код ответа'])
        for line in site_reader:
            if line[1] != '' and line[2] != '' and line[3] != '':
                site_writer.writerow(check_site(line[2], line[3], line[4]))
                time.sleep(1)
            else:
                print(line[1], ' - ', 'Неправильный формат данных!!!')
                site_writer.writerow([line[1], line[2], 'Неправильный формат данных!!!'])
        site_writer.writerow(['Всего не доступно:', str(count_sites)])
        print('Всего не доступно:', str(count_sites))
        site_writer.writerow(['Конец сканирования:', current_datetime])
        site_writer.writerow(' ')
        print('Результат проверки в файле - Result_Scan.csv')


if __name__ == '__main__':
    start_check()