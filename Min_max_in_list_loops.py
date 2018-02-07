"""Loops: maximum: Write a function named minmax_in_list that takes a list of integers as
an input and returns the minimum and maximum values in the list. Return (None, None)
if the list is empty. Note that the maximum and minimum integers in Python are given
by, respectively, the constants sys.maxsize and -sys.maxsize-1. You must use loops
rather than any built-in function"""

def minmax_in_list(ls):
    if ls == []:
        return (None, None)
    maxi = ls[0]
    mini = ls[0]
    for item in ls:
        if item < mini:
            mini = item
        if item > maxi:
            maxi = item
    return (mini, maxi)