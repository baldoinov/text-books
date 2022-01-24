from base_functions import make_wordlist


def single(word: str) -> str:
    """Sorts the letters of a word and return it as a string."""

    s = sorted(list(word))
    return ''.join(s)


def find_anagrams(word_list: list) -> dict:
    """Finds all anagrams in a word list."""
    
    d = dict()

    for word in word_list:
        
        unique_key = single(word)
        
        if unique_key in d:
            d[unique_key].append(word)
        else:
            d[unique_key] = [word]

    return d


def print_anagrams(d: dict) -> None:
    """Prints the anagram sets in d."""

    t = []
    for v in d.values():

        if len(v) > 1:
            t.append((len(v), v))
    
    t.sort(reverse=True)

    for i in t:
        print(i)


word_list = make_wordlist()
print_anagrams(find_anagrams(word_list))
