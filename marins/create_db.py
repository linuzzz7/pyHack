import csv
import requests
import re

nuance = []


def nuance_list():
    print('Сайты без автоматической проверки:\n')
    for i in nuance:
        print(i)
    print('-'*58)


def generate_full_list():
    with open('list_input_site.csv', 'r') as csvfile_reader, \
            open('Output_Data_base.csv', 'a') as csvfile_writer:
        site_reader = csv.reader(csvfile_reader)
        site_writer = csv.writer(csvfile_writer)
        for line in site_reader:
            if line[0] != '' and line[2] == '1':
                url = str('https://' + line[0])
                try:
                    reqs = requests.get(url)
                    title = re.findall('<title>(.*?)</title>', reqs.text)[0]
                    site_writer.writerow([line[1], url, reqs.url, title, reqs.status_code])
                    print([reqs.url, title])
                    reqs.url = '---=ERROR=---'
                except (requests.exceptions.ConnectionError, IndexError, requests.exceptions.TooManyRedirects):
                    site_writer.writerow([line[1], url, reqs.url, 'Any Error!!!!!!!!!!!!!'])
                    print([reqs.url, 'Any Error!!!!!!!!!!!!!'])
                    continue
            elif line[0] != '':
                nuance.append(line[0] + ' - ' + line[2])
                continue
            else:
                break
    print('Создание БД закончено.\n', '-'*58)
    nuance_list()




if __name__ == '__main__':
    generate_full_list()
