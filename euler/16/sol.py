"""
Solution to Euler Problem number 16.
"""
VALUE = 2 ** 1000
SUM = 0
for digit in str(VALUE):
    SUM += int(digit)
print SUM