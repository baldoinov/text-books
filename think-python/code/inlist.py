"""
To check whether a word is in the word list, you could use the in operator, but it would be 
slow because it searches through the words in order. 

Because the words are in alphabetical order, we can speed things up with a bisection search 
(also known as binary search), which is similar to what you do when you look a word up in 
the dictionary (the book, not the data structure). You start in the middle and check to see 
whether the word you are looking for comes before the word in the middle of the list. If so, 
you search the first half of the list the same way. Otherwise you search the second half.

Either way, you cut the remaining search space in half. If the word list has 113,809 words, 
it will take about 17 steps to find the word or conclude that it's not there.

Write a function called in_bisect that takes a sorted list and a target value and returns True 
if the word is in the list and False if it's not.
"""

def make_wordlist() -> list:

    fin = open('think-python-2e-exercises/words.txt')

    word_list = []
    
    for line in fin:
        word = line.strip()
        word_list.append(word)
    
    return word_list


def in_bisect_loop(word_list: list, value: str) -> bool:
    """Takes a sorted list and a target value and returns True if the 
    word is in the list and False if it's not.
    """

    while len(word_list) > 0:

        middle = len(word_list) // 2

        if word_list[middle] == value:
            return True
        
        elif word_list[middle] > value: # Search the first half
            word_list = word_list[:middle]
        
        elif word_list[middle] < value: # Search the second half 
            word_list = word_list[middle + 1:]

    return False


def in_bisect_recursion(word_list: list, value: str) -> bool:
    """Takes a sorted list and a target value and returns True if the 
    word is in the list and False if it's not.
    """
    
    if len(word_list) == 0:
        return False
    
    middle = len(word_list) // 2

    if word_list[middle] == value:
        return True
    
    elif word_list[middle] > value: # Search the first half
        return in_bisect_recursion(word_list[:middle], value)
    
    else: # Search the second half        
        return in_bisect_recursion(word_list[middle + 1:], value)

if __name__ == '__main__':
    list_of_words = make_wordlist()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list (checking with bisect_loop)', in_bisect_loop(list_of_words, word))

    print()

    for word in ['aa', 'alien', 'allen', 'zymurgy']:
        print(word, 'in list (checking with bisect_recursion)', in_bisect_recursion(list_of_words, word))

