numbers = []

print("Enter 5 numbers:")
for i in range(5):
	num = int(input(f"Enter number {i+1}: "))
	numbers.append(num)

print("\nNumbers entered:", numbers)
print("Maximum number:", max(numbers))
print("Minimum number:", min(numbers))
print("Sorted numbers:", sorted(numbers))