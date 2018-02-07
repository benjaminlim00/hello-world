# -*- coding: utf-8 -*-
"""
Created on Tue Feb  6 14:50:37 2018

@author: Benjamin

Functions: palindrome: A number is a palindrome number if it reads the same from left to
right as from right to left. For example, 1, 22, 12321, 441232144 are palindrome numbers.
Write a function named is_palidrome that takes an input integer and returns a boolean
value that indicates whether the integer is a palindrome number
"""

def is_palindrome(num):
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False