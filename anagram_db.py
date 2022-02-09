"""
Write a module that imports anagram_sets and provides two new functions: store_anagrams should 
store the anagram dictionary in a “shelf”; read_anagrams should look up a word and return a 
list of its anagrams.
"""

# Wrote this little module with all the functions widely used in the book's exercises.
import base_functions

if __name__ == '__main__':
    
    word_list = base_functions.make_wordlist('think-python-2e-exercises/words.txt')
    anagrams = base_functions.find_anagrams(word_list)
    
    base_functions.store_anagrams(dictionary=anagrams, db_name='anagrams')
    print(base_functions.read_anagrams(db_name='anagrams', key='aals'))