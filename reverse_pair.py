"""
Two words are a “reverse pair” if each is the reverse of the other. 

Write a program that finds all the reverse pairs in the word list.
"""


def make_wordlist() -> list:
    """Makes a list of words and returns it as a list"""
    fin = open('think-python-2e-exercises/words.txt')

    word_list = []
    
    for line in fin:
        word = line.strip()
        word_list.append(word)
    
    return word_list


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


def find_reverse_pair(word_list: list) -> list:
    """Takes a word list, finds and returns all words that forms a reverse pair.
    """

    reverse_pairs = []
    for word in word_list:
        
        if in_bisect(word_list, word[::-1]): # Searches the reverse word in the word list
            reverse_pairs.append((word, word[::-1]))

    return reverse_pairs


if __name__ == '__main__':

    # This program takes considerably longer to run than the solution proposed by Allen Downey
    # because I store the lists into memory, rather than printing them right away.
    
    wordlist = make_wordlist()
    pairs = find_reverse_pair(wordlist)

    for i in pairs:
        print(i)



