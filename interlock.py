"""
Two words 'interlock' if taking alternating letters from each forms a new word. For example, 
'shoe' and 'cold' interlock to form 'schooled'.
"""

from reverse_pair import make_wordlist
from inlist import in_bisect_loop


def find_interlock(word_list: list, word: str) -> bool:
    """Checks if a word can be obtained by interlocking two other words.
    
    word_list: list of strings
    word: string
    """

    even = word[::2]
    odd = word[1:2]

    return in_bisect_loop(word_list, even) and in_bisect_loop(word_list, odd)


if __name__ == '__main__':

    word_list = make_wordlist()

    for word in word_list:
        
        if find_interlock(word_list, word):
            
            print(word, word[::2], word[1::2])
