import os
# we'll store the number in another file for convenience
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'number.txt'), 'r')
haystack = f.readline()

size = 13

def initProduct(i):
    return reduce(lambda x, y: int(x) * int(y), haystack[i:i + size], 1)


curr = initProduct(0)
best = curr

for i in range(1, len(haystack) - size):
    if (int(haystack[i - 1]) == 0):
        curr = initProduct(i)
        continue

    curr = curr / int(haystack[i - 1]) * int(haystack[i + size - 1])

    if curr > best:
        best = curr
print best
