import shutil

def copy_file(src, dst):
    shutil.copy(src, dst)

def copy_folder(src, dst):
    shutil.copytree(src, dst)
# copy file
#copy_file('./files/02_file.txt', './files/subfolder')
# copy folder
copy_folder('python-3-working-files/03/demos/files', './new_flder')
