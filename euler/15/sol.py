"""
Solution to Euler Problem number 15.
"""
import time
N = 20

def nCr(n, r):
    return fact(n)/(fact(r) * fact(n-r))

def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)

start = time.time()
print nCr(2*N, N)
end = time.time()
print end - start
