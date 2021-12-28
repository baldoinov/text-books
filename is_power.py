"""A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b and returns True 
if a is a power of b. Note: you will have to think about the base case.

https://stackoverflow.com/questions/4738908/finding-out-whether-a-is-a-power-of-b
"""


def is_power(a, b):
    """ This functions check if the number a is a power of b.
    That is, if the following is true for a certain number n: a == b**n.
    """

    if (a == 1):
        return True
    elif (a == b):
        return True
    elif (a == 0) and (b != 0):
        return False
    elif (a != 1) and (b == 1):
        return False
    else:
        if (a % b == 0) and is_power((a/b), b):
            return True
        else:
            return False
        

print("is_power(0, 0): ", is_power(0, 0))
print("is_power(1, 0): ", is_power(1, 0))
print("is_power(0, 1): ", is_power(0, 1))
print("is_power(1, 1): ", is_power(1, 1)) 
print("is_power(1, 2): ", is_power(1, 2)) 
print("is_power(2, 1): ", is_power(2, 1))
print("is_power(2, 2): ", is_power(2, 2)) 
print("is_power(3, 2): ", is_power(3, 2))
print("is_power(4, 2): ", is_power(4, 2)) 
print("is_power(5, 2): ", is_power(5, 2))
print("is_power(6, 2): ", is_power(6, 2))
print("is_power(7, 2): ", is_power(7, 2))
print("is_power(8, 2): ", is_power(8, 2)) 
print("is_power(9, 2): ", is_power(9, 2))
print("is_power(10, 2): ", is_power(10, 2))
print("is_power(-10, 2): ", is_power(-10, 2))
print("is_power(-8, -2): ", is_power(-8, -2))