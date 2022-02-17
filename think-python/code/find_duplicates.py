"""
In a large collection of MP3 files, there may be more than one copy of the same song, stored in 
different directories or with different file names. The goal of this exercise is to search for 
duplicates.

1. Write a program that searches a directory and all of its subdirectories, recursively, and 
returns a list of complete paths for all files with a given suffix (like .mp3). Hint: os.path 
provides several useful functions for manipulating file and path names.

2. To recognize duplicates, you can use md5sum to compute a “checksum” for each files. If two 
files have the same checksum, they probably have the same contents.

3. To double-check, you can use the Unix command diff.
"""

import glob
import hashlib
from base_functions import make_histogram

def search_dir(dir_name: str, file_suffix: str) -> list:
    """Iterates through a directory and all of its subdirectories and returns
    a list of absolute paths for all file with a given suffix.

    dir_name: absolute paht to directory
    file_suffix: string with file extension (e.g: .xlsx; .txt; etc)
    """
    
    files = [file for file in glob.glob(f"{dir_name}/**/*{file_suffix}", recursive=True)]
    return files

def check_sum(files: list) -> list:
    """Computes the check sum for all files in a list and returns a list with the
    files that have the same content.
    
    files: list with files absolute paht
    """
    checks = []
    
    for file in files: 
        with open(file, 'rb') as f:
            checks.append(hashlib.md5(f.read()).hexdigest())
    
    dups_index = dup_index(checks).values()

    # Flattening the dict's values
    dup_files_index = [index for sublist in dups_index for index in sublist]
    dup_files = [files[i] for i in dup_files_index]
    
    return dup_files
    
    
def dup_index(s: list) -> dict:
    """Gets a list that might have duplicates and creates a dict with the list
    items as keys and their index as values. Only return items that have duplicates.
    """
    d = {}

    for element in s:

        # This could be easily done with a Numpy array    
        indices = [index for index, e in enumerate(s) if e == element]
        d[element] = indices
    
    dups = {key: value for key, value in d.items() if len(value) > 1}
    
    return dups

if __name__ == '__main__':
    files = search_dir(r'C:/Users/vitor/OneDrive/Imagens', '.jpg')
    dup_files = check_sum(files)
    
    # Writing the results to a file because I actually need to get some duplicated files purged
    with open('duplicated_files.txt', 'w') as file:
        for line in dup_files:
            file.write(f"{str(line)}\n")
