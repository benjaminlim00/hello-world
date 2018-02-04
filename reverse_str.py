def reverse(str):
    place = ""
    for ch in str:
        place = ch + place
    return place

x = "yellow"
print(reverse(x))    
        