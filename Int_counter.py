def intcount(string):
    total = 0
    for x in string:
        if x.isdigit():
            total += 1
    return total

y = intcount("jjbjb2323")
print(y)