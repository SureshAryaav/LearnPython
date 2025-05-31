def calculator(a, b, op):
	if op == '+':
		return a + b
	elif op == '-':
		return a - b
	elif op == '*':
		return a * b
	elif op == '/':
		return a / b
	elif op == '%':
		return a % b
	elif op == '**':
		return a ** b
	else:
		return "Invalid operator"

print(calculator(5, 3, '+'))  # 8
print(calculator(5, 3, '**')) # 125
print(calculator(5, 3, '-'))
#print(calculator('a', 3, '+'))
#print(calculator(5, 'b', '+'))
print(calculator(5, 3, ''))
print(calculator(5, 3, None))
print(calculator(5, 3, 0))

