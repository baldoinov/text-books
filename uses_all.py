"""
Write a function named uses_all that takes a word and a string ofrequired letters, 
and that returns True if the word uses all the required letters at least once. 

How many words are there that use all the vowels aeiou? How about aeiouy?
"""

def uses_all(word, required):

    for letter in required:
        if letter not in word:
            return False
        return True

required_letters = str(input("\nEnter a string with the required letters: ")).lower()

words_required = 0
fin = open('think-python-2e-exercises/words.txt')

for line in fin:
    word = line.strip()
    if uses_all(word, required_letters):
        words_required += 1

print(f"\nThere are {words_required} words that use all the letters in '{required_letters}'.")
