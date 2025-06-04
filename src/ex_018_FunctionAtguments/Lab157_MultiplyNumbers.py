def multiply_all(*nums):
	result = 1
	for n in nums:
		result *= n
	return result

print("Product:", multiply_all(2, 3, 4))

