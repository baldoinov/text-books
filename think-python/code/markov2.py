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
from analyze_book import skip_header

class Markov:

    def __init__(self, file_path: str, prefix_lenght: int = 2) -> None:
        
        self.file_path = file_path
        self.prefix_lenght = prefix_lenght

    def read_file(self):
        
        self.file = skip_header(open(self.file_path, 'r', encoding='utf-8'))

    def build_dict(self) -> dict:
        
        self.map = {}
        
        for line in self.file:
            l = line.strip()

            if l.startswith('*** END OF THE'):
                break

            l = l.split()
            l_len = len(l)
            for i in range(1, l_len - 1):

                if l_len >= self.prefix_lenght + 1:
                    key = line[i - 1] + ' ' + line[i]
                
                    # This construction makes the suffixes list hava duplicates and I kept that way 
                    # to choose the suffixes based on their probability of appearing in the text
                    self.map[key] = self.map.get(key, []) + [line[i + 1]]
    
    def random_text(self, n: int = 50) -> str: 
        #This method depends of the implementation build in build_dict. That should be changed?

        text = []
        prefix_start = random.choice(list(self.map.keys()))
        suffix_start = random.choice(self.map[prefix_start]) 

        text += [prefix_start, suffix_start]

        while len(text) <= n:
            prefix_start = text[-2].split()
            suffix_start = text[-1].split()

            prefix = prefix_start[-1] + " " + suffix_start[-1]
            suffix = random.choice(self.map.get(prefix, [None]))

            if suffix == None:
                suffix = random.choice(list(self.map.keys()))
        
            text += [suffix]

        self.markov_text = " ".join(text)
    
    def perform_markov(self) -> str:

        self.read_file()
        self.build_dict()
        self.random_text()

        return self.markov_text