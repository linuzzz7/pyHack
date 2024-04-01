import registration_end_date
import one_site_check
import all_sites_check
import create_db
import view_db


def print_menu():
    print("Проверка сайтов компании:",
          "\t Выбирете задачу:",
          "[1] Проверка БД сайтов на окончания регистрации.",
          "[2] Проверка БД сайтов на доступность.",
          "[3] Проверка одного сайта на доступность.",
          "[4] Создание БД для проверки. Данные из list_input_site.csv",
          "[5] Просмотр БД сайтов.",
          "[0] Выход.\n",
          sep="\n")


def main_loop():
    while True:
        print_menu()
        selection = input("Ваш выбор: ")
        print('-'*58)
        if selection == '1':
            registration_end_date.start_check()
            registration_end_date.print_results()
        elif selection == '2':
            all_sites_check.start_check()
        elif selection == '3':
            one_site_check.check_one_site()
        elif selection == '4':
            create_db.generate_full_list()
        elif selection == '5':
            view_db.view_db()
        elif selection == '0':
            print('Выход системы произведен')
            break
        else:
            continue


if __name__ == '__main__':
    main_loop()
