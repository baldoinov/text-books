import time

def wordlist_1() :

    fin = open('think-python-2e-exercises/words.txt')

    word_list = []
    start_time = time.time()
    
    for line in fin:
        word = line.strip()
        word_list.append(word)
    
    append_time = time.time() - start_time

    print(f"The append method took {append_time} seconds to run.")


def wordlist_2():

    fin = open('think-python-2e-exercises/words.txt')

    word_list = []
    start_time = time.time()
    
    for line in fin:
        word = line.strip()
        word_list = word_list + [word]


        # Written this way it's slower because we are creating a new list at each
        # iteration, but append always use the same list.
        # https://stackoverflow.com/questions/25216962/python-concatenation-vs-append-speed-on-lists

        # To be faster with the idiom we can write  in this way: word_list += 1
    
    idiom_time = time.time() - start_time

    print(f"The idiom took {idiom_time} seconds to run.")

wordlist_1()
wordlist_2()
