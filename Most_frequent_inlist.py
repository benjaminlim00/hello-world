'''Dictionary: Write a function named most_frequent that takes in a list of integers and
returns a list of the ones that have the most occurrences. If more than one number have
the most number of occurrences, all of them should be reported. You can assume that the
input list is never empty. For example:
input=[2,3,40,3,5,4,-3,3,3,2,0]
most_frequent = [3]
input=[9,30,3,9,3,2,4]
most_frequent = [9, 3]'''
import sys

def most_frequent(lst):
    dic = {}
    ans = []
    for item in lst:
        if item not in dic:
            dic[item] = 1
        else:
            dic[item] += 1
    biggest = 0
    for key, value in dic.items():
        if value >= biggest:
            if value > biggest:
                biggest = value
                ans = [key]
            else:
                ans.append(key)
    return ans