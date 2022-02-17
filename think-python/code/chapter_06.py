from math import sqrt

def compare(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1

def hypotenuse(a, b):
    a_square = a**2
    b_square = b**2

    return sqrt(a_square + b_square)

def is_between(x, y, z):
    return x <= y <= z

result = is_between(3, 4, 5)
print(result)

isinstance()