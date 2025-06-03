pairs = [(x, y) for x in [1, 2] for y in [3, 4]]
print(pairs)  # Output: [(1, 3), (1, 4), (2, 3), (2, 4)]


#Traditional
for x in [1, 2]:
	for y in [3, 4]:
		print((x, y))
