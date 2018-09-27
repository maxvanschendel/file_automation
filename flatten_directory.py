# moves all files in main directory subdirectories to main directory

from os import listdir, rename
from glob import glob
from pathlib import Path


directory = 'C:/Users/admin/PycharmProjects/ROoT/habitats/terrestrial_mammals/split/'
subdirectories = glob(directory+'*')

for dir in subdirectories:
    try:
        for f in listdir(Path(dir)):
            rename(Path(dir) / f, Path(directory) / f)
    except NotADirectoryError:
        pass
