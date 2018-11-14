def list_functions():
    print('Available functions:')
    print('- flatten_directory')
    print('- remove_filename_prefix')
    print('- spaced_to_underscored')
    print('- get_all_files_in_tree')


# moves all files in main directory subdirectories to main directory
def flatten_directory():
    from os import listdir, rename
    from glob import glob
    from pathlib import Path

    directory = 'C:/Users/admin/PycharmProjects/ROoT/habitats/terrestrial_mammals/split/'
    subdirectories = glob(directory + '*')

    for dir in subdirectories:
        try:
            for f in listdir(Path(dir)):
                rename(Path(dir) / f, Path(directory) / f)
        except NotADirectoryError:
            pass


def remove_filename_prefix():
    from os import listdir, rename
    from tkinter import filedialog

    directory = filedialog.askdirectory() + '/'
    files = listdir(directory)

    for i in files:
        rename(directory + i, directory + i[9:])


def spaced_to_underscored():
    from os import listdir, rename
    from tkinter import filedialog

    directory = filedialog.askdirectory() + '/'
    files = listdir(directory)

    for i in files:
        rename(directory + i, directory + i.replace(' ', '_'))


def get_all_files_in_tree():
    import os
    from tkinter import filedialog

    stem_dir = filedialog.askdirectory() + '\\'
    all_files = []
    all_subdirs = []
    directories = [stem_dir]

    while len(directories):
        d = directories.pop(0)
        subdirectories = [x[0] for x in os.walk(d)][1:]
        files = os.listdir(d)

        for f in files:
            if d + f not in subdirectories:
                all_files.append(d + f)

    return all_files


