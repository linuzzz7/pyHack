import json


def read_print_json(fn, pretty, sort):
    with open(fn) as json_file:
        data = json.load(json_file)
        print(json.dumps(data, sort_keys=sort, indent=4) if pretty else data)


def update_author_json(fn, arr_name, pos, key, value):
    with open(fn, 'r') as json_file:
        data = json.load(json_file)
        # получаем доступ к данным которые хотим обновиить
        data[arr_name][pos] = value
        with open(fn, 'w') as write_file:
            json.dump(data, write_file)


# read_print_json('./files_to_read/authors.json', False, False)
update_author_json('./files_to_read/authors.json', 'authors', 1, 'courses', 10)
