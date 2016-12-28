"""
Solution to Project Euler, Problem 11.
"""

import helpers

FILE = helpers.open_local_file('data.txt')
DATA = [[int(x) for x in row.split()] for row in FILE]
del row, helpers
GROUP_SIZE = 4
ROWCOL_LEN = len(DATA)

champ = 0
for i in range(0, ROWCOL_LEN):
    for j in range(0, ROWCOL_LEN - GROUP_SIZE):
        #diagonals
        if i >= GROUP_SIZE:
            # to the left
            current = 1
            temp_array = [DATA[j - offset][i - offset] for offset in range(0, GROUP_SIZE)]
            temp = reduce(lambda x, y: x * y, temp_array, 1)
            champ = max(champ, temp)

            #to the right
            current = 1
            temp_array = [DATA[j - offset][i + offset - GROUP_SIZE] for offset in range(0, GROUP_SIZE)]
            temp = reduce(lambda x, y: x * y, temp_array, 1)
            champ = max(champ, temp)

        #horizontal
        current = 1
        temp_array = [DATA[i][j + offset] for offset in range(0, GROUP_SIZE)]
        temp = reduce(lambda x, y: x * y, temp_array, 1)
        champ = max(champ, current)

        #verical
        current = 1
        temp_array = [DATA[j + offset][i] for offset in range(0, GROUP_SIZE)]
        temp = reduce(lambda x, y: x * y, temp_array, 1)
        champ = max(champ, current)
print champ
