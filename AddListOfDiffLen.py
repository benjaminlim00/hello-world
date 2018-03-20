a = [1,2,3]
b = [1,2,3,4]


largest = len(a)
largerls = a[:]
smaller = b[:]
if largest < len(b):
    largest = len(b)
    largerls = b[:]
    smaller = a[:]
    
for i in range(len(smaller)):
    largerls[i] += smaller[i]
    
print(largerls)