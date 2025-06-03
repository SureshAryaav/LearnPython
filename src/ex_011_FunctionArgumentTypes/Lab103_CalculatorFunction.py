def calculator(a=10, b=5, operation="add"):
	if operation == "add":
		return a + b
	elif operation == "subtract":
		return a - b
	else:
		return "Invalid Operation"

print(calculator())
print(calculator(20, 10, operation="subtract"))
print(calculator(b=3, a=7))
