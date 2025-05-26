original = [1, 2, 3, 4, 5]
reversed_list = []

for item in original:
	reversed_list = [item] + reversed_list

print(reversed_list)  # [5, 4, 3, 2, 1]
