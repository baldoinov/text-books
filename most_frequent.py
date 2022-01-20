"""
Write a function called most_frequent that takes a string and prints the letters in decreasing 
order of frequency. Find text samples from several different languages and see how letter 
frequency varies between languages. Compare your results with the tables at 
http://en.wikipedia.org/wiki/Letter_frequencies .

"""

from base_functions import make_histogram

def most_frequent(string: str) -> None:
    """Takes a string and prints its letters in decreasing order of frequency."""

    frequency = make_histogram(string)

    t = []
    for letter, freq in frequency.items():
        t.append((freq, letter))
   
    t.sort(reverse=True)

    for i in t:
        print(i)


if __name__ == '__main__':

    string = open('think-python-2e-exercises/words.txt').read()
    most_frequent(string)
