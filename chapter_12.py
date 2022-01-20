# As an exercise, write a function called sum_all that takes any number of 
# arguments and returns their sum.

def sum_all(*args) -> int:

    c = 0
    for val in args:
        c += val

    return c

print(sum_all(1, 2, 3, 4, 5))