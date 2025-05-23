number = int(input("Enter the number: "))

if number % 3 == 0 and number % 5 == 0:
	print(f"{number} is divisible by both 3 and 5.")
else:
	print(f"{number} is NOT divisible by both 3 and 5.")