def getPrimes(upper_bound = int(5E5)):
    nums = {x: True for x in range(1,upper_bound + 1)}
    nums[1] = False
    for k, v in nums.iteritems():
        if v == True and k != 1:
            c = 2
            while c * k <= upper_bound:
                nums[c * k] = False
                c += 1
    return [k for k, v in nums.iteritems() if v == True]

print getPrimes()[10001 - 1]
