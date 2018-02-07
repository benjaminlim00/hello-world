def is_prime(n):
    if n == 0 or n == 1:
        return False
    if n == 2:
        return True
    for x in range(2, n):
        if n % x == 0:
            return False
    return True
print ("is_prime (9)")
ans= is_prime (9)
print (ans)