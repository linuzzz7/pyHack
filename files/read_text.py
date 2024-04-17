def read_txt(fn):
    with open(fn, 'r') as f:
        print(f.read())

def read_txt_by_line(fn):
    with open(fn, 'r') as f:
        lines = f.readlines()
        for line in lines:
            print(line, end='')
            line = f.readline()

def write_new_txt(fn, str):
    with open(fn, 'w', encoding='utf-8') as f:
        f.write(str)

def append_line_txt(fn, str):
    with open(fn, 'a', encoding='utf-8') as f:
        f.write('\n')
        f.write(str)

# Чтение файла целиком
# read_txt('./files_to_read/backup.py')
# построчное чтение файлов
# read_txt_by_line('./files_to_read/backup.py')
# Запись в новый файл
# write_new_txt('./files_to_read/example.txt', 'this is a test...')
append_line_txt('./files_to_read/example.txt', 'new line 2')
