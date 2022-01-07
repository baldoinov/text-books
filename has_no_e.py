"""

In 1939 Ernest Vincent Wright published a 50,000 word novel called Gadsby 
that does not contain the letter “e”. Since “e” is the most common letter 
in English, that's not easy to do.

Write a function called has_no_e that returns True if the given word 
doesn't have the letter “e” in it.

Write a program that reads words.txt and prints only the words that 
have no “e”. Compute the percentage of words in the list that have no “e”.

"""

def has_no_e(word):

    if "e" in word.lower():
        return False
    
    return True

total_words = 0
no_e_words = 0
fin = open('think-python-2e-exercises/words.txt')

for line in fin:
    word = line.strip()
    total_words += 1
    
    if has_no_e(word):

        no_e_words += 1
        print(word)

pct_no_e = (no_e_words / total_words) * 100

print(f"\n {pct_no_e:.2} % don't have 'e'")
