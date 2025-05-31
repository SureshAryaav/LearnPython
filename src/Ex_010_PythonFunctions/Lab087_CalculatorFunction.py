def calculator(a, b):
	print("Sum:", a + b)
	print("Difference:", a - b)
	print("Product:", a * b)
	if b != 0:
		print("Quotient:", a / b)
	else:
		print("Division by zero not allowed")

x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
calculator(x, y)
