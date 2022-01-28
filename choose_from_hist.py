# Write a function named choose_from_hist that takes a histogram as defined in Section 11.2 and 
# returns a random value from the histogram, chosen with probability in proportion to frequency. 

import random
from typing import Tuple
from chapter_13 import readbook

def choose_from_hist(hist: dict) -> Tuple[str, float]:
    """Takes a histogram and chooses its keys with probability in proportion to frequency.
    
    hist: histogram
    
    returns: (chosen key, probability of getting this key)
    """

    t = []
    sample_space = 0

    for key, value in hist.items():
        
        sample_space += value
        t.extend([key] * value)

    chose = random.choice(t)
    prob = str(hist[chose]) + "/" + str(sample_space)

    return chose, prob

if __name__ == '__main__':

    book = readbook()
    chosen, prob = choose_from_hist(book)

    print(f"We chose the word '{chosen}'. The probability of getting this again is {prob}.")
    