"""
A Caesar cypher is a weak form of encryption that involves “rotating” each letter 
by a fixed number of places. To rotate a letter means to shift it through the 
alphabet, wrapping around to the beginning if necessary, so 'A' rotated by 3 is 'D'
and 'Z' rotated by 1 is 'A'.

Write a function called rotate_word that takes a string and an integer as parameters, 
and returns a new string that contains the letters from the original string rotated 
by the given amount.

You might want to use the built-in function ord, which converts a character to a numeric 
code, and chr, which converts numeric codes to characters. Letters of the alphabet are 
encoded in alphabetical order.
"""

def rotate_word1(word, t):
    new_word = ''
    num_sequence = []
    
    for char in word:
        num_sequence.append(ord(char) + t)
    
    for num in num_sequence:
        new_word += chr(num)
    
    return new_word

def rotate_word(word, t):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    len_alph = len(alphabet)
    new_word = ''


    for char in word.lower():
        
        index = alphabet.find(char)

        if index + t > len_alph:
            new_word += alphabet[(index + t) - len_alph]
        else:
            new_word += alphabet[index + t] 
    
    return new_word


if __name__ == '__main__':

    encoded = rotate_word1('zelia', 3)
    encoded2 = rotate_word('zelia', 3)
    print(encoded)
    print(encoded2)
