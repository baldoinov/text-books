def ack(m, n):
    """Computes the Ackermann function A(m, n)
    
    See http://en.wikipedia.org/wiki/Ackermann_function
    
    n, m: non-negative integers
    """

    if m == 0:
        return n + 1
    
    if (m > 0) and (n == 0):
        return ack(m - 1, 1)
    
    if (m > 0) and (n > 0):
        return ack((m - 1), ack(m, (n - 1)))

    return None

b = ack(3, 4)
print(b)
