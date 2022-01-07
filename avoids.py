"""

Write a function named avoids that takes a word and a string of forbidden letters,
and that returns True if the word doesn't use any ofthe forbidden letters.

Write a program that prompts the user to enter a string of forbidden letters and 
then prints the number of words [in words.txt] that don't contain any of them. 
Can you find a combination of 5 forbidden letters that excludes the smallest 
number of words?

"""

from heapq import nsmallest

def avoids(word, forbidden):
    
    for letter in word.lower():
        if letter in forbidden:
            return False
    return True


forbidden_letters = str(input("Enter a string with 5 forbidden letters: ")).lower()

words_not_forbidden = 0
fin = open('think-python-2e-exercises/words.txt')

for line in fin:
    word = line.strip()
    if avoids(word, forbidden_letters):
        words_not_forbidden += 1

print(f"\nThere is {words_not_forbidden} that don't use the forbidden letters.")


# Finding the combination of 5 forbidden letters that excludes the smallest number of words

letters_dict = {}
fin2 = open('think-python-2e-exercises/words.txt')

for line in fin2:
    word = line.strip().lower()

    for letter in word:
        if letter in letters_dict.keys():
            letters_dict[letter] += 1
        else:
            letters_dict[letter] = 1

smallest = nsmallest(5, letters_dict, key=letters_dict.get)

print(f"\nThe combination of letters that excludes the smallest number of words is {str(smallest)}")