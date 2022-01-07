"""
Write a function called is_abecedarian that returns True if the letters in 
a word appear in alphabetical order (double letters are ok). 

How many abecedarian words are there?
"""

def is_abecedarian(word):
    i = 0
    j = 1
    
    while j < len(word):
        
        if word[i] > word[j]:
            return False
        
        i += 1
        j += 1
    
    return True

word_count = 0
fin = open('think-python-2e-exercises/words.txt')

for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        word_count += 1

print(f"\nThere are {word_count} words that its letters appears in alphabetical order.")
