def print_even_numbers(limit):
	for i in range(1, limit + 1):
		if i % 2 == 0:
			print(i, end=" ")

print_even_numbers(20)
