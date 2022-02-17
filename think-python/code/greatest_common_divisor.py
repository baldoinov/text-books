"""The greatest common divisor (GCD) of a and b is the largest number that 
divides both ofthem with no remainder.
One way to find the GCD oftwo numbers is based on the observation that 
if r is the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). 
As a base case, we can use gcd(a, 0) = a. Write a function called gcd 
that takes parameters a and b and returns their greatest common divisor."""

def gcd(a, b):
    
    if b == 0:
        return a
    else:
        r = a % b
        return gcd(b, r)


print("gcd(6, 3): ", gcd(6, 3))
print("gcd(8, 4): ", gcd(8, 4))
print("gcd(25, 22): ", gcd(25, 22))
print("gcd(28, 30): ", gcd(28, 30))
print("gcd(1, 2): ", gcd(1, 2))
print("gcd(2, 1): ", gcd(2, 1))
print("gcd(2, 2): ", gcd(2, 2)) 
print("gcd(3, 2): ", gcd(3, 2))
print("gcd(4, 2): ", gcd(4, 2)) 
print("gcd(5, 2): ", gcd(5, 2))
print("gcd(6, 2): ", gcd(6, 2))
print("gcd(7, 2): ", gcd(7, 2))
print("gcd(8, 2): ", gcd(8, 2)) 
print("gcd(9, 2): ", gcd(9, 2))
print("gcd(10, 2): ",gcd(10, 2))