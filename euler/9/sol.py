import math

def findAB():
    for a in range(1, 500):
        for b in range(a + 1, 500):
            if a ** 2 + b ** 2 == (1000 - (a + b)) ** 2:
                print a * b * (1000 - (a + b))
                return

print 'Solution:'
import time
start = time.time()
findAB()
end = time.time()
print 'Duration:'
print str(end - start) + ' seconds'
