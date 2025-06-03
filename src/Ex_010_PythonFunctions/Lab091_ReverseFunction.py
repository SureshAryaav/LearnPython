def reverse_number(num):
	reversed_num = 0
	while num > 0:
		digit = num % 10
		reversed_num = reversed_num * 10 + digit
		num //= 10
	return reversed_num

# User input
n = int(input("Enter a number: "))
print("Reversed number:", reverse_number(n))
