"""
Solution to Euler Problem number 13.
"""
import helpers


FILE = helpers.open_local_file('data.txt')
DATA = [int(row) for row in FILE]
ARGSUM = sum(DATA)

# Just get the first 10 digits
ARGSUM = str(ARGSUM)[0:10]
print ARGSUM
