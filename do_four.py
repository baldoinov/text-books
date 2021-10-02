# -*- coding: utf-8 -*-
"""
@author: Vitor Baldoino

Think Python, 2ed. Chapter 3.
"""

def do_twice(f, value):
    f(value)
    f(value)
    
def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_four(f, value):
    do_twice(f, value)
    do_twice(f, value)

do_four(print_twice, 'spam')

