limit = 4E6

def fibs():
    a, b = 0, 1
    yield a
    yield b

    while b < limit:
        a, b = b, a + b
        yield b

print sum([f for f in fibs() if f % 2 == 0])
