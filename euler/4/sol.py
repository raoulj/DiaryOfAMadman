# # return whether the number is a palindrome
def max_palindrome_in_range(a, b):
    champ = 0
    for i in range(a, b + 1):
        for j in range(i + 1, b + 1):
            curr = i * j
            if str(curr) == str(curr)[::-1] and curr > champ:
                champ = curr
    return champ

print max_palindrome_in_range(100, 999)
