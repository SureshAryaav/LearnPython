nums = [1, 2, 3, 4, 5]
even_squares = list(map(lambda x: x * x, filter(lambda x: x % 2 == 0, nums)))
print(even_squares)  # Output: [4, 16]
