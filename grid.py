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

def start_middle():
    print('|        ', end=' ')
    
def start_header():
    print('+ - - - -', end=' ')

def print_header():
    start_header()
    print('+', end=' ')

def print_middle():
    start_middle()
    print('+', end=' ')

def one_four_one(one, four, hone):
    one()
    do_four(four)
    hone()
    
def print_grid():
    one_four_one(print_header, print_middle, print_header)

print_grid()