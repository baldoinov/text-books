"""
Memoize the Ackermann function from Exercise 6.2 and see if memoization makes it 
possible to evaluate the function with bigger arguments.
"""

# Known values took from Wikipedia
know = {(0, 0): 1, (0, 1): 2, (1, 0): 2, (1, 1): 3, (1, 2): 4, (2, 1): 5}

def ack(m, n):
    """Computes the Ackermann function A(m, n)
    
    See http://en.wikipedia.org/wiki/Ackermann_function
    
    n, m: non-negative integers
    """

    if m == 0:
        return n + 1
    
    if n == 0:
        return ack(m - 1, 1)
    
    if (m, n) in know:
        return know[(m, n)]
        
    else:
        know[(m, n)] = ack((m - 1), ack(m, (n - 1)))
        return know[(m, n)]


print(ack(3, 4))
print(ack(3, 6))
print(know)