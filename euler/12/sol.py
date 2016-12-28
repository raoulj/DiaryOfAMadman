"""
Solution to Euler Problem number 12.
"""
from sympy.ntheory import factorint

def triangle_numbers():
    """
    Generator for the "triangle numbers": 1, 3, 6, 10...
    Each term in the sequence is a partial sum of the natural numbers
    1 = 1, 1 + 2 = 3, 1 + 2 + 3 = 6, 1 + 2 + 3 + 4 = 10, 1 + 2 + ...
    """
    partial_sum = 0
    i = 1
    while True:
        partial_sum += i
        yield partial_sum
        i += 1

for n in triangle_numbers():
    div_count = reduce(lambda x, y: x * (y + 1), factorint(n).values(), 1)
    if div_count > 500:
        print n
        break
