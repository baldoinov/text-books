"""
Recently I had a visit with my mom and we realized that the two digits that make up my 
age when reversed resulted in her age. For example, if she's 73, I'm 37. We wondered how
often this has happened over the years but we got sidetracked with other topics and we 
never came up with an answer. 

When I got home I figured out that the digits of our ages have been reversible six times
so far. I also figured out that if we're lucky it would happen again in a few years, and
if we're really lucky it would happen one more time after that. In other words, it would
have happened 8 times over all. So the question is, how old am I now?

Write a Python program that searches for solutions to this Puzzler. 
Hint: you might find the string method zfill useful.

"""

def reverse_number(number: int) -> int:
    """Takes an integer and returns the reverse of this integer."""

    number = str(number).zfill(2)
    reversed = int(number[::-1])

    return reversed


def are_reversed(number1: int, number2: int) -> bool:
    """Check if two integers are the reverse of each other"""

    if number1 == number2:
        return False
    
    number1 = str(number1).zfill(2)
    number2 = str(number2).zfill(2)

    if number1 == number2[::-1]:
        return True
    
    else:
        return False


def number_ocurrences(diff: int) -> list:   #TODO: Fix this function
    
    kid = 0
    parent = kid + diff
    matches = []

    while True:
        
        if parent > 100:
         
            break
        #elif reverse_number(kid) > parent:
        #    print("break2")
        #    break
    
        if are_reversed(kid, parent) or are_reversed(kid, parent + 1):
            print("appending")
            matches.append((kid, parent))
        
        kid += 1
        parent = kid + diff
    
    return matches

print(number_ocurrences(10))
