import zipfile

to_zip = ['./files/subfolder/01_file_test.txt',
          './files/subfolder/02_file.txt']

def create_zip(zipf, files, opt):
    with zipfile.ZipFile(zipf, opt, allowZip64=True) as archive:
        for f in files:
            archive.write(f)

create_zip('./files.zip', to_zip, 'w')
