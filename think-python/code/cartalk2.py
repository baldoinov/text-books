"""
I was driving on the highway the other day and I happened to notice my odometer. 
Like most odometers, it shows six digits, in whole miles only. So, if my car had 
300,000 miles, for example, I'd see 3-0-0-0-0-0. 

Now, what I saw that day was very interesting. I noticed that the last 4 digits 
were palindromic; that is, they read the same forward as backward. For example, 
5-4-4-5 is a palindrome, so my odometer could have read 3-1-5-4-4-5. 

One mile later, the last 5 numbers were palindromic. For example, it could have 
read 3-6-5-4-5-6. One mile after that, the middle 4 out of 6 numbers were palindromic. 
And you ready for this? One mile later, all 6 were palindromic! 

The question is, what was on the odometer when I first looked?


Write a Python program that tests all the six-digit numbers and prints any numbers 
that satisfy these requirements.
"""

# String slicing has the following form: string[start_index[:end_index[:step]]].
# So, if you do the following: string[0:5:1], you are slicing the string from
# the 0-th character to the 4-th character by character.

# If you try this: string[::-1], you are slicing the whole string from its last
# character to its first, which means you're reversing the string.

def palindrome(word):
    return word == word[::-1]


palindrome_numbers = []
counter = 0

for num in range(100000, 1000000):

    if palindrome(str(num)):
        counter += 1
        palindrome_numbers.append(num)

print(f"\nThere are {counter} six-digits numbers that are palindromes."
      f"\nThe numbers are:"
      f"\n{palindrome_numbers}")
