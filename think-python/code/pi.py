import math

def estimate_pi():

    estimated = 0
    inverted_pi = math.pi**(-1)
    constant = (2 * math.sqrt(2)) / 9801
    x = 0 
    
    while abs(estimated - inverted_pi) > 1e-15:
        num = fatorial(4 * x) * (1103 + 26390 * x)
        den = (fatorial(x) ** 4) * (396 ** (4 * x))
        term = constant * (num / den)

        estimated += term
        x += 1
    
    return estimated ** (-1)

def fatorial(n):

    if n <= 0:
        return 1
    else:
        return n * fatorial(n-1)


pi_s = estimate_pi()
pi_n = math.pi

print(f"Por math.pi, temos: {pi_n}\n"
      f"Pela nossa estimativa, temos {pi_s}")