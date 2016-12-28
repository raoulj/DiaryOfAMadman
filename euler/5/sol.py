from sympy.ntheory import factorint

upper_bound = 20
factors = {k: 0 for k in range(0, upper_bound + 1)}

for i in range(1,upper_bound + 1):
    additions = {k:v for k,v in factorint(i).iteritems() if v > factors[k]}
    for k, v in additions.iteritems():
        factors[k] = v

prod = 1
for k,v in factors.iteritems():
    prod *= k ** v
print prod
