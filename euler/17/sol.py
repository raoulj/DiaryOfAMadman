"""
Solution to Euler Problem number 17.
"""
from helpers import INT_STRINGS_SIZES

def calculate_integer_length(n):
    string = str(n)
    # thousands
    if len(string) == 4:
        digit = int(string[0])
        rest = int(str(n)[1:])
        return INT_STRINGS_SIZES[digit] + len("thousand") + calculate_integer_length(rest)

    # hundreds
    if len(string) == 3:
        digit = int(string[0])
        rest = int(string[1:])
        if n % 100 != 0: #needed for the 'ands'
            return INT_STRINGS_SIZES[digit] + len("hundred") + 3 + calculate_integer_length(rest)
        return INT_STRINGS_SIZES[digit] + len("hundred") + calculate_integer_length(rest)

    #tens
    if len(string) == 2:
        if n in INT_STRINGS_SIZES: #teens
            return INT_STRINGS_SIZES[n]
        
        digit = int(string[0])
        rest = int(string[1:])
        return INT_STRINGS_SIZES[digit * 10] + calculate_integer_length(rest)

    # single digits by this point
    return INT_STRINGS_SIZES[n]

SUM = 0
for i in range(1, 1000 + 1):
   SUM += calculate_integer_length(i)
print SUM