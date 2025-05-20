print("Simple Calculator")

while True:
	# Input numbers from the user
	num1=float(input("Enter the first number:"))
	num2=float(input("Enter the second number:"))

# Ask for the operation
	print("Choose operation: +, -, *, /,**,%:")
	operation = input("Enter Operator: ")

# Perform the operation
	if operation == "+":
		result = num1 + num2
	elif operation == "-":
		result = num1 - num2
	elif operation == "*":
		result = num1 * num2
	elif operation == "/":
		if num2 == 0:
			print("Cannot divide by zero")
		else:
			result = num1 / num2
	elif operation == "**":
		result = num1 ** num2
	elif operation == "%":
		if num2 == 0:
			result = "Error: Cannot perform modulo by zero."
		else:
			result = num1 % num2
	else:
		print("Invalid operation")
		exit()

# Show the result
	print(f"Result: {result}")

# Ask user if they want to calculate again
	again = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
	if again != 'yes':
		print("Thanks for using the calculator. Goodbye!")
	break