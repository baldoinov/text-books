# As an exercise, use get to write histogram more concisely. You should be 
# able to eliminate the if statement.

from reverse_pair import make_wordlist, in_bisect
import time

def histogram(s: str or list) -> dict:
    
    d = dict()
    for char in s:
        d[char] = 1 + d.get(char, 0)
    
    return d


# A previously computer value that is store for later use
# is called a memo.

known = {0:0, 1:1}

def fibonacci(n: int) -> int:

    if n in known:
        return known[n]

    val = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = val
    return val


# Write a function that reads the words in words.txt and stores them as keys 
# in a dictionary. It doesn’t matter what the values are. Then you can use 
# the in operator as a fast way to check whether a string is in the dictionary.

# You can compare the speed of this implementation with the list in operator 
# and the bisection search.


def make_worddict() -> dict:
    """Creates a dictionary with all words in a file."""

    fin = open('think-python-2e-exercises/words.txt')

    word_dict = {}
    
    for line in fin:
        word = line.strip()
        word_dict[word] = 1
    
    return word_dict


def compare_methods():
    """Compares the speed of three different forms of using the in operator."""


    start_t = time.time()
    if "shoe" in make_worddict():
        print("\nI found the word shoe in the dictionary.")
    end_t = time.time()
    print(f"The execution using a dict took {end_t - start_t} seconds.\n")


    start_t = time.time()
    if "shoe" in make_wordlist():
        print("I found the word shoe in the list.")
    end_t = time.time()
    print(f"The execution using a list took {end_t - start_t} seconds.\n")
    

    start_t = time.time()
    if in_bisect(make_wordlist(), "shoe"):
        print("I found the word shoe using binary search.")
    end_t = time.time()
    print(f"The execution using in_bisect() took {end_t - start_t} seconds.")


