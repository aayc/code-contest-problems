from math import gcd
from functools import reduce

def getTotalX(a, b):
    ans = 0
    start = reduce(lcm, a)
    end = reduce(gcd, b)
    n = start
    while n <= end:
        ans += 1 if end % n == 0 else 0
        n += start
    return ans

def lcm (a, b):
    return a * b // gcd(a, b)

def reference_gcd (a, b):
    # how to impl gcd?
    pass

print(getTotalX([2, 4], [12]))
