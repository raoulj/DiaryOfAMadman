"""
Solution to Euler Problem number 14.
"""
import helpers

SEQ_LENGTH = {1: 1}

def collatz_length(n):
    if n in SEQ_LENGTH:
        return SEQ_LENGTH[n]

    if n % 2 == 0:
        SEQ_LENGTH[n] = collatz_length(n/2) + 1
        return SEQ_LENGTH[n]
    SEQ_LENGTH[n] = collatz_length(3*n + 1) + 1
    return SEQ_LENGTH[n]

LIMIT = int(1E6)
champ = 0
champ_value = 0
for n in range(1, LIMIT + 1):
    current = collatz_length(n)
    if current > champ:
        champ = current
        champ_value = n
print champ_value
