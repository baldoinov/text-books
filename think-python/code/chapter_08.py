def print_while_bcwd(string):
    
    index = -1
    while index >= -len(string):
        letter = string[index]
        print(letter)
        index = index - 1
        

def print_for_bcwd(string):

    size = - (len(string) + 1)

    for i in range(-1, size, -1):
        print(string[i])


def string_concat(string):
    prefixes = 'JKLMNOPQ'
    suffix1 = 'ack'
    suffix2 = 'uack'

    for letter in prefixes:

        if letter == 'O' or letter == 'P':
            print(letter + suffix2)

        print(letter + suffix1)


def find(word, letter, start=0):
    
    if start > len(word):
        return
    
    while start < len(word):
        if word[start] == letter:
            return start
        start += 1
    
    return -1


def count_1(string, letter):

    count = 0
    for i in string:
        if i == letter:
            count += 1
    
    return count


def count_2(string, letter):

    count = 0
    i = 0

    while i < len(string):
        k = find(string, letter, i)
        
        if k == -1:
            break

        count = count + 1
        i = k + 1


def is_reverse(w1, w2):

    if len(w1) != len(w2):
        return False
    
    i = 0
    j = len(w2) - 1

    while j >= 0:
        if w1[i] != w2[j]:
            return False
        
        i += 1
        j -= 1
    
    return True

# print_while_bcwd("Vitor")
# print_for_bcwd("Baldoino")
# print(find("Vitor Baldoino", "B"))
# print(find("Vitor Baldoino", "V", 3))
# print(count_1("Vitor Baldoino", "V"))
# print(count_1("Vitor Baldoino", "o"))
# print(is_reverse('stop', 'pots'))
# print('banana'.count('a'))