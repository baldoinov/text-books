# -*- coding: utf-8 -*-
"""
@author: Vitor Baldoino

Think Python, 2ed. Chapter 3.
"""

def right_justify(s):
    num_char = len(s)
    missing_chars = 70 - num_char
    print(' ' * missing_chars + s)
    