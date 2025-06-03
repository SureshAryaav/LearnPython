def multiply_table(start, end):
	for i in range(start, end + 1):
		for j in range(start, end + 1):
			print(f"{i} * {j} = {i * j}")
		print("-" * 10)
		print()

multiply_table(1, 10)