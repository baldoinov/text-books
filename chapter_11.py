# As an exercise, use get to write histogram more concisely. You should be 
# able to eliminate the if statement.

def histogram(s: str or list) -> dict:
    
    d = dict()
    for char in s:
        d[char] = 1 + d.get(char, 0)
    
    return d


# A previously computer value that is store for later use
# is called a memo.

known = {0:0, 1:1}

def fibonacci(n: int) -> int:

    if n in known:
        return known[n]

    val = fibonacci(n - 1) + fibonacci(n - 2)
    known[n] = val
    return val