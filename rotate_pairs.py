"""
Two words are “rotate pairs” if you can rotate one of them and get the other 
(see rotate_word in Exercise 8.5).
Write a program that reads a wordlist and finds all the rotate pairs.
"""

from base_functions import make_wordlist, make_worddict, in_bisect, my_rotate_word


def rotate_pairs(word_list: list) -> dict:
    """Takes a word list and finds all the words that can be obtained
    through the rotation of others.
    """

    pairs = {}

    for word in word_list:

        lenght = len(word) + 1

        for rotation in range(1, lenght):

            rotated = my_rotate_word(word, rotation)

            if in_bisect(word_list, rotated):

                pairs[dict] = rotated
    
    return pairs


def rotate_pairs_v2(word_dict: dict) -> dict:
    """Takes a word list and finds all the words that can be obtained
    through the rotation of others.
    """

    pairs = {}

    for word in word_dict:
        
        # lenght = len(word) + 1

        for rotation in range(1, 14):

            rotated = my_rotate_word(word, rotation)

            if rotated in word_dict:
                
                if pairs.get(word) == None:
                    pairs[word] = [rotated]
                else:
                    pairs[word] += [rotated]

    return pairs


if __name__ == '__main__':

    # words_list = make_wordlist()
    # pairs = rotate_pairs(words_list)
    # print(pairs)

    words_dict = make_worddict()
    pairs_v2 = rotate_pairs_v2(words_dict)
    print(pairs_v2)