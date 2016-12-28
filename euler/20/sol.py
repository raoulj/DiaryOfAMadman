"""
Solution to Euler Problem number 20.
"""


def fact(n):
    """
    Recurvively calculate n!.  We assume positive input.
    """
    # base case
    if n == 1:
        return 1
    return n * fact(n - 1)

print sum([int(x) for x in str(fact(100))])
