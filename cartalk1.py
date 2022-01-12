"""
Give me a word with three consecutive double letters. I'll give you a couple of 
words that almost qualify, but don't. For example, the word committee, 
c-o-m-m-i-t-t-e-e. It would be great except for the 'i' that sneaks in there. 
Or Mississippi: M-i-s-s-i-s-s-i-p-p-i. If you could take out those i's it would work. 
But there is a word that has three consecutive pairs of letters and to the 
best of my knowledge this may be the only word. Of course there are probably 500 
more but I can only think of one. What is the word?
"""

def three_consective(word):
    
    consecutive = 0
    i = 0
    j = 1

    while j < len(word):
        if word[i] == word[j]:
            
            consecutive += 1
            j += 2
            i = j - 1
            
            if consecutive >= 3:
                return True
        
        else:
            i = j
            j = j + 1
            consecutive = 0
    
    return False
    


words_consecutive = []
word_count = 0
fin = open('think-python-2e-exercises/words.txt')

for line in fin:
    word = line.strip()
    if three_consective(word):
        word_count += 1
        words_consecutive.append(word)

print(f"\nThere are {word_count} words that have three consecutive letters."
      f"\nThe words are:"
      f"\n{words_consecutive}")
