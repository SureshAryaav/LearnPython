def is_even(n):
	return n % 2 == 0

num = int(input("Enter a number: "))
if is_even(num):
	print("Even number")
else:
	print("Odd number")
