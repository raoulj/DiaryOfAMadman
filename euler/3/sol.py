num = 600851475143

fact = 3 #since num is odd
while num != fact:
    while num % fact == 0:
        num = num / fact
    fact += 2
print num
