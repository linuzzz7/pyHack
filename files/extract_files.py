import zipfile

# для извлечения одного файла
def extract_file(zipf, fn, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extract(fn, path=path)
# извлечь один файл
def extract_all(zipf, path):
    with zipfile.ZipFile(zipf, 'r') as archive:
        archive.extractall(path=path)

# extract_file('./files.zip', 'files/01_file.csv', 'extracted')
extract_all('./files.zip', 'python-3-working-files/04/demos/extracted')