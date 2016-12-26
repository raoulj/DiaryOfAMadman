import sys

def perim(b, s, h):
    if b + 2 * s + 2 * h:
        return False
    return True

def is_valid(p, b, s, h):
    import math
    flap_height = math.sqrt(h ** 2 - (b / 2) ** 2)

    # the diagonals must be integer
    if not math.sqrt((b / 2.0) ** 2 + (s + flap_height) ** 2).is_integer():
        return False
    if not math.sqrt(b ** 2 + s ** 2).is_integer():
        return False

    # the flap must be able the span the base
    if 2 * h < b:
        return False

    # the flap must not surpass the envelope height
    if squared_flap_height > (s ** 2):
        return False
    return True

def primitive(a, b, c):

def getMultipleLengths(p, b, s, h):


def S(p):
    # to keep track
    prim_envelopes = {}
    acc = 0

    base = 1
    side = 1
    hyp = 1

    while(perim(base, side, hyp) <= p):
        if primitive(base, side, hyp) not in prim_envelopes and is_valid(base, side, hyp):
            prim_envelopes[(base, side, hyp)] = True
            acc += getMultipleLengths(p, base, side, hyp)

    return acc

if len(sys.argv) < 2:
    raise Exception('You need more arguments than that!')
max_perim = int(sys.argv[1])
print "Result: " + str(S(max_perim))
