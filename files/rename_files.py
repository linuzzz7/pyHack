import os
from pathlib import Path

def rename_file_1(src, dst):
    os.rename(src, dst)

def rename_file_2(src, dst):
    f = Path(src)
    f.rename(dst)

rename_file_1('./files/01_file_test.txt', 'python-3-working-files/03/demos/files/01_new_file_test')