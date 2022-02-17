# -*- coding: utf-8 -*-
"""
@author: Vitor Baldoino

Think Python, 2ed. Chapter 3.
"""

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def middle():
    print('|        ', end=' ')
    
def header():
    print('+ - - - -', end=' ')

def print_header():
    do_twice(header)
    print('+', end=' ')
    print()

def print_middle():
    do_twice(middle)
    print('|', end=' ')
    print()

def print_grid():
    print_header()
    do_four(print_middle)
    
do_twice(print_grid)
print_header()

