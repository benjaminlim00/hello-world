'''Functions: reverse: The reverse method of a list reverses the list. Write a function
my_reverse, which takes a list as an input and returns the reverse of the list, without
changing the original list. For example, if the input list is [5, -2, 15, 4] then the function
must return the list [4, 15, -2, 5]. Use loops and do not use any built-in function to reverse
a list, or [::-1].'''

def my_reverse(list1):
    list2 = []
    x = len(list1)
    for index in range(x - 1, -1, -1):
        list2.append(list1[index])
    return list2