import math
def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x-1)
    
    
def approx_pi(n):
    fract = 0
    k = 0
    constant = (2 * math.sqrt(2) / 9801)
    epsilon = 1e10-20
    while True:
        num = factorial(4 * k) * (1103 + 26390 * k)
        deno = factorial(k) ** 4 * 396 ** (4 * k)
        fract = constant * num / deno
        total += fract
        if abs(fract) < epsilon: #usage of floating points
            break
        k += 1
    return 1/total
        