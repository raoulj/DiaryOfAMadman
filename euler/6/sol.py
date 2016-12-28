upper_bound = 100
sum_square = sum([x ** 2 for x in range(1, upper_bound + 1)])
square_sum = (upper_bound * (upper_bound + 1) / 2) ** 2
print square_sum - sum_square

# after submission, I realize that I would write the first
# statement as:
# sum_square = (2 * upper_bound + 1) * (upper_bound + 1) * upper_bound /6
