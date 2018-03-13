string = '-1 2 2 2 \n'
x = string.replace('-', '').replace(' ', '').replace('\n', '')
print(x)
print(x.isdigit()) #method 1

y = string.replace('-', '').split()
y = ''.join(y)
print(y)
print(y.isdigit()) #method 2
