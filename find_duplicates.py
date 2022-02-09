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
from pathlib import Path

def search_dir(dir_name: str, file_suffix: str) -> list:
    """Iterates through a directory and all of its subdirectories and returns
    a list of absolute paths for all file with a given suffix.

    dir_name: absolute paht to directory
    file_suffix: string with file extension (e.g: .xlsx; .txt; etc)
    """
    
    files = [file for file in glob.glob(f"{dir_name}/**/*{file_suffix}", recursive=True)]
    return files

if __name__ == '__main__':
    print(search_dir(r'C:/Users/vitor/OneDrive/code-projects', '.py'))