limit = 1000
def multiples_of(num):
    return [num * x for x in range(1, (limit - 1)/num + 1)]

three_multiples = multiples_of(3)
five_multiples = multiples_of(5)
all_multiples = set(three_multiples + five_multiples)
print sum(all_multiples)
