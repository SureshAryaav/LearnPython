from functools import reduce

nums = [2, 4, 6, 8]
sum_even = reduce(lambda x, y: x + y, nums)
print(sum_even)  # Output: 20
