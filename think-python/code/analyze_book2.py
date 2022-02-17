"""
Python provides a data structure called set that provides many common set operations. 
You can read about them in Section 19.5, or read the documentation at 
http://docs.python.org/3/library/stdtypes.html#types-set .

Write a program that uses set subtraction to find words in the book that are not in the word list.
"""

from analyze_book import process_line

def skip_header(file: open) -> None:

    for line in file:
        
        if line.startswith("*** START OF THE"):
            
            break
    

def readbook() -> frozenset:
    """Reads a plain text file from Project Gutenberg and makes a histogram with the words in
    the book."""

    file = open('think-python-2e-exercises/great-expectations.txt', 'r', encoding='utf-8')
    skip_header(file)

    words = set()

    for line in file:
        
        if line.startswith('*** END OF THE'):
            break

        for word in process_line(line):
            
            words.update([word])

    return words

def readfile() -> set:

    file = open('think-python-2e-exercises/words.txt', 'r', encoding='utf-8')
    listwords = set()

    skip_header(file)

    for line in file:

        if line.startswith('*** END OF THE'):
            break

        for word in process_line(line):
            
            listwords.update([word])
    
    # print(listwords)

    return listwords


if __name__ == '__main__':
    
    book = readbook()
    words = readfile()
    
    print(book.difference(words))
