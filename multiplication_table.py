# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:52:31 2018

@author: Benjamin
"""

def get_conversion_table_a():
    ls = []
    n = 0
    for x in range (10):
        ls.append([])
    while n <= 100:
        for i in ls:
            i.append(n)
            i.append(f_to_c(n))
            i.append(f_to_c_approx(n))
        n += 10
    return ls

print(get_conversion_table_a())