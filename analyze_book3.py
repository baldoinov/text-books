from analyze_book import process_line, readbook
import random
from bisect import bisect

def random_words(hist):

    hist_keys = hist.keys()
    index_list = []
    words = []
    accumulator = 0

    for i in hist_keys:
        accumulator = accumulator + hist[i]
        words.append(i)
        index_list.append(accumulator)
    

    rand_n = random.randint(0, accumulator - 1)
    indx = bisect(index_list, rand_n)

    return words[indx]


if __name__ == '__main__':
    book = readbook()
    print(random_words(book))
