names = []

count = int(input("How many names do you want to enter? "))

for i in range(count):
	name = input(f"Enter name {i+1}: ")
	names.append(name)

names.sort()  # Sort in alphabetical order

print("\nSorted names:")
for name in names:
	print(name)
