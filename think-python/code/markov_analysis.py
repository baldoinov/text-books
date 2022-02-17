
import random
from analyze_book import skip_header


def markov(file_path: str, prefix_lenght: int = 2) -> dict:
    """Opens a book and perform Markov analysis on it.
    
    file_path: string with the path to the plain text file from Project Gutenberg (http://gutenberg.org)
    suffix_lenght: size of the prefix to be considered during the Markov analysis
    
    returns a dict mapping from prefixes to a collection of possible suffixes.
    """

    d = {}
    file = open(file_path, 'r', encoding='utf-8')
    skip_header(file)


    for l in file:
        line = l.strip()
        
        if line.startswith('*** END OF THE'):
            break

        line = line.split()
        list_len = len(line)
        
        for i in range(1, list_len - 1):
            
            if list_len >= prefix_lenght + 1:
                key = line[i - 1] + ' ' + line[i]
                
                # This construction makes the suffixes list hava duplicates and I kept that way 
                # to choose the suffixes based on their probability of appearing in the text
                d[key] = d.get(key, []) + [line[i + 1]]
                

    return d 
                
def random_text(d: dict, n: int) -> str:
    """Generates random text with n words based on a mapping from prefixes to suffixes."""

    text = []
    p_start = random.choice(list(d.keys()))
    s_start = random.choice(d[p_start])

    text += [p_start, s_start]

    while len(text) <= n:
            
        p_start = text[-2].split()
        s_start = text[-1].split()
        
        prefixes = p_start[-1] + " " + s_start[-1]
        suffix = random.choice(d.get(prefixes, [None]))

        if suffix == None:
            
            suffix = random.choice(list(d.keys()))

        text += [suffix]
    
    return " ".join(text)
        

if __name__ == '__main__':

    d = markov('think-python-2e-exercises/great-expectations.txt')
    text = random_text(d, 45)
    print(text)