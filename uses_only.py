"""
Write a function named uses_only that takes a word and a string of letters, 
and that returns True if the word contains only letters in the list.

Can you make a sentence using only the letters acefhlo? Other than “Hoe alfalfa”?
"""


def uses_only(word, only):
    
    for letter in word.lower():
        if letter not in only:
            return False
        return True

only_letters = str(input("\nEnter a string with the allowed letters: ")).lower()

words_allowed = 0
fin = open('think-python-2e-exercises/words.txt')

for line in fin:
    word = line.strip()
    if uses_only(word, only_letters):
        words_allowed += 1

print(f"\nThere are {words_allowed} words that use only the letters in '{only_letters}'.")
