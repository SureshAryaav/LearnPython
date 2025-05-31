def add_numbers(*args):
	total = 0
	for number in args:
		total += number
	print("Total:", total)

add_numbers(10, 20, 30)  # You can pass any number of arguments
