"""
Write a function called sed that takes as arguments a pattern string, a replacement string, 
and two filenames; it should read the first file and write the contents into the second file 
(creating it if necessary). If the pattern string appears anywhere in the file, it should be 
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files, your program should 
catch the exception, print an error message, and exit.
"""

def sed(pattern: str, replacement: str, source: str, dest: str) -> None:
    
    try:
        src_file = open(source, 'r')
        dest_file = open(dest, 'w')
        
        replaced = src_file.read().replace(pattern, replacement)
        dest_file.write(replaced)

        src_file.close()
        dest_file.close()

    except:
        print("An error occured while reading or writing the file.")


if __name__ == '__main__':
    sed('zymology', 'vitor', 'think-python-2e-exercises/words.txt', 'think-python-2e-exercises/new_text.txt')