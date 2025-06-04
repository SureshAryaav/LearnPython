nums = [1, 2, 3, 4, 5]
# Double even numbers
result = list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, nums)))
print(result)  # Output: [4, 8]
