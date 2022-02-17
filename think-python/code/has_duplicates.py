"""
If you did Exercise 10.7, you already have a function named has_duplicates that takes a 
list as a parameter and returns True if there is any object that appears more than once 
in the list.

Use a dictionary to write a faster, simpler version of has_duplicates.
"""


def has_duplicates1(t: list) -> bool:
    """Version using lists."""

    s = list(t)
    s.sort()
    
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return True
    
    return False


def has_duplicates2(s:list) -> dict:
    """Version using dictionaries."""

    d = dict()

    for char in s:
        
        if char in d:
            return True

        d[char] = 1
    
    return False


if __name__ == '__main__':
    
    t = [1, 2, 3]
    print(has_duplicates1(t))
    t.append(1)
    print(has_duplicates1(t))

    t = [1, 2, 3]
    print(has_duplicates2(t))
    t.append(1)
    print(has_duplicates2(t))