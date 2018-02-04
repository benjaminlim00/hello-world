#Write a function that removes all occurrences of a given letter from a string.

def remove(str, ch):
    place = ""
    for x in str:
        if x != ch:
            place += x
    return place



y = remove("school", "o")
print(y)
        