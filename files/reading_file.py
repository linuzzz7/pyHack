import zipfile

def read_zip(zipf):
    with zipfile.ZipFile(zipf, 'r') as archive:
        lst = archive.namelist()
        for l in lst:
            zfint = archive.getinfo(l)
            print(f'{l} => {zfint.file_size} bytes, {zfint.compress_size} compressed')

read_zip('./files.zip')
