def rotate_word(word, t):
    new_word = ''
    num_sequence = []
    
    for char in word:
        num_sequence.append(ord(char) + t)
    
    for num in num_sequence:
        new_word += chr(num)
    
    return new_word

def rotate_word2(word, t):

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


encoded = rotate_word('zelia', 3)
encoded2 = rotate_word2('zelia', 3)
print(encoded)
print(encoded2)


