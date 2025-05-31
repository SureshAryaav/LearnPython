def factorial(n):
	result = 1
	for i in range(2, n + 1):
		result *= i
	return result

# User input
number = int(input("Enter a number to find factorial: "))
print("Factorial:", factorial(number))
