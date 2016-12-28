"""
Solution to Project Euler, Problem 11.
"""

import helpers

def update_champ(current, champ):
    if current > champ:
        return current
    return champ

FILE = helpers.open_local_file('data.txt')
DATA = [line.split() for line in FILE]
SIZE = 4

champ = 0
for i, r in enumerate(DATA):
    for j, x in enumerate(range(0, len(r))):
        #diagonals to the left
        if j >= SIZE and i <= len(r) - SIZE:
            current = 1
            for offset in range(0,SIZE):
                current = DATA[i - offset][j - offset] * current
        champ = update_champ(champ, current)

        #diagonals to the right
        if j <= len(r) - SIZE and len(r) - i >= SIZE:
            current = 1
            for offset in range(0,SIZE):
                current = DATA[i + offset][j + offset] * current
        champ = update_champ(champ, current)

        #horizontal
        #verical
        test = reduce(lambda x, y: x * y, r[i:i+4],1)
        if test > h_max:
            hmax = test
print hmax    