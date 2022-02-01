
import string
from base_functions import make_wordlist

"""
Write a program that reads a file, breaks each line into words, strips whitespace and 
punctuation from the words, and converts them to lowercase.
"""

def readfile():

    file = open('think-python-2e-exercises/great-expectations.txt', 'r', encoding='utf-8')
    listwords = []

    skip_header(file)

    for line in file:

        if line.startswith('*** END OF THE'):
            break

        for word in process_line(line):

            listwords.append(word)
    
    print(listwords)

"""
Go to Project Gutenberg (http://gutenberg.org) and download your favorite out-of-copyright 
book in plain text format. 

Modify your program from the previous exercise to read the book you downloaded, skip over the 
header information at the beginning of the file, and process the rest of the words as before.

Then modify the program to count the total number of words in the book, and the number of times 
each word is used.

Print the number of different words used in the book. Compare different books by different authors, 
written in different eras. Which author uses the most extensive vocabulary?
"""

def process_line(line: str) -> list:
    """Removes punctuation, hyphens and withespaces from lines.
    """

    removables = string.punctuation + '“' + '”' + "‘" + "’"
    mytable = "".maketrans({str(i): "" for i in removables})

    line = line.replace("-", " ")
    line = line.replace("—", " ")
    line = line.strip(string.whitespace)
    line = line.translate(mytable).lower()
    
    return line.split()


def skip_header(file) -> None:

    for line in file:
        
        if line.startswith("*** START OF THE"):
            
            break
    

def readbook() -> dict:
    """Reads a plain text file from Project Gutenberg and makes a histogram with the words in
    the book."""

    file = open('think-python-2e-exercises/great-expectations.txt', 'r', encoding='utf-8')
    skip_header(file)

    hist = {}

    for line in file:
        
        if line.startswith('*** END OF THE'):
            break

        for word in process_line(line):
        
            hist[word] = 1 + hist.get(word, 0)

    return hist


def most_frequent(hist: dict) -> list:
    """Takes a dict and builds a list in decreasing order of frequency."""

    t = []
    
    for word, freq in hist.items():
        t.append((freq, word))
   
    t.sort(reverse=True)

    return t

"""
Modify the previous program to read a word list (see Section 9.1) and then print all 
the words in the book that are not in the word list. How many of them are typos? 
How many of them are common words that should be in the word list, and how many of 
them are really obscure?
"""

def comparebook():

    word_list = make_wordlist()
    words_book = readbook()

    not_in_list = {}

    for word in words_book:

        if word not in word_list:
            
            # Gets the words and adds how many times it appears in the book
            not_in_list[word] = words_book[word]
            
    
    return not_in_list



if __name__ == '__main__':

    # hist = readbook()
    # frequency = most_frequent(hist)
    # for i in range(20):
    #     print(frequency[i])
    
    
    # compare = comparebook()
    # freq = most_frequent(compare)
    # for i in freq:
    #     print(i)
    
    pass
