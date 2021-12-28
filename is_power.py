"""A number, a, is a power of b if it is divisible by b and a/b is a power of b. 
Write a function called is_power that takes parameters a and b and returns True 
if a is a power of b. Note: you will have to think about the base case."""

def is_power(a, b):

    if (a <= 0) or (b <= 0):
        return "A função não está definida para número menores ou iguais a 0."
    
    elif (a == 1) or (a == (a/b)):
        return True
    
    else: 
        if ((a % b) == 0) and (is_power((a/b), b)):
            return True
        else:
            return False
    

print("is_power(0, 0): ", is_power(0, 0))
print("is_power(1, 0): ", is_power(1, 0))
print("is_power(0, 1): ", is_power(0, 1))
print("is_power(1, 1): ", is_power(1, 1)) 
print("is_power(1, 2): ", is_power(1, 2)) 
print("is_power(2, 1): ", is_power(2, 1))   # TODO: Esse resultado está errado devido à condição (a == (a/b))
print("is_power(2, 2): ", is_power(2, 2)) 
print("is_power(3, 2): ", is_power(3, 2))
print("is_power(4, 2): ", is_power(4, 2)) 
print("is_power(5, 2): ", is_power(5, 2))
print("is_power(6, 2): ", is_power(6, 2))
print("is_power(7, 2): ", is_power(7, 2))
print("is_power(8, 2): ", is_power(8, 2)) 
print("is_power(9, 2): ", is_power(9, 2))
print("is_power(10, 2): ", is_power(10, 2))