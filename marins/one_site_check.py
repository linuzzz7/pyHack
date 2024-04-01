import re
import requests


def check_one_site():
    url = input('Введите адрес сайта: ')
    try:
        reqs = requests.get(url)
        print('Код ответа сервера -', reqs.status_code)
        title = re.findall('<title>(.*?)</title>', reqs.text)[0]
        print('Заголовок на странице', "<<", title, ">>")
        print('-'*58)
    except:
        print('Site not available!!!')
        print('-' * 58)


if __name__ == '__main__':
    check_one_site()
