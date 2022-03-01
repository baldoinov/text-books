# 

def uses_all(word, required):
    """Checks if the word uses all the required letters."""
    
    for letter in required:
        if letter not in word:
            return False
        return True


def uses_all_advanced(word, required):
    return all(letter in word for letter in required)


def has_duplicates(t):

    d = {}

    for x in t:
        if x in d:
            return True
        d[x] = True
    return False


def has_duplicates_sets(t):
    return len(set(t)) < len(t)


def uses_only_sets(word, available):
    return set(word) <= set(available)


def avoids_og(word, forbidden):
    
    for letter in word.lower():
        if letter in forbidden:
            return False
    return True


def avoids_sets(word, forbidden):
    
    return not(set(forbidden) <= set(word))


def binomial_coeff(n: int, k: int) -> int:
    """Compute the binomial coefficient 'n choose k'.
    
    n: number of trials
    k: number of successes
    """

    return 1 if k == 0 else 0 if n == 0 else (binomial_coeff(n - 1, k) + binomial_coeff(n - 1, k - 1)) 


if __name__ == '__main__':

    print(binomial_coeff(8, 5))