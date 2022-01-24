"""
Two words form a “metathesis pair” if you can transform one into the other by 
swapping two letters; for example, “converse” and “conserve”. Write a program 
that finds all of the metathesis pairs in the dictionary. Hint: don't test all 
pairs of words, and don't test all possible swaps.
"""

# 1º: Only test for words that have anagrams
# 2º: Test the swaps in the following way: traverse the words and each time 
# the letters are different, add +1 to a counter. If the counter is not equal to 2,
# the words can not form a metathesis pair. It's not necessary to add other tests 
# than that because we are already using anagrams from the word list.

from base_functions import make_wordlist, find_anagrams
from itertools import combinations

def letters_swap(word1: str, word2: str) -> bool:
    """Returns True if two words have only two letters swapped.
    """
    counter = 0
    
    for i in range(len(word1)):
        
        if word1[i] != word2[i]:
            counter += 1

    if counter != 2:
        return False
    else:
        return True


def metathesis(sets: dict) -> list:
    """Tests for all metathesis pairs inside a dictionary with anagrams.
    Returns a list with all the pairs.
    """

    pairs = []

    for vals in sets.values():
        
        # Using combinations in the case the same set of letters has more than two anagrams.
        for x in combinations(vals, r=2):

            if letters_swap(*x):
                pairs.append(x)

    return pairs


if __name__ == '__main__':
    
    word_list = make_wordlist()
    anagram_sets = find_anagrams(word_list)
    pairs = metathesis(anagram_sets)
    print(pairs)
