"""
If there are 23 students in your class, what are the chances that two of you have the same 
birthday? You can estimate this probability by generating random samples of 23 birthdays 
and checking for matches. 

Hint: you can generate random birthdays with the randint function in the random module.
"""

import random

random.seed(5)

def has_duplicates(t: list) -> bool:
    """Returns True if any element appears more than once in a sequence."""

    s = list(t)
    s.sort()
    
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            return True
    
    return False


def random_birthdays(n: int) -> list:
    """Generates n random birthdays, expressing them as an integer betweem 1
    and 365. 
    
    Returns a list with the generated birthdays.
    """

    t = []

    for i in range(n):
        bday = random.randint(1, 365)
        t.append(bday)

    return t


def birthday_problem(num_students: int, num_simulations: int) -> int:
    """Executes the birthday problem experiment for a given number of students.
    
    Returns the number of times there were a match inside the group of students.

    https://en.wikipedia.org/wiki/Birthday_problem
    """

    count = 0

    for i in range(num_simulations):
        bdays = random_birthdays(num_students)
        
        if has_duplicates(bdays):
            count += 1
    
    return count


def main():
    """Runs the birthday simulation and prints the number of matches."""
    
    num_students = 23
    num_simulations = 1000
    count = birthday_problem(num_students, num_simulations)

    print(f"\nAfter {num_simulations} simulations\n"
          f"with {num_students} students\n"
          f"there were {count} simulations with at least one match.")

main()