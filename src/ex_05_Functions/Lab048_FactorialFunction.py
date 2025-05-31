def factorial(num):
	fact=1
	for i in range(1, num+1):
		fact*=i
	return fact
	
print(factorial(6))
print(factorial(1))
print(factorial(5))
