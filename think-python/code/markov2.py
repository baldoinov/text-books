"""

This example suggests a development plan for designing objects and methods: 
    1. Start by writing functions that read and write global variables (when necessary).
    2. Once you get the program working, look for associations between global variables 
    and the functions that use them.
    3. Encapsulate related variables as attributes of an object. 
    4. Transform the associated functions into methods of the new class.
As an exercise, download my Markov code from http://thinkpython2.com/code/markov.py, and 
follow the steps described above to encapsulate the global variables as attributes of a 
new class called Markov. Solution: http://thinkpython2.com/code/markov2.py.

"""

import random
from unittest import skip

from py import process
from analyze_book import skip_header

class Markov:
    """Represents the statiscal summary of a text."""

    def __init__(self) -> None:
        
        self.map = {}         # Mapping from prefixes to suffixes
        self.markov_text = "" # Current state of the generated text
    
    def process_file(self, filename: str, n: int = 2):
        """Opens a file and builds a mapping from prefixes to suffixes.
        
        filename: path to the file as a string
        n: number of words in the prefix
        """

        file = open(filename, 'r', encoding='utf-8')
        skip_header(file)

        for i in file:
            
            line = i.strip()

            if line.startswith('*** END OF THE'):
                break

            line = line.split()
            list_len = len(line)
            
            for i in range(1, list_len - 1):
            
                if list_len >= n + 1:
                    key = line[i - 1] + ' ' + line[i]
                    
                    # This construction makes the suffixes list hava duplicates and I kept that way 
                    # to choose the suffixes based on their probability of appearing in the text
                    self.map[key] = self.map.get(key, []) + [line[i + 1]]
    
    def random_text(self, n: int = 50):
        """Generates random text with n words based on a mapping from prefixes to suffixes."""

        text = []
        p_start = random.choice(list(self.map.keys()))
        s_start = random.choice(self.map[p_start])

        text += [p_start, s_start]

        while len(text) <= n:
                
            p_start = text[-2].split()
            s_start = text[-1].split()
            
            prefixes = p_start[-1] + " " + s_start[-1]
            suffix = random.choice(self.map.get(prefixes, [None]))

            if suffix == None:
                
                suffix = random.choice(list(self.map.keys()))

            text += [suffix]
        
        self.markov_text = " ".join(text)


if __name__ == '__main__':
    
    m = Markov()
    m.process_file('text-books/think-python/great-expectations.txt')
    m.random_text()
    print(m.markov_text)
