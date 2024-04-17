import shutil

def mv_files(src, dst):
    shutil.move(src, dst)

# mv_files('./files/01_file.txt', './files/subfolder/text.txt')
mv_files('./xyz', 'python-3-working-files/03/demos/files')
