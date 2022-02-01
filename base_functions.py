"""
This script aggregates all the most used functions in the book.
"""

import string

def make_wordlist(file) -> list:
    """Creates a word list."""

    fin = open(file, 'r', encoding='utf-8')

    word_list = []
    
    for line in fin:
        word = line.strip()
        word_list.append(word)
    
    return word_list


def make_worddict() -> dict:
    """Creates a dictionary with all words in a file.
    
    First created in chapter_11.py
    """

    fin = open('think-python-2e-exercises/words.txt')

    word_dict = {}
    
    for line in fin:
        word = line.strip()
        word_dict[word] = ""
    
    return word_dict


def in_bisect(word_list: list, value: str) -> bool:
    """Takes a sorted list and a target value and returns True if the 
    word is in the list and False if it's not.
    """
    
    if len(word_list) == 0:
        return False
    
    middle = len(word_list) // 2

    if word_list[middle] == value:
        return True
    
    elif word_list[middle] > value: # Search the first half
        return in_bisect(word_list[:middle], value)
    
    else: # Search the second half        
        return in_bisect(word_list[middle + 1:], value)


def my_rotate_word(word: str, t: int) -> str:
    """My version of Caesar cypher. Uses only the aplphabet letters, makes no 
    distinction between lower case or upper case letters and was not tested for
    negative rotations.

    Created in the exercise rotate.py
    
    word: string that's going to be encrypted.
    t: the number by which the string is rotated.
    """

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    len_alph = len(alphabet)
    new_word = ''


    for char in word.lower():
        
        index = alphabet.find(char)

        if index + t >= len_alph:
            new_word += alphabet[(index + t) - len_alph]

        else:
            new_word += alphabet[index + t] 
    
    return new_word


def book_rotate_word(word: str, t: int) -> str:
    """Book's version of Caesar cypher. It's mote general and uses all character
    available in a computer. Makes distinction between lower case and upper case
    letter.

    Created in the exercise rotate.py
    """

    new_word = ''
    num_sequence = []
    
    for char in word:
        num_sequence.append(ord(char) + t)
    
    for num in num_sequence:
        new_word += chr(num)
    
    return new_word


def has_duplicates(s:list) -> dict:
    """Returns True if any element appears more than once in a sequence."""

    d = dict()

    for char in s:
        
        if char in d:
            return True

        d[char] = 1
    
    return False


def make_histogram(s: str or list) -> dict:
    """Takes a string or a list, finds its elements frequency and returns a dictionary with
    element-frequency as key-value pairs.
    """

    d = dict()
    for char in s:
        d[char] = 1 + d.get(char, 0)
    
    return d


def single(word: str) -> str:
    """Sorts the letters of a word and return it as a string to create an
    unique key in a dictionary.
    """

    s = sorted(list(word))
    return ''.join(s)


def find_anagrams(word_list: list) -> dict:
    """Finds all anagrams in a word list and returns it in a dictionary
    with the letters as a key.
    """
    
    d = dict()

    for word in word_list:
        
        unique_key = single(word)
        
        if unique_key in d:
            d[unique_key].append(word)
        else:
            d[unique_key] = [word]

    return d


def checks_anagrams(word: str, word_seq: dict) -> bool:
    """Checks if the given word has any anagrams in the word list."""

    s = ''.join(sorted(word))

    if s in word_seq:
        return True
    
    return False


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


if __name__ == '__main__':
    pass