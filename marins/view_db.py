import csv


def view_db():
    print("Loading...")
    with open('Result_Scan.csv', 'r') as csvfile_reader:
        site_reader = csv.reader(csvfile_reader)
        # print('Адрес сайта', '\tДоступность', '\tКод ответа')
        for line in site_reader:
            if line[0] == 'Начало сканирования:':
                print(line[0], line[1])
                continue
            if line[0] == 'Всего не доступно:':
                print(line[0], line[1])
                break
            print(line[0], '-', line[1], '-', line[2])
    print('-' * 58)


if __name__ == '__main__':
    view_db()

