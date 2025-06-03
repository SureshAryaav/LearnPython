def find_largest(a, b, c):
	return max(a, b, c)

x = int(input("Enter 1st number: "))
y = int(input("Enter 2nd number: "))
z = int(input("Enter 3rd number: "))

print("The largest number is:", find_largest(x, y, z))
